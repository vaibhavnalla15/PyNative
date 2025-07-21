import os
import subprocess
import pytest

# Step 1: Get the path to the exercises folder
BASE_DIR = os.path.dirname(__file__)  # tests/
EXERCISE_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # Random Data Generation Exercise/

# Step 2: Gather all .py files in the folder
exercise_files = [
    os.path.join(EXERCISE_DIR, f)
    for f in os.listdir(EXERCISE_DIR)
    if f.endswith(".py")
]

# Step 3: Function to detect risky patterns
def is_risky(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    if "input(" in code:
        return "uses input()"
    if "tkinter" in code or "webbrowser" in code:
        return "GUI module"
    if code.count("secrets.SystemRandom") > 2:
        return "too many secrets.SystemRandom"
    if "time.sleep(" in code and any(x in code for x in ["10", "15", "20"]):
        return "long sleep"
    return None

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)

    # Step 4: Check if it's risky and skip or fail
    risk = is_risky(exercise_file)
    if risk:
        pytest.skip(f"⛔ Skipped {file_name} — {risk}")

    # Step 5: Run with a 5-second timeout
    try:
        result = subprocess.run(
            ["python", exercise_file],
            capture_output=True,
            text=True,
            timeout=5  # ⏱ Timeout to prevent hang
        )
        assert result.returncode == 0, f"❌ {file_name} failed\n{result.stderr}"
    except subprocess.TimeoutExpired:
        pytest.fail(f"⏳ {file_name} timed out (over 5s)")

