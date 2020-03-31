from string import digits
class Luhn:
    def __init__(self, card_num):
        self.card_num=card_num.replace(" ","")
      
     
        self.new=""
    
    def valid(self):
        print(self.card_num)
        for i in self.card_num:
            if i not in digits:
                return False
        
        a=str(int(self.card_num))

        for i in range(len(a)):
            if i%2==0:
                print(a[i])
                self.new+=str(int(a[i])*2) if int(a[i])*2<=9 else str(int(a[i])*2-9)
        #         self.new+=str([i]*2 if (a[i]*2)<9 else a[i]*2-9
            else:
                self.new+=str(a[i])
        #         self.new+=a[i]
        print(self.new)
        print(sum(map(int,self.new))%10==0)
        print("sum:",sum(map(int,self.new)))
        return sum(map(int,self.new))%10==0 

print(Luhn("590 231").valid())