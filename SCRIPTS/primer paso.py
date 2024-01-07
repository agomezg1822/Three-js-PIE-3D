import sys
import subprocess
import os

# Especifica la ruta donde deseas crear el entorno virtual
env_path = "/Users/andresguevara/Library/CloudStorage/OneDrive-UniversidadDistritalFranciscoJosédeCaldas/UNIVERSIDAD/pie 3d/PRUEBA FINAL"

# Crea el entorno virtual
subprocess.call([sys.executable, "-m", "venv", env_path])

# Activa el entorno virtual
if sys.platform == "darwin":  # "macos" se ha cambiado a "darwin"
    activate_script = os.path.join(env_path, "bin", "activate")
else:
    activate_script = os.path.join(env_path, "bin", "activate")

subprocess.call(f"source {activate_script}", shell=True)

# Instala pandas utilizando pip
subprocess.call([sys.executable, "-m", "pip", "install", "pandas"])
subprocess.call([sys.executable, "-m", "pip", "install", "openpyxl"])
subprocess.call([sys.executable, "-m", "pip", "install", "matplotlib"])
