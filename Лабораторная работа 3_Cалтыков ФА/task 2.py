def find_common_participants(first_group, second_group, names_separator=','):  # создаем функцию, она получает в качестве аргументов 2 списка, разделитель (по умолчанию - запятая)
    first_group = first_group.split(names_separator)  # получаем первый список участников без разделителей
    second_group = second_group.split(names_separator)  # получаем второй список участников без разделителей
    common_participants = set(first_group).intersection(second_group)  # находим пересечение списка, преобразованного во множество и второго списка
    return list(common_participants)  # функция возвращает пересечение, преобразованное в список

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, names_separator='|'))  # выводим ответ в нужном формате с заданным разделителем
