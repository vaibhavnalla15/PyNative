# 🔁 Script to Rename Python Files with Leading Zeros
# This script renames files like "Exercise 1.py", "Exercise 2.py", etc.
# to "Exercise01 (First 10 natural numbers).py", "Exercise02.py", ..., so they appear in correct order when viewed on GitHub or in any file explorer.
# Useful for sorting exercises or projects numerically.

import os

folder_path = r"F:\Python\100Days of Projects\PyNative\Python Basic Exercise"

print("📁 Checking folder:", folder_path)

files = os.listdir(folder_path)
print("Files found:", files)

for filename in files:
    if filename.lower().startswith("exercise") and filename.lower().endswith(".py"):
        # Handle the space between "Exercise" and number
        number_part = filename.replace("Exercise ", "").replace(".py", "")
        if number_part.isdigit():
            new_number = number_part.zfill(2)
            new_filename = f"Exercise{new_number}.py"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {filename} → {new_filename}")
        else:
            print(f"❌ Skipped (not a number): {filename}")
    else:
        print(f"❌ Skipped (doesn't match pattern): {filename}")
