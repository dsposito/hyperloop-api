from flask import Flask, redirect, url_for

from api.api import api
from docs.docs import docs

# Boot the application and its components.
app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(docs)

@app.route("/")
def index():
    return redirect(url_for("docs.index"))
