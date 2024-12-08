class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка должна быть от 0 до 10'
        else:
            return 'Ошибка'

    def average_grade(self):
        total_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}')

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Функции для подсчёта средней оценки по курсу
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0


def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return round(sum(total_grades) / len(total_grades), 1) if total_grades else 0


# Примеры использования
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Jane', 'Doe', 'female')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Alice', 'Smith')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('John', 'Brown')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Bob', 'Brown')
reviewer1.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 8)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()

print(f'Средняя оценка за домашние задания по курсу "Python": {average_student_grade([student1, student2], "Python")}')
print(f'Средняя оценка за лекции по курсу "Python": {average_lecturer_grade([lecturer1, lecturer2], "Python")}')

# Сравнение студентов и лекторов
print()
print(f'Сравнение студентов: {student1.name} < {student2.name}: {student1 < student2}')
print(f'Сравнение лекторов: {lecturer1.name} < {lecturer2.name}: {lecturer1 < lecturer2}')
