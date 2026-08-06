def bubble_sort(list_to_sort):
    for outer_index in range(len(list_to_sort) - 1):
        has_made_changes = False

        for index in range(len(list_to_sort) - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True

        if not has_made_changes:
            return

def validated_bubble_sort(list_to_sort):
    if len(list_to_sort) == 0:
        raise ValueError("Error: the list is empty")

    for element in list_to_sort:
        if not isinstance(element, (int, float)):
            raise ValueError("Error: the list contains non numeric elements")

    bubble_sort(list_to_sort)
    return list_to_sort

try:
    validated_bubble_sort([7, "Chicken", 8])
except ValueError as error:
    print(error)

try:
    validated_bubble_sort([])
except ValueError as error:
    print(error)

result = validated_bubble_sort([5, 3, 4, 1, 2])
print(result)