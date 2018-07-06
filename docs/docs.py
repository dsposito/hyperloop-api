from flask import Blueprint, render_template

from docs.openapi import OpenAPI

import os

docs = Blueprint("docs", "docs", url_prefix="/docs", template_folder="templates", static_folder="static")

@docs.route("/")
def index():
    # Keep docs up-to-date by rebuilding on each page load.
    if os.environ.get("FLASK_ENV") == "development":
        OpenAPI.buildSpec()

    return render_template("index.html")
