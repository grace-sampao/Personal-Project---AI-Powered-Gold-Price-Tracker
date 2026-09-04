import json
import time
from pathlib import Path
from typing import Optional

from ..config import config
from ..agent import generate_summary


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

def _write_state(timestamp: float, summary: str) -> None:   # Handles JSON persistence
  """
  Writes the given timestamp and summary to the state file.
  """
  STATE_FILE.parent.mkdir(parents=True, exist_ok=True)    # Ensure directory exists
  with open(STATE_FILE, 'w') as f:
    json.dump(
      {
        "timestamp": timestamp, "summary": summary
      },
      f, indent=2
    )

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

    # Summary is missing or stale; generate a new onw
    print("Generating new summary...")
    new_summary = generate_summary()
    _write_state(current_time, new_summary)

    return new_summary
