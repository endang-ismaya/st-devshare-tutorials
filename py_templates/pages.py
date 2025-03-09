import streamlit as st
from _src.settings import PY_TEMPLATES_DIR, THANK_YOU_MESSAGES


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

    page = st.navigation(
        {
            "Homepage": [homepage, dashboard],
            "Manage Tutrial": [manage],
            "Manage Contributor": [
                contrib_register,
                contributor_list,
                contributor_deletion,
            ],
        },
        expanded=True,
    )

    with st.sidebar:
        for message in THANK_YOU_MESSAGES.values():
            st.markdown(f"**{message}**")

    page.run()
