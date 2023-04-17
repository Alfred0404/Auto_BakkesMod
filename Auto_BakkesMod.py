import os
import psutil

#? Python script that checks if Rocket League is running and if BakkesMod is running, if not it runs BakkesMod
#? Use this to always play Rocket League with BakkesMod without having to open BakkesMod manually

#! --------------------- VARIABLES --------------------- #

#* ----- paths
RL_path = r"C:\Program Files (x86)\Steam\steamapps\common\rocketleague\Binaries\Win64\RocketLeague.exe"
bakkesmod_path = r"C:\Program Files\BakkesMod\BakkesMod.exe"

#* ----- apps process
RL_exe = "RocketLeague.exe"
bakkesmod_exe = "BakkesMod.exe"


#! --------------------- FUNCTIONS --------------------- #

#* ----- function that runs an app
def run_app(file_path) :
    if os.path.exists(file_path) :
        os.startfile(file_path)
        return 0
    return 1


#* ----- function that checks if a process is running
def check_process(process_name) :
    return str(process_name) in (i.name() for i in psutil.process_iter())


#* ----- function that checks if RL is running and if BakkesMod is running, if not it runs BakkesMod
def run() :
    if check_process(RL_exe) :
        if not check_process(bakkesmod_exe) :
            run_app(bakkesmod_path)
run()