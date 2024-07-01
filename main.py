import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  """Home Page route."""
  return render_template('index.html')

@app.route("/pages/enterprise")
def enterprise_dashboard():
  return f"This is page enterprise_dashboard!"

@app.route("/pages/sme")
def sme_dashboard():
  return f"This is page sme_dashboard!"

@app.route("/pages/supplier")
def supplier_dashboard():
  return f"This is page supplier_dashboard!"

@app.route("/pages/help")
def help_pages():
  return f"This is some help!"

@app.route("/api/enterprise_dashboard")
def enterprise_api():
  return "{\"title\": \"This is the information to be displayed on the enterprise dashboard!\"}"

@app.route("/api/sme_dashboard")
def sme_api():
  return "{\"title\": \"This is the information to be displayed on the sme_dashboard!\"}"

@app.route("/api/supplier_dashboard")
def supplier_api():
  return "{\"title\": \"This is the information to be displayed on the supplier_dashboard!\"}"

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))