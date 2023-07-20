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
        self.__inventory={}
        self.__idVal=0
        
    def verfItem(self,item):
        if item in self.__inventory:
            if self.__inventory[item]=="deleted": return [-1]
            else: return [1,item]
        for key in self.__inventory:
            if(self.__inventory[key]!="deleted" and self.__inventory[key]["item_name"==item]):
                return [2,item]
        
        return [0]
    def addItem(self,name,stock,price):
        self.__idVal+=1
        self.__inventory[self.__idVal]={"item_id":f"{self.__idVal:04}", "item_name": name, "stock_count": stock, "item_price" : price}
        return 0
   
    def updItem(self,item_id,name,stock,price):
        if name==None: name=self.__inventory[item_id]["item_name"]
        if stock==None: stock=self.__inventory[item_id]["stock_count"]
        if price==None: price=self.__inventory[item_id]["item_price"]
        self.__inventory[item_id]={"item_id":f"{self.__idVal:04}", "item_name": name, "stock_count": stock, "item_price" : price}
        return 0

    def checkItem(self,item_id):
        return self.__inventory[item_id]

    def checkInventory(self):
        return self.__inventory
    
    def delItem(self,item_id):
        self.__inventory[item_id]="deleted"
    


dicInv={}

def run():
    pass
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
    if(val.isdigit()):
        val=int(val)
        if(val>=0 and val<=5):
            return options(arg,val)
    options(op0=-1)
    return menu(arg)

def options(arg=0,op0=0,op1=1,op2=1,op3=1,list0=[0,0,0]):
    if(op0==-1):
        print("-----------------------------------------------------")
        print("\nEntrada no válida")
        print("-----------------------------------------------------")
        time.sleep(1)
    elif(op0==-2):
        print("-----------------------------------------------------")
        print("\nEl item ha sido eliminado")
        print("-----------------------------------------------------")
        time.sleep(1)
        
    elif(op0==0):
        print("-----------------------------------------------------")
        print("Finalizando programa...                              ")
        print("-----------------------------------------------------")
        time.sleep(1)
    elif(op0==1):
        if(op1==1):
            print("-----------------------------------------------------")
            print(f"Añadiendo item de Id: {(len(arg.checkInventory())+1):04}")
            print("-----------------------------------------------------")
            print("\nIngrese el nombre:")
            print("-----------------------------------------------------")
            list0[0]=input("\n")
            if not isinstance(list0[0],str): 
                options(op0=-1)
                return options(arg,1)
        if(op2==1):
            print("-----------------------------------------------------")
            print("Ingrese el stock:")
            print("-----------------------------------------------------")
            list0[1]=input("\n")
            if not list0[1].isdigit(): 
                options(op0=-1)
                return options(arg,1,0,list0=list0)
        if(op3==1):
            print("-----------------------------------------------------")
            print("Ingrese el precio:")
            print("-----------------------------------------------------")
            list0[2]=input("\n")
            try:
                float(list0[2])
            except:
                options(op0=-1)
                return options(arg,1,0,0,list0=list0)
        arg.addItem(list0[0],list0[1],list0[2])

    elif(op0==2):
            print("-----------------------------------------------------")
            print("Ingrese el Id o el nombre del producto a continuación:")
            print("-----------------------------------------------------")
            print("\n")
            val=arg.verfItem(input())
            if(val[0]==-1):
                print("-----------------------------------------------------")
                print("El producto ha sido eliminado:")
                print("-----------------------------------------------------")
                print("\n")
            elif(val[0]):
                pass

            


    else:
        options(op0=-1)
                


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