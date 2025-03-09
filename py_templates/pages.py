import streamlit as st
from _src.settings import PY_TEMPLATES_DIR


def pages_main():
    dashboard = st.Page(
        PY_TEMPLATES_DIR / "dashboard.py",
        title="Dashboard",
        icon=":material/browse_activity:",
        default=True,
    )

    manage = st.Page(
        PY_TEMPLATES_DIR / "manage.py",
        title="Manage",
        icon=":material/settings:",
    )

    page = st.navigation(
        {
            "Homepage": [dashboard],
            "Manage Tutrial": [manage],
        },
        expanded=True,
    )

    with st.sidebar:
        st.header("Welcome!")

    page.run()
