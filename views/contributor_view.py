import pandas as pd

from streamlit import session_state as state
from typing import Tuple
from pandas import DataFrame
from _src.settings import ADMIN_USER
from models.contributor import Contributor, ContributorModel, ContributorKeys as Ckey
from utils.validation import validate_contributor, validate_password, validate_username


def add_contributor_view(
    username: str, linkedin_url: str, password: str
) -> Tuple[bool, str]:
    """Adds a new contributor to the database"""

    # validating username
    is_valid, msg = validate_username(username)
    if not is_valid:
        return False, msg

    # validate password
    if not validate_password(password):
        return (False, "Password invalid. Please follow the criteria")

    # validate contributor
    # create an instance of Contributor
    contributor_db = ContributorModel()

    is_valid, msg = validate_contributor(username, contributor_db)
    if not is_valid:
        return False, msg

    # create new contributor
    is_created = contributor_db.add(username, linkedin_url, password)
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


def delete_contributor_view(username: str, password: str) -> Tuple[bool, str]:
    """Deletes a contributor by username"""
    contributor_db = ContributorModel()
    contributor_data: Contributor = contributor_db.get_by_username_object(username)
    contributor_admin: Contributor = contributor_db.get_by_username_object(ADMIN_USER)

    if contributor_data:
        # check password
        if contributor_db.check_password(
            password=password, hashed_password=contributor_data.hash_password
        ) or contributor_db.check_password(
            password=password, hashed_password=contributor_admin.hash_password
        ):
            is_deleted = contributor_db.delete_by_username(contributor_data.username)
            if is_deleted:
                return True, f"Contributor '{username}' has been deleted successfully"

            return False, "Error when deleting contributor"

        return False, "Incorrect username and/or password"

    return False, f"Contributor '{username}' not found."


def update_contributor_view(
    username: str,
    current_pwd: str,
    new_username: str,
    new_linkedin_url: str,
    new_pwd: str,
) -> Tuple[bool, str]:
    """Updates a contributor and displays a success message."""
    contributor_db = ContributorModel()
    current_contributor_data: Contributor = contributor_db.get_by_username_object(
        username
    )
    contributor_admin: Contributor = contributor_db.get_by_username_object(ADMIN_USER)

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
            contributor_db.update(
                contributor_id, new_username, new_linkedin_url, new_pwd
            )

            return True, f"Contributor '{username}' has been updated successfully"

        return False, "Incorrect name and/or current password"

    return False, f"Contributor '{username}' not found."


def user_login(username: str, password: str) -> Tuple[bool, str]:
    # create model instance
    contributor_db = ContributorModel()

    # check if username exists
    user = contributor_db.get_by_username_object(username)

    if not user:
        return False, "User not found!."

    # check password
    is_pwd_ok = contributor_db.check_password(
        password=password, hashed_password=user.hash_password
    )

    if not is_pwd_ok:
        return False, "User or Password Mismatch!"

    # set state
    state[Ckey.USER_DATA.value] = user

    return True, "Login Successful"
