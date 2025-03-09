import streamlit as st
from streamlit import session_state as state
from views.contributor_callback import (
    decrease_contributor_page_num,
    increase_contributor_page_num,
)
from views.contributor_view import get_contributors_pagination_view
from models.contributor import ContributorKeys as Ckey


st.title("Contributor List", anchor=False)

page_num = state.get(Ckey.PAGE_NUM.value, 1)

contributors_df, total_pages = get_contributors_pagination_view(page_num)

if not contributors_df.empty:
    st.dataframe(contributors_df, hide_index=True)

    st.write(f"Page {page_num} of {total_pages}")

    col1, col2, col3, col4 = st.columns([6, 3, 3, 6])

    if page_num > 1:
        col2.button(
            "Previous Page",
            on_click=decrease_contributor_page_num,
            type="primary",
            use_container_width=True,
        )
    else:
        col2.button(
            "Previous Page",
            type="secondary",
            use_container_width=True,
            disabled=True,
        )

    if page_num < total_pages:
        col3.button(
            "Next Page",
            on_click=increase_contributor_page_num,
            type="primary",
            use_container_width=True,
        )
    else:
        col3.button(
            "Next Page",
            type="secondary",
            use_container_width=True,
            disabled=True,
        )

else:
    st.write("No contributors found.")
