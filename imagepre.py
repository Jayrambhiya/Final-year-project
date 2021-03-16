import streamlit as st
from PIL import Image
st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="png")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
