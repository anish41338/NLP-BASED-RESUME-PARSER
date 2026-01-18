from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def generate_project_ideas(resume_text, skills):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        try:
            openai_api_key = st.secrets["OPENAI_API_KEY"]
        except:
            return HARD_CODED_PROJECTS

    if not openai_api_key:
        return HARD_CODED_PROJECTS

    try:
        prompt = PromptTemplate(
            input_variables=["resume", "skills"],
            template=(
                "Based on the following resume and skills, suggest 3 impactful project topics and descriptions "
                "which tackle real life problems (not limited to AI/ML) that align with the candidate's background "
                "and would impress recruiters in their field.\n"
                "Resume:\n{resume}\n"
                "Skills:\n{skills}\n"
                "Project Ideas:"
            )
        )

        llm = ChatOpenAI(
            temperature=0.5,
            model="gpt-3.5-turbo",
            openai_api_key=openai_api_key
        )

        return llm.invoke(
            prompt.format(
                resume=resume_text,
                skills=", ".join(skills)
            )
        ).content

    except Exception:
        return HARD_CODED_PROJECTS


# 🔒 STATIC HARDCODED PROJECT IDEAS (NO VARIABLES)
HARD_CODED_PROJECTS = """
### Project 1: Smart Resume Analyzer
**Problem:** Students struggle to understand why their resumes get rejected.
**Description:** Build a system that analyzes resumes against job descriptions and highlights gaps.
**Technologies:** Python, NLP, Streamlit
**Why Valuable:** Demonstrates practical problem-solving and recruiter relevance.

### Project 2: Skill-Based Learning Path Generator
**Problem:** Learners often waste time choosing irrelevant courses.
**Description:** Create a platform that suggests structured learning paths based on career goals.
**Technologies:** Python, Recommendation Systems, APIs
**Why Valuable:** Shows system design thinking and real-world applicability.

### Project 3: Personal Productivity & Habit Tracker
**Problem:** Consistency in skill development is difficult.
**Description:** Develop a tool to track habits, goals, and progress over time.
**Technologies:** Web App (React/Streamlit), Backend, Database
**Why Valuable:** Highlights full-stack thinking and user-centric design.
"""
