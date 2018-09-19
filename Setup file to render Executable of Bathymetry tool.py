import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["numpy","matplotlib","rasterio","gdal","sklearn","scipy"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe =Executable(script="bathymetryfinal.py", base=base,targetName="Bathymetry_Tool2.exe")

setup(  name = "Bathymetry Tool",
        version = "1.0",
        description = "Incorporates Lyzenga WCC & Depth Processing",
		options = {"build_exe": build_exe_options},
        executables = [exe])