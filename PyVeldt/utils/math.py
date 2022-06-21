import math

def relative_position(point:tuple, datum:tuple):
    return tuple(map(lambda i, j: i - j, point, datum))

def distance(pos_a:tuple, pos_b:tuple):
    delta = relative_position(pos_a, pos_b)
    return math.sqrt(sum(x**2 for x in delta))

