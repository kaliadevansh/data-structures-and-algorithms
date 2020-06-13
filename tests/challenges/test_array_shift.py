from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray, remove_shift_array

import pytest


# insert shift array tests

def test_insert_shift_array_none_none():
    with pytest.raises(TypeError):
        insertShiftArray(None, None)


def test_insert_shift_array_none_number():
    with pytest.raises(TypeError):
        insertShiftArray(None, 1)


def test_insert_shift_array_array_none():
    with pytest.raises(TypeError):
        insertShiftArray([], None)


def test_insert_shift_array_array_float():
    with pytest.raises(TypeError):
        insertShiftArray([], -1.0)


def test_insert_shift_array_string_string():
    with pytest.raises(TypeError):
        insertShiftArray("1", 1)


def test_insert_shift_array_array_string():
    with pytest.raises(TypeError):
        insertShiftArray([], "1")


def test_insert_shift_array_empty_array():
    actual = insertShiftArray([], 1)
    expected = [1]
    assert actual == expected


def test_insert_shift_array_one_element():
    actual = insertShiftArray([1], 5)
    expected = [1, 5]
    assert actual == expected


def test_insert_shift_array_odd_element():
    actual = insertShiftArray([1, 2, 3], 5)
    expected = [1, 2, 5, 3]
    assert actual == expected


def test_insert_shift_array_even_element():
    actual = insertShiftArray([1, 2], 5)
    expected = [1, 5, 2]
    assert actual == expected


def test_insert_shift_array_example1():
    actual = insertShiftArray([2, 4, 6, 8], 5)
    expected = [2, 4, 5, 6, 8]
    assert actual == expected


def test_insert_shift_array_example2():
    actual = insertShiftArray([4, 8, 15, 23, 42], 16)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# remove shift array tests
def test_remove_shift_array_none():
    with pytest.raises(TypeError):
        remove_shift_array(None)


def test_remove_shift_array_empty():
    with pytest.raises(ValueError):
        remove_shift_array([])


def test_remove_shift_array_string():
    with pytest.raises(ValueError):
        remove_shift_array([])


def test_remove_shift_array_number():
    with pytest.raises(TypeError):
        remove_shift_array(1)


def test_remove_shift_array_one_element():
    actual = remove_shift_array([1])
    expected = []
    assert actual == expected


def test_remove_shift_array_two_elements():
    actual = remove_shift_array([1, 2])
    expected = [2]
    assert actual == expected


def test_remove_shift_array_odd_elements():
    actual = remove_shift_array([1, 2, 3, 4, 5])
    expected = [1, 2, 4, 5]
    assert actual == expected


def test_remove_shift_array_even_elements():
    actual = remove_shift_array([1, 2, 3, 4])
    expected = [1, 3, 4]
    assert actual == expected


def test_remove_shift_array_example2():
    actual = remove_shift_array([4, 8, 15, 23, 42])
    expected = [4, 8, 23, 42]
    assert actual == expected
