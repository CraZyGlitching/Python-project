import Gamemode as gm

#Functions that make up the gameplay when combined togther.
class Puissance4:
    def __init__(self):
        self.Val = 0
        self.table = []

    def CreateEmpty(self):
            for l in range(7):
                tempval = l
                self.table.append([])
                for n in range(6):
                    self.table[tempval].append(0)
            return self.table
    
    def Organize(self):
         for indnum in range(6):
              print(self.table[indnum])

    #def Checkmatch(self):

    def Taken(self):
         freespace = 0 ; taken = 0
         for t in range(7):   
            if self.table[t][self.Val] == 0:
                 freespace += 1
            else:
                 taken += 1
         if freespace > taken:
              return True
         elif freespace == taken:
              return 1
         else:
              return False
         
    #def Modify(self):
    #     if self.Taken == True:
         

    def User1Input(self):
            temp =  int(input("(Value range from 0 to 5),User Value: "))
            self.Val = temp
    

test = Puissance4()

test.CreateEmpty()
print(test.table)
test.Organize()
test.User1Input()
print(f'Value: {test.Val}')
