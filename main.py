from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.tools import tool

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")

output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instructions = PromptTemplate(
    template = REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input","agent_scratchpad","tool_names"]
).partial(format_instructions=output_parser.get_format_instructions())




agent = create_react_agent(llm, tools, react_prompt_with_format_instructions)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

chain = agent_executor


def main():
    print("Welcome to the AI Search Agent!")
    result = chain.invoke(
        input={
            "input": "Search for 10 beginner LLM Engineer paid internship opportunities focusing on LangChain in Bengaluru and list their details"
        }
    )
    print(result)


if __name__ == "__main__":
    main()
