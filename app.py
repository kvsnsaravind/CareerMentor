import streamlit as st
from utils.file_parser import extract_text_from_file
from controller.controller import process_request

st.set_page_config(page_title="CareerMentor", layout="centered")
st.title("🎯 CareerMentor – AI-Powered Resume & Interview Coach")

# Upload resume
uploaded_file = st.file_uploader("📄 Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("💼 Target Job Role (e.g., Backend Engineer)")

# Choose task
task = st.radio("What do you want help with?", ["Resume Feedback", "Interview Questions"])
task_map = {"Resume Feedback": "feedback", "Interview Questions": "interview"}

if st.button("🔍 Analyze"):
    if uploaded_file and job_role:
        with st.spinner("Processing..."):
            resume_text = extract_text_from_file(uploaded_file)
            result = process_request(task_map[task], resume_text, job_role)
            st.success("Done!")
            st.markdown("### 💡 Result")
            st.markdown(result)
    else:
        st.error("Please upload a resume and enter the job role.")