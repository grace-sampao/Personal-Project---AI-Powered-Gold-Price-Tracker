from langchain.tools import tool, ToolRuntime


@tool
def get_response(date: str, runtime: ToolRuntime) -> str:
  """
  Retrieve the latest agent response from the memory.
  """
  store = runtime.store
  response = store.get(("responses",), date)

  return str(response.value)
