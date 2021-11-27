import cv2 
import os


directorio = "datos"
directorio_destino = "datos_tratados"
try:
    os.mkdir("datos_tratados")
except:
    pass
i = 485033
for filename in os.listdir(directorio):
    if "jpeg" in filename:
        print(filename)

        nombre_destino = directorio_destino+"/"+"img"+str(i)+".jpg"
        fichero_inicial = filename[:-5]
        fichero_inicial = fichero_inicial+".txt"
        fichero_final = "img"+str(i)+".txt"
        fichero_final = directorio_destino+"/"+fichero_final
        
        imagen = cv2.imread(directorio+"/"+filename,cv2.IMREAD_COLOR)
        os.rename(directorio+"/"+fichero_inicial,fichero_final)
        cv2.imwrite(nombre_destino,imagen)
        i = i+1
    
