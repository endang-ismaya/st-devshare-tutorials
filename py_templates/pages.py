import streamlit as st
from _src.settings import PY_TEMPLATES_DIR


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

    page = st.navigation(
        {
            "Homepage": [homepage, dashboard],
            "Manage Tutrial": [manage],
        },
        expanded=True,
    )

    with st.sidebar:
        st.header("Welcome!")

    page.run()
