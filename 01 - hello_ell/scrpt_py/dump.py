import glob
import os
import eel
from easygui import *


@eel.expose
def dumpHtml():
    nameSalveDump = fileopenbox(msg="Select .hex file", default="./hex/*.*", filetypes=["*.hex", "*.bsk", "*.txt"])
    eel.expose()
    eel.js_setPathDump(nameSalveDump)

    if not nameSalveDump:
        msgbox('Select the File', 'Dump')
        raise RuntimeError("No world file selected.")

    # https://python.hotexamples.com/pt/examples/easygui/-/fileopenbox/python-fileopenbox-function-examples.html
    # repeat = boolbox("Again?", 'title', ("Yes", "No"),image="GLOW_PLUG.png")
    # msgbox("Format complete!", ok_button="Close", image="GLOW_PLUG.png")

    with open(nameSalveDump, 'r') as f:
        lines = f.readlines()

        if nameSalveDump[-3:] == 'hex':
            # tamanho formatado
            sFORMATADO_DADOS = slice(0, -1)

            # pega o comprimento
            sizeLinesRead = len(lines[sFORMATADO_DADOS])
            lines = lines[sFORMATADO_DADOS]

            for cont in range(sizeLinesRead):
                dadosLines = lines[cont]

                address = dadosLines[3:7]

                if address[0:3] == '000':
                    address = address[3:4]

                elif address[0:2] == '00':
                    address = address[2:4]

                elif address[0:1] == '0':
                    address = address[1:4]

                # transforma hex para int
                an_integer = int(address, 16)
                address = an_integer

                # formata os dados 32 byte
                dadosHex = dadosLines[9:-3]

                # print("endereço:{0} e dados:{1}".format(dadosHex,address))
                # Call Javascript function, and pass explicit callback function
                eel.expose()
                eel.js_imprimirHex(address, dadosHex)

        # if TXT
        elif nameSalveDump[-3:] == 'txt':
            address = 0
            # tamanho formatado
            sFORMATADO_DADOS = slice(0, -1)

            # pega o comprimento
            sizeLinesRead = len(lines[sFORMATADO_DADOS])
            lines = lines[sFORMATADO_DADOS]

            for cont in range(sizeLinesRead):
                # formata os dados 32 byte
                dadosHex = lines[cont]

                # Call Javascript function, and pass explicit callback function
                eel.js_imprimirHex(address, dadosHex)

                address += 16


@eel.expose
def dataSet():
    # Dump
    print('call dumHtml')
    nameSalveDump = fileopenbox(msg="Select .hex file", default="./hex/*.*", filetypes=["*.hex", "*.bsk", "*.txt"])
    eel.expose()
    eel.js_setPathDataSet(nameSalveDump)

    if not nameSalveDump:
        msgbox('No world file selected.', 'Dump')
        raise RuntimeError("No world file selected.")

    with open(nameSalveDump, 'r') as f:
        lines = f.readlines()

        if nameSalveDump[-3:] == 'hex':
            # tamanho formatado
            sFORMATADO_DADOS = slice(0, -1)

            # pega o comprimento
            sizeLinesRead = len(lines[sFORMATADO_DADOS])
            lines = lines[sFORMATADO_DADOS]

            for cont in range(sizeLinesRead):
                dadosLines = lines[cont]

                address = dadosLines[3:7]

                if address[0:3] == '000':
                    address = address[3:4]

                elif address[0:2] == '00':
                    address = address[2:4]

                elif address[0:1] == '0':
                    address = address[1:4]

                # transforma hex para int
                an_integer = int(address, 16)
                address = an_integer

                # formata os dados 32 byte
                dadosHex = dadosLines[9:-3]

                # print("endereço:{0} e dados:{1}".format(dadosHex,address))
                # Call Javascript function, and pass explicit callback function
                eel.expose()
                eel.js_imprimirHexSeForDiferente(address, dadosHex)

        # if TXT
        elif nameSalveDump[-3:] == 'txt':
            address = 0
            # tamanho formatado
            sFORMATADO_DADOS = slice(0, -1)

            # pega o comprimento
            sizeLinesRead = len(lines[sFORMATADO_DADOS])
            lines = lines[sFORMATADO_DADOS]

            for cont in range(sizeLinesRead):
                # formata os dados 32 byte
                dadosHex = lines[cont]

                # Call Javascript function, and pass explicit callback function
                eel.expose()
                eel.js_imprimirHexSeForDiferente(address, dadosHex)

                address += 16
            # eel.expose()
            # eel.js_imprimirHexSeForDiferente(address, dadosHex)


def dumpFiatX6H():
    folder_path = r'D:\Simulações\Fiat_363_v1.22'
    file_type = '\*hex'  # se nao quiser filtrar por extenção deixe apenas *
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)

    # nameSalveDump = folder_path + '\\' + nameSalveDump
    nameSalveDump = folder_path + '\\' + max_file
    eel.expose()
    eel.js_setPathDump(nameSalveDump)

    with open(max_file, 'r') as f:
        # le todo os dados
        lines = f.readlines()

        # tamanho formatado
        sFORMATADO_DADOS = slice(0, -1)

        # pega o comprimento
        sizeLinesRead = len(lines[sFORMATADO_DADOS])
        lines = lines[sFORMATADO_DADOS]

        for cont in range(sizeLinesRead):
            dadosLines = lines[cont]

            address = dadosLines[3:7]

            if address[0:3] == '000':
                address = address[3:4]

            elif address[0:2] == '00':
                address = address[2:4]

            elif address[0:1] == '0':
                address = address[1:4]

            # transforma hex para int
            an_integer = int(address, 16)
            address = an_integer

            # formata os dados 32 byte
            dadosHex = dadosLines[9:-3]

            # print("endereço:{0} e dados:{1}".format(dadosHex,address))
            # Call Javascript function, and pass explicit callback function
            eel.expose()
            eel.js_imprimirHex(address, dadosHex)


def send_file_dump_analise(nameSaveDump):
    address = 0
    name_salve_file = nameSaveDump + '.txt'

    with open('../hex/' + name_salve_file, 'r') as f:
        # le todo os dados
        lines = f.readlines()

        # tamanho formatado
        sFORMATADO_DADOS = slice(0, -1)

        # pega o comprimento
        sizeLinesRead = len(lines[sFORMATADO_DADOS])
        lines = lines[sFORMATADO_DADOS]

        for cont in range(sizeLinesRead):
            # formata os dados 32 byte
            dadosHex = lines[cont]

            # Call Javascript function, and pass explicit callback function
            eel.js_imprimirHex(address, dadosHex)
            # eel.sleep(1)

            address += 16


def openPage():
    eel.init("../web/html")
    eel.show('dump.html')
    eel.sleep(2)
