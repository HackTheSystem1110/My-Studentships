


# Right Slash
def RightSlash(Val):
    for i in range(Val):
        print("/",end="") # End is None


# Left Slash
def LeftSlash(Val):
    for i in range(Val):
        print("\\",end="") # End is none and \\ for Reverse-Slash "\" is SyntaxError
# Space
def Space(Val):
    for i in range(Val):
        print(" ",end="") # End is None

# New Line
def NewLine():
    print() # Simple Jump to New Line


def TopTrigonal(Val=0,Right=1,Left=1):
    StSp = Val//2-1 #StartSpace
    for i in range(Val//2):
        Space(StSp-i)
        RightSlash(Right)
        Space(i*2)
        LeftSlash(Left)
        NewLine()
def BotTrigonal(Val,Right=1,Left=1):
    StSp = Val-2 #Start-Space
    for i in range(Val//2):
        Space(i)
        LeftSlash(Left)
        Space(StSp - (i*2))
        RightSlash(Right)
        NewLine()
def Parallelogram(Val,Right=1,Left=1): # Make The Common-Caller
    TopTrigonal(Val,Right,Left) # Make Top of Parallelogram
    BotTrigonal(Val,Right,Left) # Make Bot of Parallelogram
while(True): #Endless Loop
    Parallelogram(20) # Make 20 Value Parallelogram...
