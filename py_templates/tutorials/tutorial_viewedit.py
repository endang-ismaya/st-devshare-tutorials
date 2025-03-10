import time
from typing import Union
import streamlit as st

from streamlit import session_state as state
from _src.settings import MAX_NUM_TUTORIALS
from models.contributor import Contributor
from models.tutorial import Tutorial, TutorialModel, TutorialKeys as Tkey
from utils.user_util import get_user_obj
from views.tutorial_view import update_tutorial_view

st.title(":material/movie_edit: View & Edit Tutorial", anchor=False)
st.divider()

user: Contributor = get_user_obj()
tutorial: Union[Tutorial, None] = state[Tkey.SEARCH_TUTORIAL.value]
cola, colb = st.columns(2)

with cola.form("search_tutorial"):
    col1, col2 = st.columns([8, 4])
    tutorial_id = col1.number_input(
        label="Enter Tutorial ID",
        min_value=1,
        max_value=MAX_NUM_TUTORIALS,
        step=1,
        key="TXT_TUTORIAL_ID",
        value=(1 if not tutorial else tutorial.tutorial_id),
    )
    col2.markdown("<p style='margin-top: 30px;'></p>", unsafe_allow_html=True)
    btn_search = col2.form_submit_button(
        label="Search Tutorial",
        type="primary",
        icon=":material/search:",
        use_container_width=True,
    )

    if btn_search:
        tutorial_db = TutorialModel()
        tutorial = tutorial_db.get_tutorial_by_id(tutorial_id)
        if tutorial:
            state[Tkey.SEARCH_TUTORIAL.value] = tutorial

edit_part, delete_part = st.columns(2)

if tutorial and (tutorial.contributor_id == user.user_id):
    with edit_part.expander("Edit Tutorial"):
        with st.form("edit_tutorial_form"):
            title = st.text_input("Title", value=tutorial.title)
            channel_name = st.text_input("Channel Name", value=tutorial.channel_name)
            video_url = st.text_input("Video URL", value=tutorial.video_url)
            brief_description = st.text_area(
                "Brief Description", value=tutorial.brief_description
            )
            submit_button = st.form_submit_button(
                "Update Tutorial", type="primary", icon=":material/save:"
            )

            if submit_button:
                is_updated, msg = update_tutorial_view(
                    tutorial.tutorial_id,
                    title,
                    channel_name,
                    video_url,
                    brief_description,
                )

                if is_updated:
                    st.success(msg)
                else:
                    st.error(msg)

                time.sleep(1.5)
                st.rerun()

if tutorial:
    with st.container(border=True):
        st.write(f"Tutorial ID: {tutorial.tutorial_id}")
        st.write(f"Tutorial Title: {tutorial.title}")
        st.write(f"Channel Name: {tutorial.channel_name}")
        st.write(f"Description: {tutorial.brief_description}")
        st.divider()
        col1, col2, col3 = st.columns([3, 6, 3])
        col2.video(tutorial.video_url)
