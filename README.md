# Groq LLM Chatbot

An interactive Q&A chatbot built using **LangChain, Groq-hosted LLMs, and Streamlit**. Users can select different language models and customize response generation.

## Features

- Select from three hosted LLMs
- Adjustable temperature and maximum response length
- LangChain prompt templates and output parsing
- Interactive Streamlit interface
- Deployed and accessible through a web browser

## Demo

**Live App:** [Try the Groq LLM Chatbot](https://groq-llm-chatbot-pwgdwfazvccvolytzydecp.streamlit.app/)

## Tech Stack

Python · LangChain · Groq API · Streamlit

## Available LLMs

The chatbot offers three language models hosted by Groq:

- **GPT-OSS 20B (`openai/gpt-oss-20b`):** An open-weight language model designed for general-purpose reasoning and problem-solving.
- **ALLAM 2 7B (`allam-2-7b`):** An Arabic-focused language model that can also handle general language tasks.
- **Qwen 3.8 27B (`qwen/qwen3.8-27b`):** A Qwen-family model available through the Groq API for conversational and general-purpose tasks.

*Responses may vary depending on the selected model and the question.*

## User Controls

- **Temperature (0–1):** Controls how varied the responses can be. Lower values generally produce more focused and predictable answers, while higher values allow more variation.
- **Max Tokens (50–300):** Sets the maximum length of the generated response. Lower values produce shorter answers, while higher values allow longer answers. Tokens are pieces of text, not necessarily whole words.

## Setup and Usage

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/groq-llm-chatbot.git
cd groq-llm-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.env` file using `.env.example` as a reference and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

**Keep your API key private. Never commit your `.env` file to GitHub.**

### 4. Run the application

```bash
streamlit run app.py
```

## Note

An active Groq API key and access to the selected model are required for local use. API usage is subject to applicable rate limits and account terms.