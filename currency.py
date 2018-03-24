# -*- coding: utf-8 -*-

class Money():

    def __init__(self, amount=0, currency="RUR"):
        self._amount = amount
        self._currency = currency

    def __eq__(self, money):
        return self._amount == money._amount and self._currency == money._currency
        
    def __ne__(self, money):
        return self._amount != money._amount or self._currency != money._currency
    
    def __add__(self, money):
        return Money(self._amount + money._amount, self._currency)
    
    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def eur(amount):
        return Money(amount, "EUR")

    def currency(self):
        return self._currency

    def __str__(self):
        return '{} {}'.format(self._currency, self._amount)

    def mult(self, multiplier):
        return Money(self._amount * multiplier, self._currency)
    
