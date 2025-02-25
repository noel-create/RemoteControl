import shutil
import os
from pathlib import Path
import time
import sys
import subprocess
import tempfile

time.sleep(1)

user_profile = os.environ['USERPROFILE']
target_path = os.path.join(user_profile, 'AppData', 'Roaming', 'Microsoft', 'Windows')
shutil.rmtree(os.path.join(target_path, "skibidi-startup"))
shutil.rmtree(os.path.join(target_path, "skibidi-mainmain"))
startup_dir = Path(os.getenv("APPDATA")) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
shortcut_name="MyPythonScript"
shortcut_path = startup_dir / f"{shortcut_name}.lnk"
os.remove(shortcut_path)
file_path = __file__

# Create a temporary batch script
batch_script = f'''@echo off
timeout /t 2 /nobreak >nul
del "{file_path}"
del "%~f0"
'''

# Save the batch script in a temporary file
batch_path = os.path.join(tempfile.gettempdir(), "delete_me.bat")
with open(batch_path, "w") as bat_file:
    bat_file.write(batch_script)

# Run the batch file in a hidden process
subprocess.Popen(
    [batch_path],
    shell=True,
    creationflags=subprocess.CREATE_NO_WINDOW
)

sys.exit()