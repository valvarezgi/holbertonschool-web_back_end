#!/usr/bin/env python3
"""
Basic authentication module for API
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
from models.base import DATA


class BasicAuth(Auth):
    """basic authentication handling"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns Base64 part of the Authorization header for basic auth"""
        if authorization_header is None or type(authorization_header) != str \
           or authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns decoded value of Base64 str base64_authorization_header"""
        if base64_authorization_header is None or \
           type(base64_authorization_header) != str:
            return None
        try:
            decoded_header = base64.b64decode(base64_authorization_header)
        except base64.binascii.Error:
            return None
        try:
            return decoded_header.decode('utf-8')
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """returns user email and password from Base64 decoded value"""
        if decoded_base64_authorization_header is None or \
           type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on email and password"""
        if user_email is None or type(user_email) != str \
           or user_pwd is None or type(user_pwd) != str:
            return None
        if not DATA.get('User'):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        auth_header = super().authorization_header(request)
        extracted_ah = self.extract_base64_authorization_header(auth_header)
        decoded_ah = self.decode_base64_authorization_header(extracted_ah)
        email, password = self.extract_user_credentials(decoded_ah)
        return self.user_object_from_credentials(email, password)
