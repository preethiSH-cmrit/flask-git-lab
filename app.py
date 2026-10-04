from flask import Flask

app = Flask(**name**)

@app.route("/")
def home():
  return "Hello from Flask and Git!"

@app.route("/search")
def search():
  return "search"

if **name** == "**main**":
app.run(debug=True)
