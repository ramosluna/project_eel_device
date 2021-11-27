import eel
from easygui import *
from onix import *
from dump import *
from fiat_363 import *

eel.init("../web/html")

@eel.expose
def openProject(project, nameSaveDump=None):
    print('open project')
    if project == '1':  # X6H/363/X6S
        #startCANoe() #fiat
        #runKeyStart()
        #diaG()
        openPage()
        #getDump(nameSaveDump)
        dumpFiat363()

    elif project == '2':  # ONIX
        print("call onix")
        openPage()
        #startCANoe()
        send_file_dump_analise(nameSaveDump)

    elif project == '3':  # BR2
        print('BR2 not implemented')

    elif project == '4':  # GSB
        print('GSB not implemented')

    else:
        msgbox('Select the Project', 'Project')


eel.start("main.html",
          mode='chrome',
          host='localhost',
          block=True,
          position=(300, 137),
          size=(500, 200))