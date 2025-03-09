from typing import Tuple
from models.contributor import Contributor
from utils.fn_utils import validate_contributor_name


def add_contributor_view(
    name: str, linkedin_url: str, password: str
) -> Tuple[bool, str]:
    """Adds a new contributor to the database"""

    # cheking names
    if not validate_contributor_name(name):
        return False, "Contributor's name is not allowed!"

    # create an instance of Contributor
    contributor = Contributor()

    # check if contributor exists
    existing_contributor = contributor.get_by_name_object(name=name)
    if existing_contributor:
        return False, "Contributor's name already exists"

    # create new contributor
    is_created = contributor.add(name, linkedin_url, password)
    if is_created:
        return True, "Contributor added successfully"
    else:
        return False, "Failed to add contributor"
