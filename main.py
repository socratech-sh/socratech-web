from flask import Flask, render_template

app = Flask(__name__)


@app.get("/health")
def health():
    return 200


@app.get("/")
def render_links():
    return render_template("links.html")


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
