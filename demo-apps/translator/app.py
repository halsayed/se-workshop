import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.callbacks.base import BaseCallbackHandler
import os
from decouple import config


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
    api_key = st.text_input('API Key', type='password', value=config('API_KEY', default='460054cd-34a6-4ab8-9b58-0fcc328e5341'))
    temperature = st.slider(
        "Select Temperature for Chatbot:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

with st.sidebar.expander('Language Detector', expanded=True):
    detector_model = st.sidebar.text_input('Detector Model', value=config('MODEL_NAME', default='llama-3-8b-it'))
    detector_message = st.text_area("Language Detector System Message", value='''You are a language detection model. Your task is to analyze the text provided by the user and respond with only the name of the language the text is written in. Do not provide explanations, examples, or additional information. Only output the language name. For example:

Input: "Bonjour tout le monde" → Output: "French"
Input: "Hola, ¿cómo estás?" → Output: "Spanish"
''')

with st.sidebar.expander('Language Translator', expanded=True):
    translator_model = st.sidebar.text_input('Translator Model', value=config('TRANSLATOR_MODEL_NAME', default='mistral'))
    translator_message = st.text_area("Translator System Message", value='''You are a translation model. Your task is to translate text from {source_language} to {target_language}. Provide the translation only. Do not include any explanations, context, or extra details—just the translated text.

For example:
Source: "Hello" (from English to French) → Output: "Bonjour"
''')
    default_target_language = st.selectbox(
        'Default Target Language',
        ["English", "Spanish", "French", "German", "Chinese", "Japanese", "Korean", "Russian", "Arabic"],
        index=2
    )

detector = ChatOpenAI(
                openai_api_key=api_key,
                model_name=detector_model,
                openai_api_base=api_endpoint,
                temperature=temperature,
            )

translator = ChatOpenAI(
                openai_api_key=api_key,
                model_name=translator_model,
                openai_api_base=api_endpoint,
                temperature=temperature,
                streaming=True
            )


# Check if required fields are filled
required_fields_valid = bool(api_endpoint and detector_model and translator_model and api_key)

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
st.title("AI Translator")

# Initialize session state for text input if it doesn't exist
if 'text_input' not in st.session_state:
    st.session_state.text_input = ""

def clear_text():
    st.session_state.text_input = ""

# Add clear button before the text area
if st.button("Clear Content", on_click=clear_text):
    st.rerun()

# Use session state for text input
text_input = st.text_area('Original Text', 
                         value=st.session_state.text_input,
                         height=300, 
                         max_chars=20000,
                         key='text_input')

# detect language
detected_language = ""
if len(text_input.strip()) > 4:
    detected_language = detector.invoke([
        SystemMessage(content=detector_message),
        HumanMessage(content=text_input)
    ]).content

st.write(f'Detected Language: {detected_language}')

# Get target language from user
target_language = st.text_input(
    "Enter target language:",
    value=default_target_language
)

# Add translate button and validation
translate_button = st.button(
    "Translate",
    disabled=not text_input.strip() or not detected_language.strip(),
    help="Enter text and wait for language detection to enable translation"
)

# Only perform translation when button is pressed and inputs are valid
if translate_button:
    if not text_input.strip():
        st.warning("Please enter text to translate.")
    elif not target_language.strip():
        st.warning("Please enter a target language.")
    else:
        # translate text
        chat_box = st.empty()
        accumulated_text = ""

        translated_text = translator.stream(
            [
                SystemMessage(content=translator_message.replace("{source_language}", detected_language).replace("{target_language}", target_language)),
                HumanMessage(content=text_input)
            ]
        )

        # Display the streaming output
        for chunk in translated_text:
            accumulated_text += chunk.content
            chat_box.markdown(accumulated_text)

