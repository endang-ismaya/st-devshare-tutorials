import time
import streamlit as st

from streamlit import session_state as state
from _src.settings import DEBUG, PY_TEMPLATES_DIR
from models.contributor import ContributorKeys as Ckey
from utils.user_util import get_user_obj
from utils.validation import is_authenticated
from views.contributor_view import user_login, user_logout


def pages_main():
    # unregistered user
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

    # Tutorial
    tutorial_add = st.Page(
        PY_TEMPLATES_DIR / "tutorials" / "tutorial_add.py",
        title="Add Tutorial",
        icon=":material/add_circle:",
    )
    tutorial_list = st.Page(
        PY_TEMPLATES_DIR / "tutorials" / "tutorial_list.py",
        title="List Tutorial",
        icon=":material/list_alt:",
    )

    page_data = {
        "Homepage": [homepage],
        "Manage Tutorial": [tutorial_list],
        "Manage Contributor": [contrib_register],
    }

    if is_authenticated():
        page_data["Homepage"].append(dashboard)
        page_data["Manage Contributor"].append(contributor_list)
        page_data["Manage Contributor"].append(contributor_edit)
        page_data["Manage Contributor"].append(contributor_deletion)
        page_data["Manage Contributor"].remove(contrib_register)
        page_data["Manage Tutorial"].append(tutorial_add)

    page = st.navigation(
        page_data,
        expanded=True,
    )

    with st.sidebar:
        user = get_user_obj()
        if user is None:
            # show login component
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            btn_login = st.button("Login", type="primary", icon=":material/login:")

            if btn_login:
                if username and password:
                    is_valid, msg = user_login(username, password)
                    if not is_valid:
                        st.error(msg)
                    else:
                        st.toast(msg)
                        time.sleep(1)
                        st.rerun()
                else:
                    st.error("Username and Password are required")
        else:
            st.write(f"Welcome, {user.username}!")
            btn_logout = st.button("Logout", type="primary", icon=":material/logout:")
            if btn_logout:
                user_logout()
                st.toast("Logged out successfully")
                time.sleep(1)
                st.rerun()

        if DEBUG:
            st.write(state)

    page.run()
