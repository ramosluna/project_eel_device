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

# class CaNNoe:

#if sys.argv[-1] != ASADMIN:
    #script = os.path.abspath(sys.argv[0])
    #params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    #shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    #sys.exit(0)

# openVers = os.system("C:\Program Files (x86)\CANoe 7.0\Exec32\RegCANwComponents.exe") #CANoe7
#openVers = os.system("C:\Program Files\Vector CANoe 10.0\Exec64\RegisterComponents.exe") #CANoe 10
# os.system(r'"C:\Program Files (x86)\CANoe 7.0\Exec32\RegCANwComponents.exe"')
# if (openVers == True):
# def Onix(self):

app = CANoe.CANoe()
app.open_simulation(r"D:\Simulações\Fiat_363_v1.9\Fiat_363_CANoe_9.cfg")
app.start_Measurement()
# app.set_SysVar("Control Panel","EnvSysPwrMd_",3)
app.set_EnvVar("MAIN_eKeyStat", 1)
time.sleep(0.1)
app.set_EnvVar("MAIN_eKeyStat", 2)
time.sleep(0.4)

#app.set_SysVar("DIAG MAIN", "DIAG_MDiagOn", 1)
qualovalor = app.set_EnvVar("DIAG_MDiagOn", 1)
time.sleep(0.2)
print("qual é o valor ", qualovalor)

time.sleep(0.2)
app.set_EnvVar("DIAG_eVERRead", 1)

dd = app.get_EnvVar("DIAG_MStatusBar")
print("o valor retornado é ", dd)

# pega a informacao do inf
tempSWversion = app.get_EnvVar("DIAG_eVERSwVerMC")
tempPNCustomer = app.get_EnvVar("DIAG_eVERFIATPartNoMC")
tempDataset1 = app.get_EnvVar("DIAG_eVERDSVerMC")
tempDataset2 = app.get_EnvVar("DIAG_eVERDSIdxMC")

print("SW:{0} PN:{1} DS1:{2} DS2:{3}".format(tempSWversion, tempPNCustomer, tempDataset1, tempDataset2))

# time.sleep(0.4)
# app.set_EnvVar("BSM_eESCFailSts", 1)
#
# time.sleep(0.2)
# app.set_EnvVar("DIAG_eVERRead", 1)



