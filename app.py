import os

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load local environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Groq LLM Chatbot",
)

# Retrieve API key from environment or Streamlit secrets
def get_api_key():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets.get("GROQ_API_KEY")
        except (FileNotFoundError, KeyError):
            api_key = None

    return api_key


# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer questions clearly and accurately."),
    ("human", "{question}")
])


# Generate response
def generate_response(question, model_name, temperature, max_tokens, api_key):
    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=api_key
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"question": question})


# Streamlit interface
st.title("Groq LLM Chatbot")
st.caption("An interactive Q&A chatbot powered by Groq and LangChain")

# Sidebar settings
st.sidebar.header("Model Settings")

model_name = st.sidebar.selectbox(
    "Select Model",
    [
        "openai/gpt-oss-20b",
        "allam-2-7b",
        "qwen/qwen3.8-27b"
    ]
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.1
)

max_tokens = st.sidebar.slider(
    "Maximum Response Tokens",
    min_value=50,
    max_value=500,
    value=150,
    step=50
)

# User input
with st.form("chat_form"):
    question = st.text_input(
        "Ask a question:",
        max_chars=2000
    )
    submitted = st.form_submit_button("Generate Response")

if submitted:
    if not question.strip():
        st.warning("Please enter a question.")

    else:
        api_key = get_api_key()

        if not api_key:
            st.error("Groq API key is not configured.")
        else:
            try:
                with st.spinner("Generating response..."):
                    answer = generate_response(
                        question=question,
                        model_name=model_name,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        api_key=api_key
                    )

                st.subheader("Response")
                st.write(answer)

            except Exception:
                st.error(
                    "Unable to generate a response. "
                    "Check your API configuration, model availability, "
                    "network connection, and usage limits."
                )

st.caption("Powered by Groq-hosted language models.")