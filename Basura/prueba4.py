import csv
#import pandas as pd
#import seaborn as sb
#import matplotlib.pyplot as plt

def menu():
    print("******MENU INVENTARIO******")
    print("1.  Ver invetario ------------------ 2.  Producto Nuevo")
    print("3.  Modificar Producto ------------- 4.  Eliminar Producto")
    print("5.  Buscar Producto por Código------ 6.  Filtrar Producto por Nombre")
    print("7.  Ingresar Producto -------------- 8.  Salida de Producto")
    print("9.  Ajuste por Perdida de Producto-- 10. Reporte Stock Mínimo")
    print("11. Reporte Invetario Total--------- 12. Reporte Invetario Parcial")
    print("13. Rellenar espacios vacio--------- 14. Salir")
    option=input("Introduzca el número de la opción deseada: ")
    return option

def ExisteCodigo(codigo):
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if(codigo==row['codigo']):
                return row
        return "No existe"

def VerInventario():
    #with open('Inventario.csv')as File:
        #reader=csv.DictReader(File)
        #contador=0
        #for row in reader:
            #print('' + str(row['codigo'])+'\t' + str(row['restrictiva'])+'\t' + str(row['ubicacion'])+'\t' 
            #+ str(row['descripcion'])+'\t' + str(row['unidad'])+'\t'+ str(row['tipo'])
            #+'\t' + str(row['familia'])+'\t' + str(row['stock_minimo'])+'\t' + str(row['cantidad_inicial'])
            #+'\t' + str(row['ingresos'])+'\t' + str(row['egresos'])+'\t' + str(row['perdidas'])
            #+'\t' + str(row['total'])+'\t' + str(row['observaciones'])+'\t' + str(row['observacion_perdida']))
            #contador=contador+1
        #print('****Total Filas('+str(contador)+')')
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df)




def ProductoNuevo():
    codigo = input('Ingrese codigo de producto nuevo: ')
    if ExisteCodigo(codigo)=="No existe":
        ubicacion=input('Ingrese ubicación: ')
        descripcion=input('Ingrese descripción: ')
        unidad=input('Ingrese unidad de medida: ')
        tipo=input('Ingrese tipo: ')
        familia=input('Ingrese familia: ')
        stock_minimo=input('Ingese stock minimo: ')
        cantidad_inicial=input('Ingrese cantidad inicial: ')
        ingresos="0"
        egresos="0"
        perdidas="0"
        total="0"
        observaciones="Vacio"
        observaciones_perdida="Vacio"
        restrictiva="N"
        with open ('Inventario.csv','a')as File:
            File.write('\n'+codigo+','+restrictiva+','+ubicacion+','+descripcion+','
            +unidad+','+tipo+','+familia+','+stock_minimo+','+cantidad_inicial+','+ingresos
            +','+egresos+','+perdidas+','+total+','+observaciones+','+observaciones_perdida)
    else:
        print("****Error el codigo ya existe****")

def ModificarProducto():
    codigo=input('Ingrese codigo modificar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea modificar no existe----')
    else:
        ubicacion=input('Ingrese ubicacion: ')
        descripcion=input('Ingrese descripción: ')
        unidad=input('Ingrese unidad: ')
        tipo=input('Ingrese tipo: ')
        familia=input('Ingrese familia: ')
        modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia)

def modificarBDD(codigo,ubicacion,descripcion,unidad,tipo,familia):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=codigo
                row['restrictiva']=row['restrictiva']
                row['ubicacion']=ubicacion
                row['descripcion']=descripcion
                row['unidad']=unidad
                row['tipo']=tipo
                row['familia']=familia
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                row['ingresos']=row['ingresos']
                row['egresos']=row['egresos']
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)
        
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
        #writer = csv.DictWriter(csvfile, fieldnames=["Bio_Id","Last_Name","First_Name","late","undertime","total_minutes", "total_ot", "total_nsd", "total_absences"], 
         #               extrasaction='ignore', delimiter = ';')

def EliminarProducto():
    codigo=input('Ingrese codigo a eliminar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        eleccion=input('Si esta seguro si=S no=N? ')
        if eleccion=='S':
            EstadoElimandoBDD(codigo) 

def EstadoElimandoBDD(codigo):
    result=[]
    contraseña=str(input('Ingrese contraseña: '))
    if contraseña =="1324":
        with open('Inventario.csv')as File:
            reader=csv.DictReader(File)
            estado="S"
            for row in reader:
                if row['codigo']==codigo:
                    row['codigo']=row['codigo']
                    row['restrictiva']=estado
                    row['ubicacion']=row['ubicacion']
                    row['descripcion']=row['descripcion']
                    row['unidad']=row['unidad']
                    row['tipo']=row['tipo']
                    row['familia']=row['familia']
                    row['stock_minimo']=row['stock_minimo']
                    row['cantidad_inicial']=row['cantidad_inicial']
                    row['ingresos']=row['ingresos']
                    row['egresos']=row['egresos']
                    row['perdidas']=row['perdidas']
                    row['total']=row['total']
                    row['observaciones']=row['observaciones']
                    row['observacion_perdida']=row['observacion_perdida']
                result.append(row)
        with open('Inventario.csv','w')as File:
            fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
            ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
            writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
            writer.writeheader()
            writer.writerows(result)
    else:
        print('Contraseña incorrecta')

def BuscarProducto():
    codigo=input('Ingrese codigo de producto a buscar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        BuscarBDD(codigo) 

def BuscarBDD(codigo):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            if row['codigo']==codigo:
                print('' + str(row['codigo'])+'\t' + str(row['restrictiva'])+'\t' + str(row['ubicacion'])+'\t' 
                + str(row['descripcion'])+'\t' + str(row['unidad'])+'\t'+ str(row['tipo'])
                +'\t' + str(row['familia'])+'\t' + str(row['stock_minimo'])+'\t' + str(row['cantidad_inicial'])
                +'\t' + str(row['ingresos'])+'\t' + str(row['egresos'])+'\t' + str(row['perdidas'])
                +'\t' + str(row['total'])+'\t' + str(row['observaciones'])+'\t' + str(row['observacion_perdida']))

def BuscarPorNombre():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    palabra=str(input('Ingrese el nombre a filtrar: '))
    print(df[df['descripcion'].str.contains(palabra)])

def IngresarProducto():
    codigo=input('Ingrese codigo de producto a ingresar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        IngresarProductoBDD(codigo) 

def IngresarProductoBDD(codigo):
    result=[]
    print('Datos del producto') 
    BuscarBDD(codigo)
    ingresos=input('Cantidad a ingresar a bodega: ')
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['restrictiva']=row['restrictiva']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['tipo']=row['tipo']
                row['familia']=row['familia']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                verificar=int(str(row['ingresos']))
                temp=int(str(ingresos))
                total_ingreso=0
                if verificar>0:
                    total_ingreso=verificar+temp
                    temp1=str(total_ingreso)
                    row['ingresos']=temp1
                else:
                    row['ingresos']=ingresos         
                row['egresos']=row['egresos']
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)    
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)
    
def SalidaDeProducto():
    codigo=input('Ingrese codigo de producto para darle salida: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        SalidaProductoBDD(codigo) 

def SalidaProductoBDD(codigo):
    result=[]
    print('Datos del producto') 
    BuscarBDD(codigo)
    egresos=input('Cantidad de salida de bodega: ')
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                row['restrictiva']=row['restrictiva']
                row['ubicacion']=row['ubicacion']
                row['descripcion']=row['descripcion']
                row['unidad']=row['unidad']
                row['tipo']=row['tipo']
                row['familia']=row['familia']
                row['stock_minimo']=row['stock_minimo']
                row['cantidad_inicial']=row['cantidad_inicial']
                row['ingresos']=row['ingresos']
                verificar=int(str(row['egresos']))
                temp=int(str(egresos))
                total_egresos=0
                if verificar>0:
                    total_egresos=verificar+temp
                    temp1=str(total_egresos)
                    row['egresos']=temp1
                else:
                    row['egresos']=egresos
                row['perdidas']=row['perdidas']
                a=int(str(row['cantidad_inicial']))
                b=int(str(row['ingresos']))
                c=int(str(row['egresos']))
                d=int(str(row['perdidas']))
                operacion=(a+b)-(c+d)
                total=int(str(operacion))
                stock=int(str(row['stock_minimo']))
                if total <= stock:
                    temp=str(total)
                    observaciones="Solicitar Material"
                    row['total']=temp
                    row['observaciones']=observaciones
                else:
                    observaciones="Stok a favor"
                    row['total']=total
                    row['observaciones']=observaciones
                row['observacion_perdida']=row['observacion_perdida']
            result.append(row)    
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)

def AjustePerdida():
    codigo=input('Ingrese codigo de producto perdido: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        AjustePerdidaBDD(codigo) 

def AjustePerdidaBDD(codigo):
    result=[]
    contraseña=str(input('Ingrese contraseña: '))
    if contraseña == "1324":    
        print('Datos del producto')
        BuscarBDD(codigo)
        perdidas=input('Cantidad de producto perdido: ')
        observacion_perdida=input('Escriba observación de perdida: ')
        with open('Inventario.csv')as File:
            reader=csv.DictReader(File)
            for row in reader:
                #Compara el codigo hasta encontrar lugar vacio
                if row['codigo']==codigo:
                    row['codigo']=row['codigo']
                    row['restrictiva']=row['restrictiva']
                    row['ubicacion']=row['ubicacion']
                    row['descripcion']=row['descripcion']
                    row['unidad']=row['unidad']
                    row['tipo']=row['tipo']
                    row['familia']=row['familia']
                    row['stock_minimo']=row['stock_minimo']
                    row['cantidad_inicial']=row['cantidad_inicial']
                    row['ingresos']=row['ingresos']
                    row['egresos']=row['egresos']
                    verificar=int(str(row['perdidas']))
                    temp=int(str(perdidas))
                    total_perdidas=0
                    if verificar>0:
                        total_perdidas=verificar+temp
                        temp1=str(total_perdidas)
                        row['perdidas']=temp1
                    else:
                        row['perdidas']=perdidas
                    a=int(str(row['cantidad_inicial']))
                    b=int(str(row['ingresos']))
                    c=int(str(row['egresos']))
                    d=int(str(row['perdidas']))
                    operacion=(a+b)-(c+d)
                    total=int(str(operacion))
                    stock=int(str(row['stock_minimo']))
                    if total <= stock:
                        temp=str(total)
                        observaciones="Solicitar Material"
                        row['total']=temp
                        row['observaciones']=observaciones
                    else:
                        observaciones="Stok a favor"
                        row['total']=total
                        row['observaciones']=observaciones
                    if row['observacion_perdida']=="Vacio":
                        row['observacion_perdida']=observacion_perdida
                    else:
                        row['observacion_perdida']=row['observacion_perdida']+","+observacion_perdida
                result.append(row)    
        with open('Inventario.csv','w')as File:
            fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
            ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
            writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
            writer.writeheader()
            writer.writerows(result)
    else:
        print('Contraseña incorrecta')

def ReporteStockMinimo():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df[df['observaciones'].str.contains("Solicitar Material")])

def ReporteInventarioTotal():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    ord=df.sort_values(by=['ubicacion'])[['ubicacion','tipo','familia']]
    print(ord)

def ReporteParcialStock():
    df=pd.read_csv(r'Inventario.csv',engine='python')
    print(df[df['observaciones'].str.contains("Stok a favor")])

def RellenarEspacios():
    codigo=input('Ingrese codigo de producto a rellenar: ')
    if ExisteCodigo(codigo)=="No existe":
        print('----Error el codigo que desea eliminar no existe----')
    else:
        RellenarEspaciosBDD(codigo) 

def RellenarEspaciosBDD(codigo):
    result=[]
    with open('Inventario.csv')as File:
        reader=csv.DictReader(File)
        restrictiva="N"
        ubicacion="Vacio"
        descripcion="Vacio"
        unidad="Vacio"
        tipo="Vacio"
        familia="Vacio"
        stock_minimo="0"
        cantidad_inicial="0"
        ingresos="0"
        egresos="0"
        perdidas="0"
        total="0"
        observaciones="Vacio"
        observaciones_perdida="Vacio"
        for row in reader:
            #Compara el codigo hasta encontrar lugar vacio
            if row['codigo']==codigo:
                row['codigo']=row['codigo']
                if row['restrictiva'] =="":
                    row['restrictiva']=restrictiva
                else:
                    row['restrictiva']=row['restrictiva']
                
                if row['ubicacion'] =="":
                    row['ubicacion']=ubicacion
                else:
                    row['ubicacion']=row['ubicacion']
                
                if row['descripcion']=="":
                    row['descripcion']=descripcion
                else:
                    row['descripcion']=row['descripcion']
                
                if row['unidad']=="":
                    row['unidad']=unidad
                else:
                    row['unidad']=row['unidad']
                
                if row['tipo']=="":
                    row['tipo']=tipo
                else: 
                    row['tipo']=row['tipo']
                
                if row['familia']=="":
                    row['familia']=familia
                else: 
                    row['familia']=row['familia']
                
                if row['stock_minimo']=="":
                    row['stock_minimo']=stock_minimo
                else:
                    row['stock_minimo']=row['stock_minimo']
                
                if row['cantidad_inicial']=="":
                    row['cantidad_inicial']=cantidad_inicial
                else:
                    row['cantidad_inicial']=row['cantidad_inicial']
                
                if row['ingresos']=="":
                    row['ingresos']=ingresos
                else: 
                    row['ingresos']
                
                if row['egresos']=="":
                    row['egresos']=egresos
                else:
                    row['egresos']=row['egresos']
                
                if row['perdidas']=="":
                    row['perdidas']=perdidas
                else: 
                    row['perdidas']=row['perdidas']
                
                if row['total']=="":
                    row['total']=total
                else:
                    row['total']=row['total']
                
                if row['observaciones']=="":
                    row['observaciones']=observaciones
                else:
                    row['observaciones']=row['observaciones']
                
                if row['observacion_perdida']=="":
                    row['observacion_perdida']=observaciones_perdida
                else: 
                    row['observacion_perdida']=row['observacion_perdida']
            result.append(row)
        
    with open('Inventario.csv','w')as File:
        fieldnames=['codigo','restrictiva','ubicacion','descripcion','unidad','tipo','familia','stock_minimo','cantidad_inicial'
        ,'ingresos','egresos','perdidas','total','observaciones','observacion_perdida']
        writer=csv.DictWriter(File,fieldnames=fieldnames,extrasaction='ignore')
        writer.writeheader()
        writer.writerows(result)


def main():
    while True:
        option=menu()
        if option == '1':
            VerInventario()
        elif option == '2':
            ProductoNuevo()
        elif option == '3':
            ModificarProducto()
        elif option == '4':
            EliminarProducto()
        elif option == '5':
            BuscarProducto()
        elif option == '6':
            BuscarPorNombre()
        elif option == '7':
            IngresarProducto()
        elif option == '8':
            SalidaDeProducto()
        elif option == '9':
            AjustePerdida()
        elif option == '10':
            ReporteStockMinimo()
        elif option == '11':
            ReporteInventarioTotal()
        elif option == '12':
            ReporteParcialStock()
        elif option == '13':
            RellenarEspacios()
        elif option == '14':
            break
    return

main()


