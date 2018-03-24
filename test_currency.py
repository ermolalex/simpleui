# -*- coding: utf-8 -*-

import pytest
from currency import Money, Dollar, Eur

"""
$5 * 2 = $10
$5 + 60rub = $6  при курсе 60р/$
"""

def test_mult():
    five = Money.dollar(5,5)
    assert five.mult(2) == Dollar(10)
    assert five.mult(3) == Dollar(15)
    
def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(6) != Dollar(5)
    assert Eur(5) == Eur(5)
    assert Eur(6) != Eur(5)    
    assert not Dollar(6) == Eur(6)    
    assert Dollar(6) != Eur(6)    

    
def test_eur_mult():
    five = Eur(5)
    assert five.mult(2) == Eur(10)
    assert five.mult(3) == Eur(15)
    
