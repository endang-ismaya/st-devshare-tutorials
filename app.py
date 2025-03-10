"""
Main Program
"""

import streamlit as st
from streamlit import session_state as state
from py_templates.pages import pages_main
from models.contributor import ContributorKeys as Ckey
from models.tutorial import TutorialKeys as Tkey

st.set_page_config(
    page_title="YouTube DevShare Tutorials!",
    page_icon=":material/youtube_activity:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# app initial state
if all(
    key not in state.keys()
    for key in (
        # Contributor
        Ckey.PAGE_NUM.value,
        Ckey.USER_DATA.value,
        # Tutorial
        Tkey.PAGE_NUM.value,
        Tkey.SEARCH_TUTORIAL.value,
    )
):
    # Contributor
    state[Ckey.PAGE_NUM.value] = 1
    state[Ckey.USER_DATA.value] = None

    # Tutorial
    state[Tkey.PAGE_NUM.value] = 1
    state[Tkey.SEARCH_TUTORIAL.value] = None

# running page with navigation
pages_main()
