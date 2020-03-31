import re
from itertools import chain
class Luhn:
    def __init__(self, card_num):
        self.luhn = True
        card_num = card_num.replace(" ","")
        if len(card_num) < 2 or any([not item.isdigit() for item in card_num]):
            self.luhn = False

        self.card_num = list(map(int,re.findall(r'\d+',card_num)[0]))

    def valid(self):
        self.firstdigit  = self.card_num[len(self.card_num)-1 ::-2]
        self.seconddigit = self.card_num[len(self.card_num)-2::-2]
        self.seconddigit = list(map(lambda x:x*2-9 if x*2>9 else x*2 ,self.seconddigit))
        total = sum(chain(self.firstdigit,self.seconddigit))
        if not self.luhn:
            return self.luhn
        return total%10==0