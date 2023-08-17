from math import pi, sqrt, pow, hypot


def test_filter():
    numbers = [1, 2, 3, 4, 5]
    result = list(filter(lambda n: n > 3, numbers))
    assert result == [4, 5]


def test_map():

    # Тестируем функцию, которая возводит числа в квадрат
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x ** 2, numbers))

    expected_result = [1, 4, 9, 16, 25]
    assert squared_numbers == expected_result

    # Тестируем функцию, которая преобразует числа в строки
    numbers = [10, 20, 30, 40, 50]
    string_numbers = list(map(str, numbers))

    expected_result = ['10', '20', '30', '40', '50']
    assert string_numbers == expected_result

    # Тестируем функцию, которая возвращает длину строк
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    word_lengths = list(map(len, words))

    expected_result = [5, 6, 6, 4, 10]
    assert word_lengths == expected_result

def test_sorted():
    lst = [3, 4, 2, 5, 1]
    result = sorted(lst)
    assert result == [1, 2, 3, 4, 5]


def test_pi():
    assert pi == 3.141592653589793


def test_sqrt():
    result = sqrt(4)
    assert result == 2.0


def test_pow_positive_exponent():
    result = pow(2, 3)
    assert result == 8.0


def test_pow_negative_exponent():
    result = pow(3, -2)
    assert result == 1 / 9


def test_pow_zero_exponent():
    result = pow(4, 0)
    assert result == 1.0


def test_hypot_positive_values():
    result = hypot(3, 4)
    assert result == 5.0


def test_hypot_negative_values():
    result = hypot(-3, -4)
    assert result == 5.0


def test_hypot_zero_values():
    result = hypot(0, 0)
    assert result == 0.0
