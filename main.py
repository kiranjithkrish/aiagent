import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_file,
        schema_get_file_content,
        schema_run_python_file
    ]
)


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
    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    if verbose:
        print(f'User prompt: {user_prompt}')   
    content_res = client.models.generate_content(
                    model='gemini-2.0-flash-001', 
                    contents=messages,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        tools=[available_functions]
                        ),
                )
    if verbose:
        print_token_usage(content_res)
    
    calls = content_res.function_calls
    function_responses = []
    for call in calls:
        function_call_result = call_function(call, verbose)
        if not function_call_result.parts[0].function_response.response:
            raise Exception('empty function call result')
        function_call_response = function_call_result.parts[0].function_response.response
        if verbose:
            print(f'-> {function_call_response}')
        function_responses.append(function_call_response)
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
                
        
    
    
if __name__ == "__main__":
    main()

