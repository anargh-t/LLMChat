"""
Setup file for LLMChat

A modern, interactive LLM chat interface built with Streamlit and Ollama.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="llmchat",
    version="1.0.0",
    author="Anargh T",
    author_email="your.email@example.com",
    description="A modern, interactive LLM chat interface built with Streamlit and Ollama",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llmchat",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "llmchat=chatbot:main",
        ],
    },
    keywords="llm, chatbot, streamlit, ollama, ai, machine learning",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/llmchat/issues",
        "Source": "https://github.com/yourusername/llmchat",
        "Documentation": "https://github.com/yourusername/llmchat#readme",
    },
) 