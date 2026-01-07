import streamlit as st
import requests
import json
from typing import Dict, List, Optional
import time

# Configure the page
st.set_page_config(
    page_title="LLM Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "model_provider" not in st.session_state:
    st.session_state.model_provider = "OpenAI"


def call_openai_api(messages: List[Dict], api_key: str, model: str = "gpt-3.5-turbo") -> Optional[str]:
    """Call OpenAI API"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": messages,
        "max_tokens": 1000,
        "temperature": 0.7
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        st.error(f"Error calling OpenAI API: {str(e)}")
        return None


def call_anthropic_api(messages: List[Dict], api_key: str, model: str = "claude-3-sonnet-20240229") -> Optional[str]:
    """Call Anthropic API"""
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "anthropic-version": "2023-06-01"
    }

    # Convert messages format for Anthropic
    system_message = ""
    user_messages = []

    for msg in messages:
        if msg["role"] == "system":
            system_message = msg["content"]
        else:
            user_messages.append(msg)

    data = {
        "model": model,
        "max_tokens": 1000,
        "messages": user_messages
    }

    if system_message:
        data["system"] = system_message

    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["content"][0]["text"]
    except Exception as e:
        st.error(f"Error calling Anthropic API: {str(e)}")
        return None


def call_local_ollama(messages: List[Dict], model: str = "llama2") -> Optional[str]:
    """Call local Ollama API"""
    try:
        # Convert messages to a single prompt for Ollama
        prompt = ""
        for msg in messages:
            if msg["role"] == "system":
                prompt += f"System: {msg['content']}\n"
            elif msg["role"] == "user":
                prompt += f"User: {msg['content']}\n"
            elif msg["role"] == "assistant":
                prompt += f"Assistant: {msg['content']}\n"

        prompt += "Assistant: "

        data = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            "http://localhost:11434/api/generate",
            json=data,
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        st.error(f"Error calling Ollama API: {str(e)}")
        return None


def get_llm_response(messages: List[Dict], provider: str, api_key: str = "", model: str = "") -> Optional[str]:
    """Get response from selected LLM provider"""
    if provider == "OpenAI":
        return call_openai_api(messages, api_key, model or "gpt-3.5-turbo")
    elif provider == "Anthropic":
        return call_anthropic_api(messages, api_key, model or "claude-3-sonnet-20240229")
    elif provider == "Ollama (Local)":
        return call_local_ollama(messages, model or "llama2")
    else:
        st.error("Unknown provider selected")
        return None


# Sidebar configuration
st.sidebar.title("🤖 LLM Configuration")

# Model provider selection
provider = st.sidebar.selectbox(
    "Choose LLM Provider",
    ["OpenAI", "Anthropic", "Ollama (Local)"],
    key="model_provider"
)

# API key input (for cloud providers)
api_key = ""
if provider in ["OpenAI", "Anthropic"]:
    api_key = st.sidebar.text_input(
        f"{provider} API Key",
        type="password",
        help=f"Enter your {provider} API key"
    )

# Model selection
if provider == "OpenAI":
    model_options = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"]
elif provider == "Anthropic":
    model_options = ["claude-3-sonnet-20240229", "claude-3-opus-20240229", "claude-3-haiku-20240307"]
else:
    model_options = ["llama2", "mistral", "codellama", "neural-chat"]

selected_model = st.sidebar.selectbox("Model", model_options)

# System prompt
system_prompt = st.sidebar.text_area(
    "System Prompt",
    value="You are a helpful AI assistant. Please provide clear, concise, and accurate responses.",
    height=100
)

# Temperature setting
temperature = st.sidebar.slider("Temperature", 0.0, 2.0, 0.7, 0.1)

# Chat interface
st.title("🤖 LLM Chat Assistant")
st.markdown("Chat with your chosen LLM model!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's your question?"):
    # Validate API key for cloud providers
    if provider in ["OpenAI", "Anthropic"] and not api_key:
        st.error(f"Please enter your {provider} API key in the sidebar.")
        st.stop()

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare messages for API call
    api_messages = []
    if system_prompt:
        api_messages.append({"role": "system", "content": system_prompt})
    api_messages.extend(st.session_state.messages)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner(f"Getting response from {provider}..."):
            response = get_llm_response(api_messages, provider, api_key, selected_model)

            if response:
                st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error("Failed to get response from the model. Please check your configuration.")

# Sidebar controls
st.sidebar.markdown("---")
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# Show current configuration
with st.sidebar.expander("Current Configuration"):
    st.write(f"**Provider:** {provider}")
    st.write(f"**Model:** {selected_model}")
    st.write(f"**Temperature:** {temperature}")
    if api_key:
        st.write(f"**API Key:** {'*' * len(api_key[:8])}...")

# Instructions
with st.sidebar.expander("Setup Instructions"):
    st.markdown("""
    **OpenAI:**
    - Get API key from OpenAI platform
    - Requires credits/billing

    **Anthropic:**
    - Get API key from Anthropic console
    - Requires credits/billing

    **Ollama (Local):**
    - Install Ollama locally
    - Run: `ollama serve`
    - Pull models: `ollama pull llama2`
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Built with Streamlit 🎈")