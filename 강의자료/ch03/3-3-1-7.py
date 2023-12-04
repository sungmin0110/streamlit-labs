import streamlit as st

st.title("This a Title.")
st.code('''
st.title("This a Title.")
''')

st.header("This a Header.")
st.code('''
st.header("This a Header.")
''')

st.subheader("This a Subheader.")
st.code('''
st.subheader("This a Subheader.")
''')

st.write("This is text.")
st.code('''
st.write("This is text.")
''')

st.caption("This a Caption.")
st.code('''
st.caption("This a Caption.")
''')

with open("../contents/README.md", "r", encoding="UTF8") as f:
    markdown_text = f.read()
st.markdown(markdown_text, unsafe_allow_html =True)

st.code('''
with open("./contents/README.md", "r") as f:
    markdown_text = f.read()
st.markdown(markdown_text, unsafe_allow_html =True)
''')
