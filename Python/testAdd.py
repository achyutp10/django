# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a - b

from curses.ascii import isdigit
import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent('Al')
def test_nodigit():
    assert findstring.nodigit('N7')
    