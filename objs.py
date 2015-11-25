from enum import Enum

class User:
    def __init__(self, age, exp, sex):
        self.age = int(age)
        self.exp = int(exp)
        self.sex = Sex[sex]

class Point:
    def __init__(self, x, y, z = None):
        self.x = float(x)
        self.y = float(y)
        if z is not None:
            self.z = float(z)

    def __repr__(self):
        if self.z is not None:
            return "<Point: %f, %f, %f>" % (self.x, self.y, self.z)
        else:
            return "<Point: %f, %f>" % (self.x, self.y)

class CodePoint:
    def __init__(self, code):
        self.code = int(code)

class Posture(Enum):
    Left = 1
    Right = 2
    Both = 3

class Situation(Enum):
    Sit = 1
    Walk = 2
    Stand = 3
    Lie = 4

class Sex(Enum):
    Male = 1
    Female = 2

class Model:
    def __init__(self, model_name):
        self.model_name = model_name

    def __repr__(self):
        return "<Model: %s>" % model_name

    def screen_size(self):
        # TODO: get screen size from model name
        pass
