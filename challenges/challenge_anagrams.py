def sort(array, low, high):
    if low < high:
        reference_index = divide_array(array, low, high)

        if reference_index - 1 > low:
            sort(array, low, reference_index - 1)

        if reference_index + 1 < high:
            sort(array, reference_index + 1, high)


def divide_array(array, low, high):
    index = low - 1
    reference = array[high]

    j = low
    while j < high:
        if array[j] <= reference:
            index = index + 1
            array[index], array[j] = array[j], array[index]
        j = j + 1

    array[index + 1], array[high] = array[high], array[index + 1]

    return index + 1


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return "", "", False

    first_string = list(first_string.lower())
    second_string = list(second_string.lower())

    sort(first_string, 0, len(first_string) - 1)
    sort(second_string, 0, len(second_string) - 1)
    first_string = ''.join(first_string)
    second_string = ''.join(second_string)

    if first_string == second_string:
        return first_string, second_string, True

    return first_string, second_string, False
