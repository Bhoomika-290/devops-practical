from flask import Flask

app = Flask(__name__)   # ✅ MUST be before routes

@app.route("/")
def home():
    return "Hello! DevOps Practical Running Successfully"

@app.route("/login/<username>/<password>")
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)