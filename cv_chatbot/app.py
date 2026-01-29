import streamlit as st
from core.user_profile import UserProfile, LearningEntry, ExperienceEntry

# App Configuration
st.set_page_config(
    page_title= "AI CV Tailor (DS/ AI/ ML / CYSEC)",
    layout="centered"
)

# Session State Init
if "user_profile" not in st.session_state:
    st.session_state.user_profile = None

if "job_context" not in st.session_state:
    st.session_state.job_context = None

if "generated_cv" not in st.session_state:
    st.session_state.generated_cv = None

# UI
st.title("AI Powered CV Tailoring Assistant")
st.write(
    "Upload your cv or start from scratch, " 
    "then tailor it for Data Science, ML, AI or Cybersecurity roles"
)

st.divider()

# CV Upload
st.subheader("Step 1: How would you like to start?")

entry_mode = st.radio(
    "Choose one option",
    options=["Upload an existing CV", "I don't have a CV yet"]
)

uploaded_cv = None

if entry_mode == "Upload an existing CV":

    uploaded_cv = st.file_uploader(
        "Upload your CV (PDF or text)",
        type=["pdf", "txt"]
    )

if entry_mode == "I don't have a CV yet":
    st.subheader("Tell us about yourself")

    full_name = st.text_input("Full name")
    email = st.text_input("Email address")
    phone = st.text_input("Phone number")

    target_roles = st.multiselect(
        "Target roles",
        options=["Data Scientist", "ML Engineer", "AI Engineer", "Cybersecurity"]
    )

st.divider()


if st.button("Create your Profile"):

    if entry_mode == "I don't have a CV yet":
        if not full_name or not email:
            st.error("Full name and email are required.")
        else:
            st.session_state.user_profile = UserProfile(
                full_name=full_name,
                email=email,
                phone=phone,
                target_roles=target_roles
            )
            st.success("User profile created successfully.")

    elif entry_mode == "Upload an existing CV":
        if uploaded_cv is None:
            st.error("Please upload a CV first.")
        else:
            # Create empty profile shell 
            st.session_state.user_profile = UserProfile()
            st.success("Profile created from uploaded CV.")


# Job description 
st.subheader("Step 2: Job Description")
job_description = st.text_area(
    "Paste the job description you are applying for",
    height=200
)

# Optional clarification
st.subheader("Optional: Add clarification for this role")
clarification = st.text_area(
    "Add anything specific you want emphasized (optional)",
    height=100
)

st.divider()

# Action Button
if st.button("Generate tailored CV"):
    st.info("CV generation logic will be added in the next steps.")