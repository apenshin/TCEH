import random


def raise_random_error():
    ex = random.choice([ValueError, TypeError, RuntimeError])
    raise ex('Message for a user')

try:
    raise_random_error()
except ValueError as e:
    print('Value', e)
except TypeError as e:
    print('Type', e)
except RuntimeError as e:
    print('Runtime', e)