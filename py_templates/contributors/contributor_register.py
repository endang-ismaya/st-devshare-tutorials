import streamlit as st
from views.contributor_view import add_contributor_view

st.title("Contributor Registration", anchor=False)

with st.form("add_contributor_form"):
    name = st.text_input("Name")
    linkedin_url = st.text_input("LinkedIn URL (Optional)")
    password = st.text_input("Password", type="password")  # Password input
    st.markdown(
        """
    <small>Validates a password based on the following criteria:</small><br>
    <small>- Minimum length of 8 characters</small><br>
    <small>- At least one uppercase letter</small><br>
    <small>- At least one lowercase letter</small><br>
    <small>- At least one digit</small><br>
    <small>- At least one special character (!@#$%^&*()_+\-=\[\]{};':"\\|,.<>/?)</small>
    """,
        unsafe_allow_html=True,
    )
    submit_button = st.form_submit_button(
        "Add Contributor", type="primary", icon=":material/person_add:"
    )

    if submit_button:
        if not name or not password:
            st.error("Name and password are required fields.")
        else:
            is_created, msg = add_contributor_view(name, linkedin_url, password)
            if is_created:
                st.toast(msg, icon="🎉")
            else:
                st.toast(msg, icon="😭")
