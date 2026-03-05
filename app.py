from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Upwind CI/CD Lab, test - here we go again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

