import os
import glob
import pytest

base_path = "Loop_Exercise"

# Find all Exercise*.py files in Loop_Exercise
exercise_files = glob.glob(os.path.join(base_path, "Exercise*.py"))

# Exclude exercises that require input
skip_files = [
    "Exercise03 (Sum of 1-10).py",
    "Exercise04 (Multiplication Table).py",
    "Exercise06 (Count the total number).py",
]

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)
    if file_name in skip_files:
        pytest.skip(f"Skipped {file_name} because it requires user input")
    assert os.system(f'python "{exercise_file}"') == 0
