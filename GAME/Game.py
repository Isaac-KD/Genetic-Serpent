from Map import Map
from Snake import Snake

class SnakeGame ():
    def __init__ (self,taille,c):
        self.taille = taille
        self.centre = c
        self.snake = Snake()
        self.snake.intialize((c,c),(c,c-1),(c,c-2))
        self.map = Map(taille)
        
    def affiche(self):
        self.map.affiche()
        
if __name__ == '__main__':
    game = SnakeGame(9,4)
    game.affiche()
    
    
        
