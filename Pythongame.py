# Créé par hlone, le 28/11/2023 en Python 3.7
class Puissance4:
    def __init__(self):
        startvalue = 0
        self.tab = {}
        for i in range(6):
            self.tab = {i+1 : startvalue}

    def Show(self):
        print(self.tab)

g = Puissance4()
g.Show()