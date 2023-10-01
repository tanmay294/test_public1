class a:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    
    def display(self):
        print("the attributes are",self.name,"and",self.sal)
0
obj=a('tanmay',1000)
print(obj.__dict__)
obj.display()
