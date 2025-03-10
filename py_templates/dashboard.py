import streamlit as st

from models.contributor import ContributorModel
from models.tutorial import TutorialModel

st.title("Dashboard", anchor=False)
st.divider()

# Summary Statistics
st.header("Summary", anchor=False)

tutorial_model = TutorialModel()
contributor = ContributorModel()

col1, col2 = st.columns(2)

tutorials_df = tutorial_model.get_all()
contributors_df = contributor.get_all()

col1.metric("Total Tutorials", len(tutorials_df), border=True)
col2.metric("Total Contributors", len(contributors_df), border=True)

# Tutorials by Channel
st.header("Tutorials by Channel", anchor=False)
with st.container(border=True):
    if not tutorials_df.empty:
        channel_counts = tutorials_df["channel_name"].value_counts()
        st.bar_chart(
            channel_counts,
            x_label="Channel",
            y_label="Number of Tutorials",
            use_container_width=True,
        )
    else:
        st.write("No tutorial data available.")

# Tutorials by Contributor
st.header("Tutorials by Contributor", anchor=False)
with st.container(border=True):
    if not tutorials_df.empty and not contributors_df.empty:
        contributor_map = {
            row["id"]: row["username"] for _, row in contributors_df.iterrows()
        }
        tutorials_df["contributor_name"] = tutorials_df["contributor_id"].map(
            contributor_map
        )
        contributor_tutorial_counts = tutorials_df["contributor_name"].value_counts()
        st.bar_chart(contributor_tutorial_counts)
    else:
        st.write("No tutorial or contributor data available.")
