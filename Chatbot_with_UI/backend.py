from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph,START,END
from langchain_core.messages import BaseMessage,AIMessage,HumanMessage
from typing import TypedDict,Annotated
from pydantic import BaseModel,Field
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages
from langchain_community.tools import DuckDuckGoSearchRun



load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")

search_tool=DuckDuckGoSearchRun()
llm=model.bind_tools([search_tool])




class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],Field(description="it store different messages"),add_messages]


def chat_node(state:ChatState):
    messages = state["messages"]

    result=llm.invoke(messages).content

    return {"messages":[result]}


checkpointer=MemorySaver()

graph=StateGraph(ChatState)

graph.add_node("chat-node",chat_node)

graph.add_edge(START,"chat-node")
graph.add_edge("chat-node",END)

chatbot=graph.compile(checkpointer=checkpointer)