from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

SECRET_KEY = "super-secret-password"

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
    """)

    c.execute("INSERT INTO users(username,password) VALUES('admin','admin123')")

    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        result = c.execute(query).fetchone()

        conn.close()

        if result:
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/comment", methods=["GET","POST"])
def comment():

    if request.method == "POST":

        comment = request.form["comment"]

        return f"Comment received: {comment}"

    return render_template("comment.html")

@app.route("/ping", methods=["GET","POST"])
def ping():

    if request.method == "POST":

        host = request.form["host"]

        output = os.popen("ping -c 1 " + host).read()

        return f"<pre>{output}</pre>"

    return """
    <form method='post'>
    Host: <input name='host'>
    <button>Ping</button>
    </form>
    """

@app.route("/config")
def config():
    return f"Secret key: {SECRET_KEY}"

if __name__ == "__main__":
    app.run(debug=True)