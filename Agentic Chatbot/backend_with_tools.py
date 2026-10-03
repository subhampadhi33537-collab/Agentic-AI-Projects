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

llm = ChatGroq(model="openai/gpt-oss-120b")

search_tool = DuckDuckGoSearchRun()



tools = [ search_tool]
llm_with_tools = llm.bind_tools(tools)  
tool_node = ToolNode(tools)             


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    response = llm_with_tools.invoke(state["messages"])  
    return {"messages": [response]}


conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

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