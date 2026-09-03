from langchain.tools import tool, ToolRuntime
from langchain.agents import AgentState
from langchain.messages import ToolMessage
from langgraph.types import Command


class CustomState(AgentState):
  ai_message: str

@tool
def save_response(
  response: str, runtime: ToolRuntime[None, CustomState]
) -> Command:
  """
  Set the agent's response in the conversation state.
  """
  return Command(
    update={
      "ai_message": response,
      "messages": [
        ToolMessage(
          content=f"{response}",
          tool_call_id=runtime.tool_call_id
        )
      ]
    }
  )
