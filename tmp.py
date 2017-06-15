# """ ЗАДАЧА С КУРСА ДЕНЬ 5
# пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник

# http://ru.onlinemschool.com/math/formula/area/#h9

# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.
# """




# import math

# class Shape(object):
#     def __init__(self, *args):
#         self.sides = args


# # class Triangle(Shape):
# #     def __init__(self, *args):
# #         if self.check_sides(args):
# #             self.sides = args
# #         else:
# #             print('Cоздать треугольник с такими сторонами не возможно')
# #             return

# #     def check_sides(self, sides):
# #         sides.sort()
# #         larger_side = sides.pop(len(sides) - 1)
# #         sides_sum = 0
# #         for s in sides:
# #             sides_sum += s

# #         return (sides_sum > larger_side)

# #     def print_per(self):
# #         print('Периметр треугольника =', self.__calc_per())

# #     def __calc_per(self):
# #         return self.sides[0] + self.sides[1] + self.sides[2]

# #     def print_sqr(self):
# #         print('Площадь треугольника =', self.__calc_sqr())

# #     def __calc_sqr(self):
# #         half_per = self.__calc_per / 2
# #         return math.sqrt(half_per * (half_per - self.sides[0]) * (half_per - self.sides[1]) * (half_per - self.sides[2]))


# class Rectange(Shape):

#     def print_per(self):
#         print('Периметр прямоугольника =', self.__calc_per())

#     def __calc_per(self):
#         return (self.sides[0] + self.sides[1]) * 2

#     def print_sqr(self):
#         print('Площадь прямоугольника =', self.__calc_sqr())

#     def __calc_sqr(self):
#         return self.sides[0] * self.sides[1]


# # class Square(Rectange):
# #     def __init__(self, *args):
# #         self.sides = [args[0, args[0]]



# rect = Rectange(1)
# rect.print_per()
# rect.print_sqr()

# # sqr = Square(5)
# # sqr.print_per()
# # sqr.print_sqr()

# tpl = (1,2,3,5,6)
# print(tpl)


def neigbors(point):
    x, y = point
    for i, j in itertools.product(range(-1, 2), repeat=2):
        if any((i, j)):
            yield (x + i, y + j)

def advance(board):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board)
                for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)

    return newstate

glider = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])
for i in range(1000):
    glider = advance(glider)
print glider