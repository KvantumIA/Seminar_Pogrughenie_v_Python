"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие
только букв. Если ФИО не соответствует условию, выведите:
---ФИО должно состоять только из букв и начинаться с заглавной буквы

○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
---Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от
 0 до 100). В противном случае выведите:
---Оценка должна быть целым числом от 2 до 5
---Результат теста должен быть целым числом от 0 до 100

○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и
 по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
 следующая информация.
---Математика,Физика,История,Литература

Создайте класс Student, который будет представлять студента и его успехи по
предметам. Класс должен иметь следующие методы:
Атрибуты класса:
---name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в
качестве ключей и информацию об оценках и результатах тестов для каждого
предмета в виде словаря.

Магические методы (Dunder-методы):
---__init__(self, name, subjects_file): Конструктор класса. Принимает имя
студента и файл с предметами и их результатами. Инициализирует атрибуты name и
subjects и вызывает метод load_subjects для загрузки предметов из файла.

---__setattr__(self, name, value): Дескриптор, который проверяет установку
атрибута name. Убеждается, что name начинается с заглавной буквы и состоит
только из букв.

---__getattr__(self, name): Позволяет получать значения атрибутов предметов
(оценок и результатов тестов) по их именам.

---__str__(self): Возвращает строковое представление студента, включая имя и
список предметов.
Студент: Иван Иванов
Предметы: Математика, История

Методы класса:
---load_subjects(self, subjects_file): Загружает предметы из файла CSV.
Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут
subjects.

---add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
Убеждается, что оценка является целым числом от 2 до 5.

---add_test_score(self, subject, test_score): Добавляет результат теста по
заданному предмету. Убеждается, что результат теста является целым числом от 0
до 100.

---get_average_test_score(self, subject): Возвращает средний балл по тестам для
заданного предмета.

---get_average_grade(self): Возвращает средний балл по всем предметам.

Пример

На входе:
student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)


На выходе:
Средний балл: 4.5
Средний результат по тестам по математике: 85.0
Студент: Иван Иванов
Предметы: Математика, История
"""

import csv


class Student:
    subjects = {}

    def __new__(cls, name: str, subjects_file: str, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str, subjects_file: str):
        self.name = name
        self.subjects_file = subjects_file
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        """
        Загружает предметы из файла CSV. Использует модуль csv для чтения
        данных из файла и добавляет предметы в атрибут subjects
        """
        with open(subjects_file, 'r', encoding='utf-8') as file:
            data_csv = csv.reader(file)
            for row in data_csv:
                for subject in row:
                    self.subjects[subject] = {'grade': None, 'score': None}

    def add_grade(self, subject, grade):
        """
        Добавляет оценку по заданному предмету. Убеждается, что оценка является
        целым числом от 2 до 5.
        """
        if isinstance(grade, int) and 2 <= grade <= 5:
            temp = {'grade': grade}
            return self.subjects[subject].update(temp)
        else:
            raise ValueError(f'Оценка должна быть целым числом от 2 до 5')

    def add_test_score(self, subject, test_score):
        """
        Добавляет результат теста по заданному предмету. Убеждается, что
        результат теста является целым числом от 0 до 100.
        """
        if isinstance(test_score, int) and 0 <= test_score <= 100:
            temp = {'score': test_score}
            return self.subjects[subject].update(temp)
        else:
            raise ValueError(
                f'Результат теста должен быть целым числом от 0 до 100')

    def get_average_test_score(self, subject):
        """
        Возвращает средний балл по тестам для заданного предмета.
        """
        res = 0
        if subject in self.subjects.keys():
            res += float(self.subjects[subject]['score'])
        else:
            raise ValueError(f'Предмет {subject} не найден')
        return res

    def get_average_grade(self):
        """
        Возвращает средний балл по всем предметам
        """
        res = 0
        count = 0
        for subject, details in self.subjects.items():
            if details['grade'] is not None:
                res += details['grade']
                count += 1
        res = res / count
        return res

    def __setattr__(self, name, value: str):
        """
        Дескриптор, который проверяет установку атрибута name. Убеждается, что
        name начинается с заглавной буквы и состоит только из букв.
        """
        if name == 'name':
            if isinstance(value, str) and all(part.isalpha() for part in
                                              value.split()) and value.istitle():
                super().__setattr__(name, value)
            else:
                raise ValueError('ФИО должно состоять только из букв и '
                                 'начинаться с заглавной буквы')
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        """
        Позволяет получать значения атрибутов предметов (оценок и результатов
        тестов) по их именам.
        """
        raise ValueError(f'Предмет {name} не найден')

    def __str__(self):
        items = ''
        for subject, details in self.subjects.items():
            if details['grade'] is not None or details['score'] is not None:
                items += f'{subject}, '
        items = items.rstrip(', ')
        return (f'Студент: {self.name}\n'
                f'Предметы: {items}')


# student = Student("Иван Иванов", "subjects.csv")
#
# student.add_grade("Математика", 4)
# student.add_test_score("Математика", 85)
#
# student.add_grade("История", 5)
# student.add_test_score("История", 92)
#
# average_grade = student.get_average_grade()
# print(f"Средний балл: {average_grade}")
#
# average_test_score = student.get_average_test_score("Математика")
# print(f"Средний результат по тестам по математике: {average_test_score}")
#
# print(student)

# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История


student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

# Средний балл: 4.5
# Средний результат по тестам по математике: 85.0
# Студент: Иван Иванов
# Предметы: Математика, История


# student = Student("123 Иван", "subjects.csv")


# student = Student("Петров Петр", "subjects.csv")
#
# student.add_grade("Физика", 6)

# ValueError: Оценка должна быть целым числом от 2 до 5


# student = Student("Сидоров Сидор", "subjects.csv")
#
# average_history_score = student.get_average_test_score("Биология")

# ValueError: Предмет Биология не найден
