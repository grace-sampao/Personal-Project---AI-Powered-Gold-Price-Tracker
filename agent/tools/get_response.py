from langchain.tools import tool, ToolRuntime


@tool
def get_response(response: str, runtime: ToolRuntime) -> str:
  """
  Retrieve the latest agent response from the memory.
  """
  store = runtime.store
  response = store.get(("responses",), response)

  return str(response.value)
