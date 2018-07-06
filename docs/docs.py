from flask import Blueprint, render_template

docs = Blueprint("docs", "docs", url_prefix="/docs", template_folder="templates", static_folder="static")

@docs.route("/")
def index():
    return render_template("index.html")
