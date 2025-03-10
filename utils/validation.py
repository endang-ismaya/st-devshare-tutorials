import re
from streamlit import session_state as state
from typing import Tuple
from _src.settings import CONTRIBUTOR_RESERVED_USERNAMES, MAX_NUM_CONTRIBUTOR
from models.contributor import ContributorModel, ContributorKeys as Ckey


def validate_contributor_username(name: str) -> bool:
    """
    Validates a contributor name, checking for reserved words.
    """
    for reserved in CONTRIBUTOR_RESERVED_USERNAMES:
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


def validate_username_alphabet(username: str) -> bool:
    """Validates a username (lowercase alphabets and underscores only)."""
    pattern = r"^[a-z_]+$"
    return re.match(pattern, username) is not None


def validate_username(username: str) -> Tuple[bool, str]:
    """Validate username with all validators"""

    # validate restricted usernames
    if not validate_contributor_username(username):
        return (
            False,
            "Username can not using restricted name, such as admin, root, etc!",
        )

    # validate length
    if len(username) <= 4:
        return False, "Username is too short!"

    if not validate_username_alphabet(username):
        return (
            False,
            "Username is not valid! Please use lower alphabet and underscore only.",
        )

    return True, "Username is valid!"


def validate_contributor(
    username: str, contributor_db: ContributorModel
) -> Tuple[bool, str]:
    """Validate username with all validators"""

    # check max len of contributor
    current_count = len(contributor_db.get_all())
    if current_count > MAX_NUM_CONTRIBUTOR:
        return False, f"Maximum number of contributors ({MAX_NUM_CONTRIBUTOR}) reached."

    # check if contributor exists
    existing_contributor = contributor_db.get_by_username_object(username)
    if existing_contributor:
        return False, "Contributor with this username already exists"

    return True, "Contributor is valid"


def is_authenticated() -> bool:
    return state[Ckey.USER_DATA.value] is not None
