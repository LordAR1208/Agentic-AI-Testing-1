from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API keys
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Safety check to avoid missing keys
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing. Please set it in your .env file.")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is missing. Please set it in your .env file.")

# Create the agent
web_agent = Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="qwen/qwen3-32b", api_key=groq_api_key),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True
)   

finance_agent = Agent(
    name="Finance Agent",
    role="provide financial information",
    model=Groq(id="qwen/qwen3-32b", api_key=groq_api_key),
    tools=[YFinanceTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True
)

agent_team=Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen/qwen3-32b", api_key=groq_api_key),
    instructions="You are a team of agents. Use the web agent for general queries and the finance agent for financial queries.",
    show_tool_calls=True,
    markdown=True
)

agent_team.print_response("What is the current stock price of Apple Inc. and who won the latest Cricket World Cup?")  # Example query that uses both agents