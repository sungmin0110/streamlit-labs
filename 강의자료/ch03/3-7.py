import streamlit as st

if "prev_word_count" not in st.session_state:
    st.session_state["prev_word_count"] = 5

text = st.text_area("Paste text here to get word count.", "This is some default text.")
word_count = len(text.split())
change = word_count - st.session_state.prev_word_count
st.metric("Word Count", word_count, change)
st.session_state.prev_word_count = word_count
