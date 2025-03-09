# _src/settings/home.py (or wherever your PY_TEMPLATES_DIR points)

import streamlit as st

st.title(":material/youtube_activity: YouTube Programming Tutorial Tracker!")

st.write(
    """
    This application is designed to help you organize and track your progress through YouTube programming tutorials. 
    Whether you're learning a new language, framework, or concept, this tool will keep you on top of your studies.
    """
)

st.header("Key Features:")

st.markdown(
    """
    * **Add Tutorials:** Easily input tutorial details like title, channel, playlist, and status.
    * **Track Progress:** Update the status of your tutorials as you move from 'To Watch' to 'Completed'.
    * **Search and Filter:** Quickly find specific tutorials.
    * **Organize Your Learning:** Keep all your learning resources in one place.
    * **Object Oriented Data:** The application can return database results as python objects.
    """
)

st.subheader("How to Use:")

st.write(
    """
    1.  Use the navigation menu on the left to explore different sections of the app.
    2.  Add new tutorials to your list using the 'Add Tutorial' section.
    3.  Update the status of tutorials as you progress.
    4.  Search for tutorials using the search functionality.
    """
)

st.write(
    ":material/sentiment_very_satisfied: Happy Learning! :material/sentiment_very_satisfied:"
)


# FOOTER
st.divider()
cola, colb, col3 = st.columns(spec=3)
cola.write("Made with patience and 💝")
colb.write(f"Streamlit v{st.__version__}")
col3.markdown(
    "<p style='text-align: right;'>endang.ismaya@2025</p>",
    unsafe_allow_html=True,
)
