# INTELLIRESUMEAI-RESUME-ANALYZER-AND-IMPROVISER

# IntelliResume AI

An AI-powered Resume Analyzer built using Streamlit and Google Gemini API that helps users evaluate, improve, and optimize their resumes for better job opportunities.

---

## Overview

IntelliResume AI is a web application designed to analyze resumes and provide:

* ATS (Applicant Tracking System) Score
* Skill Match Percentage
* Missing Skills Identification
* Resume Improvement Suggestions
* Job Description Generation

This project helps job seekers enhance their resumes and align with industry expectations.

---

## Features

### Resume Analysis

* Upload resume in PDF format
* Get ATS score instantly
* Identify strengths and weaknesses

### Skill Matching

* Compare resume with job-relevant skills
* Get percentage-based skill match
* Visual representation using charts

### Resume Improvement

* AI-generated improved resume content
* Strong action verbs and structured formatting

### Job Description Generator

* Generates job descriptions based on resume
* Helps understand suitable roles

### User Interface

* Dark mode interface
* Clean and professional layout
* Logo branding
* Sidebar navigation

---

## Tech Stack

* Frontend: Streamlit
* Backend: Python
* AI Model: Google Gemini API
* Libraries:

  * pdfplumber – PDF text extraction
  * matplotlib – Data visualization
  * re – Text processing

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/IntelliResume-AI.git
cd IntelliResume-AI
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Environment Variable

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

---

## Project Structure

```
IntelliResume-AI/
│── app.py
│── test.py
│── logo.png
│── screenshots/
│── requirements.txt
│── README.md
```

---

## Sample Output

* ATS Score: 62/100
* Skill Match: 60%
* Missing Skills identified
* Improved resume generated

---

## System Architecture

```
User → Streamlit UI → PDF Processing → Gemini API → Response → UI Display
```

---

## Future Enhancements

* LinkedIn profile integration
* Interview question generator
* Resume ranking system
* Cloud deployment
* Job matching system

---

## Security Note

API keys are not included in the repository.
Store your API key securely using environment variables.

---

## Contributors

* S. Parthiv Ram (PES1UG23AM305)
* V. Chakresh (PES1UG23AM347)

---

## Conclusion

IntelliResume AI demonstrates the application of AI in real-world scenarios by providing intelligent resume analysis and helping users improve their job prospects effectively.
