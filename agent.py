import environment
import importlib

importlib.reload(environment)

from langchain.agents import create_agent

agent = create_agent(
  model="deepseek:deepseek-v4-pro",
  api_key=environment.DEEPSEEK_API_KEY
)
