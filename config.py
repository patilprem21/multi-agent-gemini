"""
Configuration module for the Multi-Agent System
Handles API key management and model configuration
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

def configure_gemini():
    """
    Configure the Gemini API with the API key from environment variables
    
    Returns:
        genai.GenerativeModel: Configured Gemini model
        
    Raises:
        ValueError: If API key is not found or invalid
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please check your .env file and ensure "
            "you have set your Gemini API key. Get your API key from: "
            "https://makersuite.google.com/app/apikey"
        )
    
    # Configure the API
    genai.configure(api_key=api_key)
    
    # Return the model instance
    # Using gemini-2.5-flash for compatibility
    return genai.GenerativeModel('gemini-2.5-flash')

def validate_api_key():
    """
    Validate that the API key is working by making a test call
    
    Returns:
        bool: True if API key is valid, False otherwise
    """
    try:
        model = configure_gemini()
        # Make a simple test call
        response = model.generate_content("Hello, this is a test.")
        return response.text is not None
    except Exception as e:
        print(f"API key validation failed: {e}")
        return False
