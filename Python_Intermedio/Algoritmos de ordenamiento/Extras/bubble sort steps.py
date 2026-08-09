def bubble_sort_steps(list_to_sort):
    iterations = 0
    swaps = 0

    for outer_index in range(len(list_to_sort) -1):
        has_made_changes = False
        iterations += 1

        for index in range(len(list_to_sort) - 1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            if current_element > next_element:
                list_to_sort[index] = next_element
                list_to_sort[index + 1] = current_element
                has_made_changes = True
                swaps += 1

        if not has_made_changes:
            break

    return iterations, swaps

my_list = [5, 3, 4, 1, 2]
iterations, swaps = bubble_sort_steps(my_list)

print(f"Sorted list: {my_list}")
print(f"Iterations: {iterations}")
print(f"Swaps: {swaps}")