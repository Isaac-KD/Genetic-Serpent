import random
from Snake import Snake
class Map():
    def __init__(self,taille):
        self.taille = taille
        self.map = [[0 for _ in range(taille)] for _ in range(taille)]
        self.snake = Snake()
        self.snake.intialize((4,4),(3,4),(5,4))
        

        
    def placepomme(self,x,y):
        if x> self.taille or y> self.taille or x<0 or y<0: raise ValueError("Invalid x and y")
        self.map[x][y] = 1
        
    def libereSnake(self):
        for i in self.snake.corp:
            self.map[i[0]][i[1]] = 1
        
    def placeSnake(self):
        for i in self.snake.corp:
            self.map[i[0]][i[1]] = -1
            
    def pommeAleatoire(self):
        while True:
            x = random.randint(0, self.taille - 1)  # Adjust to correct index range
            y = random.randint(0, self.taille - 1)
            if self.map[x][y] == 0:  # Check if the spot is free
                self.placepomme(x, y)
                return
        
    def affiche (self):
        self.libereSnake()
        self.placeSnake()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print("|"+str(self.map[j][i]),end ="|")
            print()

if __name__ == '__main__':
    map = Map(10)
    map.affiche()
    print("\ affiche pomme /")
    map.pommeAleatoire()
    map.affiche()