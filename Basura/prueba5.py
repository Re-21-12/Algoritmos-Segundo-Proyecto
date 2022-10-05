def Existe_codigo(Producto_codigo):
    #abrir archivo para leer
    with open('Producto.txt', "r") as producto_txt:
        #leer por lineas
        lectura = producto_txt.readlines()
        print(lectura)
       #leer cada linea en lectura
        for filas in lectura:
            print(filas)
            #si el parametro coincide dentro de lectura
            if(Producto_codigo + "\n") in lectura:
                #imprimir la linea donde coincide
                #indice de la linea donode se encontro + 1 para el usuario
                lectura_index = lectura.index(Producto_codigo+ "\n")
                print("En linea: "+ str(lectura_index +1))
                return "Ya existe"
            #si no contiene la serie de numeros
            else:
                print("no contiene esa")
                return "No contiene esa serie"
Producto_codigo = str(input('Ingrese el codigo del producto [A-z;1-9]: ')) 
Existe_codigo(Producto_codigo)