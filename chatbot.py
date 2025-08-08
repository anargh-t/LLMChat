"""
AI Chatbot with Streamlit and Ollama

A modern, interactive AI chatbot that allows users to generate responses
using various LLM models through Ollama.

Author: Anargh T
Date: 2025
License: MIT
"""

import streamlit as st
import ollama
import time
import requests
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="LLMChat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def check_ollama_connection() -> bool:
    """
    Check if Ollama is running and accessible.
    
    Returns:
        bool: True if Ollama is accessible, False otherwise
    """
    try:
        # Try to connect to Ollama
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False

def get_available_models() -> list:
    """
    Get list of available models from Ollama.
    
    Returns:
        list: List of available model names
    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            return [model['name'] for model in models_data.get('models', [])]
        return []
    except:
        return []

def generate_llm_response(prompt: str, model: str = "llama3.2") -> str:
    """
    Generate a response from the LLM using Ollama.
    
    Args:
        prompt (str): The user's input prompt
        model (str): The Ollama model to use (default: llama3.2)
    
    Returns:
        str: The generated response from the LLM
    
    Raises:
        Exception: If there's an error communicating with Ollama
    """
    messages = [
        {
            'role': 'user',
            'content': prompt,
        }
    ]

    try:
        response = ollama.chat(model=model, messages=messages)
        return response['message']['content']
    except Exception as e:
        raise Exception(f"Error communicating with Ollama: {str(e)}")

def format_response(response: str) -> str:
    """
    Format the response for better display.
    
    Args:
        response (str): Raw response from LLM
    
    Returns:
        str: Formatted response
    """
    # Add basic formatting if needed
    return response.strip()

def main():
    """Main application function."""
    
    # Check Ollama connection first
    if not check_ollama_connection():
        st.error("❌ **Ollama is not running or not accessible!**")
        st.markdown("""
        **To fix this issue:**
        
        1. **Install Ollama** (if not already installed):
           - Download from: https://ollama.com/download
           - Or run: `winget install Ollama.Ollama`
        
        2. **Start Ollama service:**
           - Open a new terminal/command prompt
           - Run: `ollama serve`
        
        3. **Pull a model:**
           - Run: `ollama pull llama3.2` (or any other model)
        
        4. **Restart this app** after Ollama is running
        """)
        
        st.info("💡 **Quick Start:** Open a new terminal and run these commands:")
        st.code("""
ollama serve
ollama pull llama3.2
        """)
        return
    
    # Get available models
    available_models = get_available_models()
    
    # Sidebar configuration
    with st.sidebar:
        st.title("🤖 LLMChat")
        st.markdown("---")
        
        # Model selection
        st.subheader("Model Settings")
        
        if available_models:
            model_options = available_models
            default_index = 0
        else:
            model_options = ["llama3.2", "llama3.1", "mistral", "codellama", "neural-chat"]
            default_index = 0
            st.warning("⚠️ No models found. Please pull a model using `ollama pull <model_name>`")
        
        selected_model = st.selectbox(
            "Choose Model:",
            model_options,
            index=default_index,
            help="Select the LLM model to use for generating responses"
        )
        
        # Show model status
        if available_models:
            st.success(f"✅ {len(available_models)} model(s) available")
        else:
            st.error("❌ No models available")
        
        st.markdown("---")
        
        # Information section
        st.subheader("ℹ️ About")
        st.markdown("""
        This LLM chat interface uses Ollama to generate responses.
        
        **Features:**
        - Multiple model support
        - Real-time response generation
        - Error handling
        - Clean interface
        
        **Available Models:**
        """ + "\n".join([f"- {model}" for model in available_models]) if available_models else """
        **Common Models:**
        - llama3.2 (default)
        - llama3.1
        - mistral
        - codellama
        - neural-chat
        """)
        
        st.markdown("---")
        
        # Quick actions
        st.subheader("🚀 Quick Actions")
        if st.button("Clear Chat", help="Clear the current conversation"):
            st.rerun()
        
        # Sample prompts
        st.subheader("💡 Sample Prompts")
        sample_prompts = [
            "Explain quantum computing in simple terms",
            "Write a short story about a robot learning to paint",
            "What are the benefits of renewable energy?",
            "Create a recipe for chocolate chip cookies"
        ]
        
        for prompt in sample_prompts:
            if st.button(prompt, key=f"sample_{prompt[:20]}"):
                st.session_state.user_prompt = prompt
                st.rerun()

    # Main content area
    st.title("🤖 LLMChat")
    st.markdown("Interact with an LLM assistant powered by Ollama and Streamlit")
    
    # Show connection status
    if check_ollama_connection():
        st.success("✅ Connected to Ollama")
    else:
        st.error("❌ Not connected to Ollama")
        return
    
    # Initialize session state
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    
    # User input
    st.subheader("💬 Enter Your Prompt")
    user_prompt = st.text_area(
        "What would you like to ask?",
        value=st.session_state.get('user_prompt', ''),
        height=150,
        placeholder="Type your question or prompt here...",
        help="Enter your question or prompt. The AI will generate a response based on your input."
    )
    
    # Generate response button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button(
            "🚀 Generate Response",
            type="primary",
            use_container_width=True,
            help="Click to generate an AI response"
        )
    
    # Response generation
    if generate_button:
        if user_prompt.strip() != "":
            with st.spinner("🤔 Generating response..."):
                try:
                    start_time = time.time()
                    response = generate_llm_response(user_prompt, selected_model)
                    end_time = time.time()
                    
                    # Format response
                    formatted_response = format_response(response)
                    
                    # Add to conversation history
                    st.session_state.conversation_history.append({
                        'prompt': user_prompt,
                        'response': formatted_response,
                        'model': selected_model,
                        'timestamp': time.strftime("%H:%M:%S")
                    })
                    
                    # Display success message
                    st.success(f"✅ Response generated successfully in {end_time - start_time:.2f} seconds!")
                    
                    # Display response
                    st.subheader("🤖 AI Response")
                    st.markdown(f"**Model used:** {selected_model}")
                    st.markdown(f"**Generated at:** {time.strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    # Display response in a nice format
                    st.markdown("---")
                    st.markdown(formatted_response)
                    st.markdown("---")
                    
                except Exception as e:
                    st.error(f"❌ Error generating response: {str(e)}")
                    st.info("💡 Make sure Ollama is running and the selected model is available.")
        else:
            st.warning("⚠️ Please enter a prompt to generate a response.")
    
    # Display conversation history
    if st.session_state.conversation_history:
        st.subheader("📚 Conversation History")
        
        for i, conv in enumerate(reversed(st.session_state.conversation_history)):
            with st.expander(f"💬 {conv['timestamp']} - {conv['prompt'][:50]}..."):
                st.markdown(f"**Prompt:** {conv['prompt']}")
                st.markdown(f"**Model:** {conv['model']}")
                st.markdown("**Response:**")
                st.markdown(conv['response'])
                st.markdown("---")

if __name__ == "__main__":
    main()