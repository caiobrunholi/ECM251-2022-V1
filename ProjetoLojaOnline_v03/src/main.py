import time
from src.views.login import show_login_page
from src.views.home import show_home_page
import streamlit as st


if "state" in st.session_state:
    st.session_state["state"]
else:
    st.session_state["state"]=False

class Main():
    def __init__(self) -> None:
        if st.session_state["state"]:
            time.sleep(1)
            show_home_page()
        else:
            show_login_page()

app = Main()