from contextlib import contextmanager

@contextmanager
def open_file(filename, filemode):
    print('Opening file {}...'.format(filename))
    f = open(filename, filemode)
    yield f
    print('Closing file {}...'.format(filename))


with open_file('ATATATATA', 'w') as smth:
    print(smth)



with