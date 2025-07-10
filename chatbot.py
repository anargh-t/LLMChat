"""
LLMChat - LLM Chat Interface

A modern, interactive LLM chat interface that allows users to generate responses
using various LLM models through Ollama.

Author: Anargh T
Date: 2025
License: MIT
"""

import streamlit as st
import ollama
import time
from typing import Optional

# Page configuration
st.set_page_config(
    page_title="LLMChat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def generate_llm_response(prompt: str, model: str = "llama2") -> str:
    """
    Generate a response from the LLM using Ollama.
    
    Args:
        prompt (str): The user's input prompt
        model (str): The Ollama model to use (default: llama2)
    
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
    
    # Sidebar configuration
    with st.sidebar:
        st.title("🤖 LLMChat")
        st.markdown("---")
        
        # Model selection
        st.subheader("Model Settings")
        model_options = ["llama2", "llama3", "mistral", "codellama", "neural-chat"]
        selected_model = st.selectbox(
            "Choose Model:",
            model_options,
            index=0,
            help="Select the LLM model to use for generating responses"
        )
        
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
        
        **Models Available:**
        - llama2 (default)
        - llama3
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