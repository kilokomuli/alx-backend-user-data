#!/usr/bin/env python3
"""Routing module"""
from flask import Flask, jsonify


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
def home() -> str:
    """Basic route"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
