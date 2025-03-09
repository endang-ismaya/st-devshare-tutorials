from streamlit import session_state as state
from models.contributor import ContributorKeys as Ckey


def increase_contributor_page_num():
    state[Ckey.PAGE_NUM.value] += 1


def decrease_contributor_page_num():
    state[Ckey.PAGE_NUM.value] -= 1
