from typing import Tuple
import pandas as pd
from pandas import DataFrame
from _src.settings import MAX_NUM_CONTRIBUTOR
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

    # check max len of contributor
    current_count = len(contributor.get_all())
    if current_count >= MAX_NUM_CONTRIBUTOR:
        return False, f"Maximum number of contributors ({MAX_NUM_CONTRIBUTOR}) reached."

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


def get_contributors_pagination_view(
    page_num: int = 1, page_size: int = 10
) -> Tuple[DataFrame, int]:
    """Retrieves all contributors and return DataFrame."""
    contributor = Contributor()
    contributors_df: pd.DataFrame = contributor.get_all()
    paged_df = pd.DataFrame()
    total_pages = 0

    if not contributors_df.empty:
        # remove the password column.
        contributors_df = contributors_df.drop("password", axis=1)

        start_idx = (page_num - 1) * page_size
        end_idx = start_idx + page_size
        paged_df = contributors_df.iloc[start_idx:end_idx]
        total_pages = (len(contributors_df) + page_size - 1) // page_size

    return paged_df, total_pages
