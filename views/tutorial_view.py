from typing import Tuple
import pandas as pd

from pandas import DataFrame
from models.contributor import ContributorModel
from models.tutorial import TutorialModel
from utils.validation import validate_adding_tutorial


def add_tutorial_view(
    title: str,
    channel_name: str,
    video_url: str,
    brief_description: str,
    contributor_id: int,
) -> Tuple[bool, str]:
    """Adds a new tutorial to the database"""
    if contributor_id:
        tutorial_model = TutorialModel()

        is_valid, msg = validate_adding_tutorial(
            title,
            channel_name,
            tutorial_model,
        )

        if not is_valid:
            return False, msg

        # add tutorial
        is_created = tutorial_model.add(
            title,
            channel_name,
            video_url,
            brief_description,
            contributor_id,
        )

        if is_created:
            return True, "Tutorial added successfully!"

        return False, "Something went wrong! Failed to add tutorial."

    else:
        return False, "Contributor not found!"


def get_tutorials_pagination_view(
    page_num: int = 1,
    page_size: int = 10,
) -> Tuple[DataFrame, int]:
    """Retrieves all tutorials and return DataFrame and total pages."""
    tutorial_db = TutorialModel()
    tutorials_df: pd.DataFrame = tutorial_db.get_all()
    paged_df = pd.DataFrame()
    total_pages = 0

    if not tutorials_df.empty:
        contributor = ContributorModel()

        # mapping contributor's id to contributor's name
        contributor_map = {
            row["id"]: row["username"] for _, row in contributor.get_all().iterrows()
        }
        tutorials_df["contributor"] = tutorials_df["contributor_id"].map(
            contributor_map
        )
        # drop the contributor_id column
        tutorials_df = tutorials_df.drop("contributor_id", axis=1)

        # Create clickable links for the url
        tutorials_df["video_url"] = tutorials_df["video_url"].apply(
            lambda url: f'<a href="{url}" target="_blank">link</a>'
        )

        # get total pages
        start_idx = (page_num - 1) * page_size
        end_idx = start_idx + page_size
        paged_df = tutorials_df.iloc[start_idx:end_idx]
        total_pages = (len(tutorials_df) + page_size - 1) // page_size

    return paged_df, total_pages
