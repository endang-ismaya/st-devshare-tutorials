import streamlit as st
import time

from streamlit import session_state as state
from views.contributor_view import update_contributor_view
from models.contributor import Contributor, ContributorKeys as Ckey

st.title(":material/edit_note: Contributor Update", anchor=False)

user: Contributor = state[Ckey.USER_DATA.value]

if user:
    username = st.text_input(
        label="Contributor Username",
        key="TXT_CONTRIBUTOR_NAME_UPDATE",
        value=user.username,
        disabled=True,
    )

    st.divider()
    new_username = st.text_input(
        label="New Contributor Username",
        key="TXT_CONTRIBUTOR_NEW_USERNAME_UPDATE",
        value=user.username,
    )
    st.markdown(
        "<small>Username should meet the following criteria:</small><br>"
        "<small >- Lowercase alphabets and underscores only</small><br>"
        "<small >- Minimum length of 5 characters</small>",
        unsafe_allow_html=True,
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
        if (
            username
            and new_username
            and new_linkedin_url
            and current_password
            and new_password
        ):
            is_ok_to_updated, msg = update_contributor_view(
                username=username,
                current_pwd=current_password,
                new_username=new_username,
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

else:
    st.warning("Seems like you are not logged in.")
