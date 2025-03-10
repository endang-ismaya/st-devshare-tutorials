from typing import Tuple
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
