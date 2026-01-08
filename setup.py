import sys
from shutil import which as hasCommand
import venv

isVenv: bool = not (sys.prefix == sys.base_prefix) #checking if the environment is the vitrual environment
version: str = sys.version
isGeminiInstalled = hasCommand("gemini")

print("Start environment check...")

print(f"environment check... {'ok' if isVenv else 'Recommend to use the vitural environment.'}")
print(f"python version check {'ok' if '3.13' in sys.version.split()[0] else '{} which is not compatible, use 3.13.X instaed'.format(sys.version.split()[0])}")
print(f"Gemini CLI check... {'ok' if isGeminiInstalled else 'Not installed, instal by python package later.'}")

if not isVenv:
    print("[WARNING] This will erase the existed venv under the pwd")
    name = input("Creating the new venv with the name: ")
    venv.EnvBuilder(
        with_pip=True,
        clear=False,
        symlinks=True,
        upgrade=False
    ).create(name)

if sys.platform == "win32":
    exec("venv/bin/pip.exe install -r ")
elif sys.platform == "darwin" or sys.platform == "linux":
    pass