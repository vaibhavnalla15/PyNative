# tests/test_exercises.py
import os
import pytest
import glob


# Function to check if a file needs user input
def needs_input(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        return "input(" in content


# Dynamically get the folder name where this test file lives
current_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Collect all .py files recursively in that folder (excluding tests)
exercise_files = glob.glob(os.path.join(current_folder, "**", "*.py"), recursive=True)
exercise_files = [f for f in exercise_files if "tests" not in f]


@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)

    # Skip if the file requires user input
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} because it requires user input")

    # Run the file and assert it exits without error
    assert os.system(f'python "{exercise_file}"') == 0
