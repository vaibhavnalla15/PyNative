import os
import glob
import pytest
import subprocess

# ✅ Helper: Check if file needs user input
def needs_input(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return "input(" in f.read()

# ✅ Helper: Check for risky patterns
def has_infinite_or_gui_code(file_path):
    risky_patterns = [
        "while True",
        "webbrowser.open(",
        "tkinter",
        "cv2.imshow(",
        "pygame.init(",
        "plt.show(",
        "time.sleep(",  # we’ll check actual value below
        "secrets.SystemRandom("
    ]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        for pattern in risky_patterns:
            if pattern in content:
                return pattern
        return None

# ✅ Helper: Check for long sleep
def has_long_sleep(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "time.sleep(" in line:
                try:
                    value = float(line.strip().split("sleep(")[1].split(")")[0])
                    if value > 5:
                        return True
                except:
                    continue
    return False

# ✅ Find all .py files in the exercise folder (excluding test files)
current_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
exercise_files = glob.glob(os.path.join(current_folder, "*.py"))

@pytest.mark.parametrize("exercise_file", exercise_files)
def test_exercise_file(exercise_file):
    file_name = os.path.basename(exercise_file)

    if needs_input(exercise_file):
        pytest.skip(f"❌ Skipped {file_name} (uses input())")

    risky_code = has_infinite_or_gui_code(exercise_file)
    if risky_code:
        pytest.fail(f"🚨 {file_name} contains risky pattern: {risky_code}")

    if has_long_sleep(exercise_file):
        pytest.fail(f"🕒 {file_name} contains time.sleep() > 5 sec")

    # Run with timeout: 10 seconds
    try:
        result = subprocess.run(
            ["python", exercise_file],
            timeout=10,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, f"❌ {file_name} failed\n{result.stderr}"
    except subprocess.TimeoutExpired:
        pytest.fail(f"⏱️ Timeout: {file_name} took too long to complete (10s)")
