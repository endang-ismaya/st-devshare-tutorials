"""
Main Program
"""

import streamlit as st
from streamlit import session_state as state
from py_templates.pages import pages_main

st.set_page_config(
    page_title="Youtube Programming Tutorials Tracker",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)


# app initial state
if all(key not in state.keys() for key in ()):
    pass


pages_main()
