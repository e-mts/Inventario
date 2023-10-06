# build.py

import subprocess

subprocess.run([
    'pyinstaller',
    '--onefile',  # Create a single executable file
    'main.py',  # Replace with the name of your main script
])