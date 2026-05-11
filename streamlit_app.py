import streamlit as st

import requests


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Healthcare AI",
    layout="wide"
)


# -----------------------------------
# TITLE
# -----------------------------------

st.title("🏥 Healthcare AI System")

st.write("Upload Medical Report Image")


# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)


# -----------------------------------
# PROCESS BUTTON
# -----------------------------------

if uploaded_file is not None:

    if st.button("Analyze Report"):

        with st.spinner("Processing..."):

            files = {
                "file": uploaded_file
            }

            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                files=files
            )

            result = response.json()


            # -----------------------------------
            # OUTPUT
            # -----------------------------------

            st.success("Analysis Completed")


            st.subheader("📄 Extracted Text")

            st.text(result["extracted_text"])


            st.subheader("🦠 Detected Disease")

            st.write(result["disease"])


            st.subheader("📚 Medical Knowledge")

            st.write(result["rag_response"])


            st.subheader("🤖 AI Final Report")

            st.write(result["final_report"])