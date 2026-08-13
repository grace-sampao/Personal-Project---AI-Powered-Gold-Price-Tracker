import sys
from pathlib import Path
# import importlib

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(
  str(root_dir)
)

from flask import Blueprint, render_template
from agent.agent import invoke_agent
import markdown


bp = Blueprint(
  "agent_response", __name__
)

@bp.route("/", methods=["GET"])
def homepage():
  markdown_response = invoke_agent()
  response = markdown.markdown(
    markdown_response, extensions=["extra", "codehilite"]
  )

  return render_template(
    "index.html", gold_price_summary=response
  )
