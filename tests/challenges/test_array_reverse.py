from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverseArray
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverse_array_stack
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import reverse_array_iterate
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import skip_reverse
from data_structures_and_algorithms.challenges.array_reverse.array_reverse import floor


# Tests for index manipulation method
def test_empty_list():
    input_list = []
    reversed_list = reverseArray(input_list)
    assert reversed_list == []


def test_none_list():
    input_list = None
    reversed_list = reverseArray(input_list)
    assert reversed_list is None


def test_negative_numbers():
    input_list = [-1, -2]
    reversed_list = reverseArray(input_list)
    assert reversed_list == [-2, -1]


def test_even_number_elements():
    input_list = [1, 2, 3, 4]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [4, 3, 2, 1]


def test_odd_number_elements():
    input_list = [-1, -2, -3, -4, -5]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [-5, -4, -3, -2, -1]


def test_list_size_1():
    input_list = [1]
    reversed_list = reverseArray(input_list)
    assert reversed_list == [1]


def test_example1():
    input_list = [1, 2, 3, 4, 5, 6]
    reversed_list = reverseArray(input_list)
    assert reversed_list == [6, 5, 4, 3, 2, 1]


def test_example2():
    input_list = [89, 2354, 3546, 23, 10, -923, 823, -12]
    reversed_list = reverseArray(input_list)
    assert reversed_list == [-12, 823, -923, 10, 23, 3546, 2354, 89]


def test_example3():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    reversed_list = reverseArray(input_list)
    assert reversed_list == [199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109,
                             107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17,
                             13, 11, 7, 5, 3, 2]


# Tests for stack method
def test_empty_list_reverse_array_stack():
    input_list = []
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == []


def test_none_list_reverse_array_stack():
    input_list = None
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list is None


def test_negative_numbers_reverse_array_stack():
    input_list = [-1, -2]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [-2, -1]


def test_even_number_elements_reverse_array_stack():
    input_list = [1, 2, 3, 4]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [4, 3, 2, 1]


def test_odd_number_elements_reverse_array_stack():
    input_list = [1, 2, 3]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [3, 2, 1]


def test_list_size_1_reverse_array_stack():
    input_list = [1]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [1]


def test_example1_reverse_array_stack():
    input_list = [1, 2, 3, 4, 5, 6]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [6, 5, 4, 3, 2, 1]


def test_example2_reverse_array_stack():
    input_list = [89, 2354, 3546, 23, 10, -923, 823, -12]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [-12, 823, -923, 10, 23, 3546, 2354, 89]


def test_example3_reverse_array_stack():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    reversed_list = reverse_array_stack(input_list)
    assert reversed_list == [199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109,
                             107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17,
                             13, 11, 7, 5, 3, 2]


# Tests for iterate method
def test_empty_list_reverse_array_iterate():
    input_list = []
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == []


def test_none_list_reverse_array_iterate():
    input_list = None
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list is None


def test_negative_numbers_reverse_array_iterate():
    input_list = [-1, -2]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [-2, -1]


def test_even_number_elements_reverse_array_iterate():
    input_list = [1, 2, 3, 4]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [4, 3, 2, 1]


def test_odd_number_elements_reverse_array_iterate():
    input_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [5, 4, 3, 2, 1]


def test_list_size_1_reverse_array_iterate():
    input_list = [1]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [1]


def test_example1_reverse_array_iterate():
    input_list = [1, 2, 3, 4, 5, 6]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [6, 5, 4, 3, 2, 1]


def test_example2_reverse_array_iterate():
    input_list = [89, 2354, 3546, 23, 10, -923, 823, -12]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [-12, 823, -923, 10, 23, 3546, 2354, 89]


def test_example3_reverse_array_iterate():
    input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    reversed_list = reverse_array_iterate(input_list)
    assert reversed_list == [199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109,
                             107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17,
                             13, 11, 7, 5, 3, 2]


# Tests for helper methods
def test_skip_reverse_empty_input():
    assert skip_reverse([]) == []


def test_floor_whole_number_0():
    assert floor(0) == 0


def test_floor_whole_number_1():
    assert floor(1) == 1


def test_floor_whole_number_2():
    assert floor(2) == 2


def test_floor_negative_1():
    assert floor(-1) == -1


def test_floor_negative_0():
    assert floor(-0) == -0


def test_floor_real_positive_1_4():
    assert floor(1.4) == 1


def test_floor_real_positive_1_5():
    assert floor(1.5) == 1


def test_floor_real_positive_1_9():
    assert floor(1.9) == 1


def test_floor_real_negative_1_4():
    assert floor(-1.4) == -2


def test_floor_real_negative_1_5():
    assert floor(-1.5) == -2


def test_floor_real_negative_1_9():
    assert floor(-1.9) == -2
