from langchain.tools import tool, ToolRuntime


@tool
def save_response(
  date: str,
  summary: dict[str, str],
  runtime: ToolRuntime) -> str:
  """
  Save the agent response into the memory.
  """
  store = runtime.store
  store.put(("responses",), date, summary)

  return "Sucessfully saved agent response."
