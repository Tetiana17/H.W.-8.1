def add_one(some_list):
    # конвертуємо список цифр у число
    num = int(''.join(str(some_list) for some_list in some_list))
    # додаємо одиницю
    num += 1
    # конвертуємо число знову у список цифр
    result = [int(some_list) for some_list in str(num)]
    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
