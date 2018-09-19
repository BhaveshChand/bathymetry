import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["numpy","matplotlib","rasterio","gdal"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe =Executable(script="depthlabel.py", base=base,targetName="Bathymetry_Tool.exe")

setup(  name = "Bathymetry Tool",
        version = "1.0",
        description = "Enables creating csv file having labels of training data",
		options = {"build_exe": build_exe_options},
        executables = [exe])