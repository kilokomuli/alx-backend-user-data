#!/usr/bin/env python3
"""Expiration date to a sessionID"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """session expiry class"""
    def __init__(self):
        """class instance"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Overload method"""
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user id session overload"""
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        if self.session_duration <= 0:
            return session_dict.get("user_id")
        if "created_at" not in session_dict:
            return None

        created_at = session_dict["created_at"]
        expired_at = created_at + timedelta(seconds=self.session_duration)
        if expired_at < datetime.now():
            return None
        return session_dict.get("user_id")
