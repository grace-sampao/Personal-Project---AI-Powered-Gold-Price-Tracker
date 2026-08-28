import sys
from pathlib import Path
# import importlib

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(
  str(root_dir)
)

from agent.config import config
from agent.tools.search_tool import tavily_search
from agent.tools.save_response import save_response
from agent.tools.get_response import get_response
import agent.prompts.prompts as prompt

# importlib.reload(config)

from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langgraph.store.memory import InMemoryStore

import datetime as dt


model = ChatDeepSeek(
  model="deepseek-v4-flash",
  api_key=config.DEEPSEEK_API_KEY,
  temperature=0,
  max_tokens=None,
  timeout=None,
  max_retries=2,
)

store = InMemoryStore()

agent = create_agent(
  model=model,
  tools=[tavily_search, save_response, get_response],
  store=store,
)

def invoke_agent():
  start_date = dt.date(2026, 8, 15)
  current_date = dt.date.today()
  period_elapsed = current_date - start_date

  if period_elapsed.days % 7 == 0:
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

    response = response["messages"][-1].content

    return response
  else:
    response = agent.invoke(
      {
        "messages": [
          {
            "role": "user",
            "content": "Output only the contents of the latest brief summary you have saved."
          }
        ]
      }
    )

    response = response["messages"][-1].content

    return response
