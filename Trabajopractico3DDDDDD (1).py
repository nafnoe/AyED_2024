import pickle
import os
import io
from getpass import getpass
import random
from datetime import datetime
from datetime import timedelta
from math import factorial


archLoAdmin:io.BufferedRandom
archLoMode:io.BufferedRandom
archLoEst:io.BufferedRandom
archLoLike:io.BufferedRandom
archLoRepo:io.BufferedRandom

archFiscEst= os.getcwd()+"/estudiantes.dat"
if not os.path.exists(archFiscEst):
    archLoEst= open(archFiscEst, "w+b")     # genera el archivo binario si no existe
else:
    archLoEst= open(archFiscEst, "r+b")     # lee y escribe el archivo binario

archFiscMode= os.getcwd()+"/moderadores.dat"
if not os.path.exists(archFiscMode):
    archLoMode= open(archFiscMode, "w+b") # genera el archivo binario si no existe
else:
    archLoMode= open(archFiscEst, "r+b")    # lee y escribe el archivo binario

    
archFiscAdmin= os.getcwd()+"/administrador.dat"
if not os.path.exists(archFiscAdmin):
    archLoAdmin= open(archFiscAdmin, "w+b") # genera el archivo binario si no existe
else:
    archLoAdmin= open(archFiscAdmin, "r+b") # lee y escribe el archivo binario

archFiscLike= os.getcwd()+"/like.dat"
if not os.path.exists(archFiscLike):
    archLoLike= open(archFiscLike, "w+b") # genera el archivo binario si no existe
else:
    archLoLike= open(archFiscLike, "r+b") # lee y escribe el archivo binario

archFiscRepo= os.getcwd()+"/reportes.dat"
if not os.path.exists(archFiscRepo):
    archLoRepo= open(archFiscRepo, "w+b") # genera el archivo binario si no existe
else:
    archLoRepo= open(archFiscRepo, "r+b") # lee y escribe el archivo binario


class Estudiante:
    def __init__(self):
        self.id_estudiante= 0                  # estudiante: entero
        self.email= ""                         # email: string
        self.nombreyapellido = ""              # nombre: string
        self.sexo= ""                          # sexo: chart
        self.contrasena= ""                    # contrasena: string
        self.estado = True                     # estado: Booleano
        self.hobbies= ""                       # hobbies: string
        self.materia_favorita = ""             # materia_favorita: string
        self.deporte_favorito = ""             # deporte_favorito: string
        self.materia_fuerte = ""               # materia_fuerte: string
        self.materia_debil = ""                # materia_debil: string
        self.biografia = ""                    # biografia:  string
        self.pais = ""                         # pasis: string
        self.ciudad = ""                       # ciudad: string
        self.fecha_nacimiento = ""             # fecha_naciemiento: string
        
class Moderador:
    def __init__(self):       
        self.id_moderador= 0                  # estudiante: entero
        self.email= ""                        # email:  string                   
        self.contrasena= ""                   # contrasena: string
        self.estado = True                    # estado: Booleano
        
class Administrador:
    def __init__(self):       
        self.id_administrador= 0             # estudiante: entero
        self.email= ""                       # email: string                   
        self.contrasena= ""                  # contrasena: string
        self.estado = True
class Like:
    def __init__(self):       
        self.remitente= 0                   # remitente: entero
        self.destinatario= 0                # destinatario: entero                  
      
class Reporte:
    def __init__(self):       
        self.id_reportante= 0              # id_reportante: entero
        self.id_reportado= 0               # id_reortado: entero                   
        self.razon_reporte= ""             #razon_reporte: string
        self.estado= 0                     #estado: entero 




#-------------------------------------------------------------------------------------------------------------------------
def fn_generar_edad(fecha:str):
    hoy = datetime.now()
    res = datetime.strptime(fecha, "%Y-%m-%d")
    edad = ((hoy - res).days)/ 365
    return int(edad)

def cant_registro(archLo, archFisc):  
    cantidad=0
    if os.path.getsize(archFisc)!=0:
        archLo.seek(0,0)
        pickle.load(archLo)
        long_reg = archLo.tell()
        tam_arch = os.path.getsize(archFisc)
        cantidad = tam_arch // long_reg
    return cantidad   


def pr_formatear_est(reg_est:Estudiante):# hay que formatear cada items de estudainte
    reg_est.id_estudiante = str(reg_est.id_estudiante).ljust(10," ")
    reg_est.email = str(reg_est.email).ljust(32," ")
    reg_est.nombreyapellido= str(reg_est.nombreyapellido).ljust(32," ")
    reg_est.contrasena = str(reg_est.contrasena).ljust(32," ")
    reg_est.estado = str(reg_est.estado).ljust (10," ")
    reg_est.hobbies= str(reg_est.hobbies).ljust(255, " ")
    reg_est.materia_favorita = str(reg_est.materia_favorita).ljust(16, " ")
    reg_est.deporte_favorito = str(reg_est.deporte_favorito).ljust(16," ")
    reg_est.materia_fuerte= str(reg_est.materia_fuerte).ljust(16," ")
    reg_est.materia_debil = str(reg_est.materia_debil).ljust(16," ")
    reg_est.biografia = str(reg_est.biografia).ljust(255," ")
    reg_est.pais= str(reg_est.pais).ljust(32," ")
    reg_est.ciudad= str(reg_est.ciudad).ljust(255," ")
    reg_est.fecha_nacimiento = str(reg_est.fecha_nacimiento).ljust(10," ")

def pr_formatear_mode(reg_mode:Moderador): 
    reg_mode.id_moderador=str(reg_mode.id_moderador).ljust(10," ")
    reg_mode.email = str(reg_mode.email).ljust(32," ")
    reg_mode.contrasena = str(reg_mode.contrasena).ljust(32," ")
    reg_mode.estado = str(reg_mode.estado).ljust (10," ")

def pr_formatear_admin(reg_admi:Administrador):
    reg_admi.id_administrador=str(reg_admi.id_administrador).ljust(10," ")
    reg_admi.email = str(reg_admi.email).ljust(32," ")
    reg_admi.contrasena = str(reg_admi.contrasena).ljust(32," ")
    reg_admi.estado = str(reg_admi.estado).ljust (10," ")

def pr_formater_like(reg_like:Like):
    reg_like.remitente = str(reg_like.remitente).ljust(10," ")
    reg_like.destinatario = str(reg_like.destinatario).ljust(10," ")

def pr_formatear_reporte(reg_repo:Reporte):
    reg_repo.id_reportante = str(reg_repo.id_reportante).ljust(10," ")
    reg_repo.id_reportado = str(reg_repo.id_reportado).ljust(10," ")
    reg_repo.razon_reporte = str(reg_repo.razon_reporte).ljust(255," ")
    reg_repo.estado = str(reg_repo.estado).ljust (10," ")


#TODO
def pr_carga_random_likes():
    for i in range(0,archLoLike):
        for k in range(0,estudiantes_cargados):
            matrizLike[i][k] = random.randint(0, 1)

# Función para verificar si existen likes cargados
def verificar_likes_existentes():
    return os.path.exists(archFiscEst) and os.path.getsize(archFiscEst) > 0

# Función para generar likes aleatorios
def generar_likes_aleatorios():
    #Supongamos que tenemos algunos usuarios creados
    #
    likes = [] 
    # Asignar likes aleatorios entre los usuarios
    for i in cant_registro():
        num_likes = random.randint(0, cant_registro())  
        usuarios_que_dieron_like = random.sample([u for u in usuarios if u != usuario], num_likes)
        for like in usuarios_que_dieron_like:
            likes.append(f"{usuario} recibió un like de {like}\n")
    
    # Guardar los likes en el archivo
    with open("likes.txt", "w") as archivo_likes:
        ""
# Procedimiento de inicialización

def inicializar_likes():
    if not verificar_likes_existentes():
        generar_likes_aleatorios()
        print("Likes generados aleatoriamente.")
    else:
        print("Ya existen likes cargados. No es necesario inicializar.")



    
def crear_administrador():
    admi_datos = ["0","administrador@ayed.com","888111"]
    if os.path.getsize(archFiscAdmin) == 0:
        admi = Administrador()
        admi.id_administrador = admi_datos[0]
        admi.email = admi_datos[1]
        admi.contrasena = admi_datos [2]
        pr_formatear_admin(admi)
        pickle.dump(admi,archLoAdmin)
        archLoAdmin.flush()
  


def crear_moderador():
    mode_datos = ["0","moderador@ayed.com","999111","True"]

    if os.path.getsize(archFiscMode) == 0:
        mode = Moderador()
        mode.id_moderador= mode_datos[0]
        mode.email= mode_datos[1]
        mode.contrasena= mode_datos[2]
        mode.estado= mode_datos[3]
        pr_formatear_mode(mode)
        pickle.dump(mode,archLoMode)
        archLoMode.flush()
        

def crear_estudiante():
    est_datos = [["0", "estudiante0@ayed.com", "Ana García", "F", "111222", "True", "escribir", "matemáticas", "fútbol", "historia", "tecnología", "en un futuro cercano...", "España", "Madrid", "22-03-1998"],
    ["1", "estudiante1@ayed.com", "Luis Fernández", "M", "333444", "True", "leer", "ciencia", "tenis", "química", "literatura", "misterios del universo", "España", "Barcelona", "15-07-1996"],
    ["2", "estudiante2@ayed.com", "Carla Martínez", "F", "555666", "True", "dibujar", "biología", "voleibol", "matemáticas", "arte", "días soleados...", "México", "Ciudad de México", "03-11-1995"],
    ["3", "estudiante3@ayed.com", "Pedro López", "M", "777888", "True", "cantar", "física", "baloncesto", "literatura", "música", "historias fantásticas...", "Colombia", "Bogotá", "29-08-1997"]]
   
    if os.path.getsize(archFiscEst) == 0:
    
     for i in range (4):
        est = Estudiante()
        est.id_estudiante = est_datos[i][0]          
        est.email = est_datos[i][1]             
        est.nombreyapellido =  est_datos[i][2]                
        est.sexo = est_datos[i][3]                
        est.contrasena = est_datos[i][4]           
        est.estado = est_datos[i][5]              
        est.hobbies = est_datos[i][6]                 
        est.materia_favorita = est_datos[i][7]     
        est.deporte_favorito = est_datos[i][8]       
        est.materia_fuerte = est_datos[i][9]           
        est.materia_debil = est_datos[i][10]           
        est.biografia = est_datos[i][11]          
        est.pais = est_datos[i][12]            
        est.ciudad = est_datos[i][13]                
        est.fecha_nacimiento = est_datos[i][14]
        pr_formatear_est(est)
        pickle.dump(est,archLoEst)
        archLoEst.flush()
      


def fn_BusquedaSec(email,archFis,archLog):
   Tam= os.path.getsize(archFis)
   pos=0
   archLog.seek(0,0)
   Reg= pickle.load(archLog)
   while (archLog.tell() < Tam) and (Reg.email!= email):
       # pos= archLog.tell()
       Reg= pickle.load(archLog)
       if (Reg.email == email):
           return Reg
       else:
           return -1

def buscaSecuen(email,archFis,archLo):
	t = os.path.getsize(archFis)
	if t > 0:
		pos = 0
		archLo.seek(pos, 0) 
		Reg = pickle.load(archLo)

		while (archLo.tell()<t) and (Reg.email != email):
			print(Reg.email)
			pos = archLo.tell()
			Reg = pickle.load(archLo)
		if Reg.email == email:		
			return pos
		else:
			return -1
	else:
		return -1


           

def fn_busquedaSecEst(email):
    return fn_BusquedaSec(email,archFiscEst,archLoEst)

def fn_busquedaSecMod(email):
    return fn_BusquedaSec(email,archFiscMode,archLoMode)

def fn_busquedaSecAdm(email):
    return fn_BusquedaSec(email,archFiscAdmin,archLoAdmin)

# def fn_consulta_registro():    #CONSULTA DE UN REGISTRO
#     email = input("ingrese email: ")
#     Posi= fn_BusquedaSec(email)
#     if Posi != -1: 
#         archLoEst.seek(Posi,0)
#         regEst = pickle.load(archLoEst)
#         print(regEst,email)
#     else: 
#         print("El email ingresado no existe")
    
def pr_menu_mod():
    print

def fn_editar_datos_personales():
      def RenovarConsola():
        menu_reutilizable = "\n\n1-Hobbie\n\n5-Biografía\n6- Ver modificaciones\n\n0-Volver\n"
        pr_limpiar_consola()
        pr_crear_titulo("Configuración de perfil")
        print("")
        print(menu_reutilizable)
        print("\n¿Que desea modificar? \n")


def fn_gestionar_mi_perfil():
    menu_reutilizable = (
        "\na-Editar mis datos personales\n\nb-Eliminar mi perfil\n\nc-Volver\n"
    )
    pr_limpiar_consola()
    pr_crear_titulo("GESTIONAR MI PERFIL")
    print(menu_reutilizable)
    opcion = fn_validar_letras()
    while opcion != "c" and opcion != "-1":
        match (opcion):
            case "a":
                fn_editar_datos_personales()
            case "b":
                opcion = fn_eliminar_mi_perfil()
        if opcion == "-1":
            return opcion
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR MI PERFIL")
        print(menu_reutilizable)
        opcion = fn_validar_letras()    



def pr_menu_est():
    menu_reutilizable = """\n1-Gestionar mi perfil\n2-Gestionar Candidatos\n3-Matcheos\n4-Reportes Estadsticos\n0-Salir\n"""
    pr_limpiar_consola()
    pr_crear_titulo("MENU PRINCIPAL")
    print(menu_reutilizable)
    # VALIDA EL RANGO DE NUMERO [0-5]
    opcion = fn_validar_rango_de_numero(0, 4)
    while opcion != 0 and opcion != "-1":
        match (opcion):
            case 1:
                if fn_gestionar_mi_perfil() == "-1":
                    opcion = "-1"
            case 2:
                 gestionar_candidatos()
            case 3:
                 construccion()
            case 4:
                 reporte_estadisticos()         
        if opcion != "-1":
            pr_limpiar_consola()
            pr_crear_titulo("MENU PRINCIPAL")
            print(menu_reutilizable)
            opcion = fn_validar_rango_de_numero(0, 4)
        
def pr_menu_adm():
    print


def pr_registrarse():
    print
          
def pr_iniciarSesion():
    pr_limpiar_consola()
    pr_crear_titulo("Bienvenidos")
    # GENERAMOS LA VARIABLE INTENTO <= 3 PARA QUE NO HAYA ERROR
    intento = 0
    # LA VARIABLE AUTENTICADO SIRVE COMO BOOLEANO PARA SABER CUANDO EL USUARIO ESTA LOGEADO
    autenticado = False
    while intento < 3 and not (autenticado):
        email = input("Ingrese el email: ")
        contrasena = input("Ingrese una contraseña: ") 
        # PRIMER CASO BUSCAMOS POR USUARIO EXISTENTE
    
        pos = buscaSecuen(email,archFiscEst,archLoEst)
        RegEst = Estudiante()
        archLoEst.seek(pos,0)
        RegEst= pickle.load(archLoEst)

        if (pos != -1 and RegEst.contrasena == contrasena and RegEst.estado  == True):
            autenticado = True
            pr_menu_est()
            # e = Estudiante.estado 
            #podemos mostrar directamente el menu de estudiante

        # SEGUNDO CASO BUSCAMOS POR MODERADOR EXISTENTE
        
        elif pos == buscaSecuen(email,archFiscMode,archLoMode):
            RegMode = Moderador()
            archLoMode.seek(pos,0)
            RegMode= pickle.load(archLoMode)

            if (pos != -1 and RegMode.contrasena== contrasena and RegMode.estado == True):
                autenticado = True
                pr_menu_mod()
              # m = Moderador.estado #podemos mostrar directamente el menu de moderador
        else:
            # TERCER CASO BUSCAMOS POR ADMINISTRADOR EXISTENTE
            pos = buscaSecuen(email,archFiscAdmin,archLoAdmin)
            RegAdmin = Administrador()
            archLoAdmin.seek(pos,0)
            RegAdmin= pickle.load(archLoAdmin)
            if (pos != -1 and RegAdmin.contrasena == contrasena and RegAdmin.estado == True): 
                autenticado = True
                pr_menu_adm()
                
                #a = Administrador.estado 
        
        if not (autenticado):
            print("\nEl email o la contraseña son incorrectas")
            intento = intento + 1
    if autenticado:
        if Estudiante.email == e: 
            pr_menu_est()
            
        if Moderador.email == m:
            pr_menu_mod()
            
        else:
            Administrador.email== a
            pr_menu_adm()
    else:
        print("Te has quedado sin intentos")
     
def pr_bonustracks():
    print

def pr_limpiar_consola():
    os.system("cls")


def PausarPrograma():
    os.system("pause")
    

def Mostrar(string):
    print("\n" + string + "\n")
    
 
def fn_validar_letras():
    letra = str(input("Ingrese una opción: "))
    while (letra != "a") and (letra != "b") and (letra != "c"):
        print("Error, debe elegir una letra del menú")
        letra = str(input("Ingrese una opción: "))
    return letra
      
def fn_validar_rango_de_numero(inicio: int, limite: int):
    try:
        numero = int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("Error, ingrese nuevamente el número")
            numero = int(input("Ingrese una opción: "))
        return numero
    except:
        Mostrar("Error: Solamente se permiten numeros")
        return fn_validar_rango_de_numero(inicio, limite)
    
def pr_crear_titulo(titulo: str):
    columnas = ""
    cantidadLetra: int = len(titulo)        # ES LA CANTIDAD DE LETRAS QUE TIENE EL TITULO
    columnaTamaño: int = os.get_terminal_size().columns

    for i in range(0, columnaTamaño):
        columnas = columnas + "_"

    copiarColumnas = (columnaTamaño - cantidadLetra) // 2
    print(columnas)
    print("\n" + " " * copiarColumnas + titulo)
    print(columnas)

     
 
def pr_logueo():

    pr_limpiar_consola()
    pr_crear_titulo("Login")

    #preguntar si existe estudiante administrador y moderador
    cant_est = cant_registro(archLoEst,archFiscEst)
    cant_adm = cant_registro(archLoAdmin,archFiscAdmin)
    cant_mod = cant_registro(archLoMode,archFiscMode)
    if not (cant_est == 4 and cant_adm == 1 and cant_mod == 1):
        crear_estudiante()
        crear_administrador()
        crear_moderador()
    
    Mostrar("\n1-Iniciar sesion\n\n2-Registrarse\n\n3-Bonus Tracks\n\n0-Salir")
    opc=fn_validar_rango_de_numero(0,3)
    while opc != 0:
        if opc == 1:
                pr_iniciarSesion()
        elif  opc == 2:
                pr_registrarse()
        elif opc == 3:
                pr_bonustracks()
    else:
        Mostrar("Usted esta saliendo del programa Estudiantes")
        PausarPrograma()
       
pr_logueo()
archLoEst.close()
archLoMode.close()
archLoAdmin.close()
archLoRepo.close()
archLoLike.close ()



  