import json
import time
from pathlib import Path

from ..config import config


def save_response(summary: str) -> None:
  """
  Saves the agent's summary along with the current timestamp to the state file.
  """
  state_file = Path(config.STATE_FILE_PATH)
  state_file.parent.mkdir(parents=True, exist_ok=True)

  state = {
    "timestamp": time.time(),
    "summary": summary
  }

  with open(state_file, 'w') as f:
    json.dump(state, f, indent=2)
