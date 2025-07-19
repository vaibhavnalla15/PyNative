# File: tests/test_exercises.py

import os
import pytest
import glob
import shutil
import tempfile

# Check if a file requires user input
def needs_input(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        return "input(" in content

# Automatically get all .py files inside the exercise folder (excluding test files)
current_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
exercise_files = glob.glob(os.path.join(current_folder, "**", "*.py"), recursive=True)
exercise_files = [f for f in exercise_files if "tests" not in f]

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file_in_temp_dir(exercise_file):
    file_name = os.path.basename(exercise_file)

    # Skip if file requires user input
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} because it requires user input")

    # Create a temporary folder as a safe test environment
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change to temp directory
        original_dir = os.getcwd()
        os.chdir(temp_dir)

        try:
            # Copy the script into temp folder and run it safely
            temp_script = os.path.join(temp_dir, file_name)
            shutil.copy(exercise_file, temp_script)

            # Run the script
            exit_code = os.system(f'python "{temp_script}"')

            assert exit_code == 0, f"{file_name} crashed with exit code {exit_code}"

        finally:
            # Always return to original directory
            os.chdir(original_dir)
