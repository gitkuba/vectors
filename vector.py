import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, vector):
        result_dimentions = [
            round(x + y, 3) for (x, y) in zip(self.coordinates, vector.coordinates)
        ]
        return Vector(result_dimentions)

    def substract(self, vector):
        result_dimentions = [
            round(x - y, 3) for (x, y) in zip(self.coordinates, vector.coordinates)
        ]
        return Vector(result_dimentions)

    def multiply(self, scalar):
        result_dimentions = [round(x * Decimal(scalar), 3) for x in self.coordinates]
        return Vector(result_dimentions)

    def magnitude(self):
        return sum([x ** 2 for x in self.coordinates]).sqrt()

    def normalize(self):
        try:
            return Vector(
                [x * (Decimal(1.0) / self.magnitude()) for x in self.coordinates]
            )
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self, vector):
        result_dimentions = [
            x * y for (x, y) in zip(self.coordinates, vector.coordinates)
        ]
        return round(sum(result_dimentions), 3)

    def angle(self, vector):
        dot_product = self.dot_product(vector)

        return math.acos(dot_product / (self.magnitude() * vector.magnitude()))

    def is_orthogonal_to(self, vector, tolerance=1e-10):
        return abs(self.dot_product(vector)) < tolerance

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_parallel_to(self, vector):
        print(f"self.is_zero() {self.is_zero()}")
        print(f"vector.is_zero() {vector.is_zero()}")
        print(f"self.angle(vector){self.angle(vector)}")
        print(f"self.angle(vector) == 0 {self.angle(vector) == 0}")
        print(f"self.angle(vector) == math.pi {self.angle(vector) == math.pi}")
        return (
            self.is_zero()
            or vector.is_zero()
            or self.angle(vector) == 0
            or self.angle(vector) == math.pi
        )
