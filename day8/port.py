import json
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from pydantic import BaseModel
from pypdf import PdfReader


load_dotenv()

my_api = os.getenv("GROQ_API_KEY")

if not my_api:
    raise ValueError("API key is not available")

client = Groq(api_key=my_api)

model = "openai/gpt-oss-20b"

resume = """
# ARYAN RAJ

**Computer Science Engineering Student | Software Development | AI & Data**

Bhopal, Madhya Pradesh, India
**LinkedIn:** https://www.linkedin.com/in/aryan-raj-521603343/
**GitHub:** https://github.com/hey-aryan-ai
**LeetCode:** https://leetcode.com/u/mr__aryan___rauniyar/
**CodeChef:** https://www.codechef.com/users/aryan_owls_38

---

## PROFESSIONAL SUMMARY

Computer Science Engineering student with hands-on experience in **Java, C++, Python, SQL, web technologies, and AI APIs**. Interested in software development, data analytics, and AI-driven applications. Experienced in building desktop applications, working with databases, integrating APIs, and developing automation workflows using **n8n**. Strong interest in problem solving and competitive programming.

---

## EDUCATION

### Bachelor of Technology — Computer Science Engineering

**TIT Excellence, Bhopal, Madhya Pradesh**
Currently pursuing B.Tech | 2nd Year
Current CGPA : 8.00 
### Class XII

**Bihar School Examination Board (BSEB)**

---

## TECHNICAL SKILLS

**Programming Languages:** C++, Java, Python, SQL

**Web Technologies:** HTML, CSS, React.js

**Data & Analytics:** Pandas, NumPy, Matplotlib, Seaborn

**Database:** MySQL, SQLite

**AI & APIs:** Groq API, n8n

**Tools & Technologies:** Git, GitHub, VS Code, MySQL Workbench, JDBC 

**Core Concepts:** Data Structures & Algorithms, OOP, DBMS, Operating Systems, Computer Organization

---

## PROJECTS


### AI Resume Portfolio & Job Matching System

**Python | FastAPI | Groq API | LLM | Pydantic | PyPDF**

* Built an AI-powered resume portfolio that allows recruiters to interact with the candidate's resume through a conversational interface.
* Developed the backend using **Python and FastAPI** to handle API requests, resume processing, and AI-generated responses.
* Implemented **PDF resume extraction** using PyPDF to extract structured information from uploaded resumes.
* Used **Groq API and LLMs** to generate responses based on the candidate's resume information.
* Designed prompts to ensure the AI answers recruiter questions using only the information available in the candidate's resume.
* Added professional profile information such as **GitHub, LinkedIn, LeetCode, and CodeChef** links for quick recruiter access.
* Implemented resume-based question answering for areas such as **education, technical skills, projects, experience, achievements, and professional profiles**.
* Developed functionality to **extract resume information and compare it with a given Job Description (JD)** to identify relevant skills and matching areas.
* Used job-description matching to help analyze how well a candidate's **skills, projects, and experience align with a specific job role**.
* Structured extracted resume information in **JSON format**, making it easier for the AI system to retrieve and use candidate information.
* Added instructions to prevent the AI from inventing information that is not available in the candidate's resume.


### AI School Addmission Agent

**Python | Groq API | LLM | Tool Calling | Regex | Function-Based Tools**

* Built an AI-powered **school admission assistant** that can understand a user's admission request and perform multiple tasks through tool calling.
* Integrated an LLM using the **Groq API** to make decisions and determine which tool should be executed next.
* Developed custom tools for **school validation, seat availability, admission fees, category-based discounts, eligibility criteria, and calculations**.
* Implemented a step-by-step agent workflow where the AI calls **only one tool at a time**, waits for the tool result, and then decides the next action.
* Used **Python functions as tools** and maintained a tool registry to dynamically execute the tool selected by the AI.
* Implemented **ReAct-style reasoning flow** using `Thought`, `Action`, `Observation`, and `Final Answer` formats.
* Used **regular expressions (Regex)** to extract the selected tool name and arguments from the LLM response.
* Added safeguards in the system prompt to prevent the AI from **guessing tool results or calling multiple tools simultaneously**.
* Implemented a maximum-step execution loop to control the agent workflow and prevent unlimited tool execution.
* Built a complete admission workflow where the agent can validate a school, check eligibility and availability, retrieve fees and discounts, and calculate the final admission amount.
* Used **temperature=0** to make tool-selection behavior more deterministic and consistent.


### AI Resume Analyzer & Job Matching System

**Python | Groq API | LLM | Pydantic | JSON | Prompt Engineering**

* Built an AI-powered resume analysis system that extracts structured candidate information such as **contact details, technical skills, experience, and projects** from unstructured resume text.
* Used **LLMs through the Groq API** to convert resume content into structured **JSON data** based on a predefined Pydantic schema.
* Implemented schema validation using **Pydantic models** to ensure extracted resume information follows a consistent structure.
* Developed an **HR-oriented Job Description (JD) matching system** that compares a candidate's resume against required job skills and requirements.
* Implemented skill matching to identify **matched skills, missing skills, match percentage, and overall candidate rating**.
* Designed prompts to prevent the model from **inventing skills or experience** that are not present in the resume.
* Added structured JSON output for easier integration with resume screening, candidate analysis, and portfolio applications.
* Built the system to support automated resume evaluation for specific roles such as **Python Developer Intern**.


### AI Smart File Organizer

**Java | Java Swing | MySQL | JDBC | n8n**

* Developed a Java desktop application to automatically organize files from a selected directory based on their file types.
* Designed a **Java Swing GUI** with Login, Registration, Dashboard, folder selection, file organization, monitoring, history, and logout functionality.
* Implemented user authentication and persistent user data storage using **MySQL and JDBC**.
* Built automated file categorization into **Images, Videos, Music, Documents, Archives, Code, and Others**.
* Integrated file-system operations to detect, categorize, and move files into appropriate folders.
* Designed an **n8n-based AI automation workflow** to extend the application with intelligent file-management capabilities.
* Used modular Java classes to separate database connectivity, authentication, dashboard functionality, and file-organization logic.

### AI-Powered Email Automation

**n8n | Gmail | Google Gemini 2.5 Flash | Google Sheets | Workflow Automation**

* Built an AI-powered email automation workflow using **n8n** to intelligently process unread Gmail messages.
* Integrated **Gmail** to automatically fetch and process newly received unread emails.
* Used **Google Gemini 2.5 Flash** to analyze email content and generate professional, context-aware replies.
* Automated the process of handling emails without requiring manual processing for every message.
* Integrated **Google Sheets** to maintain a record of processed emails and generated responses.
* Automatically marks processed Gmail messages as **read** after completing the workflow.
* Designed the workflow to run automatically on a **schedule**, making it suitable for continuous inbox management.
* Created a modular workflow that can be customized for different email-processing and automation requirements.
* Used workflow automation to reduce repetitive manual email-handling tasks and improve inbox-management efficiency.

### AI-Powered College Review Analysis

**n8n | Google Gemini 2.5 Flash | Google Sheets | AI | Workflow Automation

Built an AI-powered workflow using n8n and Google Gemini 2.5 Flash to automatically analyze student college reviews.
Integrated a review form with Google Sheets to automatically collect and store submitted feedback.
Used Gemini AI to analyze unstructured reviews and extract meaningful insights from student feedback.
Implemented the n8n Switch node to categorize reviews into Positive, Negative, and Improvement sections.
Automated the conversion of unstructured feedback into structured and actionable insights, reducing manual analysis.
Designed the workflow to be customizable and scalable for processing large volumes of student feedback.
---

## CODING PROFILES

**LeetCode:** Solving Data Structures & Algorithms problems and improving problem-solving skills.

**CodeChef:** Regular competitive programming practice with C++.

---

## RELEVANT COURSEWORK

* Data Structures & Algorithms
* Object-Oriented Programming
* Database Management Systems
* Operating Systems
* Computer Organization & Architecture
* Computer Networks

---

## INTERESTS

Software Development • Artificial Intelligence • Data Analytics • Problem Solving • Automation

## Personal Information 

Father name : Omparkash Gupta 
Mother name : Rekha Gupta 
Address : Bihar , District : Gopalganj , Hathua 
email : ar3221576@gamil.com
Contact / Phone : 6206971583 , 7247441437

## HOBBIES 

Playing Cricket • Listening Music • Reading book 
"""


class Experience (BaseModel):
    company : str | None = None
    role : str | None = None
    duration : str | None = None
    description : str | None = None
    skill_used : list[ str] = []


class Resume(BaseModel):
    name : str | None = None
    email : str | None = None
    phone : str | None = None
    contect : str | None = None
    total_experince_years :float | None = None


    father_name: str | None = None
    mother_name: str | None = None
    address: str | None = None
    linkedin: str | None = None
    github: str | None = None
    leetcode: str | None = None
    codechef: str | None = None
    
    skills : list[str] = []
    experience : list[Experience] = []
    education :  list[str] = []
    projects : list[str] = []
    certification : list[str] = []
    interset : list[str]=[]
    hobbies : list[str] = []


resume_schema = Resume.model_json_schema()

class chatRequest(BaseModel):
    question : str
    messages : list[dict]=[]


def ask_can(question, resume, messages):
    system_prompt = f"""
You are Aryan Raj's personal portfolio AI assistant.

Your job is to answer questions about Aryan using ONLY the information
provided in the candidate resume below and the conversation history.

IMPORTANT RULES:
1. Never invent, assume, or add information.
2. Aryan is currently a B.Tech Computer Science Engineering student.
   Never describe him as a graduate.
3. Only mention skills that are present in the candidate information.
4. Do not add Prompt Engineering, Generative AI, or any other skill
   unless it is explicitly present in the candidate information.
5. If the information is not available, say:
   "I don't have that information in Aryan's profile."
6. Keep normal answers short and professional (1–3 sentences).
7. Use previous conversation messages to understand words such as
   "he", "his", "that project", or "it".
8. When asked about a specific project, use the project information
   provided in the resume.
9. When asked for LinkedIn, GitHub, LeetCode, or CodeChef,
   provide the exact URL from the resume.

CANDIDATE INFORMATION:
{resume}
"""

    conversation = []

    for message in messages:
        conversation.append({
            "role": message["role"],
            "content": message["content"]
        })

    conversation.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            *conversation
        ]
    )

    return response.choices[0].message.content

def parse (resume):
    system_prompt = f"""
    You are an expert resume parser.

    Extract information from the resume based on its meaning,
    not only based on exact section headings.

    Different resumes may use different headings.

    For example:
    - Experience
    - Professional Experience
    - Work History
    - Employment
    - Internships

    These may all contain relevant experience.

    Skills may also appear in the skills section, work experience,
    internships or projects.

    Return ONLY valid JSON matching this schema:

    {resume_schema}

    Important rules:

    1. Do not invent information.
    2. If a value is not available, return null.
    3. If a list has no information, return an empty list.
    4. Include internships inside experiences.
    5. Extract skills mentioned across the entire resume.
    """
    user_prompt = f"""
    Parse the following resume:

    {resume}
    """
    message_system = {
        "role":"system",
        "content":system_prompt
    }
    message_user = {
        "role":"user",
        "content":user_prompt
    }
    response_format = {
        "type":"json_object"
    }
    messages = [message_system , message_user]
    response = client.chat.completions.create(model=model , messages=messages , response_format=response_format)
    raw_output = response.choices[0].message.content
    data = json.loads(raw_output)
    resume_for = Resume(**data)
    return resume_for

app = FastAPI(
    title="Aryan Resume AI API",
    description="FastAPI backend for AI-powered resume chat",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home ():
    return {
        "messages ": "Ye home page hai babua "
    }

@app.post("/chat")
def chat(request:chatRequest):
    # parsed_resume = parse(resume)
    ans = ask_can(request.question,resume,request.messages)
    return{
        "answer":ans
    }


