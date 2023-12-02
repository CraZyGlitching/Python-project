import Gamemode as gm

class Puissance4:
    def __init__(self):
        self.table = []

    def fill(self):
        temp = []
        for i in range(6):
            temp.append(0)
        self.table = temp
        return self.table
    
    def multiply(self):
        temp2 = []
        for k in range(7):
            self.table.append([self.fill()])
        return self.table
        
    #def Checkmatch(self):

    #def User1Input(self):

test = Puissance4()
test.fill()

test.multiply()
print(test.table)