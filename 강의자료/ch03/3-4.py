import streamlit as st
import pandas as pd

html = """
<a style='background:yellow'>This text has a yellow background</a>
"""

st.header("Without unsafe_allow_html=True")
st.markdown(html, unsafe_allow_html=True)

st.header("Without unsafe_allow_html=False")
st.markdown(html, unsafe_allow_html=False)
