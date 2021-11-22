# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:56:20 2021

app = CANoe.CANoe() #定义CANoe为app

app.open_simulation("test.cfg") #导入某个CANoe congif

app.start_Measurement() #启动CANoe

var_from_namespace = app.get_all_SysVar("mfl") #获取namespace下的所有系统变量

print(app.get_SysVar("mfl","vol_plus")) #获取系统变量的值

app.set_SysVar("mfl","vol_plus",1) #写入系统变量的值

app.stop_Measurement() #停止CANoe

@author: uidg4579
"""

import CANoe
import time

# import win32com.Shell.shell as shell

# class CaNNoe:

# if sys.argv[-1] != ASADMIN:
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
#     shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
#     sys.exit(0)

# openVers = os.system("D:\Exec32\RegCANwComponents.exe") #CANoe7
# openVers = os.system("C:\Program Files\Vector CANoe 10.0\Exec64\RegisterComponents.exe") #CANoe 10
# os.system(r'"C:\Program Files (x86)\CANoe 7.0\Exec32\RegCANwComponents.exe"')
# if (openVers == True):
# def Onix(self):

path = r"D:\Simulações\ONIX_SW\Simulacao\GMOnix_Simulation_Conti_SVDO_BRIP_04\GlobalA-IPC_V7_0.cfg"
app = CANoe.CANoe()
app.open_simulation(path)
app.stop_Measurement()
app.start_Measurement()
time.sleep(10)

adress = 0x0

app.set_EnvVar("TESTER_eDMEnterVDODiagnosis", 1)  # set VDO

app.set_EnvVar("TESTER_eGetSWVersion", 1)  # set bt getVersion

result = app.get_EnvVar("TESTER_eGetSWVersionInfo")  # get status

listaEeprom = []

s = 00
if result:
    with open('../hex/dump_eeprom_Onix.txt', 'a') as file:

        app.set_EnvVar("TESTER_eRWELength", 16)
        for i in range(16, 2048, 16):
            app.set_EnvVar("TESTER_eRWERead", 1)
            app.set_EnvVar("TESTER_eRWERead", 0)
            time.sleep(2)

            for x in range(0, 10):
                readEeprom = app.get_EnvVar("TESTER_eRWEData00{0}".format(s + x))
                # hexadecimal = hex(readEeprom)
                listaEeprom.append(readEeprom)
            for x in range(10, 16):
                readEeprom = app.get_EnvVar("TESTER_eRWEData0{0}".format(s + x))
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

print(listaEeprom)
