# test_exercises.py (inside String Exercise/tests)

import os
import pytest
import glob


# Function to check if a file needs user input
def needs_input(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        return "input(" in content


# Collect all Python files recursively from the String Exercise folder
exercise_files = glob.glob("String Exercise/**/*.py", recursive=True)
exercise_files += glob.glob("String Exercise/*.py", recursive=True)


@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)

    # Skip if the exercise requires user input
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} because it requires user input")

    # Run the exercise file and check exit code
    assert os.system(f'python "{exercise_file}"') == 0
