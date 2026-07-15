# app/utils/validators.py

import re


def validate_phone(phone: str):

    pattern = r"^\+?[0-9]{10,15}$"

    return bool(
        re.match(
            pattern,
            phone
        )
    )


def validate_serial(serial: str):

    return len(serial) >= 8


def validate_amount(amount: float):

    return amount > 0