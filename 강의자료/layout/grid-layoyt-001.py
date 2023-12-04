import streamlit as st

# a 2x2 grid the long way
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for first chart')
    with col2:
        st.line_chart((0,1), height=100)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for second chart')
    with col2:
        st.line_chart((1,0), height=100)

st.code("""
import streamlit as st

# a 2x2 grid the long way
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for first chart')
    with col2:
        st.line_chart((0,1), height=100)
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write('Caption for second chart')
    with col2:
        st.line_chart((1,0), height=100)
""")
