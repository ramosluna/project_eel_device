from easygui import *
from win32com.server.util import ListEnumeratorGateway
status=[]
velo = ("Velocidade 0 ?","Velocidade 20 ?","Velocidade 40 ?","Velocidade 60 ?","Velocidade 80 ?",
"Velocidade 100 ?","Velocidade 120 ?","Velocidade 220 ?","Velocidade 0 ?")
setValueVarVel = (0,20,40,60,80,100,120,220,0)

for value in range(len(velo)) :     
        status.append(boolbox(velo[value], 'Tacho', ("Yes", "No"),image="01 - hello_ell/picture/SPEEDOMETER_2.PNG") )
     
print(status) 