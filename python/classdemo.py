class Abc:
	name=11
	def __init__(self):
		self.name="LAlit"
	@classmethod
	def abc(c):
		print(c.name)
	@staticmethod
	def xyz():
		print(Abc.name)

	def display(self):
		print(self.name)
		print(self.fname)
	def getname(self):
		self.fname="vasoya"

a=Abc()
a.getname()
a.display()
print("Print Data using class methodabc")
Abc.abc()
print("Print Data using static method")
Abc.xyz()
