class Vehicle:
	def __init__(self,Reg_no,color):
		self.color =  color
		self.Reg_no = Reg_no

class Car(Vehicle):

	def __init__(self,Reg_no,color):
		Vehicle.__init__(self,Reg_no,color)

	def getType(self):
		return "Car"