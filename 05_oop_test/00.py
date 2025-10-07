class Student:
    def __init__(self, num, result):
        self.num = num
        self.result = result

    def getResult(self):
        return self.result
    
    @staticmethod
    def getNum():
        return 123

st = Student(741, 90)
print(st.getResult())
print(Student.getNum())

