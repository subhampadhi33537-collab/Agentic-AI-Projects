from langchain_tavily import TavilySearch
from langchain_core.tools import tool

@tool
def tavily_search(query: str):
    """Search the internet using Tavily for relevant information."""

    tool1 =  TavilySearch(
    max_results=5)

    result = tool1.invoke({
        "query": query
    })

    return result