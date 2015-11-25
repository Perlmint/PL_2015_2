from datetime import datetime
from objs import Point, CodePoint, Posture, Situation, Model, User

class KeyData:
    def __init__(self, row):
        self.time = datetime.fromtimestamp(int(row[0]) / 1000)
        self.test_name = row[1]
        self.pos = Point(row[2], row[3])
        self.code_point = CodePoint(row[4])
        self.intent_code_point = CodePoint(row[5])
        self.input_posture = Posture[row[6]]
        self.input_situation = Situation[row[7]]
        self.keyboard_condition = row[8]
        self.battery = float(row[9])
        self.model = Model(row[10])
        self.user = User(row[11], row[12], row[13])
        self.wpm = float(row[14])
        self.error_rate = float(row[15])

class SaveData:
    def __init__(self, row):
        self.time = datetime.strptime(row[0], "%Y%m%DT%H%M%S")
        self.filename = row[1]
        self.battery = float(row[2])
        self.model = Model(row[3])
        self.user = User(row[4], row[5], row[6])
        self.posture = Posture[row[7]]
        self.situation = Situation[row[8]]
        self.keyboard_condition = int(row[9])
        self.test_time = int(row[10])
        self.word_count = int(row[11])
        self.wpm = float(row[12])
        self.error_count = int(row[13])
        self.error_rate = float(row[14])
        self.letter_count = int(row[15])

class SensorData:
    def __init__(self, row):
        self.time = datetime.fromtimestamp(int(row[0]) / 1000)
        self.acc = Point(row[1], row[2], row[3])
        self.gyro = Point(row[4], row[5], row[6])
        self.mag = Point(row[7], row[8], row[9])
        self.azim = float(row[10])
        self.pitch = float(row[11])
        self.roll = float(row[12])
        self.light = int(row[13])
        self.prox = int(row[14])
        self.posture = Posture[row[15]]
        self.situation = Situation[row[16]]
        self.battery = float(row[17])
        self.model = Model(row[18])
        self.user = User(row[19], row[20], row[21])
        self.wpm = float(row[22])
        self.error_rate = float(row[23])
