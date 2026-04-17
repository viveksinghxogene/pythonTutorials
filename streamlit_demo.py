import streamlit as st
st.title('Hello this is my first stream lit usage program')
st.write('this is the text that i am writing and thats it')
inp_nmae=st.text_input('Enter you name')
if st.button("Say Hello"):
    st.success(f"Hello {inp_nmae}")