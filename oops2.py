class calculator():
  def __init__(self,num1,num2):
    self.num1=num1
    self.num2=num2
  def add(self):
    return self.num1+self.num2
  def sub(self):
    return self.num2-self.num1  
  def mult(self):
    return self.num1*self.num2
  def div(self):
    return self.num2/self.num1
num1=int(input('enter first no.='))
num2=int(input('enter second no.= '))
obj=calculator(num1,num2)
print(obj.add())
print(obj.sub())
print(obj.mult())
print(obj.div())
