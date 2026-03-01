import streamlit as st
import os
from pathlib import Path
import pandas as pd 
# use this so it does not lose context
HERE = Path(__file__).resolve().parent
img_path = HERE / "static" / "qualityxv2.png"   # or qualityx.jpg
img_path_1 = HERE / "static" / "qualityx.png"   # or qualityx.jpg


st.title("Qualityx AI" )
st.image(str(img_path), caption="Call center analytics in action")

st.header("Analytics for call centers of the future")
st.subheader("What's a call center without analytics? ")
st.markdown(" This is the AI _future_ of call centers, and we're here to help you *get there*. ")
st.caption("Don't worry this is not AGI yet")
code = """
def greet(name):
    print(f"Hello, {name}!")
"""
st.code(code, language="python")
st.divider()



st.image(str(img_path_1), caption="Call center analytics in action")
