import os
import subprocess
from google.genai import types

def format_output(output: subprocess.CompletedProcess):
    stdout = output.stdout.decode('utf-8', errors='replace') if output.stdout else ''
    stderr = output.stderr.decode('utf-8', errors='replace') if output.stderr else ''
    parts = []
    if stdout:
        parts.append(f'STDOUT: {stdout}')
    if stderr:
        parts.append(f'STDERR: {stderr}')
    if output.returncode != 0:
        parts.append(f'Process exited with code {output.returncode}')
    if not parts:
        return "No output produced"
    return '\n'.join(parts)

def run_python_file(working_directory, file_path, args=[]):
    abs_wd = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_wd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed_process = subprocess.run(
                    ['uv', 'run', file_path, *args], 
                    capture_output=True, 
                    timeout=30,
                    check=True,
                    cwd=abs_wd
                )
        return format_output(completed_process)
        
        
    except subprocess.CalledProcessError as e:
        return f'Error: executing Python file: {e}'



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file with args in the directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="The arguments required to run the python file"
            )
        },
    ),
)  