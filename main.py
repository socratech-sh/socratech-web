from flask import Flask, render_template

app = Flask(__name__)


@app.get("/health")
def health():
    return 200


@app.get("/")
def render_links():
    return render_template("index.html")

@app.get("/blog")
def render_blog():
    return render_template("blog.html")


@app.get("/timeline")
def render_timeline():
    return render_template("timeline.html")


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
