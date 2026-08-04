import config.environment
import importlib

importlib.reload(config.environment)

from langchain.agents import create_agent

agent = create_agent(
  model="deepseek:deepseek-v4-flash",
  api_key=config.environment.DEEPSEEK_API_KEY
)
