import os
import glob
import pytest

base_path = "Functions Exercise"  # Change this to your folder name

exercise_files = glob.glob(os.path.join(base_path, "Exercise*.py"))

def needs_input(file_path):
    """Check if the file contains 'input(' (case-insensitive)"""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return "input(" in content or "input (" in content

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} because it requires user input")
    assert os.system(f'python "{exercise_file}"') == 0
