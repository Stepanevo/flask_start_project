from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.get("/")
def root():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # пока без проверки, просто редирект
        return redirect(url_for("index"))
    return render_template("login.html")

@app.get("/index")
def index():
    return render_template("index.html")

@app.get("/hello")
def hello():
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug=True)
