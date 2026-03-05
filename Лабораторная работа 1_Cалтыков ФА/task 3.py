list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

numbers_of_players = len(list_players) # Считаем количество игроков в списке
middle_index = numbers_of_players // 2 # Находим индекс игрока в середине

# Создаем список игроков с 1-го игрока по игрока в середине не включительно
first_team = list_players[:middle_index]
# Создаем список игроков с игрока по середине включительно до последнего игрока
second_team = list_players[middle_index:]

print(first_team) # Выводим список игроков первой команды
print(second_team) # Выводим список игроков второй команды
