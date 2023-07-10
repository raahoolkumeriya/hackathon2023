"""
File to store constants
"""
from enum import Enum

class StreamlitSetup(Enum):
    """
    Streamlit Setup
    """
    HIDE_STREAMLIT_STYLE = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'copyrights © 2023 BOT ARMY';
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 10px;
                top: 12px;
            }
            </style>
            """
    APPLICATION_TITLE = "Food Analysis"
    DASHBOARD_FEATURES = f"""
        - TODO: Features will go here
        """
    #DEVELOP_ART_FEATURES = f"""
    #- TODO: 
    #"""
  
    PADDING = 3
    PAGE_SETUP = f""" <style>
            .reportview-container .main .block-container{{
                padding-top: {PADDING - 2}rem;
                padding-right: {PADDING}rem;
                padding-left: {PADDING}rem;
                padding-bottom: {PADDING}rem;
            }} </style> """
    # Github button size display
    BUTTON_SIZE = 'count=true&size=large&v=2'
    # Github button display on sidebar SETUP
    REPO_URL = "https://ghbtns.com/github-btn.html?user=raahoolkumeriya&repo=hackathon2023"
    FORMAT_BUTTON = 'frameborder="0" scrolling="0" width="170" height="30" title="GitHub"'
    GITHUB_BTN = f'<iframe src="{REPO_URL}&{BUTTON_SIZE}" {FORMAT_BUTTON}></iframe>'
    GITHUB_STAR = f'<iframe src="{REPO_URL}&type=star&{BUTTON_SIZE}" {FORMAT_BUTTON}></iframe>'
    GITHUB_WATCH = f'<iframe src="{REPO_URL}&type=watch&{BUTTON_SIZE}" {FORMAT_BUTTON}></iframe>'
    GITHUB_FORK = f'<iframe src="{REPO_URL}&type=fork&{BUTTON_SIZE}" {FORMAT_BUTTON}></iframe>'

    SOCIAL = f'''
    <p align="left"> 
        <a href="https://github.com/raahoolkumeriya" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="raahoolkumeriya" height="30" width="40" /></a>
        <a href="https://twitter.com/kumeriyaRahul" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/twitter.svg" alt="kumeriyaRahul" height="30" width="40" /></a>
        <a href="https://linkedin.com/in/rahulkumeriya" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="rahulkumeriya" height="30" width="40" /></a>
    </p>'''