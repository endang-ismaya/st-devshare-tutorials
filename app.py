"""
Main Program
"""

import streamlit as st
from streamlit import session_state as state
from py_templates.pages import pages_main

st.set_page_config(
    page_title="YouTube DevShare Tutorials!",
    page_icon=":material/youtube_activity:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# app initial state
if all(key not in state.keys() for key in ()):
    pass

# running page with navigation
pages_main()
