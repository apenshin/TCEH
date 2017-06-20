# ЗАДАЧА 1
#
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов: know(person),
#    который позволяет добавить другого человека в список знакомых.
# И метод is_known(person), который возвращает знакомы ли два человека

class Person(object):

    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.known_persons = []

    def know(self, person):
        if not person in self.known_persons:
            self.known_persons.append(person)
        else:
            print('{} уже знает человека по имени {}'.format(self.name, person.name))

    def is_known(self, person):
        text_action = {True : 'знает человека по имени', False : 'не знает человека по имени'}
        is_known_person = person in self.known_persons
        print('{} {} {}'.format(self.name, text_action[is_known_person], person.name))


petr = Person('Петр', 30)
olga = Person('Ольга', 26)

petr.is_known(olga)
petr.know(olga)
petr.is_known(olga)
petr.know(olga)



# ЗАДАЧА 2
#
# Есть класс, который выводит информацию в консоль: Printer,
# у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *



# ЗАДАЧА 3
#
# Написать класс Animal и Human,
# сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)
