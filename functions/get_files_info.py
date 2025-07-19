
import os

def is_subdir(parent, child):
    # Add separator to avoid prefix errors
    parent = os.path.join(parent, '')
    child = os.path.join(child, '')
    return child.startswith(parent)

def get_files_info(working_directory, directory="."):
    
    parent = os.path.abspath(working_directory)
    child = os.path.abspath(directory)
    
    if not os.path.isdir(child):
        return f'Error: "{directory}" is not a directory'
    if not is_subdir(parent, child):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    try:
        contents = os.listdir(child)
        dir_name = "current" if directory == "." else directory
        result_str = f'Result for {dir_name} directory:\n'
        for name in contents:
            fullPath = os.path.join(child, name)
            size = os.path.getsize(fullPath)
            is_dir = os.path.isdir(fullPath)
            res = f'- {name}: file_size={size} bytes, is_dir={is_dir}\n'
            result_str += res
        return result_str
    except Exception as e:
        return f'Error listing files: {e}'