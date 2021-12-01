from easygui import *
import eel
import CANoe
from easygui import *
tuplaEspias = ('BCM_eLHTurnSignalSts','BCM_eBonnetSts', 'BCM_eRHatchSts', 'TT_PositionLights_sw', 'BCM_eHighBeamSts', 'BSM_eESCFailSts',
               'BCM_eIMMOCodeWarningLightSts', 'BSM_eFunctionFailSts', 'ECM_eOilLifeSts', 'TCM_eTransmFailSts',
               'BCM_eFrontFogLightSts','BCM_eParkBrakeSts', 'ECM_eOilPressureFailSts', 'ORC_eAirBagFailSts', 'TCM_eOilTemperatureSts',
               'BSM_eABSFailSts', 'ECM_eAlternatorFail','TT_SeatBelt_sw', 'ECM_eDPFSts', 'BCM_eElectricSteeringFailSts', 'ECM_eFpsActuated',
               'GAU_eWaterTempWarn', 'BCM_eRHTurnSignalSts', 'BCM_eLowFuelWarningSts', 'BCM_ePAMSystemFault', 'ECM_eGPLGasolineMode',
               'ECM_eEMSFailSts','ECM_eEMSFailSts', 'BSM_eFailSts', 'DASM_eFCWSts', 'ECM_eFuelWaterPresentSts', 'BCM_eDriverDoorSts',
               'ECM_eGPLGasolineMode','MAIN_eKeyStat', 'ECM_eGlowPlugLampSts')

tuplaNameEspia = ('High Beam','Parking', 'Abs', 'Eobd', 'Glow Plug Activation', 'Tpms', 'Esc','Front Fog Light',
                  'Auto High Bean', 'Coolant High Temperatura','Left Turn', 'Righ turn', 'Fuel Reserve',
                  'Brake System Failure','Steering Fauld','Air Bag Failure', 'LDW'
                  )

path = r'D:\Simulações\Fiat_363_v1.22\Fiat_363_CANoe_10.cfg'

@eel.expose
def startCANoe363():
    try:
        global app
        app = CANoe.CANoe()
        app.stop_Measurement()
        eel.sleep(3)
        app.open_simulation(path)
        app.stop_Measurement()
        eel.sleep(3)
        app.start_Measurement()
        eel.sleep(10)

    except:
        print("An exception occurred openCanoe")

def runKeyStart():
    # KL15 E RUN
    eel.sleep(1)
    app.set_EnvVar("MAIN_eKeyStat", 1)
    eel.sleep(1)
    app.set_EnvVar("MAIN_eKeyStat", 2)
    eel.sleep(1)
    app.set_EnvVar("MAIN_eKeyStat", 1)

def diaG():
    # vdo
    app.set_EnvVar("DIAG_MDiagOn", 1)
    eel.sleep(1)
    app.set_EnvVar("DIAG_MDiagOn", 0)
    eel.sleep(1)

def getDump(nameSalveDump):
    nameSalveDump += nameSalveDump + '.hex'
    app.set_EnvVar('DIAG_RFDFileName', nameSalveDump)
    eel.sleep(2)
    app.set_EnvVar('DIAG_RFDReadFile', 1)
    eel.sleep(2)
    app.set_EnvVar('DIAG_RFDReadFile', 0)
    eel.sleep(10)
    saveFinaled = app.get_EnvVar('DIAG_RFDStatusBar')
    msgbox(saveFinaled, 'dump')

def versCluster():
    # version cluster
    app.set_EnvVar('DIAG_eVERRead', 1)
    eel.sleep(1)
    app.set_EnvVar('DIAG_eVERRead', 0)

    versSw = app.get_EnvVar('DIAG_eVERSwVerMC')
    versFiatPn = app.get_EnvVar('DIAG_eVERFIATPartNoMC')
    dataSet1 = app.get_EnvVar('DIAG_eVERDSVerMC')
    dataSet2 = app.get_EnvVar('DIAG_eVERDSIdxMC')

def fullEspia(onORoff):
       # all led
    for tupla in tuplaEspias:
        eel.sleep(1)
        app.set_EnvVar(tupla, onORoff)
             
    #relatorio()
    print('full espias')
    eel.sleep(10)

def tellTale(arrayDeSpias):
    eel.sleep(1)
    app.set_EnvVar("MAIN_eKeyStat", 1)
    eel.sleep(1)
    app.set_EnvVar("MAIN_eKeyStat", 2)
    eel.sleep(1)

    for tupla in arrayDeSpias:
        app.set_EnvVar(tupla, 1)
        eel.sleep(1)
        #repeat = boolbox("torned on ?", 'title', ("Yes", "No"),image="GLOW_PLUG.png")

    # listaRelatorioPassOrNo.append('Pass') #  add em sequência no array


def Tacho():
    app.set_EnvVar("MAIN_eKeyStat", 2)

    app.set_EnvVar("GAU_eEngSpd", 0)
    status = boolbox("RPM 0 ?", 'Tacho', ("Yes", "No"),    image="01 - hello_ell/picture/Tacho_Tolerance.PNG")
    app.set_EnvVar("GAU_eEngSpd", 1000)
    status = boolbox("RPM 1000 ?", 'Tacho', ("Yes", "No"), image="01 - hello_ell/picture/Tacho_Tolerance.PNG")
    app.set_EnvVar("GAU_eEngSpd", 4000)
    status = boolbox("RPM 4000 ?", 'Tacho', ("Yes", "No"), image="01 - hello_ell/picture/Tacho_Tolerance.PNG")
    app.set_EnvVar("GAU_eEngSpd", 8000)
    status = boolbox("RPM 8000 ?", 'Tacho', ("Yes", "No"), image="01 - hello_ell/picture/Tacho_Tolerance.PNG")
    app.set_EnvVar("GAU_eEngSpd", 0)
    #if status:
        #listaRelatorioPassOrNo.append('Pass') #  add em sequência no array


def Vel():
    app.set_EnvVar("MAIN_eKeyStat", 2)

    app.set_EnvVar("GAU_eVehSpd", 0) 
    status = boolbox("Velocidade 0 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 20) 
    status = boolbox("Velocidade 20 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 40) 
    status = boolbox("Velocidade 40 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 60) 
    status = boolbox("Velocidade 60 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 80) 
    status = boolbox("Velocidade 80 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 100) 
    status = boolbox("Velocidade 100 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 120) 
    status = boolbox("Velocidade 120 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG")
    app.set_EnvVar("GAU_eVehSpd", 220) 
    status = boolbox("Velocidade 220 ?", 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG",cancel_choice=[True])
    app.set_EnvVar("GAU_eVehSpd", 0)