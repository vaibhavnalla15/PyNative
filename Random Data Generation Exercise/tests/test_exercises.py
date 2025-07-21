import os
import subprocess
import pytest

# ✅ Get absolute path to the exercise folder
BASE_DIR = os.path.dirname(__file__)  # path to /tests
EXERCISE_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # path to /Random Data Generation Exercise

# ✅ Grab all exercise .py files
exercise_files = [
    os.path.join(EXERCISE_DIR, f)
    for f in os.listdir(EXERCISE_DIR)
    if f.endswith(".py")
]

def needs_input(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return "input(" in f.read()

def has_infinite_or_gui_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

        if "tkinter" in content or "webbrowser" in content:
            return "tkinter or webbrowser"

        if content.count("secrets.SystemRandom") > 3:
            return "secrets.SystemRandom() in loop"

        return None

def has_long_sleep(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return "time.sleep(" in content and any(d in content for d in ["10", "15", "20"])

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)

    if needs_input(exercise_file):
        pytest.skip(f"❌ Skipped {file_name} (uses input())")

    risky_code = has_infinite_or_gui_code(exercise_file)
    if risky_code:
        pytest.fail(f"🚨 {file_name} contains risky pattern: {risky_code}")

    if has_long_sleep(exercise_file):
        pytest.fail(f"🕒 {file_name} contains long time.sleep()")

    try:
        result = subprocess.run(
            ["python", exercise_file],
            timeout=10,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, f"❌ {file_name} failed\n{result.stderr}"
    except subprocess.TimeoutExpired:
        pytest.fail(f"⏳ {file_name} timed out (>10s)")
