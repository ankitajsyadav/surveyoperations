# Campus Tour Survey – Streamlit Mockup
A lightweight Streamlit application that demonstrates how survey programming concepts work in practice — including **skip logic, randomization, quotas, and loop & merge**.  

This mock survey is designed for interview demonstration purposes, especially for Survey Operations Analyst roles. It showcases how complex survey behavior can be operationalized using simple Python logic, similar to what is done in Python-based survey scripting environments.

---

## 🚀 Live Demo (Streamlit Cloud)

You can access and interact with the live deployed app here:

👉 **https://surveyoperations.streamlit.app/**

No installation required — the app loads instantly in your browser.

## 🎯 Features Demonstrated

### ✔ Skip Logic  
- Ends survey for users who did not attend a tour  
- Routes virtual tour respondents to a different set of questions  
- NPS follow-up questions change based on promoter/passive/detractor status  

### ✔ Randomization  
- Blocks (Tour Guide, Content & Flow, Facilities) are randomized each run  
- Certain answer lists are randomized to reduce bias  

### ✔ Quotas (Simulated)  
- Demonstrates how respondent quotas are checked (Domestic vs International)  
- If quota is full, the survey stops with a quota-full message  

### ✔ Loop & Merge  
- For each facility selected, the same satisfaction and comment questions repeat dynamically  

### ✔ Campus Tour Context  
Includes realistic question blocks themed around:
- Tour experience  
- Tour guide rating  
- Facilities visited  
- Virtual vs in-person tours  
- Net Promoter Score (NPS)  

---

## 🧪 Demo Use Case
This mockup can be shown during interviews to demonstrate your understanding of:
- Survey architecture  
- Logic-driven programming  
- User experience flow  
- Data capture logic  
- Applied survey operations concepts  

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/campus-tour-survey-mockup.git
cd campus-tour-survey-mockup
