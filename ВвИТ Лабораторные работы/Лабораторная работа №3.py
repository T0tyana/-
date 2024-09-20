# Задача 1
def read_file(name, type):
    try:
        if type == 'fool':
            with open(f'{name}', 'r') as file:
                print(file.read())


        elif type == 'line':
            with open(f'{name}', 'r') as file:
                for line in file:
                    print(line)
    except FileNotFoundError:
        print('Нет файла с таким назанием')

name_of_file = input('Введите название файла: ')
Type = input('Укажите, как Вы хотите прочитать файл: полностью(fool) или построчно(line): ')
print()

read_file(name_of_file, Type)

#Задача 2
'''def write_file(ans):
    if ans == 'rewrite':
        text = input('Введите текст: ')
        with open('user_input_txt', 'w') as file:
            file.write(text + '\n')

    elif ans == 'add':
        text_two = input('Введите текст, который хотите добавить: ')
        with open('user_input_txt', 'a') as file:
            file.write(text_two + '\n')

que = input('Перезаписать файл(rewrite) или добавить текст(add): ')
write_file(que)


with open('user_input_txt', 'r') as file:
    print(file.read())'''
