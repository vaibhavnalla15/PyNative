import os
import pytest
import glob
import subprocess


# Check if file uses input()
def needs_input(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return "input(" in file.read()


# Locate the root "File Handling Exercise" folder
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get all Python files inside each ExerciseXX folder (but not in 'tests')
exercise_files = []
for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    if "tests" in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".py"):
            exercise_files.append(os.path.join(dirpath, filename))


@pytest.mark.parametrize("exercise_file", exercise_files)
def test_file_handling_exercise(exercise_file):
    file_name = os.path.basename(exercise_file)

    # Skip files with input()
    if needs_input(exercise_file):
        pytest.skip(f"Skipped {file_name} (uses input())")

    # Run the script in its own directory to access txt files locally
    working_dir = os.path.dirname(exercise_file)
    result = subprocess.run(["python", exercise_file], cwd=working_dir)

    assert result.returncode == 0, f"{file_name} failed with exit code {result.returncode}"
