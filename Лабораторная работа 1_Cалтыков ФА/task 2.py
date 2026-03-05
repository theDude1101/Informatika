# Записываем дано в переменные:
information_volume_in_Mb = 1.44 # информацонный объем дискеты в мегабайтах
number_of_pages = 100 # количество страниц в книге
number_of_lines_per_page = 50 # число строк на странице
number_of_characters_per_line = 25 # количество символов в строке
size_of_character_in_bytes = 4 # количество байт на 1 символ

volume_of_one_book_in_bytes = number_of_pages * number_of_lines_per_page * number_of_characters_per_line * size_of_character_in_bytes # Считаем объем одной книги в байтах
information_volume_in_bytes = information_volume_in_Mb * 1024 * 1024 # Считаем объем дискеты в байтах

books_on_disk = round(information_volume_in_bytes / volume_of_one_book_in_bytes) # Считаем количество книг, помещающихся на дискету, округленное до целого

print("Количество книг, помещающихся на дискету:", books_on_disk) # выводим количество книг, помещающиеся на дискету
