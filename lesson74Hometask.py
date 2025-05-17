import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:

        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавить ученика 
        5. Добавить предмет
        6. Редактировать имя ученика
        7. Редактировать название предмета
        8. Удалить ученика
        9. Удалить предмет
        10. Вывести все оценки по ученику
        11. Вывести средний бал ученика по всем предметам 
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()



    elif command == 4:
        print('4. Добавить ученика ')
        # добавляем  имя ученика
        name = input('Введите имя ученика, которого нужного добавить: ')
        students.append(name)
        print(students)


    elif command == 5:
        print('5. Добавить предмет')
        # добавляем  предмет
        name1 = input('Введите название предмета: ')
        classes.append(name1)
        print(classes)

    elif command == 6:
        print('6.Редактировать имя ученика')
        # Редактируем имя ученика
        name = input('Введите ученика, у которого нужно изменить имя: ')
        students.remove(name)
        name = ('Введите изменённое имя ученика: ')
        students.append(name)
        print(students)

    elif command == 7:
        print('7. Удалить предмет')
        # Редактируем название предмета
        name1 = input('Введите название предмета, который нужно изменить: ')
        classes.remove(name1)
        name2 = input('Введите изменённое название предмета: ')
        classes.append(name2)
        print(classes)
    elif command == 8:
        print('8.Удалить имя ученика')
        # Удаляем имя ученика
        name = input('Введите ученика, которого удалить: ')
        students.remove(name)
        print(students)
    elif command == 9:
        print('9. Удалить предмет')
        # Удаляем предмет
        name1 = input('Введите название предмета, который нужно удалить: ')
        classes.remove(name1)
        print(classes)


    elif command == 10:
        print('10. Вывести все оценки по ученику')
        name = input('Введите имя ученика: ')
        for student in name:
            print(student)
        # цикл по предметам
        for class_ in classes:
            print(f'\t{class_} - {students_marks[name][class_]}')
            print()
    elif command == 11:
        print('11. Вывести средний балл ученика по всем предметам ')
        students = input('Введите имя ученика: ')
        for student in students:
            print(student)
        # цикл по предметам
        for class_ in classes:
            # находим сумму оценок по предмету
            marks_sum = sum(students_marks[students][class_])
            # находим количество оценок по предмету
            marks_count = len(students_marks[students][class_])
            # выводим средний балл по предмету
            print(f'{class_} - {marks_sum // marks_count}')
        print()
    elif command == 12:
                print('12. Выход из программы')
                break
