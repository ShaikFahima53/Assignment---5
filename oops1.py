class Point:
    def  __init__(self,x,y,z):
        self.x= x
        self.y= y
        self.z= z
        
    def sqsum(self):
        return(self.x*self.x+self.y*self.y+self.z*self.z)
    
sqno=Point(1,3,5)
print(sqno.sqsum())
