from flask import Flask
from fibbonachi import fibb

app = Flask(__name__)

@app.route("/")
def main_page():
    return "<h1>Fibonachi generator</h1>"

@app.route("/<int:num>")
def generate(num):
    fib = fibb()
    return [next(fib) for i in range(num)]

if __name__ == "__main__":
    app.run(host="localhost", port=8000)

