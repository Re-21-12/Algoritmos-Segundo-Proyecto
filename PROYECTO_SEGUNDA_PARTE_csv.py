# Libreria utilizada para manejar archivos csv
import csv



# -_-_-_-_-_-_-_-_MENU-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
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
        if opt == '2':
            Buscar_Producto()
        if opt == '3':
            modificar_producto()
        elif opt == '4':
            print('Tenga lindo dia', bienvenida.capitalize())
            break
        return
# -_-_-_-_-_-_-_-_-_-_DESCUENTO-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


def Descuento(Producto_costo, Producto_existencia):
    if Producto_existencia > 4:
        # costo * 25/100
        # descuento del 25%
        descuento = Producto_costo * 0.25
        total_por_uno = Producto_costo - descuento
        # forula para el total
        total = float(Producto_costo * Producto_existencia) - \
            (descuento * Producto_existencia)
       # conversrio a str
        total_str = str(total)
        return total_str
    else:
        return "Q.0.00"
# -_-_-_-_-_-_-_-_-_-_EXISTENCIA_CODIGO-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


def Existe_codigo(Producto_codigo):
    with open('Producto.csv')as producto_csv:
       # Omitimos el encabezado
        Lector = csv.DictReader(producto_csv)
        next(producto_csv, None)
        for Fila in producto_csv:
            # removemos salto de linea
            Fila = Fila.rstrip()
            # lo volemos un arreglo
            # sep == separadoro
            sep = ','
            lista = Fila.split(",")
            if Producto_codigo in lista:
                return "Ya existe"
            else:
                return "No contiene esa serie"
# -_-_-_-_-_-_-_-_-_-_BUSCAR_PRODUCTOS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


def Buscar_Producto():
    print('Haz seleccionado buscar producto')
    buscar_producto = str(input("Ingrese el producto a buscar: "))
    buscar_producto_cap = buscar_producto.capitalize()
    escribir = []
    with open('Producto.csv')as producto_csv:
        palabra = 0
        next(producto_csv, None)
        for Fila in producto_csv:
            palabra += 1
            Fila = Fila.rstrip()
            sep = ','
            lista = Fila.split(",")
            if buscar_producto_cap in lista:
                escribir.append(str(palabra) + " -> " + Fila)

    with open("Salida_txt.txt", "w") as salida:
        for Fila in escribir:
            salida.write(Fila)
            print(" En linea: " + str(Fila))
            print("Su producto se enviara a: Salida_txt.txt")
    
    with open("Producto.csv") as producto_txt:
       [print(linea.strip()) for linea in producto_txt.readlines()]

# -_-_-_-_-_-_-_-_-_-_-_-_AGREGAR_PRODUCTOS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


def agregar_producto():
    print('Haz seleccionado agregar producto')

    Producto_codigo = str(input('Ingrese el codigo del producto [A-z;1-9]: '))
    if Existe_codigo(Producto_codigo) == "No contiene esa serie":
        with open("Producto.csv", "a+") as producto_txt:
            # -_--_--_--_--_--_--_--_--_--_-INFORMACIOCN-_--_--_--_--_--_--_--_--_--_-
            # nombre
            Producto_nombre = input(
                'Ingresa el nombre del  producto: ')
            # nombre con mayuscula
            Producto_nombre_fix = Producto_nombre.capitalize()
            # nombre del proveedor
            Producto_proveedor = input(
                'Ingrese nombre del proveedor: ')
            # nombre del proveedor con mayuscula
            Producto_proveedor_fix = Producto_proveedor.capitalize()
            # -_--_--_--_--_--_--_--_-DINERO-_--_--_--_--_--_--_--_--_--_--_--_-
            # el costo
            Producto_costo = float(
                input('Ingrese el costo del producto: '))
            print('El costo que ha ingresado es Q', Producto_costo)
            Producto_costo_str = str(Producto_costo)
            # existencias del producto
            Producto_existencia = int(
                input('Ingrese la cantidad de existencias: '))
            Producto_existencia_str = str(Producto_existencia)
            # Descuento
            Producto_Descuento = Descuento(
                Producto_costo, Producto_existencia)
            Producto_Descuento_str = str(Producto_Descuento)
            total_producto = str(Producto_costo * Producto_existencia)
            print("El costo del producto total es: ", total_producto)
            print("El descuento realizado es: ", Producto_Descuento)
            # -_--_--_--_--_--_--_--_--_--_-ESTADO-_--_--_--_--_--_--_--_--_--_--_-
            Producto_estado = str(
                input('Seleccione el estado del producto: A = Aprobado |R = reprobado -> '))
            Producto_estado_fix = Producto_estado.capitalize()
            aprobado = "A"
            reprobado = "R"

            # -_--_--_--_--_--_-Disenio-_--_--_--_--_--_-
            encabezados = ['Codigo', 'Nombre', 'Costo',
                           'Proveedor', 'Estado', 'Descuento', 'Existencias']
            # -_-_-_-_-_-_Disenio_de_encabezado-_-_-_-_-_-_
            Producto_dict = {'Codigo': Producto_codigo, 'Nombre': Producto_nombre_fix, 'Costo': Producto_costo_str, 'Estado': Producto_estado_fix,
                             'Proveedor': Producto_proveedor_fix, 'Descuento': Producto_Descuento_str, 'Existencias': Producto_existencia_str}
            # -_-_-_-_-_-_-_-_-_-_Leer_archivo_-_-_-_-_-_-_-_-_
            Producto_object = csv.DictWriter(
                producto_txt, fieldnames=encabezados)
            # -_-_-_-_-_-_-_-_-_-_Escribir_arhivo-_-_-_-_-_-_-_-_
            Producto_object.writerow(Producto_dict)
            producto_txt.close()
            # -_--_--_--_--_--_-LISTA-_--_--_--_--_--_--_--_--_--ESTADO-_--_--_--_--_--_--_--_--_--_-
            if Producto_estado_fix == aprobado:
                print('Usted ha seleccionado: ' +
                      '[', Producto_estado, ']'+': Aprobado')
            elif Producto_estado_fix == reprobado:
                print('Usted ha seleccionado: ' +
                      '[', Producto_estado, ']'+': Reprobado')
            else:
                print('Por favor seleccione un estado valido!')

                # valdiacion de codigo
    if Existe_codigo(Producto_codigo) == "Ya existe":
        print("El codigo contiene existencias")

    with open("Producto.csv") as producto_txt:
       [print(linea.strip()) for linea in producto_txt.readlines()]


# -_-_-_-_-_-_-_-_-_-_MODIFICAR_PRODUCTOS-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def modificar_producto():
    Producto_codigo = str(input('Ingrese el codigo del producto [A-z;1-9]: '))
    with open('Producto.csv', "r+")as producto_csv:
        for Fila in producto_csv:
            Fila = Fila.rstrip()
            sep = ','
            lista = Fila.split(",")
            if Producto_codigo in lista:
                # -_--_--_--_--_--_--_--_--_--_-INFORMACIOCN-_--_--_--_--_--_--_--_--_--_-
                # nombre
                Producto_nombre = input( 'Ingresa el nombre del  producto: ')
            # nombre con mayuscula
                Producto_nombre_fix = Producto_nombre.capitalize()
            # nombre del proveedor
                Producto_proveedor = input( 'Ingrese nombre del proveedor: ')
            # nombre del proveedor con mayuscula
                Producto_proveedor_fix = Producto_proveedor.capitalize()
            # -_--_--_--_--_--_--_--_-DINERO-_--_--_--_--_--_--_--_--_--_--_--_-
            # el costo
                Producto_costo = float(
                    input('Ingrese el costo del producto: '))
                print('El costo que ha ingresado es Q', Producto_costo)
                Producto_costo_str = str(Producto_costo)
            # existencias del producto
                Producto_existencia = int(
                    input('Ingrese la cantidad de existencias: '))
                Producto_existencia_str = str(Producto_existencia)
            # Descuento
                Producto_Descuento = Descuento(Producto_costo, Producto_existencia)
                Producto_Descuento_str = str(Producto_Descuento)
                total_producto = str(Producto_costo * Producto_existencia)
                print("El costo del producto total es: ", total_producto)
                print("El descuento realizado es: ", Producto_Descuento)
            # -_--_--_--_--_--_--_--_--_--_-ESTADO-_--_--_--_--_--_--_--_--_--_--_-
                Producto_estado = str(input('Seleccione el estado del producto: A = Aprobado |R = reprobado -> '))
                Producto_estado_fix = Producto_estado.capitalize()
                aprobado = "A"
                reprobado = "R"

                if Producto_estado_fix == aprobado:
                    print('Usted ha seleccionado: ' +
                      '[', Producto_estado, ']'+': Aprobado')
                elif Producto_estado_fix == reprobado:
                    print('Usted ha seleccionado: ' +
                      '[', Producto_estado, ']'+': Reprobado')
                else:
                    print('Por favor seleccione un estado valido!')

    with open("Producto.csv", "w+") as producto_csv:
        next(producto_csv, None)
            # -_--_--_--_--_--_-Disenio-_--_--_--_--_--_-
        encabezados = ['Codigo', 'Nombre', 'Costo',
                           'Proveedor', 'Estado', 'Descuento', 'Existencias']
           # disenio = {'Codigo':'01', 'Nombre':'Juan', 'Costo': '10', 'Proveedor':'Maria', 'Estado': 'A', 'Descuento':'10', 'Existencias': '20'}
            # -_-_-_-_-_-_Disenio_de_encabezado-_-_-_-_-_-_
        Producto_dict = {'Codigo': Producto_codigo, 'Nombre': Producto_nombre_fix, 'Costo': Producto_costo_str, 'Estado': Producto_estado_fix,
                             'Proveedor': Producto_proveedor_fix, 'Descuento': Producto_Descuento_str, 'Existencias': Producto_existencia_str}
            # -_-_-_-_-_-_-_-_-_-_Leer_archivo_-_-_-_-_-_-_-_-_
        Producto_object = csv.DictWriter(
                producto_csv, fieldnames=encabezados)
            # -_-_-_-_-_-_-_-_-_-_Escribir_arhivo-_-_-_-_-_-_-_-_
        Producto_object.writerow(Producto_dict)
        producto_csv.close()
        
    with open("Producto.csv") as producto_txt:
       [print(linea.strip()) for linea in producto_txt.readlines()]
        


menu()
