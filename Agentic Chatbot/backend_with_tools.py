import os
import sqlite3
from typing import TypedDict, Annotated

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()
os.environ["LANGCHAIN_PROJECT"] = "chatbot_using_tools"

# ---------- LLM ----------
llm = ChatGroq(model="openai/gpt-oss-120b")

# ---------- Tools ----------
search_tool = DuckDuckGoSearchRun()



tools = [ search_tool]
llm_with_tools = llm.bind_tools(tools)   # model now knows about the tools
tool_node = ToolNode(tools)              # real ToolNode object, not the module

# ---------- State ----------
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# ---------- Nodes ----------
def chat_node(state: ChatState):
    response = llm_with_tools.invoke(state["messages"])   # llm_with_tools, not llm
    return {"messages": [response]}

# ---------- Checkpointer ----------
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

# ---------- Graph ----------
graph = StateGraph(ChatState)
graph.add_node("chatnode", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chatnode")
graph.add_conditional_edges("chatnode", tools_condition)
graph.add_edge("tools", "chatnode")

chatbot = graph.compile(checkpointer=checkpointer)

def get_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config["configurable"]["thread_id"])
    return list(all_threads)