import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import re
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function
from prompts import system_prompt

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
    if verbose:
        print(f'User prompt: {user_prompt}')
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
  
    for i in range(20):
        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print(f"Recieved the final response {final_response}")
                break
        except Exception as e:
            print(f'Error: Generate content failed with Error {e}')

def generate_content(client, messages, verbose):
    content_res = client.models.generate_content(
                    model='gemini-2.0-flash-001', 
                    contents=messages,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt,
                        tools=[available_functions]
                        ),
                )
    if content_res.candidates:
        for variation in content_res.candidates:
            content = variation.content
            messages.append(content)
    if verbose:
        print_token_usage(content_res)
    
    if not content_res.function_calls:
        if verbose:
            print('No function calls, return the response')
        return content_res.text
        
    function_calls = content_res.function_calls
    function_responses = []
    for function_call_part in function_calls:
        function_call_result = call_function(function_call_part, verbose)
       
        function_call_response = function_call_result.parts[0].function_response.response
        if not function_call_response:
            raise Exception('empty function call result')
        if verbose:
            print(f'Calling function {function_call_part.name}')
            print(f'-> {function_call_response}')
        function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    message = types.Content(role="tool", parts=function_responses)
    messages.append(message)
        

    
if __name__ == "__main__":
    main()

