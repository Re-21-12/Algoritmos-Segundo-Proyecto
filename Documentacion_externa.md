# Documentacion Externa: Segundo Proyecto(Sistema de Inventarios)

## **Proyecto desarrollado por:**
### Victor Alfredo Macario Enriquez 7690-22-5042
### Jefferson Ramiro Lopez Ramirez  7690-21-1522
### Roberto Antonio Ramírez Gómez   7690-22-12700
### José Miguel Arellano Bran       7690-22-5733
***

# Link GitHub:
https://github.com/Re-21-12/Algoritmos-Segundo-Proyecto

## **Documentacion externa sistema inventarios** _(Python)_
![A python image language](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngall.com%2Fwp-content%2Fuploads%2F5%2FPython-PNG-Pic.png&f=1&nofb=1&ipt=cbae4236b82f2be7007f59ac54d52cb040659dfd5a7f62dbf57dba49d21aad96&ipo=images "Pythom_img")
---
### Librerias
- En este caso se importo una libreria llamada csv, que nos permite manipular archivos con extension .csv
    ~~~
    import csv
    ~~~

### El menu
---
- Para la realizacion del menu, se uso una __funcion__ definida por:
  ~~~
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
        elif opt == '3':
            print('Tenga lindo dia', bienvenida.capitalize())
            break
        return
  ~~~
     En esta funcion se genera un similar a __SwitchCase__ pero en _Python_ anidando una serie de opciones son _If's_ logrando de esta manera que si el ususario ingresa un numero: 1, 2 o una de las opciones disponibles lance otra funcion con la ejecucion del programa.
  
### El Descuento
---
- Para la realizacion del descuento se usaron dos _Parametros_ el primero: *Producto_Costo* y el segundo: *Producto_existencia* utilizando una regla cuando el producto a llevar sea mayor que 4 existencias entonces se realizara el descuento:
   ~~~
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
   ~~~
    Agregado a ello luego de seguir la sentencia se establece un descuento del _25%_ al total de existencias y se le resta, para asi obtener el descuento total, de cumplir lo anterior regresara el _total_ si no regresara _Q.00_

### Existencia de codigo
---
- Para comprobar la existencia de un producto, la manera mas facil sera siempre comprobarlo a traves de una serie de numeros unicos, en este caso en un sistema alphanumerico que nos permita determinar la existencia del producto o productos; Para ello manipularemos a traves de una libreria anteriormente mencionada **Csv** un archivo de extension **.Csv** y lo leeremos fila por fila, luego lo filtraremos eliminando las filas vacias o los espacios que genera _Python_ de manera individual, luego a traves de una sentencia se realizada una busqueda en cada linea para determina; Si existe el parametro que se le paso en __Producto_Codigo__ dentro de la lista sin los espacios de no encontrarse se retornara _"No contiene esa serie"_
    ~~~
    def Existe_codigo(Producto_codigo):
    with open('Producto.csv')as producto_csv:
       #Omitimos el encabezado
       Lector = csv.DictReader(producto_csv)
       next(producto_csv, None)
       for Fila in producto_csv:
           #removemos salto de linea
           Fila = Fila.rstrip()
           #lo volemos un arreglo
           # sep == separadoro
           sep = ','
           lista = Fila.split(",")
           if Producto_codigo in lista:
               return "Ya existe"
           else:
               return "No contiene esa serie"
    ~~~

### Buscar un producto
---
- Para nosotros querer buscar un producto en nuestro _"Sistema"_, debemos :
    1. Ingresar nuestro producto a buscar.
    2. Capitalizar nuestro producto para facilitar la busqueda.
    3. Darle una salida a nuestro *(Opcional)*.
    4. Leer nuestro archivo.
    5. Indicar donde se encontro.
    6. Filtrar la busqueda para ser facilitada.
   
    Con los pasos mencionados anteriormente se realizo la siguiente funcion:
    ~~~
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
                escribir.append(str(palabra)+ " -> "+ Fila)
                
    with open("Salida_txt.txt", "w") as salida:
        for Fila in escribir:
            salida.write(Fila)
            print(" En linea: " + str(Fila))
            print("Su producto se enviara a: Salida_txt.txt")   
    ~~~
    Donde en dicha funcion se realizan todos los pasos mencionados anteriormente y la salida o el producto ingresado lo dirije a un archivo de salida .txt.

### Agregar un producto
---
- Para nosotros querer agregar un producto primero debemoms revisar si ese producto no se encuentra ya ingresado, para ello haremos uso de la funcion antes mencionada __Existe_codigo__ donde primeramente validaremos a traves de una variable pasandoselo como parametro a la funcion mencionada, para su posteriormente validacion, si este no existe dentro de nuestro sistema entonces, podemos continuar; Cabe mencionar que como queremos agregar un producto debemos hacer uso de: __El modo a+ de nuestra sintaxis with open__
para agregar un producto y no sobreescribirlo.

- A traves de una serie de variables con sus respectivos inputs, procederemos a ir ingresando uno por uno para ingresarlo a nuestro archivo **.Csv** pero para que se vea correctamente ingresado en nuestro archivo haremos uso de:
    1. Una lista llamada **Encabezados**
    2. Un diccionario para organizar de manera correcta la informacion.
    3. Una variable llamada **Producto_object** para escribir los datos ingresados con un formato.
    4. Usaremos la funcion **writerow** para escribirlo por lineas.
   
   ~~~
   ef agregar_producto():
    print('Haz seleccionado agregar producto')
    
    Producto_codigo = str(input('Ingrese el codigo del producto [A-z;1-9]: ')) 
    if Existe_codigo(Producto_codigo)=="No contiene esa serie":
     with open("Producto.csv", "a+") as producto_txt:    
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
                    
                #-_--_--_--_--_--_-Disenio-_--_--_--_--_--_-
                    encabezados = ['Codigo', 'Nombre','Costo', 'Proveedor', 'Estado', 'Descuento','Existencias']
                   # disenio = {'Codigo':'01', 'Nombre':'Juan', 'Costo': '10', 'Proveedor':'Maria', 'Estado': 'A', 'Descuento':'10', 'Existencias': '20'}
                    #-_-_-_-_-_-_Disenio_de_encabezado-_-_-_-_-_-_
                    Producto_dict = {'Codigo': Producto_codigo, 'Nombre':Producto_nombre_fix, 'Costo':Producto_costo_str,'Estado':Producto_estado_fix,'Proveedor':Producto_proveedor_fix, 'Descuento':Producto_Descuento_str,'Existencias':Producto_existencia_str}
                    #-_-_-_-_-_-_-_-_-_-_Leer_archivo_-_-_-_-_-_-_-_-_
                    Producto_object = csv.DictWriter(producto_txt, fieldnames=encabezados)  
                    #-_-_-_-_-_-_-_-_-_-_Escribir_arhivo-_-_-_-_-_-_-_-_
                    Producto_object.writerow(Producto_dict)
                    producto_txt.close()
                        #-_--_--_--_--_--_-LISTA-_--_--_--_--_--_--_--_--_--_--_--_-
                    if Producto_estado_fix == aprobado :
                            print('Usted ha seleccionado: '+'[',Producto_estado,']'+': Aprobado')
                    elif Producto_estado_fix == reprobado:
                            print('Usted ha seleccionado: '+'[',Producto_estado,']'+': Reprobado')
                    else:
                            print('Por favor seleccione un estado valido!')
                            
                            #valdiacion de codigo
    if Existe_codigo(Producto_codigo) == "Ya existe":
        print("El codigo contiene existencias")
   ~~~

### Modificar un producto
---
- Al modificar un producto se pueden utilizar variadas maneras de realizarsem a traves de archivos _temporales_, con _funciones replace_ o de la mas sencillas  _asignando nuevos datos a variables_ ya existentes; En este caso para fines practico se realizo la tercera, primeramente lo se debe realizar es una funcion en este caso llamada **Modificar_producto** donde primero Indexaremos nuestro codigo, es decir lo buscaremos en nuestro sistema, para ello se realizar un ciclo for y se va limpiando como se menciona en anteriores explicaciones, luego de ello similar a cuando buscamos por nombre validamos el codigo sin alterar su dato es decir buscamos en la fila donde se encuentra sin alterarlo.
  
- Seguidamente realizamos una serie de inputs o entradas con los datos a solicitar al usuario.

- Con otro _with open_ se realiza un **w+** para poder escribir y leer en nuestro archivo, junto a encabezados para identificar la posicion en la que se deben guardar los datos, usamoms tambien un diccionario para la nueva asignacion de valores, y a traves de la funcion *Dictwriter* lo transformamos en un objeto y se realizan las asignaciones correspondientes.

- Por ultimo realizamos un with open por default para que nos muestre los datos ingresados.

- De esta manera:
  ~~~
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
  ~~~
---
## **Codigo fuente** _(Python)_
~~~
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

~~~
---
## **Video en** _(Python)_
[![imagen_screen](alt_img.jpeg)](https://www.youtube.com/watch?v=HRv3DA2-LF8&ab_channel=VictorMacario "captura")
<p style="text-align: center;" target="_blank">Haga click </p>

---
## **Captura de resultado en:** _(Python)_
  1. Agregar un producto ![agregar_producto](/Capturas_Py/WhatsApp%20Image%202022-10-06%20at%206.11.10%20PM.jpeg)
  2. Buscar un producto ![buscar_producto](/Capturas_Py/WhatsApp%20Image%202022-10-06%20at%206.11.10%20PM%20(1).jpeg)
  3. Modificar un producto ![modificar_producto](/Capturas_Py/WhatsApp%20Image%202022-10-06%20at%206.11.10%20PM%20(2).jpeg)
  4. Producto Csv ![producto_csv](/Capturas_Py/WhatsApp%20Image%202022-10-06%20at%206.11.10%20PM%20(4).jpeg)
  5. Salida Txt ![salida_txt](/Capturas_Py/WhatsApp%20Image%202022-10-06%20at%206.11.10%20PM%20(3).jpeg)
   

***

## **Documentacion externa sistema inventarios** _(C++)_
![A python image language](https://raw.githubusercontent.com/isocpp/logos/master/cpp_logo.png "C++_img")

## Las librerias

#include <iostream> : nos permite hacer uso del cin y el cout para obtener o imprimir valores.<br>

#include <fstream> : permite la manipulacion de archivos desde el programa, tanto leer y escribir en ellos.<br>

#include <windows.h> : contiene las declaraciones de todas las funciones de la biblioteca Windows API, todas las macros utilizadas por los programadores de aplicaciones para Windows, y todas las estructuras de datos utilizadas en gran cantidad de funciones y subsistemas.

## Manual principal

Esta parte del codigo nos permite seleccionar una opcion por elemplo: Agregar un producto, buscar producto, modificar los datos.<br>

int menu(){<br>

int x;<br>

string nombre;<br>

system("cls");<br>

cout<<" MENU "<<endl;<br>

cout<<" |------------------|"<<endl<<endl;<br>

cout<<" 1. AGREGAR PRODUCTO"<<endl;<br>

cout<<" 2. BUSCAR UN PRODUCTO"<<endl;<br>

cout<<" 3. MODIFICAR LOS DATOS DE UN PRODUCTO"<<endl;<br>

cout<<" 4. SALIR"<<endl<<endl;;<br>

cout<<" SELECCIONA UNA OPCION: ";<br>

cin>>x;<br>

return x;<br>

}

##### Este proceso verifica que si ya existe un codigo dentro del archivo, ya no lo ingresa nuevamente.

bool verifica (string cod){<br>

ifstream leer("Productos.txt", ios::in);<br>

producto productos;<br>

leer>>productos.codigo;<br>

while(!leer.eof()){<br>

leer>>productos.nombre;<br>

leer>>productos.precio;<br>

leer>>productos.proveedor;<br>

leer>>productos.existencia;<br>

leer>>productos.estado;<br>

leer>>productos.descuento;<br>

if(productos.codigo == cod){<br>

cout<<endl;<br>

cout<<" ESTE CODIGO DE PRODUCTO YA EXISTE, POR FAVOR INGRESE UNO NUEVO..."<<endl;<br>

cout<<endl;<br>

leer.close();<br>

system("pause");<br>

return false;<br>

}<br>

leer>>productos.codigo;<br>

}<br>

leer.close();<br>

return true;<br>

}

## Funcion agregar

Esta funcion nos permite ingresar productos al archivo llamados prodectos.txt con todos sus atributos como su nombre,descuento y codigo etc.<br>

void agregar(ofstream &escribir){<br>

system("cls");<br>

producto productos;<br>

escribir.open("Productos.txt", ios::out | ios::app);<br>

cout<<" AGREGAR PRODUCTO"<<endl<<endl;<br>

cout<<" INGRESE EL CODIGO DEL PRODUCTO: ";<br>

cin>>productos.codigo;<br>

cout<<" INGRESE EL NOMBRE DEL PRODUCTO: ";<br>

cin>>productos.nombre;<br>

cout<<" INGRESE EL PRECIO DEL PRODUCTO (Q): ";<br>

cin>>productos.precio;<br>

fflush(stdin);<br>

cout<<" INGRESE EL PROVEEDOR DEL PRODUCTO: ";<br>

cin>>productos.proveedor;<br>

cout<<" INGRESE LA EXISTENCIA DEL PRODUCTO (UNIDADES): ";<br>

cin>>productos.existencia;<br>

fflush(stdin);<br>

cout<<" INGRESE EL ESTADO DEL PRODUCTO (A = APROVADO R = REPROVADO): ";<br>

cin>>productos.estado;<br>

cout<<" INGRESE EL DESCUENTO DEL PRODUCTO (%): ";<br>

cin>>productos.descuento;<br>

fflush(stdin);<br>

cout<<endl;<br>

if(verifica(productos.codigo))<br>

escribir << productos.codigo << " "<< productos.nombre << " "<< productos.precio << " " << productos.proveedor << " " << productos.existencia << " " << productos.estado << " "<< productos.descuento<<endl;<br>

escribir.close();<br>

}

## Funcion buscar

Este proceso nos permite buscar el producto que sea necesario buscar con todos sus atributos.<br>

void buscar(ifstream &lectura){<br>

system("cls");<br>

lectura.open("Productos.txt", ios::in);<br>

producto productos;<br>

bool encontrado = false;<br>

string codigo;<br>

cout<<" BUSCAR "<<endl<<endl;<br>

cout<<" INGRESE EL CODIGO DEL PRODUCTO QUE DESEA BUSCAR: ";<br>

cin>>codigo;<br>

cout<<endl;<br>

lectura>>productos.codigo;<br>

while(!lectura.eof() && !encontrado){<br>

lectura>>productos.nombre;<br>

lectura>>productos.precio;<br>

lectura>>productos.proveedor;<br>

lectura>>productos.existencia;<br>

lectura>>productos.estado;<br>

lectura>>productos.descuento;<br>

if(productos.codigo == codigo){<br>

cout<<" CODIGO: "<<productos.codigo<<endl;<br>

cout<<" NOMBRE: "<<productos.nombre<<endl;<br>

cout<<" PRECIO (Q): "<<productos.precio<<endl;<br>

cout<<" PROVEEDOR: "<<productos.proveedor<<endl;<br>

cout<<" EXISTENCIA (U): "<<productos.existencia<<endl;<br>

cout<<" ESTADO: "<<productos.estado<<endl;<br>

cout<<" DESCUENTO (%): "<<productos.descuento<<endl<<endl;<br>

encontrado = true;<br>

}<br>

lectura>>productos.codigo;<br>

}<br>

lectura.close();<br>

if(!encontrado)<br>

cout<<" PRODUCTO NO ENCONTRADO "<<endl<<endl;<br>

system("pause");<br>

}

## Funcion modificar

Esta funcion nos permite cambiar o modificar los atribustos del producto que se requeira modificar.<br>

void modificar(ifstream &lectura){<br>

system("cls");<br>

string ncodigo;<br>

string nnombre;<br>

float nprecio;<br>

string nproveedor;<br>

int nexistencia;<br>

string nestado;<br>

float ndescuento;<br>

producto productos;<br>

lectura.open("Productos.txt", ios::in);<br>

ofstream auxiliar("auxiliar.txt", ios::out);<br>

if(lectura.is_open()){<br>

cout<<" MODIFICAR LOS ATRIBUTOS DE UN CODIGO "<<endl<<endl;<br>

cout<<" INGRESE EL CODIGO DEL PRODUCTO QUE DESEA MODIFICAR: ";<br>

cin>>ncodigo;<br>

cout<<endl;<br>

lectura>>productos.codigo;<br>

while(!lectura.eof()){<br>

lectura>>productos.nombre;<br>

lectura>>productos.precio;<br>

lectura>>productos.proveedor;<br>

lectura>>productos.existencia;<br>

lectura>>productos.estado;<br>

lectura>>productos.descuento;<br>

if(productos.codigo == ncodigo){<br>

cout<<" NUEVO NOMBRE DEL PRODUCTO: ";<br>

cin>>nnombre;<br>

cout<<" NUEVO PRECIO DEL PRODUCTO (Q): ";<br>

cin>>nprecio;<br>

cout<<" NUEVO PROVEEDOR DEL PRODUCTO: ";<br>

cin>>nproveedor;<br>

cout<<" NUEVA EXISTENCIA DEL PRODUCTO (u): ";<br>

cin>>nexistencia;<br>

cout<<" NUEVO ESTADO DEL PRODUCTO: ";<br>

cin>>nestado;<br>

cout<<" NUEVO DUSCUENTO DEL PRODUCTO (%): ";<br>

cin>>ndescuento;<br>

cout<<endl;<br>

cout<<" EL PRODUCTO SE MODIFICO EXITOSAMENTE"<<endl<<endl;<br>

system("pause");<br>

auxiliar<<productos.codigo<<" "<<nnombre<<" "<<nprecio<<" "<<nproveedor<<" "<<nexistencia<<" "<<nestado<<" "<<ndescuento<<endl;<br>

}else{<br>

auxiliar << productos.codigo << " "<< productos.nombre << " "<< productos.precio << " " << productos.proveedor << " " << productos.existencia << " " << productos.estado << " "<< productos.descuento<<endl;<br>

}<br>

lectura>>productos.codigo;<br>

}<br>

lectura.close();<br>

auxiliar.close();<br>

}else<br>

cout<<" ¡NOS SE PUDO ABRIR EL ARCHIVO!";<br>

remove("Productos.txt");<br>

rename("auxiliar.txt", "Productos.txt");<br>

}

## Funcion principal

En esta funcion es para busacar y agregar el prodecto para que nos muestre el usuario.<br>

int main(){<br>

struct producto productos;<br>

ofstream escribir;<br>

ifstream lectura;<br>

int opcion;<br>

do{<br>

system("cls");<br>

opcion = menu();<br>

switch(opcion){<br>

case 1:<br>

agregar(escribir);<br>

break;<br>

case 2:<br>

buscar(lectura);<br>

break;<br>

case 3:<br>

modificar(lectura);<br>

break;<br>

case 4:<br>

return 0;<br>

break;<br>

}<br>

}while(opcion != 4);<br>

return 0;<br>

}


## **Video en** _(C++)_
[![imagen_screen](/Capturas_C%2B%2B/WhatsApp%20Image%202022-10-07%20at%209.33.51%20AM.jpeg)](https://youtu.be/1AP6gRQXqds "captura")
<p style="text-align: center;" target="_blank">Haga click </p>

## **Captura de resultado en:** _(C++)_
 1. Agregar un producto ![agregar_producto](/Capturas_C++/WhatsApp%20Image%202022-10-07%20at%209.33.51%20AM.jpeg)
 2. Salida del producto a txt ![salida_producto](/Capturas_C++/WhatsApp%20Image%202022-10-07%20at%209.34.19%20AM.jpeg)
 3. Buscar un producto ![buscar_producto](/Capturas_C++/WhatsApp%20Image%202022-10-07%20at%209.34.28%20AM.jpeg)
 4. Modificar un producto ![modificar_producto](/Capturas_C++/WhatsApp%20Image%202022-10-07%20at%209.34.38%20AM.jpeg)

