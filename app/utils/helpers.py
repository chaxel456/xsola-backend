# app/utils/helpers.py

import uuid
from datetime import datetime


def generate_reference(prefix: str):
    return f"{prefix}-{uuid.uuid4().hex[:10]}"


def current_timestamp():
    return datetime.utcnow()


def success_response(
    message: str,
    data=None
):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(
    message: str
):
    return {
        "success": False,
        "message": message
    }