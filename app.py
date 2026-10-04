from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello from Flask and Git!"

@app.route("/search")
def search():
  return "search"

@app.route("/booking")
def booking():
  return booking

if __name__ == "__main__ ":
  app.run(debug=True)
