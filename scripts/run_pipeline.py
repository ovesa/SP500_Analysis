import subprocess
import sys
import os

steps = [
    ("Downloading raw data", "scripts/download_data.py"),
    ("Cleaning data + generating Power BI CSV", "scripts/clean_data.py"),
]

for label, script in steps:
    if not os.path.exists(script):
        print(f"Script not found: {script}")
        sys.exit(1)
    print(f"\n{'='*50}")
    print(f"Running: {label}")
    print(f"{'='*50}")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"\nPipeline failed at: {script}")
        sys.exit(1)

print("\n" + "="*50)
print("Pipeline complete.")
print("Output: data/cleaned/all_sectors_combined.csv")
print("Upload this file to Power BI to refresh your dashboard.")
print("="*50)