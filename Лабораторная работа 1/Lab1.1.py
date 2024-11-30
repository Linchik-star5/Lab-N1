# Объем дискеты в мегабайтах
disk_size_mb = 1.44

# Параметры книги
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Расчет объема одной книги в байтах
volume_per_book = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Преобразование объема дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Подсчет количества книг, помещающихся на дискету
number_of_books = disk_size_bytes // volume_per_book

# Вывод результата
print("Количество книг, помещающихся на дискету:", int(number_of_books))