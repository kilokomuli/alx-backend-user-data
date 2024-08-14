#!/usr/bin/env python3
"""hash password"""
import bcrypt
from user import User
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()


def _hash_password(password: str) -> bytes:
    """Returns bytes as a salted hash of the input
    password"""
    e_pwd = password.encode()
    return bcrypt.hashpw(e_pwd, bcrypt.gensalt())
