import io
import os
import pickle

archLoEst: io.BufferedRandom
archFiscEst = os.getcwd() + "/test_estudiantes.dat" #ruta

if not os.path.exists(archFiscEst):
    archLoEst = open(archFiscEst, "w+b")  # genera el archivo binario si no existe
else:
    archLoEst = open(archFiscEst, "r+b")  # lee y escribe el archivo binario


class Estudiante:
    def __init__(self):
        self.id_estudiante = 0  # estudiante: entero
        self.email = ""  # email: string
        self.nombre = ""
        self.estado = False
        
def pr_formatear_est(reg_est: Estudiante):  # hay que formatear cada items de estudainte
    reg_est.id_estudiante = str(reg_est.id_estudiante).ljust(10, " ")
    reg_est.email = str(reg_est.email).ljust(32, " ")
    reg_est.nombre = str(reg_est.nombre).ljust(32," ")
    
def crear_estudiante():
    est_datos = [
        ["0", "estudiante0@ayed.com", "Ana García"],
        ["1", "estudiante1@ayed.com", "Luis Fernández"],
        ["2", "estudiante2@ayed.com", "Carla Martínez"],
        ["3", "estudiante3@ayed.com", "Pedro López"]
    ]

    if os.path.getsize(archFiscEst) == 0:
        for i in range(len(est_datos)):
            est = Estudiante()
            est.id_estudiante = est_datos[i][0]
            est.email = est_datos[i][1]
            est.nombre = est_datos[i][2]
            pr_formatear_est(est)
            pickle.dump(est, archLoEst)
            archLoEst.flush()


def fn_busquedaRegistroSecuencial(email,archFis,archLog):
    tamanioArchivo= os.path.getsize(archFis)
    archLog.seek(0,0) #posicionamiento del puntero al principio del *ARCHIVO LOGICO*
    while (archLog.tell() < tamanioArchivo):
        #print("Posición del puntero antes del pickle load:",archLog.tell())
        registro = pickle.load(archLog)
        #print("Posición del puntero despues del pickle load:",archLog.tell())
        #print(f"ingresamos:{email}--tenemos:{registro.email}--encontrado:{registro.email == email}")
        #print(f"ingresamos:{email}--tenemos:{registro.email.strip()}--encontrado:{registro.email.strip() == email}\n")
        #print(f"ingresamos:{email}--tenemos:{registro.nombre}--")  #ingresamos:estudiante0@ayed.com--tenemos:Pedro López                     --
        #print(f"ingresamos:{email}--tenemos:{registro.nombre.strip()}--\n") #ingresamos:estudiante0@ayed.com--tenemos:Pedro López--
        
def fn_busquedaRegistroEstudiante(email):
    return fn_busquedaRegistroSecuencial(email,archFiscEst,archLoEst)

crear_estudiante()
estudiante = fn_busquedaRegistroEstudiante("estudiante0@ayed.com")
print(estudiante)