
import os
from google.genai import types

def write_file(working_directory, file_path, content):
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(os.path.join(working_directory, file_path))
    if not child.startswith(parent):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(child, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: File path filed to create with error {e}'
    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
