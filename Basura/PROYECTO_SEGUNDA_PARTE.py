'''
Algoritmo de Python SEGUNDO PROYECTO
Victor Macario 7690-22-5042
'''
import csv
#El segundo parametro de la funcion open es el modo


def menu():
    bienvenida = input('Ingrese su nombre: ')
    print('Bienvenido: ', bienvenida.capitalize())
    while True:
        print('-_--_--_--_--_--_--_--_-Menu-_--_--_--_--_--_-')
        print('[1]. Agregar producto')
        print('[2]. Buscar producto')
        print('[3]. Modificar producto')
        opt = input('Selecciona una opcion: ')
        if opt == '1':
            agregar_producto()
        elif opt == '2':
            print('Tenga lindo dia', bienvenida.capitalize())
            break
        return
    
'''
nombre,codigo,proveedor,existencia,estado,descuento?
'''
def Existe_codigo(Producto_codigo):
    #abrir archivo para leer
    with open('Producto.txt', "r") as producto_txt:
        #leer por lineas
        lectura = producto_txt.readlines()
        print(lectura)
       #leer cada linea en lectura
        for filas in lectura:
            print(filas.rstrip())
            
            #si el parametro coincide dentro de lectura
            if(Producto_codigo+"\n") in lectura:
                #imprimir la linea donde coincide
                #indice de la linea donode se encontro + 1 para el usuario
                lectura_index = lectura.index(Producto_codigo+"\n")
                print("En linea: "+ str(lectura_index))
                return "Ya existe"
            #si no contiene la serie de numeros
            else:
                return "No contiene esa serie"
     

def Descuento(Producto_costo,Producto_existencia):
    if Producto_existencia > 4:
        #costo * 25/100 
        #descuento del 25%
        descuento = Producto_costo * 0.25
        total_por_uno = Producto_costo - descuento
        #forula para el total
        total = float(Producto_costo * Producto_existencia) -(descuento * Producto_existencia)
       #conversrio a str
        total_str = str(total)
        return total_str
    else:
        return "Q.0.00"
        
        
        
def agregar_producto():
    print('Haz seleccionado agregar producto')
    
    Producto_codigo = str(input('Ingrese el codigo del producto [A-z;1-9]: ')) 
    if Existe_codigo(Producto_codigo)=="No contiene esa serie":
        with open("Producto.txt", "a+") as producto_txt:    
            #-_--_--_--_--_--_--_--_--_--_-INFORMACIOCN-_--_--_--_--_--_--_--_--_--_-
                #nombre
                    Producto_nombre = input('Ingresa el nombre del  producto: ')
                #nombre con mayuscula
                    Producto_nombre_fix = Producto_nombre.capitalize()
                #nombre del proveedor
                    Producto_proveedor = input('Ingrese nombre del proveedor: ')
                #nombre del proveedor con mayuscula
                    Producto_proveedor_fix = Producto_proveedor.capitalize()
                #-_--_--_--_--_--_--_--_-DINERO-_--_--_--_--_--_--_--_--_--_--_--_-
                #el costo
                    Producto_costo = float(input('Ingrese el costo del producto: '))
                    print('El costo que ha ingresado es Q',Producto_costo)
                    Producto_costo_str = str(Producto_costo)
                #existencias del producto
                    Producto_existencia = int(input('Ingrese la cantidad de existencias: '))
                    Producto_existencia_str = str(Producto_existencia)
                #Descuento
                    Producto_Descuento = Descuento(Producto_costo,Producto_existencia)
                    Producto_Descuento_str = str(Producto_Descuento)
                    total_producto = str(Producto_costo * Producto_existencia)
                    print("El costo del producto total es: ", total_producto)
                    print("El descuento realizado es: ",Producto_Descuento )
                #-_--_--_--_--_--_--_--_--_--_-ESTADO-_--_--_--_--_--_--_--_--_--_--_-
                    Producto_estado = str(input('Seleccione el estado del producto: A = Aprobado |R = reprobado -> '))
                    Producto_estado_fix = Producto_estado.capitalize()
                    aprobado = "A" 
                    reprobado = "R"
                #-_--_--_--_--_--_-LISTA-_--_--_--_--_--_--_--_--_--_--_--_-
                   # Producto_lista = [Producto_nombre_fix, Producto_costo_str,Producto_proveedor_fix,Producto_estado_fix,Producto_Descuento_str,Producto_existencia_str,Producto_codigo]
                #-_--_--_--_--_--_-ESCRITURA DEL ARCHIVO-_--_--_--_--_--_--_--_--_-
                    producto_txt.write(Producto_nombre_fix+','+Producto_costo_str+','+Producto_proveedor_fix+','+Producto_estado_fix+','+Producto_Descuento_str+','+Producto_existencia_str+','+Producto_codigo+"\n")
                   # producto_txt.writelines(Producto_lista)
                #-_--_--_--_--_-VALIDACION DEL ESTADO-_--_--_--_--_--_--_--_--_--_-
                    if Producto_estado_fix == aprobado :
                            print('Usted ha seleccionado: '+'[',Producto_estado,']'+': Aprobado')
                    elif Producto_estado_fix == reprobado:
                            print('Usted ha seleccionado: '+'[',Producto_estado,']'+': Reprobado')
                    else:
                            print('Por favor seleccione un estado valido!')
                            
                            #valdiacion de codigo
    if Existe_codigo(Producto_codigo) == "Ya existe":
     print("El codigo contiene existencias")

        #agregar validacion de codigo
    with open("Producto.txt") as producto_txt:
       [print(linea.strip()) for linea in producto_txt.readlines()]


        
def buscar_producto(buscar_producto):
    with open("Producto.txt", "r") as archivo_lectura:
        buscar_producto = input("Ingresa el nombre del producto")
        escribir = []
        palabra = 0
        for contenido in archivo_lectura:
            palabra+=1
            contenido = contenido.rstrip()
            palabra_1 = contenido.split(" ")
            if buscar_producto in palabra_1:
                escribir.append(str(palabra)+ " ~ "+ contenido)
                
    with open("Producto_salida", "w")as producto_salida:
        for contenido in escribir:
            producto_salida.write(contenido + "\n")
            print("En linea: " + str(palabra)+ "Se encontro: " + str(buscar_producto))
            print("Su producto se enviara a: "+ producto_salida)
menu()
