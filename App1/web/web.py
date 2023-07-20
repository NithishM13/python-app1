import streamlit as st
import functions

todos = functions.read_todos()

st.title("My Web App")

st.header("To-Do App")
st.subheader("To increase user's productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a to-do ...")