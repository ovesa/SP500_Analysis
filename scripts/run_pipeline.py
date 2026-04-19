import subprocess
import sys

steps = [
    ("Downloading raw data", "scripts/download_data.py"),
    ("Cleaning data", "scripts/clean_data.py"),
]

for label, script in steps:
    print(f"Running: {label}")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"\nPipeline failed at: {script}")
        sys.exit(1)

print("\nPipeline complete. Ready for EDA.")
