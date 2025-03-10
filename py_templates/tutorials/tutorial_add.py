import time
import streamlit as st

from models.contributor import Contributor
from utils.user_util import get_user_obj
from views.tutorial_view import add_tutorial_view

st.title(":material/add_circle: Add Tutorial", anchor=False)
st.divider()

user: Contributor = get_user_obj()


if user:
    with st.form("add_tutorial_form"):
        title = st.text_input("Title")
        channel_name = st.text_input("Channel Name")
        video_url = st.text_input("Video URL")
        brief_description = st.text_area("Brief Description [optional]")
        submit_button = st.form_submit_button(
            "Add Tutorial", type="primary", icon=":material/add:"
        )

        if submit_button:
            if not title or not channel_name or not video_url:
                st.error("Title, Channel Name, video_url are required fields.")
            else:
                is_created, msg = add_tutorial_view(
                    title,
                    channel_name,
                    video_url,
                    brief_description,
                    user.user_id,
                )

                if is_created:
                    st.success(msg)
                else:
                    st.error(msg)

                time.sleep(1.5)
                st.rerun()

else:
    st.warning("Seems like you are not logged in.")
