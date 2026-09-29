import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="International Currency Detection",
    page_icon="💰"
)

st.title("💰 International Currency Detection")
st.write("AI and ML based currency detection using Python")

st.header("Upload Currency Image")

uploaded_file = st.file_uploader(
    "Choose a currency note image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Currency Note",
        use_container_width=True
    )

    st.success("Currency image uploaded successfully!")

    if st.button("Detect Currency"):

        st.info("Currency detection model is ready to be connected.")

        st.write("Country/Currency: Prediction will appear here")
        st.write("Denomination: Prediction will appear here")

else:
    st.info("Please upload a currency note image.")
