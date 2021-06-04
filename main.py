tasks = []
HELP = '''
* help - справка,
* add - добавить задачу, 
* show - показать список задач,
* exit - выйти из программы
'''
stop = True
while stop:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "add":
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена")
  elif command == "show":
    print(tasks)
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    stop = False
  else:
    print("Неизвестная команда")
    print(HELP)