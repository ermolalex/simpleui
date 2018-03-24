# -*- coding: utf-8 -*-

class Money():

    def __init__(self,amount):
        self._amount = amount

    def __eq__(self, money):
        return self._amount == money._amount and self.__class__ == money.__class__
        
    def __ne__(self, money):
        return self._amount != money._amount or self.__class__ != money.__class__
    
    def dollar(self, amount):
        return Dollar(amount)

class Dollar(Money):

    def mult(self, multiplier):
        return Dollar(self._amount * multiplier)
        
     
class Eur(Money):

    def mult(self, multiplier):
        return Eur(self._amount * multiplier)
        
"""    def __eq__(self, dollar2):
        return self._amount == dollar2._amount
        
    def __ne__(self, dollar2):
        return self._amount != dollar2._amount                
"""        