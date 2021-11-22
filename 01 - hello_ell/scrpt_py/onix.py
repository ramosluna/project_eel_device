import CANoe
import time
import eel
from easygui import *
from os.path import exists
path = r"D:\Simulações\ONIX_SW\Simulacao\GMOnix_Simulation_Conti_SVDO_BRIP_04\GlobalA-IPC_V7_0.cfg"
adress = 0x0
listaEeprom = []


def startCANoe():
    try:
        global app
        app = CANoe.CANoe()
        app.open_simulation(path)
        app.stop_Measurement()
        app.start_Measurement()

        eel.sleep(10)
    except:
        print("An exception occurred openCanoe")

# def openPage():
#
#     eel.init("../web/html")
#     eel.show('dump.html')
#     eel.sleep(2)

def readEprom(nameSaveDump):
    name_salve_file = nameSaveDump + '.txt'
    #file_exists = exists(name_salve_file) # precisa implementar, se o arquivo ja existir emitir uma msg para mudar de nome !

    app.set_EnvVar("TESTER_eDMEnterVDODiagnosis", 1)  # set VDO

    app.set_EnvVar("TESTER_eGetSWVersion", 1)  # set bt getVersion

    get_status_vdo = app.get_EnvVar("TESTER_eGetSWVersionInfo")  # get status

    if get_status_vdo:

        with open(name_salve_file, 'a') as file:

            app.set_EnvVar("TESTER_eRWELength", 16)
            for i in range(16, 2048, 16):
                app.set_EnvVar("TESTER_eRWERead", 1)
                app.set_EnvVar("TESTER_eRWERead", 0)
                time.sleep(2)

                for x in range(0, 10):
                    readEeprom = app.get_EnvVar("TESTER_eRWEData00{0}".format(00 + x))
                    # hexadecimal = hex(readEeprom)
                    listaEeprom.append(readEeprom)
                for x in range(10, 16):
                    readEeprom = app.get_EnvVar("TESTER_eRWEData0{0}".format(00 + x))
                    # hexadecimal = hex(readEeprom)
                    listaEeprom.append(readEeprom)

                    # with open('dump_eeprom_Onix.txt', 'w') as file:
                test = ''.join('{:02X}'.format(a) for a in listaEeprom)
                file.write(test)
                file.write('\n')
                print('este é o teste:', test)

                adress = adress + 0x10

                app.set_EnvVar("TESTER_eRWEAddr", adress)
                app.set_EnvVar("TESTER_eRWERead", 1)
                app.set_EnvVar("TESTER_eRWERead", 0)
                listaEeprom.clear()



    msgbox("Dump sucess","## Dump Onix ##")

def dids():
    pass
def espias():
    # set all espia (toggle_env)
    app.set_EnvVar('IND_edTurnOnAll', 1)

    status = boolbox("ABS ON ?", 'Espias', ("Yes", "No"), image="01 - hello_ell/picture/ABS.PNG")

    #pwm 100%
    app.set_EnvVar('PWM_eAllChannels', 1)

def speed():
    #tacho
    app.set_EnvVar('EnvEngSpd_', 19.5)

    # speed
    app.set_EnvVar('EnvFILvlPct_', 19.5)

