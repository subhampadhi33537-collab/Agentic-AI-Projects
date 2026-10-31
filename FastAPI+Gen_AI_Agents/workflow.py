from agents.search_agent import agent1
from agents.thinking_agent import agent2
from agents.writing_agent import agent3
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



prompt1=PromptTemplate(
    template="generate a detailed report about this {topic}",
    input_variables=["topic"]
)

chain= agent1 | agent2 | agent3 


