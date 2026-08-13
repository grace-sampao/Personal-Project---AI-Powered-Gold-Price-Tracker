import sys
from pathlib import Path
# import importlib

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(
  str(root_dir)
)

from agent.config import config
from agent.tools.search_tool import tavily_search
import agent.prompts.prompts as prompt

# importlib.reload(config)

from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek


model = ChatDeepSeek(
  model="deepseek-v4-flash",
  api_key=config.DEEPSEEK_API_KEY,
  temperature=0,
  max_tokens=None,
  timeout=None,
  max_retries=2,
)

agent = create_agent(
  model=model,
  tools=[tavily_search],
)

def invoke_agent():
  response = agent.invoke(
    {
      "messages": [
        {
          "role": "system",
          "content": prompt.system_message
        },
        {
          "role": "user",
          "content": prompt.user_message
        }
      ]
    }
  )

  response = response["messages"][-1].content_blocks[-1]["text"]

  return response
