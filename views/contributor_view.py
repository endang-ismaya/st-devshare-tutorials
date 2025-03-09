from typing import Tuple
import pandas as pd
from pandas import DataFrame
from _src.settings import ADMIN_USER, MAX_NUM_CONTRIBUTOR
from models.contributor import Contributor, ContributorModel
from utils.fn_utils import validate_contributor_name, validate_password


def add_contributor_view(
    name: str, linkedin_url: str, password: str
) -> Tuple[bool, str]:
    """Adds a new contributor to the database"""

    # validate name
    if not validate_contributor_name(name):
        return False, "Contributor's name is not allowed!"

    if len(name) <= 4:
        return False, "Contributor's name is too short!"

    # validate password
    if not validate_password(password):
        return (False, "Password invalid. Please follow the criteria")

    # create an instance of Contributor
    contributor_db = ContributorModel()

    # check max len of contributor
    current_count = len(contributor_db.get_all())
    if current_count >= MAX_NUM_CONTRIBUTOR:
        return False, f"Maximum number of contributors ({MAX_NUM_CONTRIBUTOR}) reached."

    # check if contributor exists
    existing_contributor = contributor_db.get_by_name_object(name=name)
    if existing_contributor:
        return False, "Contributor's name already exists"

    # create new contributor
    is_created = contributor_db.add(name, linkedin_url, password)
    if is_created:
        return True, "Contributor has been succesfully registered."
    else:
        return False, "Failed to register contributor"


def get_contributors_pagination_view(
    page_num: int = 1, page_size: int = 10
) -> Tuple[DataFrame, int]:
    """Retrieves all contributors and return DataFrame and total pages."""
    contributor_db = ContributorModel()
    contributors_df: pd.DataFrame = contributor_db.get_all()
    paged_df = pd.DataFrame()
    total_pages = 0

    if not contributors_df.empty:
        # remove the password column.
        contributors_df = contributors_df.drop("password", axis=1)

        # Create clickable links
        contributors_df["linkedin_url"] = contributors_df["linkedin_url"].apply(
            lambda url: f'<a href="{url}" target="_blank">{url}</a>'
        )

        start_idx = (page_num - 1) * page_size
        end_idx = start_idx + page_size
        paged_df = contributors_df.iloc[start_idx:end_idx]
        total_pages = (len(contributors_df) + page_size - 1) // page_size

    return paged_df, total_pages


def delete_contributor_view(name: str, password: str) -> Tuple[bool, str]:
    """Deletes a contributor by name"""
    contributor_db = ContributorModel()
    contributor_data: Contributor = contributor_db.get_by_name_object(name)
    contributor_admin: Contributor = contributor_db.get_by_name_object(ADMIN_USER)

    if contributor_data:
        # check password
        if contributor_db.check_password(
            password=password, hashed_password=contributor_data.hash_password
        ) or contributor_db.check_password(
            password=password, hashed_password=contributor_admin.hash_password
        ):
            is_deleted = contributor_db.delete_by_name(contributor_data.name)
            if is_deleted:
                return True, f"Contributor '{name}' has been deleted successfully"

            return False, "Error when deleting contributor"

        return False, "Incorrect name and/or password"

    return False, f"Contributor '{name}' not found."


def update_contributor_view(
    name: str,
    current_pwd: str,
    new_name: str,
    new_linkedin_url: str,
    new_pwd: str,
) -> Tuple[bool, str]:
    """Updates a contributor and displays a success message."""
    contributor_db = ContributorModel()
    current_contributor_data: Contributor = contributor_db.get_by_name_object(name)
    contributor_admin: Contributor = contributor_db.get_by_name_object(ADMIN_USER)

    if current_contributor_data:
        # check password
        if contributor_db.check_password(
            password=current_pwd, hashed_password=current_contributor_data.hash_password
        ) or contributor_db.check_password(
            password=current_pwd, hashed_password=contributor_admin.hash_password
        ):
            # validate new password
            if not validate_password(new_pwd):
                return (False, "Password invalid. Please follow the criteria")

            contributor_id = current_contributor_data.user_id
            contributor_db.update(contributor_id, new_name, new_linkedin_url, new_pwd)

            return True, f"Contributor '{name}' has been updated successfully"

        return False, "Incorrect name and/or current password"

    return False, f"Contributor '{name}' not found."
