from flask import Flask, render_template
import os


app = Flask(__name__)


@app.get("/health")
def health():
    return 200


@app.get("/")
def render_links():
    render_context = {
#        #"hostpath": hostpath,
        "articles": [
            {
                "title":"Proxmox for your homelab",
                "link": "https://test.com"
            },
            {
                "title":"Setting Up a Hardened Linux server",
                "link": "https://test22.com"
            },
        ]
    }
    return render_template("index.html", **render_context)


@app.get("/blog")
def render_blog():
    return render_template("blog.html")


@app.get("/timeline")
def render_timeline():
    return render_template("timeline.html")


if __name__ == "__main__":
    app.run("0.0.0.0", os.getenv("PORT"))
