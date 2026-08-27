from langchain.tools import tool


@tool(
    description="Retrives and outputs the most recent agent response logged into the database when less than a week i.e., 7 days have elapsed."
)
def current_response() -> str:
  """
  Retrieve and output the latest agent response from the database.
  """
