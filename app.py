import streamlit as st
import pdfplumber
import google.generativeai as genai
import re
import matplotlib.pyplot as plt

# 🔑 API KEY (replace with your key)
genai.configure(api_key="AIzaSyCd-hHYokprdhaxAYKroiPkQVvYTkbU5BA")
model = genai.GenerativeModel("models/gemini-flash-latest")

# 🎨 PAGE CONFIG (uses logo as tab icon)
st.set_page_config(
    page_title="IntelliResume AI",
    page_icon="logo.png",
    layout="wide"
)

# 🎨 DARK UI STYLE
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}
.section {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🔥 BIG CENTERED LOGO (NO EXTRA TEXT)
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("logo.png", width=500)  # adjust 280–400 as you like

# 📌 SIDEBAR
st.sidebar.image("logo.png", width=150)

option = st.sidebar.radio("Navigation", [
    "Analyze Resume",
    "Improve Resume",
    "Job Description"
])

st.write("Upload your resume and get AI insights")

# 📄 FILE UPLOAD
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# 📄 TEXT EXTRACTION
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# 🎯 SAMPLE JOB SKILLS (edit based on role if needed)
job_skills = ["Python", "SQL", "Machine Learning", "AI", "Data Analysis"]

# ================= MAIN =================
if uploaded_file:
    resume_text = extract_text(uploaded_file)
    st.success("Resume uploaded successfully!")

    # ================= ANALYZE =================
    if option == "Analyze Resume":

        if st.button("🔍 Analyze Resume"):

            with st.spinner("Analyzing..."):
                prompt = f"""
                Analyze the resume and provide:

                ATS Score: (out of 100)

                Skills:
                - ...

                Missing Skills:
                - ...

                Resume:
                {resume_text}
                """
                response = model.generate_content(prompt)
                result = response.text

            st.markdown('<div class="section">', unsafe_allow_html=True)

            # 📊 ATS SCORE
            match = re.search(r'ATS Score[:\s]*(\d+)', result)
            if match:
                score = int(match.group(1))
                st.progress(score / 100)

                if score >= 80:
                    st.success(f"ATS Score: {score}/100 (Excellent)")
                elif score >= 60:
                    st.warning(f"ATS Score: {score}/100 (Average)")
                else:
                    st.error(f"ATS Score: {score}/100 (Needs Improvement)")

            # 📈 SKILL MATCH %
            matched = sum(1 for skill in job_skills if skill.lower() in resume_text.lower())
            match_percent = int((matched / len(job_skills)) * 100)

            st.subheader("📈 Skill Match")
            st.progress(match_percent / 100)
            st.write(f"{match_percent}% match with job skills")

            # 📊 LAYOUT (TEXT + SMALL GRAPH)
            col1, col2 = st.columns([2, 1])

            with col1:
                st.subheader("📊 Analysis")
                st.write(result)

            with col2:
                labels = ["Matched", "Missing"]
                values = [matched, len(job_skills) - matched]

                fig, ax = plt.subplots(figsize=(3, 3))  # 👈 small chart
                ax.pie(values, labels=labels, autopct='%1.1f%%')
                ax.set_title("Skill Match")
                st.pyplot(fig, use_container_width=False)

            st.markdown('</div>', unsafe_allow_html=True)

    # ================= IMPROVE =================
    elif option == "Improve Resume":

        if st.button("✨ Improve Resume"):

            with st.spinner("Improving..."):
                response = model.generate_content(
                    f"Improve this resume professionally:\n{resume_text}"
                )
                improved = response.text

            st.markdown('<div class="section">', unsafe_allow_html=True)

            st.subheader("✨ Improved Resume")
            st.write(improved)

            st.download_button(
                label="📥 Download Improved Resume",
                data=improved,
                file_name="improved_resume.txt",
                mime="text/plain"
            )

            st.markdown('</div>', unsafe_allow_html=True)

    # ================= JOB DESCRIPTION =================
    elif option == "Job Description":

        if st.button("💼 Generate Job Description"):

            with st.spinner("Generating..."):
                response = model.generate_content(
                    f"Generate a professional job description based on this resume:\n{resume_text}"
                )

            st.markdown('<div class="section">', unsafe_allow_html=True)

            st.subheader("💼 Job Description")
            st.write(response.text)

            st.markdown('</div>', unsafe_allow_html=True)