from langchain.tools import tool, ToolRuntime


@tool
def save_response(response: str, runtime: ToolRuntime) -> str:
  """
  Save the agent response into the memory.
  """
  store = runtime.store
  store.put(("responses",), response)

  return "Sucessfully saved agent response."
