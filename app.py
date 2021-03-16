import streamlit as st

filename = st.text_input('Enter a file path:')
try:
    with open(filename) as input:
        st.text(input.read())
except FileNotFoundError:
    st.error('File not found.')