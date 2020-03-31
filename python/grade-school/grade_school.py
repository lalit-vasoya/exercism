class School:
    def __init__(self):
        self.name={}

    def add_student(self, name, grade):
        self.name[name]=grade

    def roster(self):
        a=sorted(self.name.items() ,key=lambda a: a[1])
        a=sorted(a,key= lambda p:(p[1],p[0]))
        return [i[0] for i in a]

    def grade(self, grade_number):
        temp=[]
        for i in self.name:
            if self.name[i]==grade_number:
                temp.append(i)

        return sorted(temp)
