import CANoe 
import eel
tuplaEspias = ('BCM_eLHTurnSignalSts','BCM_eBonnetSts', 'BCM_eRHatchSts', 'TT_PositionLights_sw', 'BCM_eHighBeamSts', 'BSM_eESCFailSts',
               'BCM_eIMMOCodeWarningLightSts', 'BSM_eFunctionFailSts', 'ECM_eOilLifeSts', 'TCM_eTransmFailSts',
               'BCM_eFrontFogLightSts','BCM_eParkBrakeSts', 'ECM_eOilPressureFailSts', 'ORC_eAirBagFailSts', 'TCM_eOilTemperatureSts',
               'BSM_eABSFailSts', 'ECM_eAlternatorFail','TT_SeatBelt_sw', 'ECM_eDPFSts', 'BCM_eElectricSteeringFailSts', 'ECM_eFpsActuated',
               'GAU_eWaterTempWarn', 'BCM_eRHTurnSignalSts', 'BCM_eLowFuelWarningSts', 'BCM_ePAMSystemFault', 'ECM_eGPLGasolineMode',
               'ECM_eEMSFailSts','ECM_eEMSFailSts', 'BSM_eFailSts', 'DASM_eFCWSts', 'ECM_eFuelWaterPresentSts', 'BCM_eDriverDoorSts',
               'ECM_eGPLGasolineMode','MAIN_eKeyStat', 'ECM_eGlowPlugLampSts')

app = CANoe.CANoe()
 

def fullEspia(onORoff=1):
       # all led
    for tupla in tuplaEspias:
        eel.sleep(1)
        app.set_EnvVar(tupla, onORoff)
       
  
fullEspia()   