from flask import Flask

app = Flask(**name**)

@app.route("/")
def home():
return "Hello from Flask and Git!"

if **name** == "**main**":
app.run(debug=True)