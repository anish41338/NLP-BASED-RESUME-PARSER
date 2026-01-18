# Smart Career Advisor – Resume & Job Matching System

An AI-based application that analyzes resumes against job descriptions to predict compatibility and provide improvement suggestions using NLP and Machine Learning.

**Developed by:** Anish  
**Institute:** RV College of Engineering (RVCE)

---

## Overview

Smart Career Advisor is an end-to-end Machine Learning project that predicts how well a candidate’s resume matches a given job description.  
It also extracts relevant skills and provides AI-based suggestions to improve resumes and career readiness.

This project focuses on **applied ML engineering**, real datasets, and clean system design.

---

## Features

- Resume–job compatibility prediction
- Skill extraction from resumes and job descriptions
- Resume improvement suggestions using LLMs
- Learning resource recommendations
- Project idea suggestions based on skill gaps
- Interactive Streamlit interface

---

## Dataset

- Source: HuggingFace  
- Dataset: `cnamuangtoun/resume-job-description-fit`
- Size: 6,241 resume–job pairs

---

## Machine Learning Approach

- Text preprocessing:
  - Tokenization
  - Lemmatization
  - Stopword removal
- Feature extraction:
  - TF-IDF with unigrams and bigrams (~10,000 features)
- Models evaluated:
  - Logistic Regression
  - Naive Bayes
  - SVM
  - Random Forest
  - Neural Network
  - XGBoost

**Best model:** XGBoost

---

## Model Performance

- Test Accuracy: **78.14%**
- ROC-AUC Score: **89.57%**
- 5-fold Cross-Validation Score: **~71.5%**

---

## NLP & Skill Extraction

- spaCy-based Named Entity Recognition (NER)
- PhraseMatcher-based fallback for reliability
- Works on both resumes and job descriptions

---

## LLM Integration

- OpenAI GPT-4 used for:
  - Resume section enhancement
  - Project idea generation
  - Learning recommendations
- Implemented using LangChain
- LLM features are optional and modular

---

## Tech Stack

- Python 3.11+
- scikit-learn
- XGBoost
- spaCy
- Streamlit
- OpenAI API
- LangChain
- pandas, numpy

---


