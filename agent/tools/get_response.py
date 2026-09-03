from langchain.tools import tool, ToolRuntime
from langchain.messages import AIMessage


@tool
def get_response(runtime: ToolRuntime) -> str:
  """
  Get the most recent message from the AI agent.
  """
  responses = runtime.state["messages"]

  # Find the last AI message
  for response in reversed(responses):
    if isinstance(response, AIMessage):
      response = response.content

      return response

  return "No AI messages found"
