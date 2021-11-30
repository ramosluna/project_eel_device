from easygui import *
import eel
import CANoe
from easygui import *
 
tuplaEspias = ('BCM_eBonnetSts', 'BCM_eRHatchSts', 'TT_PositionLights_sw', 'BCM_eHighBeamSts', 'BSM_eESCFailSts',
               'BCM_eIMMOCodeWarningLightSts', 'BSM_eFunctionFailSts', 'ECM_eOilLifeSts', 'TCM_eTransmFailSts',
               'BCM_eFrontFogLightSts','BCM_eParkBrakeSts', 'ECM_eOilPressureFailSts', 'ORC_eAirBagFailSts', 'TCM_eOilTemperatureSts',
               'BSM_eABSFailSts', 'ECM_eAlternatorFail','TT_SeatBelt_sw', 'ECM_eDPFSts', 'BCM_eElectricSteeringFailSts', 'ECM_eFpsActuated',
               'GAU_eWaterTempWarn', 'BCM_eRHTurnSignalSts','BCM_eLHTurnSignalSts', 'BCM_eLowFuelWarningSts', 'BCM_ePAMSystemFault', 'ECM_eGPLGasolineMode',
               'ECM_eEMSFailSts','ECM_eEMSFailSts', 'BSM_eFailSts', 'DASM_eFCWSts', 'ECM_eFuelWaterPresentSts', 'BCM_eDriverDoorSts',
               'ECM_eGPLGasolineMode','MAIN_eKeyStat', 'ECM_eGlowPlugLampSts',)

tuplaNameEspia = ('High Beam','Parking', 'Abs', 'Eobd', 'Glow Plug Activation', 'Tpms', 'Esc','Front Fog Light',
                  'Auto High Bean', 'Coolant High Temperatura','Left Turn', 'Righ turn', 'Fuel Reserve',
                  'Brake System Failure','Steering Fauld','Air Bag Failure', 'LDW'
                  )

path = r'D:\Simulações\Fiat_363_v1.22\Fiat_363_CANoe_10.cfg'

@eel.expose
def startCANoeX6H():
    try:
        global app
        app = CANoe.CANoe()
        app.open_simulation(path)
        app.stop_Measurement()
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

def allTellTale(arrayDeSpias, onORoff=0):
    # all led
    for tupla in arrayDeSpias:
        app.set_EnvVar(tupla, onORoff)
        eel.sleep(1)
        print(tupla)
    eel.sleep(2)
    #relatorio()

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
