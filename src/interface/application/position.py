from application.deplacement import deplacement_couleur,movementDirection

class Position:
    def __init__(self,nom,taille_tableau):
        self.nom=nom
        self.x=0
        self.y=2
        self.tableau = [["black"] * taille_tableau for _ in range(taille_tableau)]

    def getCurrentPosition(self):
        return(self.x,self.y)
    
    def updatePositionByValues(self,deplacement,color):
        self.updateTableau(color)
        self.x,self.y=deplacement

    def updatePosition(self,deplacement):
        self.updateTableau(deplacement)
        if (deplacement=="green" or deplacement=="ligtblue"):
            self.x+=1
        elif deplacement=="yellow":
            self.x+=-1
        elif deplacement=="pink":
            self.y+=1
        elif deplacement=="blue":
            self.y+=-1
    
    def updateTableau(self,color):
        (x,y)=self.getCurrentPosition()
        if color!="black":
            self.tableau[x][y]=color
    def getTableau(self):
        return self.tableau
    def getEnd(self):
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau)):
                if self.tableau[i][j]=="red":
                    return (i,j)
    def getStart(self):
        for i in range(len(self.tableau)):
            for j in range(len(self.tableau)):
                if self.tableau[i][j]=="lightblue":
                    return (i,j)
    def readTableau(self,myMarty):
        self.x,self.y=self.getStart()
        fin=self.getEnd()
        while((self.x,self.y)!=fin):
            color=self.tableau[self.x][self.y]
            self.updatePosition(color)
            movement = deplacement_couleur(color)
            movementDirection(myMarty,movement)
        


        