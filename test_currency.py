# -*- coding: utf-8 -*-

import pytest
from currency import Money

"""
$5 * 2 = $10
$5 + 60rub = $6  при курсе 60р/$
"""

def test_mult():
    assert Money.dollar(5).mult(2) == Money.dollar(10)
    assert Money.dollar(5).mult(3) == Money.dollar(15)
    
def test_equality():
    assert Money.dollar(5) == Money.dollar(5)
    assert Money.dollar(6) != Money.dollar(5)
    assert not Money.dollar(6) == Money.eur(6)    
    assert Money.dollar(6) != Money.eur(6)    

   
def test_currency():
    assert "EUR" == Money.eur(1).currency()
    assert "USD" == Money.dollar(1).currency()

def test_simple_add():
    assert (Money.dollar(5) + Money.dollar(3)) == Money.dollar(8)
    
