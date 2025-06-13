#sistema de cventas de zapatillas

#diccionario de bases de datos de satock de zapatillas

inventario = {
    "001": {"modelo": "air max", "precio": 89990, "stock": 15},
    "002": {"modelo": "calsic", "precio": 49990, "stock": 50},
    "003": {"modelo": "runner", "precio": 69990, "stock": 20},
    "004": {"modelo": "basquet", "precio": 79990, "stock": 5},
}
# funcion para mostar inventario dsipobneible
def mostrar_inventario():
    print("\n========INVENTARIO DE ZAPATILLAS=======")
    print("codigo | modelo | precio | stock")
    print("-----------------------------------------")

    #ciclo for para iterar cada ite del inventario
    for codigo,datos in inventario.items():
        print(f"{codigo}  |{datos["modelo"]:8}| ${datos["precio"] } | {datos["stock"]}")

def procesar_venta():

    mostrar_inventario()

    #pregunmtar codigo del producto a vender:
    codigo = input("\n ingrese el codigo de la zapatilla: ")

    #validar que el codigo ingresado vaya en el diccionario
    if codigo not in inventario:
        print("error el codigo ingresado no existe. ")
        return
    
    #solicitar la cantidard numeria a vender de zapatillas
    try:
        cantidad = int(input("ingrese la cantidad de zapatillas a vender: "))
    except ValueError:
        print("error debe ingresar un numero valido. ")
        return
    
    #validar que la cantidad necesario sea mayor a 0
    if cantidad<=0:
        print("error: la cantidad debe ser mayor que cero. ")
        return
    elif cantidad> inventario[codigo]["stock"]:
        print("error: no hay suficiente disponible.")


    #calcula el valor de la venta
    precio_unitario = inventario[codigo]["precio"]
    total = precio_unitario * cantidad

    #actualizar stock del diccionario 
    inventario[codigo]["stock"] -= cantidad
    