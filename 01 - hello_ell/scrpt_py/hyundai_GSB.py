from time import sleep
from easygui import *
import eel
import CANoe
path = f'D:\Simulações\Hyundai_GSB_v_1\Hyundai_GSB_CANoe8_v00.cfg'


@eel.expose
def StartCANoe_HB():
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

def Stop_Canoe():
    app.stop_Measurement()
    msgbox('Finished','### Hyundai ###')

def Hb_Speeddometer_Calibration():
    value_calibrate = (0,21,41,61,85,108,124,230,0)
    indicator = (0,22,40,61,85,108,124,230,0) 

    for i in range(len(value_calibrate)):  
        app.set_SysVar("Gauges","Speedometer",value_calibrate[i])

        if ccbox(f'Pointer this in {indicator[i]} km/h ?',' ## Test_Speedometer ##'):
            """
            return position indicator[i] and a msg'Fail', if fail
            or
            return Pass if OK all teste
            """
            
            pass
        else:
            print('error')

def Hb_Tachometer_Calibration():
    value_calibrate = (0,500,1000,5000,8000,0)
    indicator = (0,500,1000,5000,8000,0) 

    for i in range(len(value_calibrate)):  
        app.set_SysVar("Gauges","Tachometer",value_calibrate[i])

        if ccbox(f'Pointer this in {indicator[i]} RMP ?',' ## Test_Tachometer ##'):
            """
            return position indicator[i] and a msg'Fail', if fail
            or
            return Pass if OK all teste
            """
            
            pass
        else:
            print('error')

def Hb_Tamperature_Calibration():
    value_calibrate = (0,21,41,61,74,108,124,230,0)
    indicator = (0,22,40,61,85,108,124,230,0) 

    for i in range(len(value_calibrate)):  
        app.set_SysVar("Gauges","Temperature",value_calibrate[i])

        if ccbox(f'in Bargraphs {indicator[i]} Segmment ON?',' ## Test_Temperature ##'):
            """
            return position indicator[i] and a msg'Fail', if fail
            or
            return Pass if OK all teste
            """
            
            pass
        else:
            print('error')

def Hb_Tag():
    pass

def Hb_Fuse_On():
    app.set_SysVar("Other","Fuse_ON",1)

def Hb_All_Telltale():

    """
    Must be activated manually:
        FUEL,300
        SEAT_BELT
        TAIL
        OIL_PRESSURE
        AIRBAG
    
    """
    app.set_SysVar("Doors","All_Doors",1)
    app.set_SysVar("Test_Variables","All_Telltales",1)
    if ccbox('It turned The Telltale TELLTALES on ?',' ## Test_All_Telltales ##'):
            """
            return msg'Fail', if fail
            or
            return Pass if OK all teste
            """          
            app.set_SysVar("Doors","All_Doors",0)
            app.set_SysVar("Test_Variables","All_Telltales",0)
    else:
        print('error')

def Hb_Espia(status_espia,msg_status_espia:str)-> None:
    espias = ('key_Out','Turn_Right','Turn_Left','Tail_Gate','TCS_Off','TCS','TT_ABS',
    'Parking_Brake','Trunk_Open','Oil_Pressure','MDPS','Immobilizer','ISG','Low_Beam',
    'Hood_Open','High_Beam','Glow','ESC','Front_Fog','TPMS','Door_Open','Cruise','Set',
    'SeatBelt','Battery','Check_engine','Airbag')
    #app.get_all_SysVar("Telltales")  

    for i in range(len(espias)):
        app.set_SysVar(espias[i],status_espia)

        if ccbox(f'It Turned The Telltale {espias[i]} {msg_status_espia} ?',' ## Test_Telltales ##'):
            """
            return msg'Fail', if fail
            or
            return Pass if OK all teste
            """          
            pass
    else:
        print('error')

def Hb_6Mt():
    """
    test manual

    """
    value_hb_6M = (1,2,3,4,5,6,1,0)
    indicator = (1,2,3,4,5,6,"R")
    app.set_EnvVar("Env_CF_Ems_UpTarGr",0)
    app.set_EnvVar("Env_CF_Ems_DownTarGr",1)
    app.set_SysVar('Transmission','C_InhibitRMT',1)
    sleep(1)
    
    for i in range(len(value_hb_6M)):  

        if value_hb_6M <= 6: 
            app.set_EnvVar('Env_CF_Ems_DesCurGr',value_hb_6M[i])
        else:
            app.set_SysVar('Transmission','C_InhibitRMT',value_hb_6M[i])

        if ccbox(f'In display is showed the {indicator[i]} ?' ,' ## Test_Speedometer ##'):
            """
            return position indicator[i] and a msg'Fail', if fail
            or
            return Pass if OK all teste
            """
            
            
            pass
        else:
            print('error')

def Hb_6At():
    """
    test manual

    """
    value_hb_6A = (0,1,2,3,4,5,6,7,0)
    indicator = ('P','1','2','3','4','5','D','N','R')
    indicatorWord =('P','D','N','R')
    
    for i in range(len(value_hb_6A)):
        app.set_EnvVar('Env_CF_Ems_DesCurGr',value_hb_6A[i])

        if(indicator[i].isnumeric()):

            if ccbox(f'In displya is showed the {indicator[i]}?' ,' ## Test_Speedometer ##'):
                pass

            else:
                print('error')

        else:
            if ccbox(f'In displya is showed the {indicatorWord[i]} and in the Test box the output {indicatorWord[i]}_OUT+ turn on?' ,' ## Test_Automatic ##'):
                pass

            else:
                print('error')

              
    
        
        














