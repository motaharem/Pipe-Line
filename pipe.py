from pygame import *
from pygame import gfxdraw
from random import sample,choice
from util import *
import copy
init()
FONT = font.Font(font.get_default_font(),50)

class Case(Rect):
        ''
        CASE = Surface((61,61))
        CASE.set_colorkey((1,1,1))
        CASERECT = CASE.get_rect()
        gfxdraw.filled_circle(CASE,30,30,30,(200,200,200))
        gfxdraw.aacircle(CASE,30,30,30,(200,200,200))
        def __init__(self,x,y,joncs):
                self.jonction = [0,0,0,0]
                self.marqueur = False
                self.image = Case.CASE.copy()
                S = sample(((Case.CASERECT.midtop,0),(Case.CASERECT.midright,1),(Case.CASERECT.midbottom,2),(Case.CASERECT.midleft,3)),3)[:choice((2,3))]
                if joncs[0]==1:
                        draw.line(self.image,(1,1,1),(30,30),Case.CASERECT.midtop,9)
                        self.jonction[0] = 1
                if joncs[1]==1:
                        draw.line(self.image,(1,1,1),(30,30),Case.CASERECT.midright,9)
                        self.jonction[1] = 1
                if joncs[2]==1:
                        draw.line(self.image,(1,1,1),(30,30),Case.CASERECT.midbottom,9)
                        self.jonction[2] = 1
                if joncs[3]==1:
                        draw.line(self.image,(1,1,1),(30,30),Case.CASERECT.midleft,9)
                        self.jonction[3] = 1
                
                Rect.__init__(self,SCREEN.blit(self.image,(x,y)))

        def rotate(self,dir):
                dir -= 2
                if dir == 1:
                        self.jonction.insert(0,self.jonction.pop())
                else:
                        self.jonction.append(self.jonction.pop(0))
                display.update(self)
                time.wait(40)
                self.image = transform.rotate(self.image,-90*dir)

###############################################################################
def HowToReturnPath(x,end,start,array2d):
        #path = [(2,3),(0,3)]

        #::DFS::
        #visited=[]
        #for i in range(len(array2d)):
        #        visited.append(False)
        #Q=Stack()
        #depthFirstSearch(x,end,[start,2],array2d,visited,Q)

        #::manhattan::
        visited=[]
        parent=[]
        for i in range(len(array2d)):
               visited.append(False)        
        for i in range(len(array2d)):
                parent.append([0,2])
        q = Stack()
        path = []
        q = manhattanHeuristicFunction(x,start,end,[start,2],array2d,visited,parent)
        while(q.isEmpty()!= True):
                path.append(q.pop)

        for i in range(path.len()):
                print("::",i)
        
        #::huristic::
        #visited=[]
        #parent=[]
        #for i in range(len(array2d)):
        #       visited.append(False)        
        #for i in range(len(array2d)):
        #        parent.append([0,2])
        #q = Stack()
        #q = heuristicFunction(x,start,end,[start,2],array2d,visited,parent)
        #while(q.isEmpty()!= True):
        #        print("!",q.pop())

        #::Astar::
        #visited=[]
        #parent=[]
        #for i in range(len(array2d)):
        #       visited.append(False)        
        #for i in range(len(array2d)):
        #        parent.append([0,2])
        #q = Stack()
        #g = 0
        #q = aStarSearch(x,start,end,[start,2],array2d,visited,parent,g)
        #path = []
        #while(q.isEmpty()!= True):
        #        path.append(q.pop)

        return path

# DFS ########################################################################        
def checkPath(Q, array2d):
        answer = False
        Q1=Stack()
        
        end = Q.pop()
        Q1.push(end)
        this = end
        temp = []         
        while(Q.isEmpty()==False):
                print ("####")
                for i in range(4):
                        temp[i] = array2d[this[0]][i]
                if(this[1]==1):
                        leftshift(temp)
                if(this[1]==3):
                        rightshift(temp)
                nextnode = Q.pop()
                Q1.push(nextnode)
                
                if(nextnode[0]==temp[0]+x):#down
                        if(temp[2]==1):
                                if(nextnode[1]==2 and array2d[nextnode[0]][0]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==3 and array2d[nextnode[0]][3]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==1 and array2d[nextnode[0]][1]==1):
                                        this=nextnode
                                        continue
                                else:
                                        break
                        else:
                                break
                        
                if(nextnode[0]==temp[0]+1):#right
                        if(temp[1]==1):
                                if(nextnode[1]==2 and array2d[nextnode[0]][3]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==3 and array2d[nextnode[0]][2]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==1 and array2d[nextnode[0]][0]==1):
                                        this=nextnode
                                        continue
                                else:
                                        break
                        else:
                                break
                                
                if(nextnode[0]==temp[0]-1):#left
                        if(temp[3]==1):
                                if(nextnode[1]==2 and array2d[nextnode[0]][1]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==3 and array2d[nextnode[0]][0]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==1 and array2d[nextnode[0]][2]==1):
                                        this=nextnode
                                        continue
                                else:
                                        break
                        else:
                                break
                                
                if(nextnode[0]==temp[0]-x):#up
                        if(temp[0]==1):
                                if(nextnode[1]==2 and array2d[nextnode[0]][2]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==3 and array2d[nextnode[0]][1]==1):
                                        this=nextnode
                                        continue
                                elif(nextnode[1]==1 and array2d[nextnode[0]][3]==1):
                                        this=nextnode
                                        continue
                                else:
                                        break
                        else:
                                break
        if(Q.isEmpty()):
                answer = True
        while(Q1.isEmpty()==False):
                Q.push(Q1.pop())
        return answer

def leftshift(jonction):
        temp = jonction[0]
        for i in range(3):
                jonction[i]=jonction[i+1]
        jonction[3] = temp
        return

def rightshift(jonction):
        temp = jonction[3]
        for i in range(1,4):
                jonction[i+1]=jonction[i]
        jonction[0] = temp
        return

def printPath(Q):
        print ("Q:")
        Q1=Stack()
        while(Q.isEmpty()==False):
                temp =Q.pop()
                print(temp)
                Q1.push(temp)
        while(Q1.isEmpty()==False):
                Q.push(Q1.pop())

def depthFirstSearch(x,end,start,array2d,visited,Q):###add Q :D
        visited[start[0]]=True
        Q.push(start)
        #print ("*start:",start)
        if (start[0]==end):###########do sth
                #visited[start[0]]=False
                if(checkPath(Q,array2d)):
                        printPath(Q)
                return
        
        if(start[0]%x!=0  and visited[start[0]-1]==False ):
                        depthFirstSearch(x,end,[start[0]-1 ,2],array2d,visited,Q)
                        Q.pop()
                        visited[start[0]-1]=False
                        if(start[0]-1!=end):
                                depthFirstSearch(x,end,[start[0]-1 ,3],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]-1]=False
                                depthFirstSearch(x,end,[start[0]-1 ,1],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]-1]=False
  
        if(start[0]%x!=(x-1)  and visited[start[0]+1]==False ):
                        depthFirstSearch(x,end,[start[0]+1 ,2],array2d,visited,Q)
                        Q.pop()
                        visited[start[0]+1]=False
                        if(start[0]+1!=end):
                                depthFirstSearch(x,end,[start[0]+1 ,1],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]+1]=False
                                depthFirstSearch(x,end,[start[0]+1 ,3],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]+1]=False
                        
        if(start[0]>= x  and visited[start[0]-x]==False ):
                        depthFirstSearch(x,end,[start[0]-x ,2],array2d,visited,Q)####maybe have changes
                        Q.pop()
                        visited[start[0]-x]=False
                        if(start[0]-x!=end):
                                depthFirstSearch(x,end,[start[0]-x ,1],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]-x]=False
                                depthFirstSearch(x,end,[start[0]-x ,3],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]-x]=False
                        
        if(start[0]+x<(x*x)  and visited[start[0]+x]==False ):
                        depthFirstSearch(x,end,[start[0]+x ,2],array2d,visited,Q)
                        Q.pop()
                        visited[start[0]+x]=False
                        if(start[0]+x!=end):
                                depthFirstSearch(x,end,[start[0]+x ,1],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]+x]=False
                                depthFirstSearch(x,end,[start[0]+x ,3],array2d,visited,Q)
                                Q.pop()
                                visited[start[0]+x]=False
                                
        return 
#########################################################################################
def breadthFirstSearch():
        return [] 
def iterativeDeepeningSearch():
        return []
def uniformCostSearch():
        return []
######################################################################################
# moshtarak manhatatan v huristic
def returnPath(parent,s,end,x):
        q = Stack()
        this = parent[end]
        q.push([end,2])
        
        while(this[0]!=s):
                q.push(this)
                this = parent[this[0]]
        if(this[0]==s):
                q.push([s,2])
        return q
####################################################################################3                
def manhattanDistance(a,b,x):
        if(a>b):
                row =(a%x)-(b%x)
                column =((a-(a%x))-(b-(b%x)))/(x*x)
        else:
                row =(b%x)-(a%x)
                column =((b-(b%x))-(a-(a%x)))/(x*x)        
        return (row+column)
                
def manhattanHeuristicFunction(x,s,end,start,array2d,visited,parent):
        visited[start[0]] = True
        Q = PriorityQueue()

        if (start[0]==end):#sharte tavaghof
                q = Stack()
                q = returnPath(parent,s,end,x)
                print("How many times !??")
                return q

        #shenasayi farzandan
        if(start[0]%x!=0  and visited[start[0]-1]==False ):#left cell
                if(array2d[start[0]][3]==1):
                        if(array2d[start[0]-1][1]==1):
                                Q.push([start[0]-1,2], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]-1][0]==1):
                                Q.push([start[0]-1,3], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]-1][2]==1)   :
                                Q.push([start[0]-1,1], manhattanDistance(start[0]-1,end,x))
        if(start[0]%x!=(x-1)  and visited[start[0]+1]==False ):#right cell
                if(array2d[start[0]][1]==1):
                        if(array2d[start[0]+1][3]==1):
                                Q.push([start[0]+1,2], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]+1][2]==1):
                                Q.push([start[0]+1,3], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]+1][0]==1):
                                Q.push([start[0]+1,1], manhattanDistance(start[0]-1,end,x))
        if(start[0]>= x  and visited[start[0]-x]==False ):#top cell
                if(array2d[start[0]][0]==1):
                        if(array2d[start[0]-x][2]==1):
                                Q.push([start[0]-x,2], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]-x][1]==1):
                                Q.push([start[0]-x,3], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]-x][3]==1):
                                Q.push([start[0]-x,1], manhattanDistance(start[0]-1,end,x))
        if(start[0]+x<(x*x)  and visited[start[0]+x]==False ):#down cell
                if(array2d[start[0]][2]==1):
                        if(array2d[start[0]+x][0]==1):
                                Q.push([start[0]+x,2], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]+x][3]==1):
                                Q.push([start[0]+x,3], manhattanDistance(start[0]-1,end,x))
                        if(array2d[start[0]+x][1]==1):
                                Q.push([start[0]+x,1], manhattanDistance(start[0]-1,end,x))
        if(Q.isEmpty()):
                return Stack()

        #backtarcking ruye farzandan
        while(Q.isEmpty()!=True):
                nextt = Q.pop()
                parent[nextt[0]] = start
                p = Stack()
                p = manhattanHeuristicFunction(x,s,end,nextt,array2d,visited,parent)
                if(p.isEmpty()==False):
                        return p
                visited[nextt[0]] = False
        
        return Stack()
#################################################################################################
def Distance(a,b,x):
        if(a>b):
                row =(a%x)-(b%x)
                column =((a-(a%x))-(b-(b%x)))/(x*x)
        else:
                row =(b%x)-(a%x)
                column =((b-(b%x))-(a-(a%x)))/(x*x)        
        return (row+column)
                
def heuristicFunction(x,s,end,start,array2d,visited,parent):
        visited[start[0]] = True
        Q = PriorityQueue()

        if (start[0]==end):#sharte tavaghof
                q = Stack()
                q = returnPath(parent,s,end,x)
                return q

        #shenasayi farzandan
        if(start[0]%x!=0  and visited[start[0]-1]==False ):#left cell
                if(array2d[start[0]][3]==1):
                        if(array2d[start[0]-1][1]==1):
                                Q.push([start[0]-1,2], Distance(start[0]-1,end,x))
                        if(array2d[start[0]-1][0]==1):
                                Q.push([start[0]-1,3], Distance(start[0]-1,end,x)+1)
                        if(array2d[start[0]-1][2]==1)   :
                                Q.push([start[0]-1,1], Distance(start[0]-1,end,x)+1)
        if(start[0]%x!=(x-1)  and visited[start[0]+1]==False ):#right cell
                if(array2d[start[0]][1]==1):
                        if(array2d[start[0]+1][3]==1):
                                Q.push([start[0]+1,2], Distance(start[0]-1,end,x))
                        if(array2d[start[0]+1][2]==1):
                                Q.push([start[0]+1,3], Distance(start[0]-1,end,x)+1)
                        if(array2d[start[0]+1][0]==1):
                                Q.push([start[0]+1,1], Distance(start[0]-1,end,x)+1)
        if(start[0]>= x  and visited[start[0]-x]==False ):#top cell
                if(array2d[start[0]][0]==1):
                        if(array2d[start[0]-x][2]==1):
                                Q.push([start[0]-x,2], Distance(start[0]-1,end,x))
                        if(array2d[start[0]-x][1]==1):
                                Q.push([start[0]-x,3], Distance(start[0]-1,end,x)+1)
                        if(array2d[start[0]-x][3]==1):
                                Q.push([start[0]-x,1], Distance(start[0]-1,end,x)+1)
        if(start[0]+x<(x*x)  and visited[start[0]+x]==False ):#down cell
                if(array2d[start[0]][2]==1):
                        if(array2d[start[0]+x][0]==1):
                                Q.push([start[0]+x,2], Distance(start[0]-1,end,x))
                        if(array2d[start[0]+x][3]==1):
                                Q.push([start[0]+x,3], Distance(start[0]-1,end,x)+1)
                        if(array2d[start[0]+x][1]==1):
                                Q.push([start[0]+x,1], Distance(start[0]-1,end,x)+1)
        if(Q.isEmpty()):
                return Stack()

        #backtarcking ruye farzandan
        while(Q.isEmpty()!=True):
                nextt = Q.pop()
                parent[nextt[0]] = start
                p = Stack()
                p = heuristicFunction(x,s,end,nextt,array2d,visited,parent)
                if(p.isEmpty()==False):
                        return p
                visited[nextt[0]] = False
        
        return Stack()
#################################################################################################
def huristic(a,b,x,direct):
        if(a>b):
                row =(a%x)-(b%x)
                column =((a-(a%x))-(b-(b%x)))/(x*x)
        else:
                row =(b%x)-(a%x)
                column =((b-(b%x))-(a-(a%x)))/(x*x)
        distance = row+column
        if(direct!=2):
                return(distance+1)
        else:
                return(direct)
                
def aStarSearch(x,s,end,start,array2d,visited,parent,g):
        visited[start[0]] = True
        Q = PriorityQueue()
        if(start[1]!=2):
                g = g+2
        else:
                g = g+1
        
        if (start[0]==end):#sharte tavaghof
                q = Stack()
                q = returnPath(parent,s,end,x)
                return q

        #shenasayi farzandan
        if(start[0]%x!=0  and visited[start[0]-1]==False ):#left cell
                if(array2d[start[0]][3]==1):
                        if(array2d[start[0]-1][1]==1):
                                Q.push([start[0]-1,2], huristic(start[0]-1,end,x,2)+g)
                        if(array2d[start[0]-1][0]==1):
                                Q.push([start[0]-1,3], huristic(start[0]-1,end,x,3)+g)
                        if(array2d[start[0]-1][2]==1)   :
                                Q.push([start[0]-1,1], huristic(start[0]-1,end,x,1)+g)
        if(start[0]%x!=(x-1)  and visited[start[0]+1]==False ):#right cell
                if(array2d[start[0]][1]==1):
                        if(array2d[start[0]+1][3]==1):
                                Q.push([start[0]+1,2], huristic(start[0]-1,end,x,2)+g)
                        if(array2d[start[0]+1][2]==1):
                                Q.push([start[0]+1,3], huristic(start[0]-1,end,x,3)+g)
                        if(array2d[start[0]+1][0]==1):
                                Q.push([start[0]+1,1], huristic(start[0]-1,end,x,1)+g)
        if(start[0]>= x  and visited[start[0]-x]==False ):#top cell
                if(array2d[start[0]][0]==1):
                        if(array2d[start[0]-x][2]==1):
                                Q.push([start[0]-x,2], huristic(start[0]-1,end,x,2)+g)
                        if(array2d[start[0]-x][1]==1):
                                Q.push([start[0]-x,3], huristic(start[0]-1,end,x,3)+g)
                        if(array2d[start[0]-x][3]==1):
                                Q.push([start[0]-x,1], huristic(start[0]-1,end,x,1)+g)
        if(start[0]+x<(x*x)  and visited[start[0]+x]==False ):#down cell
                if(array2d[start[0]][2]==1):
                        if(array2d[start[0]+x][0]==1):
                                Q.push([start[0]+x,2], huristic(start[0]-1,end,x,2)+g)
                        if(array2d[start[0]+x][3]==1):
                                Q.push([start[0]+x,3], huristic(start[0]-1,end,x,3)+g)
                        if(array2d[start[0]+x][1]==1):
                                Q.push([start[0]+x,1], huristic(start[0]-1,end,x,1)+g)
        if(Q.isEmpty()):
                return Stack()

        #backtarcking ruye farzandan
        while(Q.isEmpty()!=True):
                nextt = Q.pop()
                parent[nextt[0]] = start
                p = Stack()
                p = aStarSearch(x,s,end,nextt,array2d,visited,parent,g)
                if(p.isEmpty()==False):
                        return p
                visited[nextt[0]] = False
        
        return Stack()
###################################################################################################
score = 0
x = 3   #Number of blocks in x
y = 3  #Number of blocks in y
#s=Stack()
#Each block is 61*61
SCREEN = display.set_mode((61*x,61*y))
SRECT = SCREEN.get_rect()
with open('input.dat') as file:
    array2d = [[int(digit) for digit in line.split()] for line in file]
print array2d
ALLS = []
for i in range(x*y):
        ALLS.append(Case(61*(i%x),61*(i/x),array2d[i]))
START = choice(range(x*y)[::x])
gfxdraw.filled_circle(ALLS[START].image,30,30,30,(200,0,0))
gfxdraw.aacircle(ALLS[START].image,30,30,30,(200,0,0))
SCREEN.blit(ALLS[START].image,ALLS[START])
ALLS[START].jonction = [1,1,1,1]
END = choice(range(x*y)[x-1::x])
#print ("end:",END)
gfxdraw.filled_circle(ALLS[END].image,30,30,30,(0,0,200))
gfxdraw.aacircle(ALLS[END].image,30,30,30,(0,0,200))
SCREEN.blit(ALLS[END].image,ALLS[END])
ALLS[END].jonction = [1,1,1,1]
for i in sample(ALLS,x*y): #Animation
        time.wait(10)
        display.update(i)

event.clear()
event.post(event.Event(MOUSEBUTTONDOWN,{'button':1,'pos':(0,0)}))
coup = 0 #Number of iterations
display.set_caption('AI Project')
time.wait(999)

        
#path =
HowToReturnPath(x,END,START,array2d) #Your defined fnction
path=[(2,1),(1,1)]
for c in path:
        coup += 1
        ALLS[c[0]].rotate(c[1])
        for i in ALLS:
                i.marqueur = False
                SCREEN.fill(0,i)
                SCREEN.blit(i.image,i)
        temp = [START]
        ALLS[START].marqueur = True
        while temp:
                for case in temp:
                        for e,j in enumerate(ALLS[case].jonction):
                                if j and SRECT.contains(ALLS[case].move(((0,-61),(61,0),(0,61),(-61,0))[e]))\
                                and ALLS[case+(-x,1,x,-1)[e]].marqueur == False\
                                and ALLS[case+(-x,1,x,-1)[e]].jonction[e-2]\
                                and case != END:
                                        temp.append(case+(-x,1,x,-1)[e])
                                        ALLS[case+(-x,1,x,-1)[e]].marqueur = True
                                        SCREEN.fill(0xf00000,ALLS[case+(-x,1,x,-1)[e]])
                                        SCREEN.blit(ALLS[case+(-x,1,x,-1)[e]].image,ALLS[case+(-x,1,x,-1)[e]])
                        temp.remove(case)
        display.update()
        time.wait(999)
print coup
for i in sample(ALLS,len(ALLS)):
        SCREEN.fill(0,i)
        time.wait(10)
        display.update(i)
        


