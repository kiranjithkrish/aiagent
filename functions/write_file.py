
import os

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
    