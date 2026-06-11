# run_experiments.py
# This root file acts as a wrapper for backward compatibility.
# The clean, open-science implementation is located at code/run_experiments.py.

import os
import sys
import subprocess

if __name__ == "__main__":
    script_path = os.path.join("code", "run_experiments.py")
    if os.path.exists(script_path):
        result = subprocess.run([sys.executable, script_path])
        sys.exit(result.returncode)
    else:
        print(f"Error: Could not find experimental script at {script_path}", file=sys.stderr)
        sys.exit(1)
