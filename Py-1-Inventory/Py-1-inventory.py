# -*- coding: latin-1 -*-




# class Inventory
# Attributes about id, stocks, prices
# Methods like add item, update item, check item, delete item
# Dictionary to store the items details, key as item id and value is a dictionary containing the items details

#Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods 
# like add_item, update_item, and check_item_details. Use a dictionary to store the item details, where the key 
# is the item_id and the value is a dictionary containing the item_name, stock_count, and price.

import string
import time


class Inventory:
    def __init__(self,name,id1):
        self.nameInventory=name
        self.idInventory=id1
        #self.__inventory={"0001":{"item_name":"val"}}
        self.__inventory={"0001":{"item_id":"0001","item_name":"Car","item_stock":163,"item_price":12.20}}
        self.__idVal=len(self.__inventory)
        
    def verfItem(self,item):
        if item in self.__inventory:
            if self.__inventory[item]=="deleted": return [-1]
            else: return [1,item]
        for key in self.__inventory:
            if(self.__inventory[key]!="deleted" and self.__inventory[key]["item_name"]==item):
                return [2,key]
        
        return [0]
    def addItem(self,name,stock,price):
        self.__idVal+=1
        key=f"{self.__idVal:04}"
        self.__inventory[key]={"item_id":key, "item_name": name, "item_stock": stock, "item_price" : price}
        return 
   
    def updItem(self,item_id,name,stock,price):
        if name==None: name=self.__inventory[item_id]["item_name"]
        if stock==None: stock=self.__inventory[item_id]["item_stock"]
        if price==None: price=self.__inventory[item_id]["item_price"]
        self.__inventory[item_id]={"item_id":item_id, "item_name": name, "item_stock": stock, "item_price" : price}
        return 0

    def checkItem(self,item_id):
        return self.__inventory[item_id]

    def checkInventory(self):
        return self.__inventory
    
    def delItem(self,item_id):
        self.__inventory[item_id]="deleted"
    


dicInv={}   
def run(): pass
def menu(arg):
    print("-----------------------------------------------------")
    print("Seleccione la opción deseada ingresando su numero    ")
    print("-----------------------------------------------------")
    print("1. Añadir un item                                    ")
    print("2. Actualizar un item                                ")
    print("3. Consultar detalles de un item                     ")
    print("4. Eliminar item                                     ")
    print("5. Ver inventario completo                           ")
    print("0. Cerrar programa                                   ")
    print("-----------------------------------------------------")
    
    val=input("\n")
    if(val.isdigit() and int(val)>=0 and int(val)<=5):
        return options(arg,[int(val),1,1,1,1,1])
    options(op=[-1])
    return menu(arg)

def options(arg=0,op=[0,1,1,1,1,1],list0=[0,0,0,0]):
    if(op[0]==-1):
        print("-----------------------------------------------------")
        print("\nEntrada no válida")
        print("-----------------------------------------------------")
        time.sleep(1)
        return 0
    elif(op[0]==-2):
        print("-----------------------------------------------------")
        print("\nEl item ha sido eliminado")
        print("-----------------------------------------------------")
        time.sleep(1)
        return 0
        
    elif(op[0]==0):
        print("-----------------------------------------------------")
        print("Finalizando programa...                              ")
        print("-----------------------------------------------------")
        time.sleep(1)
        return 0
    elif(op[0]==1):
        if(op[1]==1):
            print("-----------------------------------------------------")
            print(f"Añadiendo item de Id: {(len(arg.checkInventory())+1):04}")
            print("-----------------------------------------------------")
            print("\nIngrese el nombre:")
            print("-----------------------------------------------------")
            list0[0]=input("\n")
        if(op[2]==1):
            print("-----------------------------------------------------")
            print("Ingrese el stock:")
            print("-----------------------------------------------------")
            list0[1]=input("\n")
            if not list0[1].isdigit():
                options(op=[-1])
                op[0],op[1]=1,0
                return options(arg,op,list0)
        if(op[3]==1):
            print("-----------------------------------------------------")
            print("Ingrese el precio:")
            print("-----------------------------------------------------")
            list0[2]=input("\n")
            try:
                float(list0[2])
            except:
                options(op=[-1])
                op[0],op[1],op[2]=1,0,0
                return options(arg,op,list0)
        arg.addItem(list0[0],list0[1],list0[2])
        print("-----------------------------------------------------")
        print("Producto agregado:")
        print(f"Id      : {(len(arg.checkInventory())):04}")
        print(f"Nombre  : {list0[0]}")
        print(f"Stock   : {list0[1]}")
        print(f"Precio  : {list0[2]}")
        print("-----------------------------------------------------")
        time.sleep(2)
        return menu(arg)

    elif(op[0]==2):
            if(op[1]==1):

                print("-----------------------------------------------------")
                print("Ingrese el Id o el nombre del producto a continuación:")
                print("-----------------------------------------------------")
                print("\n")
                list0[0]=arg.verfItem(input())
                if(list0[0]==[-1]):
                    options(op=[-2])
                    op[0]=2
                    return options(arg,op)
                elif(list0[0]==[0]):
                    options(op=[-1])
                    op[0]=2
                    return options(arg,op)
                else:
                    list0[0]=list0[0][1]
                    val=arg.checkItem(list0[0])
                    print("-----------------------------------------------------")
                    print("Detalles de producto:")
                    print(f"Id      :{val['item_id']}")
                    print(f"Nombre  :{val['item_name']}")
                    print(f"Stock   :{val['item_stock']}")
                    print(f"Precio  :{val['item_price']}")
                    print("-----------------------------------------------------")
                    print("\n")
                    time.sleep(1)
            val=arg.checkItem(list0[0])
            if(op[2]==1):
                print("-----------------------------------------------------")
                print("Ingrese el nuevo nombre del producto:")
                print(f"Nombre actual: {val['item_name']}")
                print('\n\nSi desea conservar el actual, escriba "none"')
                print("-----------------------------------------------------")
                print("\n")
                list0[1]=input()
                if list0[1]=="none": 
                    list0[1]==None
            if(op[3]==1):
                print("-----------------------------------------------------")
                print("Ingrese el nuevo stock del producto:")
                print(f"Stock actual: {val['item_stock']}")
                print('\n\nSi desea conservar el actual, escriba "none"')
                print("-----------------------------------------------------")
                print("\n")
                list0[2]=input()
                if list0[2]=="none": 
                    list0[2]==None
                elif not list0[2].isdigit():
                    options(op=[-1])
                    op[0],op[1],op[2]=2,0,0
                    return options(arg,op,list0)
            if(op[4]==1):
                print("-----------------------------------------------------")
                print("Ingrese el nuevo precio del producto:")
                print(f"Precio actual: {val['item_price']}")
                print('\n\nSi desea conservar el actual, escriba "none"')
                print("-----------------------------------------------------")
                print("\n")
                list0[3]=input()
                if list0[3]=="none": list0[3]==None
                else: 
                    try:
                        float(list0[3])
                    except:
                        options(op=[-1])
                        op[0],op[1],op[2],op[3]=2,0,0,0
                        return options(arg,op,list0)
            arg.updItem(list0[0],list0[1],list0[2],list0[3])
            print("-----------------------------------------------------")
            print("Producto cambiado")
            print("\n\nAntiguos valores:")
            print(f"Id      :{val['item_id']}")
            print(f"Nombre  :{val['item_name']}")
            print(f"Stock   :{val['item_stock']}")
            print(f"Precio  :{val['item_price']}")
            val=arg.checkItem(list0[0])
            print("\n\nNuevos valores:")
            print(f"Id      :{val['item_id']}")
            print(f"Nombre  :{val['item_name']}")
            print(f"Stock   :{val['item_stock']}")
            print(f"Precio  :{val['item_price']}")
            print("-----------------------------------------------------")
            time.sleep(2)
            return menu(arg)
    elif(op[0]==3):
        print("-----------------------------------------------------")
        print("Ingrese el Id o el nombre del producto a continuación:")
        print("-----------------------------------------------------")
        print("\n")
        list0[0]=arg.verfItem(input())
        if(list0[0]==[-1]):
            options(op=[-2])
            op[0]=3
            return options(arg,op)
        elif(list0[0]==[0]):
            options(op=[-1])
            op[0]=3
            return options(arg,op)
        else:
            list0[0]=list0[0][1]
            val=arg.checkItem(list0[0])
            print("-----------------------------------------------------")
            print("Detalles de producto:")
            print(f"Id      :{val['item_id']}")
            print(f"Nombre  :{val['item_name']}")
            print(f"Stock   :{val['item_stock']}")
            print(f"Precio  :{val['item_price']}")
            print("-----------------------------------------------------")
            print("\n")
        time.sleep(2)
        return menu(arg)
    elif(op[0]==4):
        if(op[1]==1):
            print("-----------------------------------------------------")
            print("Ingrese el Id o el nombre del producto a continuación:")
            print("-----------------------------------------------------")
            print("\n")
            list0[0]=arg.verfItem(input())
            if(list0[0]==[-1]):
                options(op=[-2])
                op[0]=4
                return options(arg,op)
            elif(list0[0]==[0]):
                options(op=[-1])
                op[0]=4
                return options(arg,op)
            else:
                list0[0]=list0[0][1]
                val=arg.checkItem(list0[0])
                print("-----------------------------------------------------")
                print("Detalles de producto:")
                print(f"Id      :{val['item_id']}")
                print(f"Nombre  :{val['item_name']}")
                print(f"Stock   :{val['item_stock']}")
                print(f"Precio  :{val['item_price']}")
                print("-----------------------------------------------------")
                print("\n")
        if(op[2]==1):
            print("-----------------------------------------------------")
            print("¿Desea eliminar?")
            print('\nEscribir "S/N"')
            print("-----------------------------------------------------")
            val=input("\n")
            if val=="S":
                arg.delItem(list0[0])
                print("-----------------------------------------------------")
                print("Producto eliminado")
                print("-----------------------------------------------------")
            elif val!="N":
                options(op=[-1])
                op[0],op[1]=4,0
                return options(arg,op,list0)
            time.sleep(2)
            return menu(arg)
    elif(op==5):
        inv=arg.checkInventory()
        if len(inv)==0:
            print("-----------------------------------------------------")
            print("        El inventario no tiene ningún producto       ")
            print("-----------------------------------------------------")
            return menu(arg)
        print("-----------------------------------------------------------------")
        print("                     Consulta de inventario  ")
        print(f"Nombre  : {arg.nameInventory}")
        print(f"Id      : {arg.idInventory}")
        print("-----------------------------------------------------------------")
        print("\tIdentificador\t|\tNombre\t\t|\tStock\t|\tPrecio")
               
            
def run(stat,arg):
    print("-----------------------------------------------------")
    print("Iniciando programa...                                ")
    print("-----------------------------------------------------")
    time.sleep(1)
    if(stat==0):
        if arg in dicInv: 
            return menu(dicInv[arg])
        else:
            return print("El id no corresponde a ningún inventario")
    else:
        for i in dicInv:
            if dicInv[i].nameInventory==arg:
                return menu(dicInv[i])
        return print("El nombre no corresponde a ningún inventario")


def addInventory(nameInventory):
    idInventory=f"{(len(dicInv)+1):04}"
    dicInv[idInventory]=Inventory(nameInventory,idInventory)

def showInventories():
    for key in dicInv:
        
        print(f"Id:{key}  -  Nombre: {dicInv[key].nameInventory}")


        
addInventory("shopInv")

run(1,"shopInv")




#Arreglar codigo
#def calcular_tamaño_distancia_longitud_maxima(longitud_maxima, multiplo=5, minimo=10):
#    tamaño_distancia = min(minimo, ((longitud_maxima + multiplo - 1) // multiplo) * multiplo)
#    return tamaño_distancia

#productos = [
#    {"identificador": 1, "precio": 10.99, "stock": 50, "descripcion": "Este es un", "nombre": "Producto A"},
#    {"identificador": 2, "precio": 5.99, "stock": 20, "descripcion": "Producto ABC", "nombre": "Producto B"},
#]

## Calcular la longitud máxima de cada columna
#longitud_maxima = {}
#for producto in productos:
#    for columna, valor in producto.items():
#        longitud_valor = len(str(valor))
#        longitud_maxima[columna] = calcular_tamaño_distancia_longitud_maxima(max(longitud_maxima.get(columna, 0), longitud_valor))


#print (longitud_maxima)
#print('{:colId} {:<colPrice} {:<colStock} {:<colDesc} {:<colName}'.format("ID", "Precio", "Stock", "Descripción", "Nombre",colId=longitud_maxima["identificador"],))
#print("="*70)

#for producto in productos:
#    print("{:<5} {:<10.2f} {:<8} {:<20} {:<20}".format(
#        producto["identificador"], producto["precio"], producto["stock"], producto["descripcion"], producto["nombre"]))

#ver chatgpt conversacion


##############################################################################################################################
#Codigo mejorado
#def calcular_tamaño_distancia_longitud_maxima(longitud_maxima, multiplo=5, minimo=10):
#    tamaño_distancia = max(minimo, ((longitud_maxima + multiplo - 1) // multiplo) * multiplo)
#    return tamaño_distancia

#productos = [
#    {"identificador": 1, "precio": 10.99, "stock": 50, "descripcion": "Este es un", "nombre": "Producto A"},
#    {"identificador": 2, "precio": 5.99, "stock": 20, "descripcion": "Producto ABC", "nombre": "Producto B"},
#]

# Calcular la longitud máxima de cada columna
#longitud_maxima = {}
#for producto in productos:
#    for columna, valor in producto.items():
#        longitud_valor = len(str(valor))
#        longitud_maxima[columna] = calcular_tamaño_distancia_longitud_maxima(max(longitud_maxima.get(columna, 0), longitud_valor))

#print (longitud_maxima)
#print('{:<{colId}} {:^{colPrice}} {:^{colStock}} {:^{colDesc}} {:^{colName}}'.format(
#    "ID", "Precio", "Stock", "Descripción", "Nombre",
#    colId=6,
#    colPrice=longitud_maxima["precio"],
#    colStock=longitud_maxima["stock"],
#    colDesc=longitud_maxima["descripcion"],
#    colName=longitud_maxima["nombre"]
#))
#print("=" * sum(longitud_maxima.values()))

#for producto in productos:
#    print('{:<{colId}} {:>{colPrice}.2f} {:>{colStock}} {:<{colDesc}} {:<{colName}}'.format(
#        producto["identificador"], producto["precio"], producto["stock"], producto["descripcion"], producto["nombre"],
#        colId=6,
#        colPrice=longitud_maxima["precio"],
#        colStock=longitud_maxima["stock"],
#        colDesc=longitud_maxima["descripcion"],
#        colName=longitud_maxima["nombre"]
#    ))
