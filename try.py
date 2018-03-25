import os
import shutil
from pathlib import Path
xsmps_name = 'adtrain_1'
if os.path.exists(Path('./sd/Build/Products/Debug/sdinput/') / xsmps_name):
    shutil.rmtree(os.path.join('./sd/Build/Products/Debug/sdinput', xsmps_name))
shutil.copytree(Path('./model/input/')/  xsmps_name, Path('./sd/Build/Products/Debug/sdinput/')/ xsmps_name)
os.system('cd ./sd/Build/Products/Debug && ./sd ' +  xsmps_name)
if os.path.exists(os.path.join('./model/output/',  xsmps_name)):
    shutil.rmtree(os.path.join('./model/output/',  xsmps_name))
if not os.path.exists('./sd/Build/Products/Debug/sdoutput/' + xsmps_name):
    raise ValueError("Input data files not work")
else: 
    shutil.copytree(os.path.join('./sd/Build/Products/Debug/sdoutput', xsmps_name),os.path.join('./model/output/',  xsmps_name))