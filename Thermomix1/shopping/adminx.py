'''
Created on 18 de nov. de 2015

@author: fjmora
'''
from shopping.model import ShoppingList
import xadmin

class ShoppingListAdmin(object):
    pass

xadmin.site.register(ShoppingList,ShoppingListAdmin)