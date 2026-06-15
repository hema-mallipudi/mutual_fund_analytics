"""
Master execution script
"""

import subprocess

scripts = [
    "clean_fund_master.py",
    "clean_nav_history.py",
    "clean_scheme_performance.py",
    "load_to_sqlite.py"
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])