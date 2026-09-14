import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_community.tools import DuckDuckGoSearchRun

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent


from typing import TypedDict, Annotated



load_dotenv()

SYSTEM_PROMPT = SystemMessage(
    content=(
        "You are AURA (AI Universal Response Assistant), a warm, sharp, and "
        "highly capable AI assistant. Be concise but thorough, use the "
        "web_search tool whenever a question needs current information you "
        "are not confident about, and always cite what you found when you "
        "use it. Format answers with markdown when it improves clarity."
    )
)

search_tool = DuckDuckGoSearchRun()


model = ChatGroq(model="openai/gpt-oss-120b", temperature=0.4)

agent=create_agent(
    model=model,
    tools=[search_tool],
    system_prompt=SYSTEM_PROMPT
)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]



def chat_node(state: ChatState):
    messages = state["messages"]

    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SYSTEM_PROMPT] + messages

    response = agent.invoke({
        "messages": messages
    })

    return {
        "messages": response["messages"]
    }


checkpointer = MemorySaver()



graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")

chatbot = graph.compile(checkpointer=checkpointer)