class GameTypes:
    def __init__(self,Name :str,Description:str):
        self.name = Name
        self.description = Description

    def PrintGameType(self):
        print(f'Selected Mode:{self.name},\n Description:{self.description}')


TestGameType = GameTypes('Player versus Player','''In this mode two players play against one another to try to win.
The one who manages to align their numbers wins.(1 for Player one and 2 for player two.)''')

TestGameType.PrintGameType()