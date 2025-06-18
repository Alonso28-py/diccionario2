#sistema de gestion de usuario

#crear un diccionario para ingresar usuario
#crear una funcion para crear usuarios
#crear funcion para buscar usuario
#crear para eliminar usuarios
#crear funcion principal de menu

#este comando me permite traer la libreria time que nos permite hacer demoras de tiempo en segundos de linea en linea
import time
#crear diccionario vacio que contiene usuarios
registro_usuarios = {}

#crear funcion de ingreso de usuarios
def ingresar_usuarios():
    
    #ciclo while para validar el ingreso del noombre de usuario
    while True:
        user = input("\ningrese el nombre del usuario: ")

        #validar que el nombre de usuario no exista
        if user not in registro_usuarios:
            #si no existe el usuario en el diccionario se tiene que terminar el ciclo while
            break
        else:
            print("\n Usuario ya existe, ingrese otro usuario")
            time.sleep(3)

    #ciclo while para ingreso de sexo biologico
    while True:
        sexo_biologico = input("\ningrese su sexo biologico(M/F):")

        #validar que sea F o M
        if sexo_biologico == "M" or sexo_biologico == "F":
            #en caso de que sea una de esas dos opciones se termina el ciclo while
            break
        else:
            print("\nEl dato ingresado no es valido, intente nuevamente")
            time.sleep(3)
    
    #ciclo while para validaci0nes de ingreso de contraseña
    while True:
        numeros = 0 
        letras = 0

        #ingreso de password
        password = input("\nIngrese la contraseña de usurio : ")

        #validacion para la cantidad de caracteres de la contraseña
        if len(password) >=8:
            #validar vacios de contraseña
            if " " not in password:
                #validar que la contraseña tenga numeros y letras
                for i in password:
                    #validar que tenga numero
                    if i in "0123456789":
                        numeros += 1
                    #validar que tenga alguna letra
                    if i in "abcdefghijkmnlpqxyztrw":
                        letras += 1
                #validar si los contadores son mayores o igual a 1
                if numeros > 0 and letras > 0:
                    print("\ncontraseña valida")
                    time.sleep(3)

                    #insertar los datos de usuario en el diccionario
                    registro_usuarios[user] = [sexo_biologico, password]
                    print("\nUsuario ingresado de forma exitosa")
                    time.sleep(2)
                    break
                #else de if validacion de los contadores
                else:
                    print("\nerror contraseña no valida (la conmtraseña no tiene un numero o una letra)")
                    time.sleep(3)
            #else de validacion de espacios
            else:
                print("\nerror contraseña no valida (la conmtraseña tiene espacio)")
                time.sleep(3)
        #else de if de validacion del largo de la contraseña
        else:
            print("\nError contraseña no valida (la contraseña tiene menos de 8 caracteres)")
            time.sleep(3)
# funcion def para buscar usuarios:
def buscar_usuarios(user):
    #confirmar que el nombre recibido a traves de argumento este en el diccionario
    if user in registro_usuarios:
        print("\n******DATOS DE USUARIO*******")
        print(f"NOMBRE DE USUARIO {user}")
        print("SEXO BIOLOGICO", registro_usuarios[user][0])
        print("PASSWORD", registro_usuarios[user][1])
        print("")
        time.sleep(3)
    else:
        print("\nEl usuario no esta registrado en el diccionario")
#eliminacion de usuario
def eliminar_usuario(user):
    #confimar que el nombre ingresado a traves del argumento este en el diccionario
    if user in registro_usuarios:
        #el comando del para eliminar usuario del diccionario
        del registro_usuarios[user]
        print("\nUsuario elimado")
        time.sleep(3)
    else:
        print("\nNo se encontro el usuario a eliminar")
        time.sleep(3)

#funcion maid para menu e interacciones
def main():
    #ciclo while para mostrar el menu
    while True:
        print("==============================")
        print("MENU DE GESTION DE OPCIONES")
        print("====================================")
        print("1- ingresar usuario")
        print("2- busar usuario")
        print("3- eliminar usuario")
        print("4- salir \n")

        op = input("ingrese la opcion deseada:")
        
        if op == "1":
            ingresar_usuarios()
        elif op == "2":
            usuario = input("\ningrese el usuario a buscar:")
            buscar_usuarios(usuario)
        elif op == "3":
            usuario = input("\ningrese el usuario a eliminar:")
            eliminar_usuario(usuario)
        elif op == "4":
            print("salieno del sistema")
            time.sleep(3)
        else:
            print("\nla opcion ingresada no es valida")
            time.sleep(3)
main()