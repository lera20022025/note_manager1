username = input('Введите Ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус выполнения данной заметки: ')
created_date = input('Введите дату создания заметки в формате ДД-ММ-ГГГГ: ')
issue_date = input('Введите дату окончания выполнения заметки в формате ДД-ММ-ГГГГ: ')
# вывод внесенной информации
print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус выполнения заметки:', status)
print('Заметка создана:', created_date[:5])
print('Выполнить до:', issue_date[:5])