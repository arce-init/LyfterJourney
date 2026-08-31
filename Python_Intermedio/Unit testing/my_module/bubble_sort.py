def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise TypeError("bubble_sort only accepts a list")

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
            return list_to_sort

    return list_to_sort