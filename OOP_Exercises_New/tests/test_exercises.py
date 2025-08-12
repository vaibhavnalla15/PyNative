import os
import subprocess
import pytest

# 1. Base directory (this script is inside "tests/")
BASE_DIR = os.path.dirname(__file__)
EXERCISE_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

# 2. Collect all .py files inside subfolders like Exercise01, Exercise02, etc.
exercise_files = []
for root, dirs, files in os.walk(EXERCISE_DIR):
    if "tests" in root:
        continue
    for file in files:
        if file.endswith(".py"):
            exercise_files.append(os.path.join(root, file))

# 3. Risk check (like input(), GUI, etc.)
def is_risky(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    if "input(" in code:
        return "uses input()"
    if "tkinter" in code or "webbrowser" in code:
        return "uses GUI"
    return None

# 4. Run each .py file as a test
@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)

    risky = is_risky(exercise_file)
    if risky:
        pytest.skip(f"⛔ Skipped {file_name} — {risky}")

    try:
        result = subprocess.run(
            ["python", exercise_file],
            capture_output=True,
            text=True,
            timeout=5  # Max 5 seconds per script
        )
        assert result.returncode == 0, f"❌ {file_name} failed\n{result.stderr}"
    except subprocess.TimeoutExpired:
        pytest.fail(f"⏳ {file_name} timed out (over 5s)")
