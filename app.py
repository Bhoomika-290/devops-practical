from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello I'm Bhoomika<br>I live in Ghatkopar<br>My roll no. 13<br>I'm 20<br>I like foods"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)