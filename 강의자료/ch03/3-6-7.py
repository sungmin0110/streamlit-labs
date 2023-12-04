import streamlit as st

st.sidebar.header("Sidebar Header")

st.header("Columns")
cols = st.columns(2)
cols[0].write("Column 1")
cols[1].write("Column 2")

expander = st.expander("This is an Expander")
expander.write("This is some text in an expander...")

st.header("Container")
container = st.container()
container.write("This is some text inside a container...")

tabs = st.tabs(["Tab 1", "Tab 2"])
for i, tab in enumerate(tabs):
    tabs[i].write(f"Tab {i+1}")


st.header("Empty")

empty = st.empty()
items = ["Tom", "Fred", "Stephanie"]
for item in items:
    empty.write(item)
