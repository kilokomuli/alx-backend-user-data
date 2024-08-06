#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Defines routes that dont need authentication"""
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user"""
        return None
