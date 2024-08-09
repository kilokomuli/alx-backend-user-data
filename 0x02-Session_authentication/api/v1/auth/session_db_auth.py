#!/usr/bin/env python3
"""New authentication class"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """session dbauth class"""
    def create_session(self, user_id=None):
        """creates and stores new instance of UserSession"""session_id = super().create_session(user_id)

    if session_id is None:
        return None

     kwargs = {'user_id': user_id, 'session_id': session_id}
        user_session = UserSession(**kwargs)
        user_session.save()
        UserSession.save_to_file()

        return session_id
