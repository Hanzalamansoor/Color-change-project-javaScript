class number :
    def __init__(self,n) :
        self.n = n


    def __add__(self,num): # 
        return self.n + num.n

    
    def __mul__(self,num):
        return self.n * num.n
    
  
n = number(5)
m = number (6)
print(n + m)
print(n * m)