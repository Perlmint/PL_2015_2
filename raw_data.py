from datetime import datetime
from objs import Point, CodePoint, Posture, Situation, Model, User

class KeyData:
    def __init__(self, row):
        self.time = datetime.fromtimestamp(int(row[0]))
        self.test_name = row[1]
        self.pos = Point(row[2], row[3])
        self.code_point = CodePoint(row[4])
        self.intent_code_point = CodePoint(row[5])
        self.input_posture = Posture[row[6]]
        self.input_situation = Situation[row[7]]
        self.battery = float(row[8])
        self.model = Model(row[9])
        self.user = User(row[10], row[11], row[12])
        self.wpm = float(row[13])
        self.error_rate = float(row[14])

class SaveData:
    def __init__(self, row):
        self.time = row[0]
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
