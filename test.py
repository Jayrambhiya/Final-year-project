import os
import streamlit as st
from PIL import Image
import main
def file_selector(folder_path='.'):
    filenames=[]
    for files in os.listdir(folder_path):
        if files.endswith(".png") or files.endswith("jpg"):
            filenames.append(files)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)
def submit(filename):
    main.main(filename)



if __name__ == '__main__':

    if st.checkbox('Select a file in current directory'):
        folder_path = '.'
        filename = file_selector(folder_path=folder_path)
        st.write('You selected `%s`' % filename)
        image = Image.open(filename)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")

    if st.button('Recognize'):
        submit(filename)
