import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# API Keys
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Agent settings
UPDATE_INTERVAL_SECONDS = int(
  os.getenv(
    "UPDATE_INTERVAL_SECONDS", "604800"     # 7 days
  )
)
STATE_FILE_PATH = os.getenv(
  "STATE_FILE_PATH", "instance/agent_state.json"    # Default location
)

# Optional: LLM model name
LLM_MODEL_NAME = os.getenv(
  "LLM_MODEL_NAME", "deepseek-v4-flash"
)

# Validate the required keys are present
if not DEEPSEEK_API_KEY or not TAVILY_API_KEY:
  raise ValueError(
    "Missing required API keys. Please set DEEPSEEK_API_KEY and TAVILY_API_KEY in your environment or .env file."
  )
