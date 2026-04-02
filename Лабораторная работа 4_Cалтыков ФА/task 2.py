import json  # импортируем библиотеку json
import csv  # импортируем библиотеку csv


INPUT_FILENAME = "input.csv"  # даем ссылку на CSV файл в переменную
OUTPUT_FILENAME = "output.json"  # даем ссылку на JSON файл в переменную


def task() -> None:  # создаем функцию, которая не будет ничего возвращать
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:  # открываем файл в формате CSV с помощью менеджера контекста в режиме чтения, указываем кодировку
        reader = csv.DictReader(csv_file)  # записываем прочитанные значения в виде типа данных "OrderedDict"
        data = list(reader)  # получаем список словарей, где ключи - названия столбцов
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:  # открываем файл в формате JSON с помощью менеджера контекста в режиме записи, указываем кодировку
        json.dump(data, json_file, indent=4)  # запись полученного ранее списка словарей в JSON файл с отступами 4

if __name__ == '__main__':
    # Нужно для проверки
    task()  # вызываем функцию

    with open(OUTPUT_FILENAME) as output_f:  # открываем готовый JSON файл с помощью менеджера контекста
        for line in output_f:  # проходимся по каждой строчке из готового JSON файла
            print(line, end="")  # выводим по строке в консоль, конец строки делаем пустым, чтобы не было дополнительного перевода строки