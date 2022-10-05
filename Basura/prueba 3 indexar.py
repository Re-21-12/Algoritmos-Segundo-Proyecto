archivo_entrada = "input.txt"
archivo_salida = "salidanueva.txt"
busqueda_prodcuto = input("Ingresa el producto que desea buscar : ")
escribir = []
with open(archivo_entrada, "r") as archivo_lectura:
    palabra = 0
    lectura_readlines = archivo_lectura.readlines()
    for filas in lectura_readlines:
        palabra += 1
        #filas = filas.rstrip()
        #palabra1 = filas.split(" ")
        if '['+ str(busqueda_prodcuto)+']' in palabra1:
            escribir.append(str(palabra) + " - " + filas)
            lectura = lectura_readlines.index(busqueda_prodcuto)
            lectura_index = archivo_lectura.readlines()[lectura]
            
            
 
with open(archivo_salida,  "w") as archivo_de_salida:
    for filas in escribir:
        archivo_de_salida.write(filas + "\n")
        print("En linea: " + str(palabra)+ "Se encontro: " + str(busqueda_prodcuto))
        print("Su producto se enviara a: "+ archivo_salida)
        print(lectura.index)