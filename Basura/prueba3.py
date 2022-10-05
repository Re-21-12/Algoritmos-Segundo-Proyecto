def Existe_codigo(Producto_codigo):
    #abrir archivo para leer
    with open('Producto.txt', "r") as producto_txt:
        #leer por lineas
        lectura = producto_txt.readlines()
       #leer cada linea en lectura
        for filas in lectura:
            #si el parametro coincide dentro de lectura
            if(Producto_codigo+"\n") in lectura:
                #imprimir la linea donde coincide
                #indice de la linea donode se encontro + 1 para el usuario
                lectura_index = lectura.index(Producto_codigo+"\n")
                print("En linea: "+ str(lectura_index +1))
                #lectura_index_1 = producto_txt.readlines()[lectura_index]
                #print(lectura_index_1)
                return "Ya existe"
            #si no contiene la serie de numeros
            else:
                return "No contiene esa serie"

a = input("ingrese: ")
Existe_codigo(a)
