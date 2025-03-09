import streamlit as st

from _src.settings import APP_VERSION

st.title(":material/youtube_activity:  YouTube DevShare Tutorials!")


st.write(
    """
    This is a community-driven platform where developers share their favorite YouTube programming tutorials. 
    Contribute your knowledge and discover valuable resources to enhance your coding skills!
    """
)

st.header("Why DevShare Tutorials?")

st.markdown(
    """
    * **Community-Curated:** Discover tutorials recommended by fellow developers.
    * **Share Your Knowledge:** Contribute your favorite tutorials to help others.
    * **Diverse Topics:** Find tutorials covering a wide range of programming languages and technologies.
    * **Collaborative Learning:** Learn together and support each other's growth.
    """
)

st.subheader("How to Contribute:")

st.write(
    """
    1.  Use the "Add Tutorial" section to submit your favorite YouTube programming tutorials.
    2.  Provide the tutorial title, channel, playlist (if applicable), and a brief description.
    3.  Mention your name or email as a contributor to get credit for your submission.
    """
)

st.subheader("Explore and Learn:")

st.write(
    """
    * Browse the "Tutorial List" to find valuable resources.
    * Use the search functionality to find tutorials on specific topics.
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
