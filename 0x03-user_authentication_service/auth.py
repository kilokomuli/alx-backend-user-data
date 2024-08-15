#!/usr/bin/env python3
"""hash password"""
import bcrypt
from user import User
from db import DB
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user by email and password"""
        db = self._db
        try:
            usser = db.find_user_by(email=email)
        except NoResultFound:
            user = db.add_user(email, _hash_password(password))
            return user
        else:
            raise ValueError(f"User {email} already exists")


def _hash_password(password: str) -> bytes:
    """Returns bytes as a salted hash of the input
    password"""
    e_pwd = password.encode()
    return bcrypt.hashpw(e_pwd, bcrypt.gensalt())
