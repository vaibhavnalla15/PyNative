import os
import pytest
import glob

def needs_input(file_path):
    """Return True if the file requires user input or uses 'test.txt'."""
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
        if "input(" in code:
            return True
        if "test.txt" in code:
            return True
    return False

# Collect all .py files in the folder and its subfolders
exercise_files = glob.glob("Python_Input_and_Output_Exercise/**/*.py", recursive=True)

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} because it requires user input or file")
    # Run the script and check it runs without error
    assert os.system(f'python "{exercise_file}"') == 0
