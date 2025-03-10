from models.contributor import Contributor, ContributorKeys as CKey
from streamlit import session_state as state


def get_user_obj() -> Contributor:
    user = state[CKey.USER_DATA.value]

    return user
