import os
from functions.get_files_info import is_subdir
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(file_path)
    if not os.path.isfile(child):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not is_subdir(parent, child):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS+1)
            if len(file_content_string) > MAX_CHARS:
                truncated = file_content_string[:MAX_CHARS] + f'"{file_path}" truncated at {MAX_CHARS} characters'
                file_content_string = truncated
        return file_content_string
    except Exception as e:
        return f'Error: Read file failed with {e}'

            
            
    
    
    
    