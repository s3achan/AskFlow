import streamlit as st
from langchain_openai import ChatOpenAI

# Display the app title 
st.title('Ask Flow')

# Ask the user to enter their OpenAI API key 
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    try:
        llm = ChatOpenAI(
            temperature=0.7,
            api_key=openai_api_key   
        )

        result = llm.invoke(input_text)
        st.info(result.content)

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.info("Check your API key and internet connection.")


with st.form('my_form'):
    text = st.text_area(
        'Enter text:', 
        'What are the three key pieces of advice for learning how to code?'
    )
    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
