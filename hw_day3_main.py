# Задачи на закрепление функций:
# Написать функцию, которая принимает на вход два аргумента.
# Если аргументы больше нуля, возвращаем их сумму.
# Если оба меньше - разность.
# Если знаки разные - возвращаем 0
def some_func(a, b):
    if (a > 0) and (b > 0):
        return a + b
    elif (a < 0) and (b < 0):
        return a - b
    elif a  * b < 0:
        return 0

print(some_func(1, 1))
print(some_func(-3, -1))
print(some_func(-3, 1))


# Написать функцию, которая принимает 3 аргумента - числа,
# найти среди них два максимальных, вывести в консоль

# Написать функцию, которая принимает два аргумента.
# Первый - список чисел, второй - булевый флаг.
# Если флаг действителен - возвращаем новый список с нечетными числами из входного списка,
# если флаг отрицателен - возвращаем новый список с четными числами из входного списка


# Задачи на закрепление типов аргументов:
# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба

# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему

# Написать функцию, которая принимает любое количество позиционных аргументов - строк
# и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
# Для соединения между любых двух строк вставлять glue