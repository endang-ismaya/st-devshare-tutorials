from _src.settings import CONTRIBUTOR_RESERVED_NAMES


def validate_contributor_name(name: str) -> bool:
    """
    Validates a contributor name, checking for reserved words.
    """
    for reserved in CONTRIBUTOR_RESERVED_NAMES:
        if reserved.casefold() in name.casefold():
            return False
    return True
