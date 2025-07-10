# 🤖 LLMChat

A modern, interactive LLM chat interface built with Streamlit and Ollama that allows users to generate responses using various LLM models.

## ✨ Features

- **Interactive Web Interface**: Clean and intuitive Streamlit-based UI
- **Multiple LLM Models**: Support for various Ollama models (default: llama3.2)
- **Real-time Response Generation**: Instant AI responses to user prompts
- **Error Handling**: Robust error handling with user-friendly messages
- **Responsive Design**: Works seamlessly across different devices
- **Easy Deployment**: Simple setup and deployment process

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Ollama installed and running locally
- At least one LLM model downloaded via Ollama

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llmchat.git
   cd llmchat
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install and setup Ollama**
   ```bash
   # Download Ollama from https://ollama.ai/
   # Then pull a model (e.g., llama3.2)
   ollama pull llama3.2
   ```

4. **Run the application**
   ```bash
   streamlit run chatbot.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501` to access the chatbot.

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```
streamlit>=1.28.0
ollama>=0.1.0
```

## 🎯 Usage

1. **Start the Application**: Run `streamlit run chatbot.py`
2. **Enter Your Prompt**: Type your question or prompt in the text area
3. **Generate Response**: Click the "Generate Response" button
4. **View Results**: The AI-generated response will appear below

### Example Prompts

- "Explain quantum computing in simple terms"
- "Write a short story about a robot learning to paint"
- "What are the benefits of renewable energy?"
- "Create a recipe for chocolate chip cookies"

## 🔧 Configuration

### Changing the Model

You can modify the default model in `chatbot.py`:

```python
def generate_llm_response(prompt, model="llama3.2"):  # Change model here
```

Available models include:
- `llama3.2` (default)
- `llama3.1`
- `mistral`
- `codellama`
- `neural-chat`

### Customizing the Interface

The Streamlit interface can be customized by modifying:
- Title and descriptions
- Text area sizes
- Button styling
- Response formatting

## 🛠️ Development

### Project Structure

```
llmchat/
├── chatbot.py          # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .gitignore         # Git ignore file
└── examples/          # Example prompts and responses
    └── sample_prompts.txt
```

### Adding New Features

1. **New Models**: Add support for additional Ollama models
2. **Chat History**: Implement conversation memory
3. **File Upload**: Allow users to upload documents for analysis
4. **Export Responses**: Add functionality to save conversations
5. **Custom Styling**: Enhance the UI with custom CSS

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include error handling for new features
- Test your changes before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Ollama](https://ollama.ai/) for providing easy access to LLM models
- The open-source community for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/llmchat/issues) page
2. Create a new issue with detailed information
3. Include your system information and error messages

## 🔮 Roadmap

- [ ] Add conversation history
- [ ] Support for file uploads
- [ ] Multiple model selection in UI
- [ ] Export conversation feature
- [ ] Custom model fine-tuning
- [ ] API endpoint for external integrations
- [ ] Mobile-responsive design improvements

---

**Made with ❤️ using Streamlit and Ollama**

⭐ **Star this repository if you find it helpful!** 