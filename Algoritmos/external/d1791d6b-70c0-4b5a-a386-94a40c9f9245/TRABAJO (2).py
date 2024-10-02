# TRABAJO PRACTICO N2, ALGORITMOS Y ESTRUCTURAS DE DATOS
# COMISION 113
# Rufina Sabbatini, Legajo: 53250
# Valentina Ferrari, Legajo: 53766
# Raquel Degrugiller, Legajo: 54096
# Noelia Anahi Rodas, Legajo: 54004
# Variables:

from getpass import getpass
import random
from datetime import datetime
from datetime import timedelta
from math import factorial
import os

USUARIO = "usuario"
MODERADOR = "moderador"

# CREAMOS EL ARRAY PARA ESTUDIANTE Y PARA MODERADOR
filas = 8
columnas = 8
estudiantes = [
    [
        "estudiante1@ayed.com",
        "111222",
        "0",
        "Jorge",
        "",
        "30",
        "bio",
        "hobb",
        "sexo",
        "activo",
        USUARIO,
    ],
    [
        "estudiante2@ayed.com",
        "333444",
        "1",
        "nomb2",
        "",
        "edad",
        "bio",
        "hobb",
        "sexo",
        "activo",
        USUARIO,
    ],
    [
        "estudiante3@ayed.com",
        "555666",
        "2",
        "nomb3",
        "",
        "edad",
        "bio",
        "hobb",
        "sexo",
        "activo",
        USUARIO,
    ],
    [
        "estudiante4@ayed.com",
        "777888",
        "3",
        "nomb4",
        "",
        "edad",
        "bio",
        "hobb",
        "sexo",
        "activo",
        USUARIO,
    ],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", "", "", ""],
]
moderador = [
    ["moda@ayed.com", "321", "4", "modnames", MODERADOR, "activo"],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
    ["", "", "", "", "", ""],
]

edades= [21,18,20,19,23,24]


estudiantes_cargados = 4
moderadores_cargados = 1
# creamos un array para guardar el usuario autenticado id-email-rol
usuario_logueado = ["", "", ""]
reporte = [[-1 for _ in range(columnas)] for _ in range(filas)]
arr_motivos_reporte = [["" for _ in range(columnas)] for _ in range(filas)]
# MATRIZ DE LIKES
matrizLike = [[0 for _ in range(columnas)] for _ in range(filas)]


def busqueda_sec_edad(ed):
    aux=0
    for i in range (5):
        if ed[i+1] == (ed[i])+1:
           "" 
        else: 
            aux= (ed[i])+1
    print ("El número faltante es: ",aux) 

    PausarPrograma()
            
def pr_bonustracks2(n, k):
    return int(factorial(n)/(factorial(n-k) * factorial(k)))       
            
def pr_bonustracks1(ed):
    aux=0
    for i in range (5):
        for k in range((i+1),6):
            if ed[i] > ed[k] :
                aux = ed[i]
                ed[i] = ed[k]
                ed[k] = aux   
    print("La secuencia de edades es: ",ed)            
    busqueda_sec_edad(ed)

    
def pr_bonustracks():
    pr_limpiar_consola()
    pr_crear_titulo("BONUS TRACKS")
    print("\n1-Bonus Track 1\n\n2-Bonus Tracks 2\n\n0-Salir")
    opc = int(input("\nIngresar opcion: "))
    while opc != 0:
        if opc == 1:
            pr_bonustracks1(edades)
        elif  opc == 2:
            print(f"\nEs posible formar {pr_bonustracks2(estudiantes_cargados, 2)} parejas de estudiante sin repetirse\n")
            PausarPrograma()
        pr_limpiar_consola()
        pr_crear_titulo("BONUS TRACKS")
        print("\n1-Bonus Track 1\n\n2-Bonus Tracks 2\n\n0-Salir\n")    
        opc = fn_validar_rango_de_numero(0, 3)


def pr_carga_random_matriz():
    for i in range(0,estudiantes_cargados):
        for k in range(0,estudiantes_cargados):
            matrizLike[i][k] = random.randint(0, 1)

def carga_random():
    regest=
    for i in range(0,cantReg):
        

                 



pr_carga_random_matriz()

def reporte_estadisticos():
    likes_recibidios=0
    likes_dados = 0
    match = 0
    indice_mio = int(usuario_logueado[0])
    for i in range(0,8):
        # LIKES RECIBIDOS PERO NO DADOS
        if matrizLike[i][indice_mio] == 1 and matrizLike[indice_mio][i]==0:
           likes_recibidios = likes_recibidios + 1 
        #LIKES DADOS PERO NO RECIBIDOS
        if  matrizLike[indice_mio][i] == 1 and matrizLike[i][indice_mio] ==0:
            likes_dados = likes_dados + 1
        #MATCH
        if   matrizLike[indice_mio][i] == 1 and matrizLike[i][indice_mio] ==1:
            match = match + 1
    print("-Likes dados y no recibidos =",likes_dados)
    print("-Likes recibidos y nos respondidos =",likes_recibidios)
    print(f"-Matcheados sobre el % posible =",((match*100)//estudiantes_cargados),"%")
    os.system("pause")
    
# PROCEDURES
def ValidarRangoDeNumero(inicio: int, limite: int):
    try:
        numero = int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("Error, ingrese nuevamente el número")
            numero = int(input("Ingrese una opción: "))
        return numero
    except:
        Mostrar("Error: Solamente se permiten numeros")
        return ValidarRangoDeNumero(inicio, limite)


def pr_crear_titulo(titulo: str):
    columnas = ""
    cantidadLetra: int = len(titulo)  # ES LA CANTIDAD DE LETRAS QUE TIENE EL TITULO
    columnaTamaño: int = os.get_terminal_size().columns

    for i in range(0, columnaTamaño):
        columnas = columnas + "_"

    copiarColumnas = (columnaTamaño - cantidadLetra) // 2
    print(columnas)
    print("\n" + " " * copiarColumnas + titulo)
    print(columnas)


def fn_generar_edad(fecha:str):
    hoy = datetime.now()
    res = datetime.strptime(fecha, "%Y-%m-%d")
    edad = ((hoy - res).days)/ 365
    return int(edad)

# Funcion para crear fechas devuelve una fecha
def fn_crear_fechas():
    """Devuelve una fecha ejemplo : (2004-02-03)"""
    bandera = False
    fecha_devolver = 0
    while bandera != True:
        try:
            ahora = datetime.now()
            fecha = datetime.strptime(
                input("Ingrese una fecha en el formato AAAA-MM-DD: "), "%Y-%m-%d"
            )
            fechaLimite = ahora - timedelta(days=365 * 18)
            fechaInicial = ahora - timedelta(days=365 * 100)
            if fecha >= fechaInicial and fecha <= fechaLimite:
                fecha_devolver = fecha
                bandera = True
        except:
            print("Error fecha invalida")
            os.system("pause")
            bandera = False
    return fecha_devolver.strftime("%Y-%m-%d")

def construccion():
    print("\nEn contruccion...")
    os.system("pause")

def fn_validarSi_No():
    respuesta = input("Ingrese si o no: ")
    while (respuesta != "si") and (respuesta != "no"):
        print("No es un opción valida, ingrese si o no")
        respuesta = input("Ingrese si o no: ")
    return respuesta


def fn_busqueda_secuencial(array, limite, opc, campo):
    i = 0
    while i < limite:
        if array[i][campo] == opc:
            return i
        i = i + 1
    return -1


def fn_busqueda_id_validando_mail_existe(array, limite, id):
    i = 0
    while i < limite and id < limite:
        if array[id][0] != "":
            return id
        i = i + 1
    return -1


def pr_limpiar_consola():
    os.system("cls")


def PausarPrograma():
    os.system("pause")


def Mostrar(string):
    print("\n" + string + "\n")


def pr_ver_candidatos(tipo):
    if tipo == "e":
        for i in range(0, 8):
            if estudiantes[i][0] != usuario_logueado[1]:
                fecha = estudiantes[i][4]
                if fecha == "":
                    fecha = "No se ingreso una fecha"
                else:
                    fecha = fn_generar_edad(estudiantes[i][4])
                print(
                    f"\nId:{i}\nNombre:{estudiantes[i][3]}\nFecha de Nacimiento:{estudiantes[i][4]}\nedad:{fecha}\nBiografía:{estudiantes[i][6]}\nHoobie:{estudiantes[i][7]}"
                )
    elif tipo == "m":
        for i in range(0, 8):
            fecha = estudiantes[i][4]
            if fecha == "":
                fecha = "No se ingreso una fecha"
            else:
                fecha = fn_generar_edad(estudiantes[i][4])
            print(
                f"\nId:{i}\nNombre:{estudiantes[i][3]}\nFecha de Nacimiento:{estudiantes[i][4]}\nedad:{fecha}\nBiografía:{estudiantes[i][6]}\nHoobie:{estudiantes[i][7]}\nEstado:{estudiantes[i][9]}"
            )


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


def pr_reportar_candidatos():
    pr_ver_candidatos("e")
    print("¿Desea reportar un candidato?: ")
    opcion = fn_validarSi_No()
    if opcion == "si":
        print("Ingrese el Id del candidato que desea reportar: ")

        usuario_reportado = fn_validar_rango_de_numero(0,estudiantes_cargados)
        indice = fn_busqueda_id_validando_mail_existe(estudiantes, 8, usuario_reportado)
        if indice != -1:
            if reporte[usuario_logueado[0]][indice] == 0:
                print("Existe un reporte previo, desea modificarlo?: ")
                opcion = fn_validarSi_No()
                if opcion == "si":
                    reporte[usuario_logueado[0]][indice] = 0
                    motivo = str(input("Ingrese el motivo por el cual desea reportar al usuario: "))
                    arr_motivos_reporte[usuario_logueado[0]][indice] = motivo
            else:
                reporte[usuario_logueado[0]][indice] = 0
                motivo = str(input("Ingrese el motivo por el cual desea reportar al usuario: "))
                arr_motivos_reporte[usuario_logueado[0]][indice] = motivo
    elif opcion == "no":
     return gestionar_candidatos()
     


def fn_eliminar_mi_perfil():
    print("¿Desea eliminar su perfil?: ")
    opcion = fn_validarSi_No()
    if opcion == "si":
        estudiantes[usuario_logueado[0]][9] = "inactivo"
        return "-1"


def fn_editar_datos_personales():

    def RenovarConsola():
        menu_reutilizable = "\n\n1-Nombre\n\n2-Fecha de nacimiento\n\n3-Biografía\n\n4-Hobbie\n\n5-Sexo\n\n6- Ver modificaciones\n\n0-Volver\n"
        pr_limpiar_consola()
        pr_crear_titulo("Configuración de perfil")
        print("")
        print(menu_reutilizable)
        print("\n¿Que desea modificar? \n")

    RenovarConsola()
    opcion = fn_validar_rango_de_numero(0, 6)
    i = usuario_logueado[0]
    while opcion != 0:
        match (opcion):
            case 1:
                nombre = input("Ingrese su nombre deseado: ")
                estudiantes[i][3] = nombre
            case 2:
                fecha = fn_crear_fechas()
                estudiantes[i][4] = fecha
            case 3:
                biografia = input("Ingrese su biografia: ")
                estudiantes[i][6] = biografia
            case 4:
                hoobie = input("Ingrese su hoobie: ")
                estudiantes[i][7] = hoobie
            case 5:
                sexo = input("Ingrese su sexo: ")
                estudiantes[i][8] = sexo 
            case 6:
                modiicaciones= (f"\nId:{i}\nNombre:{estudiantes[i][3]}\nFecha de Nacimiento:{estudiantes[i][4]}\nBiografía:{estudiantes[i][6]}\nHoobie:{estudiantes[i][7]}")
                print (modiicaciones)  
        opcion = fn_validar_rango_de_numero(0, 6)

def fn_verReportes():
    for x in range(filas):
        for y in range(columnas):
            estado = reporte[x][y]
            if estado == 0:
                print(
                    f"Reporte{estado}:{estudiantes[x][0]},{estudiantes[y][0]}:{arr_motivos_reporte[x][y]}"
                )
                print("Desea ignorar el reporte?: ")
                opc = fn_validarSi_No()
                if opc == "si":
                    reporte[x][y] = 2
                else:
                    print("Deseas bloquear al reportado?")
                    opc = fn_validarSi_No()
                    if opc == "si":
                        reporte[x][y] = 1
                        estudiantes[y][9] = "inactivo"


def gestionar_candidatos():
    menu_reutilizable = "\na-Ver candidatos\n\nb-Reportar un candidato\n\nc-Volver\n"
    pr_limpiar_consola()
    pr_crear_titulo("GESTIONAR MI PERFIL")
    print(menu_reutilizable)
    opcion = fn_validar_letras
    while opcion != "c":
        match (opcion):
            case "a":
                # LIKE A UN CANDIDATO
                pr_ver_candidatos("e")
                nombre = input("Ingresa el nombre de la persona con la cual te gustaria hacer match: ")
                id_candidato = fn_busqueda_secuencial(estudiantes, 8, nombre, 3)
                if id_candidato != -1:
                    mi_id = int (usuario_logueado[0])
                    matrizLike[mi_id][id_candidato] = 1
                pr_limpiar_consola()
            case "b":
                pr_reportar_candidatos()
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR MI PERFIL")
        print(menu_reutilizable)
        opcion = fn_validar_letras()


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


def fn_desactivar_perfil(id):
    print("¿Desea desactivar este perfil?: ")
    opcion = fn_validarSi_No()
    if opcion == "si":
        estudiantes[id][9] = "inactivo"
        return "-1"


def pr_desactivarUsuario():  # ingresamos el id del usuario que queremos desactivar
    pr_ver_candidatos("m")
    id = int(input("Ingrese el id del usuario: "))
    inactivo = fn_desactivar_perfil(id)
    if inactivo == -1:
        print("Este perfil ha sido desactivado")
    else:
        print("Este usuario no existe")


def fn_gestionar_usuario():
    menu_reutilizable = "\na-Desactivar Usuario\n\nb-Volver\n"
    pr_limpiar_consola()
    pr_crear_titulo("GESTIONAR USUARIO")
    print(menu_reutilizable)
    opcion = fn_validar_letras()
    while opcion != "b" and opcion != "-1":
        match (opcion):
            case "a":
                pr_desactivarUsuario()
        if opcion == "-1":
            return opcion
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR USUARIO")
        print(menu_reutilizable)
        opcion = fn_validar_letras()


def gestionar_reportes():
    menu_reutilizable = "\na-Ver Reportes\n\nb-Volver\n"
    pr_limpiar_consola()
    pr_crear_titulo("GESTIONAR REPORTES")
    print(menu_reutilizable)
    opcion = fn_validar_letras()
    while opcion != "b" and opcion != "-1":
        match (opcion):
            case "a":
                fn_verReportes()
        if opcion == "-1":
            return opcion
        pr_limpiar_consola()
        pr_crear_titulo("GESTIONAR REPORTES")
        print(menu_reutilizable)
        opcion = fn_validar_letras()

def pr_menu_mod():
    menu_reutilizable = "\n1-Gestionar Usuarios\n\n2-Gestionar Reportes\n\n3-Reportes Estadisticos\n\n0-Salir\n"
    pr_limpiar_consola()
    pr_crear_titulo("MENU PRINCIPAL")
    print(menu_reutilizable)
    # VALIDA EL RANGO DE NUMERO [0-4]
    opcion = fn_validar_rango_de_numero(0, 3)
    while opcion != 0 and opcion != "-1":
        match (opcion):
            case 1:
                if fn_gestionar_usuario() == "-1":
                    opcion = "-1"
            case 2:
                gestionar_reportes()
            case 3:
                construccion()
        if opcion != "-1":
            pr_limpiar_consola()
            pr_crear_titulo("MENU PRINCIPAL")
            print(menu_reutilizable)
            opcion = fn_validar_rango_de_numero(0, 3)


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
        indice = fn_busqueda_secuencial(estudiantes, 8, email, 0)
        if (
            indice != -1
            and estudiantes[indice][1] == contrasena
            and estudiantes[indice][9] == "activo"
        ):
            autenticado = True
            usuario_logueado[0] = indice
            usuario_logueado[1] = email
            usuario_logueado[2] = USUARIO
        else:
            # SEGUNDO CASO BUSCAMOS POR MODERADOR EXISTENTE
            indice = fn_busqueda_secuencial(moderador, 4, email, 0)
            if (
                indice != -1
                and moderador[indice][1] == contrasena
                and moderador[indice][5] == "activo"
            ):
                autenticado = True
                usuario_logueado[0] = indice
                usuario_logueado[1] = email
                usuario_logueado[2] = MODERADOR
        if not (autenticado):
            print("\nEl email o la contraseña son incorrectas")
            intento = intento + 1
    if autenticado:
        if usuario_logueado[2] == USUARIO:
            pr_menu_est()
        else:
            pr_menu_mod()
    else:
        print("Te has quedado sin intentos")


def pr_registrarse():
    global estudiantes_cargados , moderadores_cargados
    encontrado = False
    menu_reutilizable = "\n\n1-Ingresar email y Ingresar contraseña: \n\n0-Salir\n"
    pr_limpiar_consola()
    pr_crear_titulo("Registrarse")
    print(menu_reutilizable)
    opcion = ValidarRangoDeNumero(0, 1)
    while opcion != 0 and not(encontrado):
        if opcion == 1:
            email = str(input("\nIngrese email: "))
            if email != "":
                id = fn_busqueda_secuencial(estudiantes, 8, email, 0)
                if id == -1:
                    encontrado = True
                else:
                    id = fn_busqueda_secuencial(moderador, 4, email, 0)
                    if id != -1:
                        encontrado = True
            if encontrado == True:
                contrasena = input("\nIngrese contraseña: ")
                if contrasena != "":
                    bandera = True
                    while bandera: 
                        usuario_tipo = input("Que tipo de usuario se registra?:\n e - estudiante \n m - moderador v-volver\n Ingrese una opción: ")
                        if (usuario_tipo == "e" or usuario_tipo == "E") and estudiantes_cargados < 8:
                            estudiantes[estudiantes_cargados][0] = email
                            estudiantes[estudiantes_cargados][1] = contrasena
                            estudiantes[estudiantes_cargados][9] = "activo"
                            estudiantes_cargados = estudiantes_cargados + 1 
                            bandera =False
                        elif (usuario_tipo == "m" or usuario_tipo == "M") and  moderadores_cargados < 4:
                            moderador[moderadores_cargados][0] = email
                            moderador[moderadores_cargados][1] = contrasena
                            moderador[moderadores_cargados][5] = "activo"
                            moderadores_cargados = moderadores_cargados + 1 
                            bandera= False
                        elif usuario_tipo == "v":
                            bandera= False

def pr_inicializacion():
    pr_limpiar_consola()
    pr_crear_titulo("Login")
    print("\n1-Iniciar sesion\n\n2-Registrarse\n\n3-Bonus Tracks\n\n0-Salir")
    opc = input("\nIngresar opcion: ")
    while opc != "0":
        if opc == "1":
            pr_iniciarSesion()
        elif  opc == "2":
                pr_registrarse()
        else:
            opc=="3"
            pr_bonustracks()
            
        pr_limpiar_consola()
        pr_crear_titulo("Login")
        print("\n1-Iniciar sesion\n\n2-Registrarse\n\n3-Bonus Tracks\n\n0-Salir\n")
        opc = input("\nIngresar opcion: ")
        

pr_inicializacion()
