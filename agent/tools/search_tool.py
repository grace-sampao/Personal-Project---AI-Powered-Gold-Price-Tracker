from langchain.tools import tool
from langchain_tavily import TavilySearch
from agent.config import config


tavily_search = TavilySearch(
  max_results=5,
  tavily_api_key=config.TAVILY_API_KEY,
  topic="finance",
  time_range="week"
)

@tool
def search_web(query: str) -> str:
  """
  Searches the web for the latest financial and geopolitical news and commodity prices.
  Use this tool to get information relevant to the analysis.
  """
  try:
    results = tavily_search.run(query)

    return results
  except Exception as e:
    return f"Error during search {str(e)}"
