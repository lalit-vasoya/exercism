class Allergies:

    def __init__(self, score):
        self.no=score
        self.l=set()
        self.allergies={
                        'eggs':1,
                        'peanuts':2,
                        'shellfish':4,
                        'strawberries':8,
                        'tomatoes':16,
                        'chocolate':32,
                        'pollen':64,
                        'cats':128
                }

    def allergic_to(self, item=None):
        for key,value in sorted(self.allergies.items(),reverse=True,key=lambda p:p[1]):
            while self.no>=value:   
                self.no -= value
                self.l.add(key)

        return item in self.l

    @property
    def lst(self):
        self.allergic_to()
        return list(self.l)
