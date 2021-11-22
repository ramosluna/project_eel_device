
import glob
import os.path

#folder_path = r"D:\Simulações\Fiat_363_v1.9\"
folder_path = r"D:\Simulações\Fiat_363_v1.9"
file_type = '\*hex' # se nao quiser filtrar por extenção deixe apenas *
files = glob.glob(folder_path + file_type)
max_file = max(files, key=os.path.getctime)

print(max_file)


