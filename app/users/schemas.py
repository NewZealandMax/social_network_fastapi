from http import HTTPStatus

import requests
from email_hunter import EmailHunterClient
from fastapi_users import schemas
from pydantic import validator

from app.core.config import settings

BASE_URL = 'https://api.emailhunter.co'
ACTIVE_EMAIL = 'deliverable'


class UserRead(schemas.BaseUser[int]):
    """Reads user info."""
    pass


class UserCreate(schemas.BaseUserCreate):
    """Creates new user."""

    @validator('email')
    def check_email_is_active(cls, value: str):
        response = requests.get(BASE_URL)
        if response.status_code == HTTPStatus.OK:
            client = EmailHunterClient(settings.EMAIL_HUNTER_KEY)
            if not client.verify(value)['result'] == ACTIVE_EMAIL:
                raise ValueError('Email doesn\'t exist')
        return value


class UserUpdate(schemas.BaseUserUpdate):
    """Updates existing user."""

    @validator('email')
    def check_email_is_active(cls, value: str):
        response = requests.get(BASE_URL)
        if response.status_code == HTTPStatus.OK:
            client = EmailHunterClient(settings.EMAIL_HUNTER_KEY)
            if not client.verify(value)['result'] == ACTIVE_EMAIL:
                raise ValueError('Email doesn\'nt exist')
        return value
