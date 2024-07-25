def add_one(some_list):
    # Перетворюємо кожну цифру у строку та об'єднуємо їх у рядок
    num_str = int(''.join(map(str, some_list)))
    # перетворюємо рядок чисел в ціле число
    num = int(num_str)
    # додаємо одиницю
    num += 1
    # розбиваємо числа на цифри та перетворюємо їх знову в список цілих чисел
    result = list(map(int, str(num)))
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
