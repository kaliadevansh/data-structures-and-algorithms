"""
This module exposes a insertShiftArray function that inserts element at middle of an array.
"""


def insertShiftArray(array, value_to_add):
    """
    Insert element to middle of the array.
    :param array: array to insert the element to.
    :param value_to_add: value to insert into the array.
    :return: array with element inserted into the middle.
    """
    if array is None or value_to_add is None:
        raise TypeError
    elif not isinstance(array, list):
        raise TypeError
    elif not isinstance(value_to_add, int):
        raise TypeError

    array_length = len(array)

    if array_length == 0:
        array.append(value_to_add)
    else:
        array_mid = ceiling(array_length / 2)
        array.append("")

        for index in range(array_length, array_mid - 1, -1):
            if index == array_mid:
                array[index] = value_to_add
            else:
                array[index] = array[index - 1]

    return array


def remove_shift_array(array):
    """
    Removes the middle element from an array and returns the rest of the array.
    :param array: Array form which the middle element is to be removed.
    :return: array with removed middle element.
    """
    if array is None:
        raise TypeError

    array_length = len(array)

    if not isinstance(array, list):
        raise TypeError
    elif array_length == 0:
        raise ValueError
    elif array_length == 1:
        return []
    else:
        array_mid = ceiling(array_length / 2)
        for index in range(array_mid - 1, array_length - 1, 1):
            array[index] = array[index + 1]
            if index == array_length - 2:
                array.pop()
        return array


def ceiling(input_number):
    """
    This function is local implementation of ceiling function just for the scope of this problem.
    This method was created to satisfy the ask of not using in-built language functions.
    :param input_number: Number whose ceiling value is to be calculated..
    :return: Floor value of input number.
    """
    decimal_digits = 1 - input_number % 1
    if decimal_digits != 1:
        return int(input_number + decimal_digits)
    else:
        return int(input_number)
