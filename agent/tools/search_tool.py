import sys
from pathlib import Path
import importlib

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(
  str(root_dir)
)

from config import config
importlib.reload(config)

from langchain_tavily import TavilySearch


tavily_search = TavilySearch(
  max_results=5,
  tavily_api_key=config.TAVILY_API_KEY,
  topic="finance",
  time_range="week",
  # include_domains=[],
)
