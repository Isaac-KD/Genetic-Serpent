class Snake():
    def __init__(self,taille=3):
        self.taille = taille
        self.nbPommeManger = 0
        self.corp=[]
        
    def affiche(self):
        print(self.corp)
    def intialize(self,tete,corp,queu):
        self.corp=[tete,corp,queu]
        
    def gauche(self,i):
        self.corp[i]=(self.corp[i][0]-1,self.corp[i][1])
    
    def droit(self,i):
        self.corp[i]=(self.corp[i][0]+1,self.corp[i][1])
        
    def devant(self,i):
        self.corp[i]=(self.corp[i][0],self.corp[i][1]+1)
    
    def ajoute(self,x,y):
        self.taille+=1
        self.corp.insert(0,(x,y))
        
        
if __name__ == "__main__":
    snake = Snake()
    snake.intialize((0,0),(0,1),(0,2))
    snake.affiche()
    snake.droit(0)
    snake.affiche()
    snake.gauche(0)
    snake.affiche()
    snake.avance(0)
    snake.affiche()