import streamlit as st
import time
from views.contributor_view import update_contributor_view

st.title(":material/edit_note: Contributor Update", anchor=False)

name = st.text_input(
    label="Contributor Name",
    key="TXT_CONTRIBUTOR_NAME_UPDATE",
    help="Name should be case-sensitive!",
)
st.markdown(
    "<small style='color:red;'>*Name should be case-sensitive</small>",
    unsafe_allow_html=True,
)

st.divider()
new_name = st.text_input(
    label="New Contributor Name",
    key="TXT_CONTRIBUTOR_NEW_NAME_UPDATE",
    help="Name should be case-sensitive!",
)
new_linkedin_url = st.text_input(
    label="New Contributor Linkedin URL",
    key="TXT_CONTRIBUTOR_NEW_LINKEDIN_URL_UPDATE",
)
current_password = st.text_input(
    label="Contributor Current Password",
    key="TXT_CONTRIBUTOR_CURRENT_PASSWORD_UPDATE",
    type="password",
)
new_password = st.text_input(
    label="Contributor New Password",
    key="TXT_CONTRIBUTOR_NEW_PASSWORD_UPDATE",
    type="password",
)
st.markdown(
    """
    <small>New Password should meet the following criteria:</small><br>
    <small>- Minimum length of 8 characters</small><br>
    <small>- At least one uppercase letter</small><br>
    <small>- At least one lowercase letter</small><br>
    <small>- At least one digit</small><br>
    <small>- At least one special character (!@#$%^&*()_+-=[]{};':"\\|,.<>/?)</small>
    """,
    unsafe_allow_html=True,
)

if st.button(
    label="Update Contributor",
    key="BTN_CONTRIBUTOR_UPDATE",
    type="primary",
    icon=":material/edit_note:",
):
    if name and new_name and new_linkedin_url and current_password and new_password:
        is_ok_to_updated, msg = update_contributor_view(
            name=name,
            current_pwd=current_password,
            new_name=new_name,
            new_linkedin_url=new_linkedin_url,
            new_pwd=new_password,
        )
        if is_ok_to_updated:
            st.success(msg)
        else:
            st.error(msg)

    else:
        st.error("All fields are required.")

    time.sleep(1.5)
    st.rerun()
