"""
Test file for LLMChat

This file contains basic tests to ensure the LLM chat interface functionality works correctly.
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the current directory to the path so we can import chatbot
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot import generate_llm_response, format_response

class TestChatbot(unittest.TestCase):
    """Test cases for the LLMChat interface."""
    
    def test_format_response(self):
        """Test the format_response function."""
        # Test with normal response
        response = "  Hello, world!  "
        formatted = format_response(response)
        self.assertEqual(formatted, "Hello, world!")
        
        # Test with empty response
        response = ""
        formatted = format_response(response)
        self.assertEqual(formatted, "")
        
        # Test with response containing newlines
        response = "  Line 1\n  Line 2  "
        formatted = format_response(response)
        self.assertEqual(formatted, "Line 1\n  Line 2")
    
    @patch('chatbot.ollama')
    def test_generate_llm_response_success(self, mock_ollama):
        """Test successful response generation."""
        # Mock the ollama response
        mock_response = {
            'message': {
                'content': 'This is a test response'
            }
        }
        mock_ollama.chat.return_value = mock_response
        
        # Test the function
        result = generate_llm_response("Test prompt", "llama2")
        
        # Verify the result
        self.assertEqual(result, "This is a test response")
        
        # Verify ollama.chat was called correctly
        mock_ollama.chat.assert_called_once_with(
            model="llama2",
            messages=[{'role': 'user', 'content': 'Test prompt'}]
        )
    
    @patch('chatbot.ollama')
    def test_generate_llm_response_error(self, mock_ollama):
        """Test error handling in response generation."""
        # Mock ollama to raise an exception
        mock_ollama.chat.side_effect = Exception("Connection error")
        
        # Test that the function raises an exception
        with self.assertRaises(Exception) as context:
            generate_llm_response("Test prompt", "llama2")
        
        # Verify the error message
        self.assertIn("Error communicating with Ollama", str(context.exception))
    
    def test_generate_llm_response_invalid_input(self):
        """Test response generation with invalid input."""
        # Test with empty prompt
        with self.assertRaises(Exception):
            generate_llm_response("", "llama2")
        
        # Test with None prompt
        with self.assertRaises(Exception):
            generate_llm_response(None, "llama2")

if __name__ == '__main__':
    unittest.main() 