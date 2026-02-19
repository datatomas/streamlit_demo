import streamlit as st
import os

st.title("Qualityx AI" )
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
st.image(os.path.join(os.path.join(os.getcwd(),"static","call_center.jpg")), caption="Call center analytics in action")