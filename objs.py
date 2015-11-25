from enum import Enum

class User:
    def __init__(self, age, exp, sex):
        self.age = int(age)
        self.exp = int(exp)
        self.sex = Sex(sex)

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

def CodePoint:
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
