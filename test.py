import subprocess

script_path = r"C:\Users\svafadar\Projects\brightness_dimmer\BrightnessDimmer\sleepsleep.ps1"

# executable file name for interpeter | run file not interactive command
subprocess.run(['powershell.exe', '-File', script_path])

