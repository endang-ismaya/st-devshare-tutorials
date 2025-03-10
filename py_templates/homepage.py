import streamlit as st

from _src.settings import APP_VERSION

st.title(":material/youtube_activity:  YouTube DevShare Tutorials!", anchor=False)


st.write(
    """
    This is a community-driven platform where developers share their favorite YouTube programming tutorials. 
    Contribute your knowledge and discover valuable resources to enhance your coding skills!
    """
)

st.header("Why DevShare Tutorials?", anchor=False)

st.markdown(
    """
    * **Community-Curated:** Discover tutorials recommended by fellow developers.
    * **Share Your Knowledge:** Contribute your favorite tutorials to help others.
    * **Diverse Topics:** Find tutorials covering a wide range of programming languages and technologies.
    * **Collaborative Learning:** Learn together and support each other's growth.
    """
)

st.subheader("How to Contribute:", anchor=False)

st.write(
    """
    1.  You need to register as a contributor to contribute to the app. Use the "Register" on "Manage Contributor"
    2.  Login with your credential on the sidebar
    2.  Use the "Add Tutorial" section to submit your favorite YouTube programming tutorials.
    3.  Provide the tutorial title, channel, video url or playlist (if applicable), and a brief description.
    """
)

st.subheader("Explore and Learn:", anchor=False)

st.write(
    """
    * Browse the "Tutorial List" to find valuable resources.
    * Use the search functionality to find tutorials on specific topics [coming soon].
    """
)

st.write("Let's learn and grow together!")

st.write(
    ":material/sentiment_very_satisfied: Happy Learning! :material/sentiment_very_satisfied:"
)


# FOOTER
st.divider()
cola, colb, colc, cold = st.columns(spec=4)
cola.write("Made with patience and 💝")
colb.write(f"Streamlit v{st.__version__}")
colc.write(f"App Version: {APP_VERSION}")
cold.markdown(
    "<p style='text-align: right;'>endang.ismaya@2025</p>",
    unsafe_allow_html=True,
)
