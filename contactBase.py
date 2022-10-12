class Contact:
    def __init__(self, name, phone, mail):
        self.name = name.strip()

        if phone.strip() == '':
            self.phone = 'Отсутствует'
        else:
            self.phone = phone.strip()

        if mail.strip() == '':
            self.mail = 'Отсутствует'
        else:
            self.mail = mail.strip()


def read_file(file):
    all_lines = [st.strip().split(',') for st in file.readlines()]
    contacts = list(filter(lambda x: len(x) == 3, all_lines))

    arr = []

    for mas in contacts:
        person = Contact(mas[0], mas[1], mas[2])
        arr.append(person)

    return arr


def find_by_number():
    number = input('Введите номер или его часть: ')
    print('Результаты поиска по номеру телефона:')
    for obj in book:
        if obj.phone.__contains__(number):
            print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    print()


def find_by_mail():
    mail = input('Введите почту или её часть: ')
    print('Результаты поиска по почте:')
    for obj in book:
        if obj.mail.__contains__(mail):
            print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    print()


def find_incomplete():
    print('Список критериев поиска:')
    funcs = {1: 'Отсутствует только телефон', 2: 'Отсутствует только почта', 3: 'Отсутствует и телефон, и почта', 4: 'Отсутствует ровно 1 поле'}
    for val in funcs:
        print(f'{val}) {funcs[val]}')

    search = int(input('По какому критерию мы ищем? Введите номер выбранного критерия: '))
    print('Результаты поиска неполных контактов:')
    if search == 1:
        for obj in book:
            if obj.phone == 'Отсутствует' and obj.mail != 'Отсутствует':
                print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    elif search == 2:
        for obj in book:
            if obj.mail == 'Отсутствует' and obj.phone != 'Отсутствует':
                print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    elif search == 3:
        for obj in book:
            if obj.phone == 'Отсутствует' and obj.mail == 'Отсутствует':
                print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    elif search == 4:
        for obj in book:
            if obj.phone == 'Отсутствует' and obj.mail != 'Отсутствует' or obj.phone != 'Отсутствует' and obj.mail == 'Отсутствует':
                print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    print()


def find_by_name():
    surname = input('Введите фамилию: ').lower().strip()
    name = input('Введите имя: ').lower().strip()
    patronymic = input('Введите отчество: ').lower().strip()
    print()
    print('Результаты поиска по ФИО: ')
    for obj in book:
        name_parts = obj.name.lower().split()
        if name_parts[0].strip().__contains__(surname):
            if name_parts[1].strip().__contains__(name):
                if name_parts[2].strip().__contains__(patronymic):
                    print(f'Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    print()

def show_contact_list():
    print('Список ваших контактов:')
    for i, obj in enumerate(book, start=1):
        print(f'{i}) Имя: {obj.name}, Тел.: {obj.phone}, Почта: {obj.mail}')
    print()


def edit_contact():
    parts = {1: 'ФИО', 2: 'Номер телефона', 3: 'Почта'}

    show_contact_list()
    num1 = int(input('Какой контакт вы хотите изменить? Введите порядковый номер выбранного контакта: '))

    print('Что меняем?')
    for val in parts:
        print(f'{val}) {parts[val]}')
    num2 = int(input('Введите число: '))

    new_part = input('Введите новые данные: ')

    if num2 == 1:
        book[num1 - 1].name = new_part
    elif num2 == 2:
        book[num1 - 1].phone = new_part
    else:
        book[num1 - 1].mail = new_part

    print('Изменения сохранены. Теперь Ваш контакт выглядит так: '
          f'Имя: {book[num1 - 1].name}, Тел.: {book[num1 - 1].phone}, Почта: {book[num1 - 1].mail}')

    print()


def start():
    filename = input('Здравствуйте! Введите название файла, из которого необходимо считать контакты' + '\n'
                                                                                                       '(имя необходимо ввести в формате "<имя файла>.<расширение>": ')

    file = open(f'{filename}', 'r')

    global book
    book = read_file(file)
    print()


def make_acton():
    print('Вот список доступных функций:')

    actions = {1: 'Список всех контактов', 2: 'Список неполных контактов', 3: 'Поиск по номеру телефона', 4: 'Поиск по'
                                                                                                             ' почте',
               5: 'Поиск по ФИО', 6: 'Редактировать контакт'}

    for val in actions:
        print(f'{val}) {actions[val]}')

    action = int(input('Введите номер выбранной функции: '))
    print()

    if action == 1:
        show_contact_list()
    elif action == 2:
        find_incomplete()
    elif action == 3:
        find_by_number()
    elif action == 4:
        find_by_mail()
    elif action == 5:
        find_by_name()
    elif action == 6:
        edit_contact()
    else:
        print('Функции с таким номером нет. Попробуйте еще раз :(')

    global ans
    ans = input('Продолжим? Введите да/нет: ')
    print()


ans = 'да'
start()
while ans.lower() == 'да':
    make_acton()
