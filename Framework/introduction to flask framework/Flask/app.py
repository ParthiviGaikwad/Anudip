from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to my first App in Flask</h1>"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to my Index page</h2>"

@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is " + str(score)

# Run the app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
