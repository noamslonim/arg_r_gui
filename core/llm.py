import openai
import os
from typing import List, Tuple
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file automatically

def get_api_key() -> str:
    """Get the OpenAI API key from environment variables."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
        )
    return api_key

# Initialize the OpenAI client with the API key from environment
try:
    client = openai.OpenAI(api_key=get_api_key())
except ValueError as e:
    print(f"Error initializing OpenAI client: {e}")
    client = None

def call_llm(messages: List[dict], model: str = "gpt-4-turbo", temperature: float = 0.7) -> str:
    """
    Call the OpenAI API with the given messages.
    
    Args:
        messages: List of dicts like [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]
        model: The model to use, e.g., "gpt-4-turbo"
        temperature: Controls randomness in the response (0.0 to 1.0)
    
    Returns:
        str: The assistant's message
    
    Raises:
        ValueError: If the OpenAI client is not properly initialized
    """
    if client is None:
        raise ValueError("OpenAI client not properly initialized. Check your API key.")
        
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

def load_prompt_file(path: str) -> Tuple[str, str]:
    """
    Load a Markdown-formatted prompt file and return (system, user) strings.
    The file should contain a section starting with '### System' and one with '### User'.
    
    Args:
        path: Path to the prompt file
        
    Returns:
        Tuple[str, str]: The system and user messages
        
    Raises:
        ValueError: If the file doesn't contain required sections
        FileNotFoundError: If the file doesn't exist
    """
    with open(path, encoding="utf-8") as f:
        content = f.read()

    try:
        system_part = content.split("### System")[1].split("### User")[0].strip()
        user_part = content.split("### User")[1].strip()
        return system_part, user_part
    except IndexError:
        raise ValueError(f"Prompt file {path} must contain '### System' and '### User' sections.")
