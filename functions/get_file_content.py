import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(os.path.join(working_directory, file_path))
    print(f"DEBUG: Attempting to read file at: {child}") 
    if not os.path.isfile(child):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not child.startswith(parent):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(child, "r") as f:
            file_content_string = f.read(MAX_CHARS+1)
            if len(file_content_string) > MAX_CHARS:
                truncated = file_content_string[:MAX_CHARS] + f'"{file_path}" truncated at {MAX_CHARS} characters'
                file_content_string = truncated
        return file_content_string
    except Exception as e:
        return f'Error: Read file failed with {e}'

          

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)         
    
    
    
    