from models.contributor import Contributor


def add_contributor_view(name: str, linkedin_url: str, password: str) -> bool:
    """Adds a new contributor to the database"""
    contributor = Contributor()
    is_created = contributor.add(name, linkedin_url, password)
    return is_created
