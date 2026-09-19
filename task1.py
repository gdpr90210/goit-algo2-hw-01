def find_min_max(arr, left=0, right=None):
    if not arr:
        raise ValueError("Array must not be empty")

    if right is None:
        right = len(arr) - 1

    # Базовый случай: остался один элемент
    if left == right:
        return arr[left], arr[left]

    # Находим середину текущей части массива
    mid = (left + right) // 2

    # Рекурсивно ищем min и max в левой части
    left_min, left_max = find_min_max(arr, left, mid)

    # Рекурсивно ищем min и max в правой части
    right_min, right_max = find_min_max(arr, mid + 1, right)

    # Выбираем общий минимум
    if left_min > right_min:
        minimum = right_min
    else:
        minimum = left_min

    # Выбираем общий максимум
    if left_max > right_max:
        maximum = left_max
    else:
        maximum = right_max

    return minimum, maximum


numbers = [3, 1, 444, 1, 5, 19, -1, 6, 53, 3, 5]

print(find_min_max(numbers))