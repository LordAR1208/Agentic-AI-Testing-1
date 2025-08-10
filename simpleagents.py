from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
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
agent = Agent(
    model=Groq(id="qwen/qwen3-32b", api_key=groq_api_key),  # Updated to new supported model
    description="You are an assistant; please reply based on the questions.",
    tools=[DuckDuckGoTools()],
    markdown=True
)

# Ask a question
agent.print_response("Who won the latest Cricket World Cup?")
