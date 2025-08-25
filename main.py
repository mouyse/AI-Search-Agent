from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.tools import tool

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(llm, tools, react_prompt)
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
