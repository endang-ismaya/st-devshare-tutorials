import streamlit as st
from streamlit import session_state as state
from views.contributor_callback import (
    decrease_contributor_page_num,
    increase_contributor_page_num,
)
from views.contributor_view import get_contributors_pagination_view
from models.contributor import ContributorKeys as Ckey


st.title(":material/user_attributes: Contributor List", anchor=False)
st.divider()

page_num = state.get(Ckey.PAGE_NUM.value, 1)

contributors_df, total_pages = get_contributors_pagination_view(page_num)

if not contributors_df.empty:
    # st.dataframe(contributors_df, hide_index=True)
    # display as html table
    html_table = contributors_df.to_html(escape=False, index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    st.write(f"Page {page_num} of {total_pages}")

    col1, col2, col3, col4 = st.columns([3, 3, 6, 6])

    if page_num > 1:
        col1.button(
            "Previous Page",
            on_click=decrease_contributor_page_num,
            type="primary",
            use_container_width=True,
            icon=":material/arrow_back_ios:",
        )
    else:
        col1.button(
            "Previous Page",
            type="secondary",
            use_container_width=True,
            disabled=True,
            icon=":material/arrow_back_ios:",
        )

    if page_num < total_pages:
        col2.button(
            "Next Page",
            on_click=increase_contributor_page_num,
            type="primary",
            use_container_width=True,
            icon=":material/arrow_forward_ios:",
        )
    else:
        col2.button(
            "Next Page",
            type="secondary",
            use_container_width=True,
            disabled=True,
            icon=":material/arrow_forward_ios:",
        )

else:
    st.warning("No contributors found.")
