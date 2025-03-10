import streamlit as st
import time
from views.contributor_view import delete_contributor_view

st.title(":material/delete: Contributor Deletion", anchor=False)

username = st.text_input(
    label="Contributor Username",
    key="TXT_CONTRIBUTOR_NAME_DELETE",
    help="Name should be case-sensitive!",
)
st.markdown(
    "<small style='color:red;'>*Username should be case-sensitive</small>",
    unsafe_allow_html=True,
)
password = st.text_input(
    label="Contributor Password",
    key="TXT_CONTRIBUTOR_PASSWORD_DELETE",
    type="password",
)

st.warning("Are you sure you want to delete? This process cannot be undone.")
if st.button(
    label="Delete Contributor",
    key="BTN_CONTRIBUTOR_DELETE",
    type="primary",
    icon=":material/delete:",
):
    if username and password:
        is_ok_to_del, msg = delete_contributor_view(username, password)
        if is_ok_to_del:
            st.success(msg)
        else:
            st.error(msg)

        time.sleep(1)
        st.rerun()
    else:
        st.error("Username and Password are required.")
