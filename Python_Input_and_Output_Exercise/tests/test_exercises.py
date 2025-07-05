import os
import glob
import pytest

# Find all .py files recursively in all subfolders
exercise_files = glob.glob("Python_Input_and_Output_Exercise/**/*.py", recursive=True)

# Skip list: add any files that require user input
skip_files = [
    "Exercise06/file_needs_input.py",  # Example: replace with actual file if needed
    "Exercise09/another_input_file.py"
]

def needs_input(file_path):
    return any(skip_name in file_path for skip_name in skip_files)

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} because it requires user input")
    assert os.system(f'python "{exercise_file}"') == 0
