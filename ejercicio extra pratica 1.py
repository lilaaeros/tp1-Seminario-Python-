# ejercicio extra pratica 1
import sys

print ("sistema de gestion de inventario  que contiene \n")
print ("nombre del producto \n")
print ("cantidad de producto")

producto = []  # hago una lista para almacenar los valores en la lista y luego lo junto con zip
cantidades = []  # idem anterior
while True:
    nombre = input ("ingrese el nombre del prod o ponga 'salir' para terminar \n").strip().lower() 
    if nombre == 'salir':
        inventario_completo = list(zip(producto, cantidades))
        print (" el inventario quedo asi ")
        for p , c in inventario_completo:
            print (f"Producto  {p} , cuya cantidad es de {c} ")
        sys.exit(1)
    if nombre not in producto:
        producto.append(nombre)  # agrego el nombre a la lista
        cant = input ("ingrese la cantidad del producto nombrado ")
        while (not cant.isdigit() and cant != 'salir'):
            cant = input ("ingrese una cantidad valida ") 
        cantidades.append(int(cant)) 
    else:
        rta = input ("el producto ya se encuentra en el listado, desea actualizarlo?. Ponga Y para si, N para no, o VOLVER si desea volver \n ").lower()
        while rta not in ["y", "n","volver"]:            
            rta = input ("el producto ya se encuentra en el listado, desea actualizarlo?. Ponga Y para si, N para no, o VOLVER si desea volver \n ")
        if rta == "y": 
            index = producto.index(nombre)
            respuesta = input (" si desea eliminarlo presione '1' , si desea actualizar su cantidad presione '2' \n")
            while not respuesta.isdigit() or int(respuesta) not in [1, 2]:
                respuesta = input(" si desea eliminarlo presione '1' \n, si desea actualizar su cantidad presione '2' \n")
            if int(respuesta) == 2:
               cant = input ("ingrese la cantidad actualizada del producto nombrado ")
               while (not cant.isdigit() and cant != 'salir'):
                    cant = input ("ingrese una cantidad valida ")  
               cantidades[index]= int(cant)
            if int(respuesta) == 1:
               del producto[index]
               del cantidades[index]
               print(f"Producto '{nombre}' eliminado del inventario.")

                
    





