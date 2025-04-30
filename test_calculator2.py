import pytest
from calculator import add, subtract, multiply, divide

# 1. Юніт-тестування
def test_add():
    assert add(2, 3) == 5
def test_subtract():
    assert subtract(5, 3) == 2
def test_multiply():
    assert multiply(2, 3) == 6
def test_divide():
    assert divide(6, 2) == 3

# 2. Тест на крайні значення
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
def test_large_numbers():
    assert add(1000000000, 2000000000) == 3000000000

# 3. Інтеграційне тестування 
def test_calculate_whole_logic():
    assert add(10, 5) == 15
    assert subtract(20, 10) == 10
    assert multiply(4, 3) == 12
    assert divide(12, 4) == 3

# 4. Тестування на помилки вводу
def test_invalid_input_type():
    with pytest.raises(TypeError):
        add("a", 2)

