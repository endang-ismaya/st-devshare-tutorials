"""
Main Program
"""

import streamlit as st
from streamlit import session_state as state
from py_templates.pages import pages_main
from models.contributor import ContributorKeys as Ckey

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
        Ckey.PAGE_NUM.value,
        Ckey.USER_DATA.value,
    )
):
    state[Ckey.PAGE_NUM.value] = 1
    state[Ckey.USER_DATA.value] = None


# running page with navigation
pages_main()
