import streamlit as st

from streamlit import session_state as state
from _src.settings import PY_TEMPLATES_DIR
from models.contributor import ContributorKeys as Ckey


def pages_main():
    homepage = st.Page(
        PY_TEMPLATES_DIR / "homepage.py",
        title="Homepage",
        icon=":material/home:",
        default=True,
    )

    dashboard = st.Page(
        PY_TEMPLATES_DIR / "dashboard.py",
        title="Dashboard",
        icon=":material/browse_activity:",
    )

    manage = st.Page(
        PY_TEMPLATES_DIR / "manage.py",
        title="Manage",
        icon=":material/settings:",
    )

    # Contributor
    contrib_register = st.Page(
        PY_TEMPLATES_DIR / "contributors" / "contributor_register.py",
        title="Register",
        icon=":material/person_add:",
    )
    contributor_list = st.Page(
        PY_TEMPLATES_DIR / "contributors" / "contributor_list.py",
        title="List",
        icon=":material/groups:",
    )
    contributor_deletion = st.Page(
        PY_TEMPLATES_DIR / "contributors" / "contributor_deletion.py",
        title="Delete",
        icon=":material/delete:",
    )
    contributor_edit = st.Page(
        PY_TEMPLATES_DIR / "contributors" / "contributor_edit.py",
        title="Edit",
        icon=":material/edit_note:",
    )

    page = st.navigation(
        {
            "Homepage": [homepage, dashboard],
            "Manage Tutrial": [manage],
            "Manage Contributor": [
                contrib_register,
                contributor_list,
                contributor_deletion,
                contributor_edit,
            ],
        },
        expanded=True,
    )

    with st.sidebar:
        if state[Ckey.USER_DATA.value] is None:
            # show login component
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            btn_login = st.button("Login", type="primary", icon=":material/login:")

            if btn_login:
                print(username, password)
                st.rerun()
        else:
            btn_logout = st.button("Logout", type="primary", icon=":material/logout")
            if btn_logout:
                state[Ckey.USER_DATA.value] = None
                st.rerun()

    page.run()
