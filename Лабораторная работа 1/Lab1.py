# Исходный список с пропущенным элементом
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


a = (sum(filter(None, numbers)))
b = len(numbers)
c = a / b
index = numbers.index(None)
numbers[index] = 0
numbers[index] = c
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
