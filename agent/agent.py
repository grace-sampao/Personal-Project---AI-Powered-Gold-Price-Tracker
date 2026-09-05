from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek

from agent.config import config
from agent.tools.search_tool import search_web
from agent.tools.save_response import save_response
from agent.prompts.prompts import SYSTEM_MESSAGE, create_user_prompt


DEFAULT_COMMODITY = "gold"

model = ChatDeepSeek(
  model=config.LLM_MODEL_NAME,
  api_key=config.DEEPSEEK_API_KEY,
  temperature=0,
  max_tokens=None,
  timeout=None,
  max_retries=2
)

agent_prompt = ChatPromptTemplate.from_messages(
  [
    ("system", SYSTEM_MESSAGE),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
  ]
)

# Create the tool calling agent
agent = create_tool_calling_agent(
  model, [search_web], agent_prompt
)

# Wrap it with an AgentExecutor for reliable tool execution
agent_executor = AgentExecutor(
  agent=agent,
  tools=[search_web],
  verbose=True,
  handle_parsing_errors=True,
  max_iterations=5
)

def generate_summary(commodity: str = DEFAULT_COMMODITY) -> str:
  """
  Invokes the autonomous agent to produce a weekly summary for the given commodity.
  The result is saved to the state file and returned.
  """
  # Build the user prompt for the commodity
  user_prompt = create_user_prompt(commodity)

  # Invoke the agent
  result = agent_executor.invoke(
    {"input": user_prompt}
  )

  # Extract the final output from the agent's response
  summary = result.get("output", "")
  if not summary:
    summary = "No summary generated."

  # Save the new summary and timestamp to the state file
  save_response(summary)

  return summary
