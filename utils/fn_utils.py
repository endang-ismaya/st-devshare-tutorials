import re
from _src.settings import CONTRIBUTOR_RESERVED_NAMES


def validate_contributor_name(name: str) -> bool:
    """
    Validates a contributor name, checking for reserved words.
    """
    for reserved in CONTRIBUTOR_RESERVED_NAMES:
        if reserved.casefold() in name.casefold():
            return False
    return True


def validate_password(password: str) -> bool:
    """
    Validates a password based on the following criteria:
    - Minimum length of 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character (!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?)
    """
    if len(password) < 8:
        return False

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).+$"
    return re.match(pattern, password) is not None
