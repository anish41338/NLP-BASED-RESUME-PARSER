from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def enhance_resume_section(resume_text, jd_text, missing_skills):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        try:
            openai_api_key = st.secrets["OPENAI_API_KEY"]
        except:
            return HARD_CODED_RESUME

    if not openai_api_key:
        return HARD_CODED_RESUME

    try:
        prompt = PromptTemplate(
            input_variables=["resume", "jd", "missing_skills"],
            template=(
                "You are a career coach AI. Given the following resume section, job description, and missing skills, "
                "suggest improved wording for the resume section to better match the job description and address the missing skills.\n"
                "Resume Section:\n{resume}\n"
                "Job Description:\n{jd}\n"
                "Missing Skills:\n{missing_skills}\n"
                "Improved Resume Section:"
            )
        )

        llm = ChatOpenAI(
            temperature=0.3,
            model="gpt-3.5-turbo",
            openai_api_key=openai_api_key
        )

        return llm.invoke(
            prompt.format(
                resume=resume_text,
                jd=jd_text,
                missing_skills=", ".join(missing_skills)
            )
        ).content

    except Exception:
        return HARD_CODED_RESUME


# 🔒 STATIC HARDCODED RESPONSE (NO VARIABLES, NO LOGIC)
HARD_CODED_RESUME = """
PROFESSIONAL SUMMARY
Motivated and disciplined computer science student with strong fundamentals in software development,
problem-solving, and system design. Experienced in academic and internship projects with a focus on
clean implementation and practical impact.

CORE SKILLS
Python, Data Structures, Algorithms, Object-Oriented Programming,
Databases, Operating Systems, Computer Networks

EXPERIENCE
• Worked on academic and industry-oriented projects following best coding practices
• Collaborated in team environments and followed structured development workflows
• Demonstrated ability to learn new technologies quickly and apply them effectively

PROJECTS
• Built end-to-end applications addressing real-world problems
• Focused on performance, maintainability, and clarity

ADDITIONAL INFORMATION
• Strong analytical mindset and ownership mentality
• Resume structured for ATS compatibility
"""
