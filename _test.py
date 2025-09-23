import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5


def test_square():
    assert square(2)==4, print("Error")
    assert square(3) == 9,print("Error")

# Testing the cube function
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Testing the fifth power function
def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: Fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed: Fifth power of 3 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")