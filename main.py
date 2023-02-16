from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["name"]
    password = request.form["password"]
    credentials = "Name: " + name + ", Password: " + password
    return f"<h1>{credentials}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
