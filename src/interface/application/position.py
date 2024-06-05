class Position:
    def __init__(self,nom,taille_tableau):
        self.nom=nom
        self.x=0
        self.y=0
        self.tableau = [["Black"] * taille_tableau for _ in range(taille_tableau)]

    def getCurrentPosition(self):
        return(self.x,self.y)
    def updatePosition(self,deplacement):
        self.updateTableau(deplacement)
        if deplacement=="green":
            self.x+=1
        elif deplacement=="yellow":
            self.x+=-1
        elif deplacement=="pink":
            self.y+=1
        elif deplacement=="blue":
            self.y+=-1
    def updateTableau(self,color):
        (x,y)=self.getCurrentPosition()
        self.tableau[x][y]=color
    def getTableau(self):
        return self.tableau