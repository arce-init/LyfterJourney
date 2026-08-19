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

#O(n²) — dos ciclos anidados. Aunque la optimización de has_made_changes
#permite terminar antes en listas ya ordenadas, el caso promedio y peor
#caso siguen siendo O(n²), ya que Big O se mide según el peor escenario.