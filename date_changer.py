created_date = input('Создано: ') # ввод полной даты создания заметки например 23-11-2024
temp_created_date = created_date[0:5] # создание переменной для хранения сокращенной даты создания
print('Сокращенный формат даты создания:', temp_created_date) # вывод сокращенной даты 23-11
issue_date = input('Выполнить до: ') # ввод даты дедлайна например 03 декабря 2024
temp_issue_date = issue_date[0:10] # создание переменной для хранения сокращенной даты дедлайна
print('Сокращенный формат даты выполнения:', temp_issue_date) # вывод сокращенной даты выполнения 03 декабря
