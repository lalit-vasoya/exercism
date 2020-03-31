class Garden:

    def __init__(self, diagram, students=None):
        self.diagram=diagram
        self.students=sorted(students) if students!=None else students
        self.classg={"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}


    def plants(self,students):
        ind=0 if self.students==None else self.students.index(students) 
        temp=[]

        for i in self.diagram.split():
            if self.students==None:
                temp.append(self.classg[i[2*(ord(students[0])-65)]])
                temp.append(self.classg[i[2*(ord(students[0])-65)+1]])
            else:     
                temp.append(self.classg[i[2*ind]])
                temp.append(self.classg[i[2*ind+1]])
          
        return temp


