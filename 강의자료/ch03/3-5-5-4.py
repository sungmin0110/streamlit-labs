import streamlit as st
import datetime

user_text = st.text_input("Input some text here")
st.write(user_text)

default_text = st.text_area("Input some text here", "default text")
st.write(default_text)

user_number = st.number_input("Input Number",
                            min_value=1,
                            max_value=10,
                            value=5,
                            step=1)
st.write(user_number)

slider_number = st.slider("Select your Number",
                            min_value=1,
                            max_value=10,
                            value=5,
                            step=1)
st.write(slider_number)

user_date = st.date_input("Select your Date",
                            value = datetime.date(2000, 6, 12),
                            min_value = datetime.date(2000, 1, 12),
                            max_value = datetime.date(2001, 1, 12)
                            )

st.write(user_date)

user_time = st.time_input("Select your Time",
                            value = datetime.time(6, 12),
                            )
st.write(user_time)

checked = st.checkbox("Select this checkbox")
st.write(f"Current state of checkbox: {checked}")

state = st.button("Click to Change current state")
st.write(f"Button has been pressed: {state}")

options = ["Red", "Blue", "Yellow"]
radio_selection = st.radio("Select Color", options)
st.write(f"Color selected is {radio_selection}")

options = ["Red", "Blue", "Yellow"]
selectbox_selection = st.selectbox("Select Color", options)
st.write(f"Color selected is {selectbox_selection}")

options = ["Red", "Blue", "Yellow"]
multiselect_selection = st.multiselect("Select Color", options)
st.write(f"Color selected is {multiselect_selection}")


