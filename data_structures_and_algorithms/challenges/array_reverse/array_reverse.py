"""
Reverses input array/list in the order of insertion.
"""


def reverseArray(input_list):
    """
    Reverses the input array/list in the order of insertion.
    This method reverses the list by iterating half of the list and without using additional space.
    :param input_list: The list to be reversed. Returns None for None input.
    :return: The reversed list
    """
    if input_list is None or skip_reverse(input_list) is not None:
        return input_list

    list_length = len(input_list)
    counter = 0

    while counter < floor(list_length / 2):
        input_list[counter] += input_list[list_length - counter - 1]
        input_list[list_length - counter - 1] = input_list[counter] - input_list[list_length - counter - 1]
        input_list[counter] = input_list[counter] - input_list[list_length - counter - 1]
        counter += 1

    return input_list


def reverse_array_stack(input_list):
    """
    Reverses the input array/list in the order of insertion.
    This method reverses the list by using additional space of a stack and then popping elements from the stack.
    :param input_list: The list to be reversed. Returns None for None input.
    :return: The reversed list
    """
    if input_list is None or skip_reverse(input_list) is not None:
        return input_list

    stack = []

    for current_value in input_list:
        stack.append(current_value)

    reversed_list = []
    list_counter = len(stack)

    while list_counter > 0:
        reversed_list.append(stack.pop())
        list_counter -= 1

    return reversed_list


def reverse_array_iterate(input_list):
    """
    Reverses the input array/list in the order of insertion.
    This method reverses the list by iterating the input list in reverse.
    :param input_list: The list to be reversed. Returns None for None input.
    :return: The reversed list
    """
    if input_list is None or skip_reverse(input_list) is not None:
        return input_list

    reversed_list = []

    for current_value in input_list[::-1]:
        reversed_list.append(current_value)

    return reversed_list


def skip_reverse(input_list):
    """
    Checks if initialized input list has 0 or 1 elements, hence reverse operation can be skipped.
    :param input_list: The list to be checked for skipping reverse.
    :return: Input list if list has 0 or 1 elements; none otherwise.
    """
    list_length = len(input_list)

    if list_length == 0 or list_length == 1:
        return input_list


def floor(input_number):
    """
    This function is local implementation of floor function just for the scope of this problem.
    This method was created to satisfy the ask of not using in-built language functions.
    :param input_number: Number whose floor value is to be calculated..
    :return: Floor value of input number.
    """
    decimal_digits = input_number % 1
    return input_number - decimal_digits
