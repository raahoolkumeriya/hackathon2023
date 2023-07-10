"""Running the Interface Application"""

import os
import streamlit as st
from food.streamlit_UI.multipage import MultiPage
from food.pages import homepage
from food.common.constants import StreamlitSetup


def main():
    """Application Entry Point"""
    # Initial page config
    st.set_page_config(
        page_title=StreamlitSetup.APPLICATION_TITLE.value,
        page_icon='🍔',
        layout="wide",
        initial_sidebar_state="expanded")

    st.markdown(StreamlitSetup.HIDE_STREAMLIT_STYLE.value, unsafe_allow_html=True)
    st.markdown(StreamlitSetup.PAGE_SETUP.value, unsafe_allow_html=True)

    st.sidebar.header("Bot Army `ʕ•́ᴥ•̀ʔ`")
    
    # Create an instance of the app
    app = MultiPage()

    # Add all your applications (pages) here
    app.add_page("Dashboard", homepage.app)
    #app.add_page("Develop Package", create_package.app)

    # The main app
    app.run()

    st.sidebar.subheader("`ツ` Contribute")
    col1, col2, col3 = st.sidebar.columns(3)
    col1.markdown(StreamlitSetup.GITHUB_STAR.value, unsafe_allow_html=True)
    col2.markdown(StreamlitSetup.GITHUB_WATCH.value, unsafe_allow_html=True)
    col3.markdown(StreamlitSetup.GITHUB_FORK.value, unsafe_allow_html=True)
    st.sidebar.subheader("`ツ` Connect")
    st.sidebar.markdown(StreamlitSetup.SOCIAL.value, unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()    
    