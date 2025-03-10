import streamlit as st
from streamlit import session_state as state
from views.tutorial_callback import (
    increase_tutorial_page_num,
    decrease_tutorial_page_num,
)
from models.tutorial import TutorialKeys as Tkey
from views.tutorial_view import get_tutorials_pagination_view

st.title(":material/play_circle: Tutorial List", anchor=False)

page_num = state.get(Tkey.PAGE_NUM.value, 1)

tutorials_df, total_pages = get_tutorials_pagination_view(page_num)

if not tutorials_df.empty:
    # st.dataframe(contributors_df, hide_index=True)
    # display as html table
    html_table = tutorials_df.to_html(escape=False, index=False)
    st.markdown(html_table, unsafe_allow_html=True)
    st.write(f"Page {page_num} of {total_pages}")

    col1, col2, col3, col4 = st.columns([3, 3, 6, 6])

    if page_num > 1:
        col1.button(
            "Previous Page",
            on_click=increase_tutorial_page_num,
            type="primary",
            use_container_width=True,
            icon=":material/arrow_back_ios:",
            key="BTN_PREV_PAGE_TUTORIAL_1",
        )
    else:
        col1.button(
            "Previous Page",
            type="secondary",
            use_container_width=True,
            disabled=True,
            icon=":material/arrow_back_ios:",
            key="BTN_PREV_PAGE_TUTORIAL_2",
        )

    if page_num < total_pages:
        col2.button(
            "Next Page",
            on_click=decrease_tutorial_page_num,
            type="primary",
            use_container_width=True,
            icon=":material/arrow_forward_ios:",
            key="BTN_NEXT_PAGE_TUTORIAL_1",
        )
    else:
        col2.button(
            "Next Page",
            type="secondary",
            use_container_width=True,
            disabled=True,
            icon=":material/arrow_forward_ios:",
            key="BTN_NEXT_PAGE_TUTORIAL_2",
        )

else:
    st.warning("No videos found.")
