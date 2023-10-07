# build.py

import subprocess
import venv
import sys
import os
import shutil

def create_virtualenv(venv_dir):
    venv.create(venv_dir, with_pip=True)

def install_dependencies(venv_dir):
    subprocess.run([os.path.join(venv_dir, 'Scripts' if sys.platform == 'win32' else 'bin', 'pip'), 'install', '-r', 'requirements.txt'])

def build_exe(venv_dir, exe_name='your_script.exe'):
    subprocess.run([os.path.join(venv_dir, 'Scripts' if sys.platform == 'win32' else 'bin', 'pyinstaller'), 'main.py', '--onefile'])
    
    # Move the executable to the root folder with the specified name
    shutil.move(os.path.join('dist', 'main.exe'), exe_name)

def remove_virtualenv(venv_dir):
    # Remove the temporary virtual environment
    shutil.rmtree(venv_dir, ignore_errors=True)

if __name__ == '__main__':
    venv_dir = 'temp_venv'  # Directory to create the temporary virtual environment
    create_virtualenv(venv_dir)
    install_dependencies(venv_dir)
    
    # You can specify the desired name for the executable here
    exe_name = 'Sistema Administrativo de Inventario.exe'
    
    build_exe(venv_dir, exe_name)

    # Remove the temporary virtual environment after building
    remove_virtualenv(venv_dir)