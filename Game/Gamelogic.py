import Gamemode as gm

#Functions that make up the gameplay when combined togther.
class Puissance4:
    def __init__(self):
        self.Val = 0
        self.table = []
        self.freespace = 0
        self.taken = 0

    def CreateEmpty(self):
            for l in range(7):
                tempval = l
                self.table.append([])
                for n in range(6):
                    self.table[tempval].append(0)
            return self.table
    
    def Organize(self):
         for indnum in range(7):
              print(self.table[indnum])

    def Checkmatch(self):
         checktemp = 0
         for c in range(7):
              if self.table[c][self.Val] == 1:
                   checktemp += 1
                   if checktemp == 4:
                        return True
              elif self.table[c][self.Val] == 2:
                   checktemp = 0
                   return False
              else:
                   return False
              

    def Taken(self):
         for t in range(7):   
            if self.table[t][self.Val] == 0:
                 self.freespace += 1
            else:
                 self.taken += 1
         if self.freespace > self.taken:
              return False,self.freespace
         else:
              return True,self.taken
         
    def Modify(self):
         if self.Taken == False:
              self.table[self.freespace][self.Val] = 1
              return self.table
         else:
              self.table[6-self.taken][self.Val] = 1
              return self.table
              

    def UserInput(self):
            temp =  int(input("(Value range from 0 to 5),User Value: "))
            self.Val = temp
    

test = Puissance4()

def Game(tab):
     tab.CreateEmpty()
     tab.Organize()
     while tab.Checkmatch() == False:
          tab.taken = 0
          tab.UserInput()
          tab.Taken()
          tab.Modify()
          tab.Checkmatch()
          tab.Organize()
          if tab.Checkmatch() == True:
               print('You won.')

Game(test)