import time
reservacion = {}
def reservar_zapatillas():
    if len(reservacion)>= 20 :
        print("stock de reservas lleno, no se pueden hacer mas reservas")
        return
    while True:
        user = input("\nIngrese su nombre para la reservacion: ")

        if user not in reservacion:
            break
        else:
            print("\nUsuario ya existente, ingrese otro usuario. ")
            time.sleep(3)
            return
    
    while True:
        codigo_secreto = input("\ningrese el codigo secreto para confirmar reserva: ")

        if codigo_secreto != "EstoyEnListaDeReserva":
            print("codigo no valido, no se pudo realizar la reservacion deben respetar las mayusculas y las minisculas.")
            time.sleep(3)
            return
        reservacion[user] = 1
        print("reserva realizada exitosamente")
        time.sleep(3)
        break

def buscar_reservaciones():
    user = input("INGRESE EL NOMBRE DEL USUSARIO PARA BUSCARLO: ")

    if user in reservacion:
        print(f"reservacion encontrada para {user}")
        if reservacion[user] == 2:
            print("ya es una reserva vip (2 pares),")
            time.sleep(3)
        else:
            vip = input("desea pagar adicional por reservar vip (si/no): ")
            time.sleep(3)
            
            if vip == "si" :
                if len(reservacion) < 20:
                    reservacion[user] = 2
                    print("reservacion actualizada a vip (2 pares) ")
                    time.sleep(3)
                else:
                    print("no se pudo actualizar reservacion por stock completo. ")
                    time.sleep(3)
    else:
        print("no se encontro ninguna reservavion con ese nombre. ")
        time.sleep(3)

def cancelar_reservacion():
    user = input("ingrese el nombre de la reservacion para cancelarla: ")

    if user in reservacion:
        del reservacion[user]
        print("reservacion cancelada exitosamente")
        time.sleep(3)
    else:
        print("no se encontro ninguna reservacion con ese nombre. ")
        time.sleep(3)

def main():
    while True:
        print("====\nTOTEM AUTOATENCION RESERVA STRIKE=====")
        print("1- reservar zapatillas")
        print("2- buscar reservaciones")
        print("3-eliminar reservaciones")
        print("4- salir")

        opcion = input("ingrese la opcion a realizar: ")
        if opcion == "1":
            reservar_zapatillas()
            time.sleep(3)
        elif opcion == "2":
            buscar_reservaciones()
            time.sleep(3)
        elif opcion == "3":
            cancelar_reservacion()
            time.sleep(3)
        elif opcion == "4":
            print("programa terminando...")
            time.sleep(3)
            break
        else:
            print("debes ingresar una opcion valida (1,2,3,4). ")
            return
main ()