# class Inventory
# Attributes about id, stocks, prices
# Methods like add item, update item, check item, delete item
# Dictionary to store the items details, key as item id and value is a dictionary containing the items details

#Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods 
# like add_item, update_item, and check_item_details. Use a dictionary to store the item details, where the key 
# is the item_id and the value is a dictionary containing the item_name, stock_count, and price.

import time


class Inventory:
    def __init__(self):
        self.__inventory={}
        self.__idVal=0
        
#        self.inventory={001:001.dic{ item_id:000 , item_nam: "abcd" , stock_count: 0000 , item_price: 00.00  }}
#        self.itemDetail={}
    def verf_item(self,item_id):
        if item_id in self.__inventory : 
            if self.__inventory=="deleted" : return 2
            else: return 1
        else : return 0
    def add_item(self,name,stock,price):
        self.__idVal+=1
        self.__inventory[self.__idVal]={"item_id":self.__idVal, "item_name": name, "stock_count": stock, "item_price" : price}
        return 0
   
    def upd_item(self,item_id,name,stock,price):
        if name==None: name=self.__inventory[item_id]["item_name"]
        if stock==None: stock=self.__inventory[item_id]["stock_count"]
        if price==None: price=self.__inventory[item_id]["item_price"]
        self.__inventory[item_id]={"item_id":self.__idVal, "item_name": name, "stock_count": stock, "item_price" : price}
        return 0

    def check_item(self,item_id):
        return self.__inventory[item_id]
    
    def del_item(self,item_id):
        self.__inventory[item_id]="deleted"



def run():
    pass
def menu():
    print("-----------------------------------------------------")
    print("Programado                                           ")
    print("-----------------------------------------------------")
def opciones():
    pass


def run():
    print("-----------------------------------------------------")
    print("Iniciando programa...                                ")
    print("-----------------------------------------------------")
    time.sleep(1)
    menu()

    
    print("                                                     ")


run()
