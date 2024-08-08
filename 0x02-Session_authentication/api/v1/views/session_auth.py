#1/usr/bin/env python3
"""Logout"""
from api.v1.app import auth
from api.v1.views import app_views
from flask import abort, jsonify, request
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles all routes for the session authentication"""
    email = request.form.get('email')

    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')

    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        found_users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not found_users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in found_users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
    user = found_users[0]
    session_id = auth.create_session(user.id)

    SESSION_NAME = getenv("SESSION_NAME")

    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """Delete a session"""
    sessiondel_id = auth.destroy_session(request)
    if not sessiondel_id:
        abort(404)

    return jsonify({}), 200
