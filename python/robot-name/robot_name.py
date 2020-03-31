import random as r
class Robot:
    def __init__(self):
        fc=chr(r.randrange(65,89))
        fs=chr(r.randrange(65,89))
        n=r.randrange(100,998)
        self.name=fc+fs+str(n)

    def seed(self,s):
        self.name=s

    def reset(self):
        fc=chr(r.randrange(65,90))
        fs=chr(r.randrange(65,90))
        n=r.randrange(100,999)
        self.name=fc+fs+str(n)
