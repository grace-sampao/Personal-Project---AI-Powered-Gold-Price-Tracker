import json
import time
from pathlib import Path

from ..config import config


STATE_FILE = Path(config.STATE_FILE_PATH)

def _read_state() -> dict:    # Handles JSON persistence
  """
  Reads the current state from the state file.
  Returns a dict with 'timestamp' and 'summary', or empty dict if file missing/corrupt.
  """
  if not STATE_FILE.exists():
    return {}
  try:
    with open(STATE_FILE, 'r') as f:
      return json.load(f)
  except (json.JSONDecodeError, IOError):
    return {}

def get_response() -> str:
  """
  Returns the current summary if it's less than UPDATE_INTERVAL_SECONDS old.
  Otherwise, triggers a new agent run, stores the new summary and returns it.
  """
  state = _read_state()
  current_time = time.time()

  if state and 'timestamp' in state and 'summary' in state:
    age = current_time - state["timestamp"]

    if age < config.UPDATE_INTERVAL_SECONDS:
      # If summary is still fresh; return it
      return state["summary"]

    # Summary is missing or stale; generate a new one
    # Import inside function to avoid circular import
    from agent.agent import generate_summary

    print("Generating new summary...")
    new_summary = generate_summary()      # Will also call save_response internally

    return new_summary
