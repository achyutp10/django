import testAdd
import pytest

def test_add():
    assert testAdd.add(4,5) == 9
def test_sub():
    assert testAdd.sub(4,5) == -1

# python -m pytest test.py --> for testing