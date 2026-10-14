import pytest
from calculator import add, subtract, multiply
def main():
    test_add_positive()
    test_add_negative()
    test_add_zero()

def test_add_positive(): 
    assert add(2, 3) == 5

def test_add_negative(): 
    assert add(-2, -4) == -6

def test_add_zero(): 
    assert add(0, 0) == 0  

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(2, 2) == 0

def test_str():
    with pytest.raises(TypeError):
        multiply("dog")

if __name__ == "__main__":
    main()
