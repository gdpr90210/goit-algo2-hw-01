import random


def quick_select(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and the length of the array")

    numbers = arr.copy()

    def select(left, right, target_index):
        if left == right:
            return numbers[left]

        pivot_index = random.randint(left, right)
        pivot_value = numbers[pivot_index]

        # Переносим pivot в конец
        numbers[pivot_index], numbers[right] = numbers[right], numbers[pivot_index]

        store_index = left

        # Переносим элементы меньше pivot в левую часть
        for i in range(left, right):
            if numbers[i] < pivot_value:
                numbers[i], numbers[store_index] = numbers[store_index], numbers[i]
                store_index += 1

        # Ставим pivot на его итоговую позицию
        numbers[store_index], numbers[right] = numbers[right], numbers[store_index]

        if target_index == store_index:
            return numbers[store_index]

        if target_index < store_index:
            return select(left, store_index - 1, target_index)

        return select(store_index + 1, right, target_index)

    return select(0, len(numbers) - 1, k - 1)


numbers = [7, 2, 9, 4, 1, 5]

print(quick_select(numbers, 3))