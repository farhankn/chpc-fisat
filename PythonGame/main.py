from random import choice,randint

grid = [[0]*8for n in range(8)]
move = ""

randomMoves = ['T', 'B', 'L', 'R']

class Player():
    name = ""
    posx = 0
    posy = 0
    move = ""
    health = 10
    ptype =""
    def __init__(self, name,posx,posy,ptype):
        self.name = name
        self.posx = posx
        self.posy = posy
        self.ptype = ptype

    def setPostion(self,posx,posy):
        self.posx = posx
        self.posy = posy
        if self.ptype == 'P':
            grid[posx][posy]='P'
        else:
            grid[posx][posy]='E'

    def movePlayer(self,mov):
        grid[self.posx][self.posy]=0
        if mov=='L':
            if self.posy==0:
                print "Error"
            else:
                self.posy=self.posy-1
        elif mov=='R':
            if self.posy==7:
                print "Error"
            else:
                self.posy=self.posy+1
        elif mov=='T':
            if self.posx==0:
                print "Error"
            else :
                self.posx=self.posx-1
        elif mov=='B':
            if self.posx==7:
                print "Error"
            else:
                self.posx=self.posx+1
        else:
            print "Invalid Move"
        self.setPostion(self.posx,self.posy);

    def gridDisplay(self):
        print "Player -> ",farhan.health,"Enemy -> ",enemy.health
        for i in range(0,8):
            for j in range(0,8):
                print grid[i][j],
            print


#Read Player Name and Parameters
farhan = Player("Farhan",1,1,'P')
enemy = Player("Enemy",randint(0,7),randint(0,7),'E')

while move != "q":
    move = raw_input("Enter the Move ")
    farhan.movePlayer(move)
    if (farhan.posx==enemy.posx and farhan.posy==enemy.posy):
        enemy.health=enemy.health-1
    enemy.movePlayer(choice(randomMoves))
    if farhan.posx==enemy.posx and farhan.posy==enemy.posy:
        farhan.health=farhan.health-1
    farhan.gridDisplay()
