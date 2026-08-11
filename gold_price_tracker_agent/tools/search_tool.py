import sys
from pathlib import Path
import importlib

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from gold_price_tracker_agent.config import environment
importlib.reload(environment)

from langchain_tavily import TavilySearch

search_tool = TavilySearch(
  max_results=5,
  tavily_api_key=environment.TAVILY_API_KEY,
  topic="finance",
  time_range="week",
  # include_domains=[]
)
