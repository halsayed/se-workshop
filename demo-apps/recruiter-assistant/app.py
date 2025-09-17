import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.callbacks.base import BaseCallbackHandler
import os
from decouple import config
import docx
from PyPDF2 import PdfReader
import io


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


# Sidebar for user input
with st.sidebar.expander('General Configuration', expanded=False):
    api_endpoint = st.text_input('API Endpoint URL', value=config('API_ENDPOINT', default='https://ai.gpt.ntnx.pro/api/v1'))
    api_key = st.text_input('API Key', type='password', value=config('API_KEY', default='50d62eb7-9ce1-430a-bbd9-8104db9b618a'))
    temperature = st.slider(
        "Select Temperature for Chatbot:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

with st.sidebar.expander('CV Summarizer', expanded=True):
    summerizer_model = st.sidebar.text_input('Summerizer Model', value=config('MODEL_NAME', default='llama-3-8b-it'))
    summerizer_message = st.text_area("CV Summerizer System Message", value='''You are an expert assistant specialized in analyzing and summarizing curriculum vitae (CVs). Your task is to carefully read the provided CV and clearly summarize its essential facts in a structured format.

Extract and organize information under the following headings:
- Personal Information: Name, contact details (email, phone, location), LinkedIn or personal website (if available).
- Professional Summary: A brief paragraph summarizing key experiences, skills, and professional strengths.                               
''')

with st.sidebar.expander('Evaluator', expanded=True):
    evaluator_model = st.sidebar.text_input('Evaluator Model', value=config('THINKING_MODEL_NAME', default='thinking'))
    default_target_language = st.selectbox(
        'Default Target Language',
        ["English", "Spanish", "French", "German", "Chinese", "Danish", "Korean", "Russian", "Arabic"],
        index=0
    )
    evaluator_message = st.text_area("Evaluator System Message", value=f'''You are an expert assistant specialized in evaluating candidates by analyzing their summarized CV against a provided job description. Your goal is to clearly determine and explain how well the candidate aligns with the job requirements.
Regardless of the language of the job description or CV, the output should be in {default_target_language}.
Perform the following steps clearly and concisely:

(1) Job Requirements Analysis:
Extract and list the key requirements, qualifications, and skills explicitly mentioned in the provided job description.

(2) Candidate Evaluation:
Analyze the candidate's summarized CV and clearly indicate which of the key job requirements they meet, partially meet, or do not meet.
Briefly highlight candidate's relevant strengths and clearly point out any significant gaps or weaknesses regarding the job description.

(3) Feedback and Recommendations (brief and direct):
Provide practical feedback highlighting how well the candidate's experience, skills, education, and achievements match the job criteria.
Identify any areas where the candidate falls short or exceeds the requirements.

(4) Final Assessment (clearly select one option):
 - Fit: Candidate closely aligns with the job requirements, demonstrating relevant experience, skills, and qualifications.
 - Neutral: Candidate partially matches the job description, having some relevant skills and experiences but also notable gaps.
 - Unfit: Candidate significantly lacks the essential qualifications, skills, or experiences required by the job.
                                     
(5) Output language: Remember to output the evaluation in {default_target_language}.
''')

summerizer = ChatOpenAI(
                openai_api_key=api_key,
                model_name=summerizer_model,
                openai_api_base=api_endpoint,
                temperature=temperature,
                streaming=True
            )

evaluator = ChatOpenAI(
                openai_api_key=api_key,
                model_name=evaluator_model,
                openai_api_base=api_endpoint,
                temperature=temperature,
                streaming=True
            )


# Check if required fields are filled
required_fields_valid = bool(api_endpoint and summerizer_model and evaluator_model and api_key)

# Show warning if required fields are missing
if not required_fields_valid:
    st.warning("Please fill in all required fields (API Endpoint, Model Name, and API Key) in the sidebar to enable chat.")



# logo
logo_path = './ntnx_logo.png'
if os.path.exists(logo_path):
    st.image(logo_path, width=100)
else:
    st.warning("Logo file not found. Please ensure 'ntnx_logo.png' is in the same directory as this script.")

# Main chat interface
st.title("Recruitment Assistant")

# Add job description input
job_description = st.text_area("Job Description", placeholder="Paste the job description here...")


def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Add file uploader
uploaded_file = st.file_uploader("Upload CV (PDF or DOCX)", type=['pdf', 'docx'], disabled=not bool(job_description))
if uploaded_file is not None:
    try:
        # Convert the uploaded file to bytes
        file_bytes = uploaded_file.read()
        
        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(io.BytesIO(file_bytes))
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(io.BytesIO(file_bytes))
            
        # Display the extracted text in a scrollable container
        with st.expander("Extracted CV Text"):
            st.markdown(
                f"""
                <div style="border:1px solid #ccc; padding:10px; height:300px; overflow-y:scroll; background-color:black;">
                    <pre style="color:black;">{text}</pre>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        st.success("File uploaded and text extracted successfully!")

        # Add CV summarization section
        with st.spinner('Summarizing CV...'):
            with st.expander("CV Summary"):
                chat_container = st.empty()
                stream_handler = StreamHandler(chat_container)
                
                messages = [
                    SystemMessage(content=summerizer_message),
                    HumanMessage(content=text)
                ]
                
                response = summerizer(messages, callbacks=[stream_handler])

        with st.spinner('Evaluating CV...'):
            with st.expander("CV Evaluation"):
                chat_container = st.empty()
                stream_handler = StreamHandler(chat_container)
                
                messages = [
                    SystemMessage(content=evaluator_message),
                    HumanMessage(content=f"Job Description: {job_description}\n\nCV Summary: {text}")
                ]
                
                response = evaluator(messages, callbacks=[stream_handler])
                
                
            
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")




