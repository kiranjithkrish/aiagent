
from functions.get_files_info import  get_files_info
from functions.get_file_content import  get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file
from google.genai import types
from config import WORKING_DIR

function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file
}

def call_function(function_call_part, verbose=False):
    func_name = function_call_part.name
    func_args = function_call_part.args
    func_args["working_directory"] = './calculator'
    if verbose:
        print(f"Calling function: {func_name}({func_args})")
    else:
        print(f'- Calling function: {function_call_part.name}')
    function = function_map.get(func_name)
    if not function:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    try:
        function_result = function(**func_args)
    except Exception as e:
        function_result = f"Error executing {func_name}: {str(e)}"
    return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=func_name,
            response={"result": function_result},
        )
    ],
)