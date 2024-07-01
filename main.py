import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"


@app.route("/api/sme_dashboard")
def sme_dashboard():
  return f"This is api_sme_dashboard!"

@app.route("/api/large_org_json")
def sme_dashboard():
  return f"This is api_large_dashboard!"

@app.route("/dashboard")
def sme_dashboard():
  return f"This is dashboard!"

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))