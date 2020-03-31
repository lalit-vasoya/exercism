class Allergies:

    def __init__(self, score):
        self.no=score
        self.score=score
        self.l=[]
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
        temp=''
        
        for key,value in sorted(self.allergies.items(),reverse=True,key=lambda p:p[1]):
            #print(self.no,value) #(cats,128)
            if self.no>=value:  #(112 > 128)
                print(key,value) 
                self.no -= value
                temp     = key
                #print(key)
                self.l.append(temp)

        if self.score > 128:
            return temp!=item

        return temp==item

    @property
    def lst(self):
        self.allergic_to()
        return self.l

print(Allergies(112).allergic_to("chocolate"))