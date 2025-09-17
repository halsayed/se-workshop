def edit_prompt():
    import streamlit as st
    
    prompt = st.text_area(
        "Enter your prompt",
        placeholder="Enter prompt for image analysis",
        height=100
    )
    
    return prompt
