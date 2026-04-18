#1
class Mark:
    def __init__(self,mark):
        self.mark = mark
    def result(self):
        if self.mark>50:
            return "Pass"
        else:
            return "Fail"
    def grade(self):
        if self.mark>90:
            return "Grade A"
        elif self.mark>80:
            return "Grade B"
        elif self.mark>70:
            return "Grade C"
        elif self.mark>60:
            return "Grade D"
        elif self.mark>50:
            return "Grade E"
        else:
            return "Failed"
m = Mark(50)
print(m.result(),m.grade())