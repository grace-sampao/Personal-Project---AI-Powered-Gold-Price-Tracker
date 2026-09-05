from flask import Blueprint, render_template
from agent.tools.get_response import get_response


bp = Blueprint(
  "agent_response", __name__
)

@bp.route("/", methods=["get"])
def homepage():
  # Returns the cached summary if it's still fresh,
  # otherwise triggers a new agent run & returns the new summary.
  summary = get_response()

  return render_template(
    "index.html", gold_price_summary=summary
  )
