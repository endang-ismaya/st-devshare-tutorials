from streamlit import session_state as state
from models.tutorial import TutorialKeys as Tkey


def increase_tutorial_page_num():
    state[Tkey.PAGE_NUM.value] += 1


def decrease_tutorial_page_num():
    state[Tkey.PAGE_NUM.value] -= 1
