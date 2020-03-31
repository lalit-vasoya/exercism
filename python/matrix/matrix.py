class Matrix:

    def __init__(self, matrix_string):

        self.m=matrix_string.split("\n")

        for i in range(len(self.m)):
            self.m[i]=self.m[i].split()
            
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                self.m[i][j]=int(self.m[i][j])

    def row(self, index):
        return self.m[index-1]
       
    def column(self, index):
        b=[]
        for i in range(len(self.m)):
            b.append(self.m[i][index-1])

        return b
