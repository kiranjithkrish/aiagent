import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


def print_token_usage(content_res):
    if not content_res.usage_metadata:
        print("Usage metadata not available")
        return
    usage = content_res.usage_metadata
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count
    print(f'Prompt tokens: {prompt_tokens}')
    print(f'Response tokens:{response_tokens}')


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg == "--verbose"]
    if not args:
        print("Error: Please provide a prompt")
        sys.exit(1)
    user_prompt = " ".join(args)
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
        
    content_res = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)
    if verbose:
        print(f'User prompt: {content_res.text}')
        print_token_usage(content_res)
    
if __name__ == "__main__":
    main()

