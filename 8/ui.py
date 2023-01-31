from logger import input_data, print_data, change_data, delete_data, get_records_number


def interface():
    while True:
        print('Добрый день! Это бот-помощник. \n'
        'Что вы хотите сделать?\n'
        '1 - Записать данные\n'
        '2 - Вывести данные\n'
        '3 - Изменить данные\n'
        '4 - Удалить данные\n'
        '5 - Выйти\n')

        command = int(input("Ваш выбор: "))
        while command < 1 or command > 5:
            command = int(input("Ещё один шанс! Ваш выбор: "))
        
        if command == 1:
            input_data()

        elif command == 2:
            print_data()

        elif command == 3:
            file_number = int(input('Введите номер файла, запись в котором вы хотите изменить: '))
            while file_number != 1 and file_number != 2:
                file_number = int(input("Ещё один шанс! Введите номер файла, запись в котором вы хотите изменить: "))

            n = get_records_number(file_number)
            data_number = int(input(f'Найдено {n} записи/ей. Введите номер записи, которую вы хотите изменить: '))
            while data_number < 1 or data_number > n:
                data_number = int(input("Ещё один шанс! Введите номер записи, которую вы хотите изменить: "))
            
            change_data(file_number, data_number)

        elif command == 4:
            file_number = int(input('Введите номер файла, запись в котором вы хотите удалить: '))
            while file_number != 1 and file_number != 2:
                file_number = int(input("Ещё один шанс! Введите номер файла, запись в котором вы хотите удалить: "))

            n = get_records_number(file_number)
            data_number = int(input(f'Найдено {n} записи/ей. Введите номер записи, которую вы хотите удалить: '))
            while data_number < 1 or data_number > n:
                data_number = int(input("Ещё один шанс! Введите номер записи, которую вы хотите удалить: "))

            delete_data(file_number, data_number)
        else:
            break
