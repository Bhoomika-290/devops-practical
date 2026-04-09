@app.route("/login/<username>/<password>")
def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"