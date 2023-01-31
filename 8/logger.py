from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 Вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 Вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно!!')


def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data = file.readlines()
    for line in data:
        print(line.strip())

    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data = file.readlines()
    for line in data:
        print(line.strip())


def get_records_number(file_number):
    if file_number == 1:
        filename = 'first'
    elif file_number == 2:
        filename = 'second'
    with open(f'data_{filename}_variant.csv', 'r', encoding = 'utf-8') as file:
        data = file.readlines()
    if file_number == 1:
        return len(data) // 5
    elif file_number == 2:
        return len(data) // 2


def change_data(file_number, data_number):

    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    if file_number == 1:
        filename = 'first'
        n_start = (data_number - 1) * 5
        data_len = 4
        add_data = f'{name}\n{surname}\n{phone}\n{adress}\n'
                
    elif file_number == 2:
        filename = 'second'
        n_start = (data_number - 1) * 2
        data_len = 1
        add_data = f'{name};{surname};{phone};{adress}\n'

    with open(f'data_{filename}_variant.csv', 'r', encoding = 'utf-8') as file:
        data = file.readlines()

    data_new = data[:n_start] + [add_data] + data[n_start+data_len:]
    
    with open(f'data_{filename}_variant.csv', 'w', encoding = 'utf-8') as file:
        for line in data_new:
            file.write(line)

    print('Успешно!!')

def delete_data(file_number, data_number):

    if file_number == 1:
        filename = 'first'
        n_start = (data_number - 1) * 5
        data_len = 4
                
    elif file_number == 2:
        filename = 'second'
        n_start = (data_number - 1) * 2
        data_len = 1

    with open(f'data_{filename}_variant.csv', 'r', encoding = 'utf-8') as file:
        data = file.readlines()

    if data_number == 1:
        data_new = data[1+data_len:]
    elif data_number == get_records_number(file_number):
        data_new = data[:-data_len-1]
    else:
        data_new = data[:n_start] + data[n_start+data_len:]

    with open(f'data_{filename}_variant.csv', 'w', encoding = 'utf-8') as file:
        for line in data_new:
            file.write(line)

    print('Успешно!!')