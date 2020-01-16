


# Right Slash
def RightSlash(Val):
    for i in range(Val):
        print("/",end="")


# Left Slash
def LeftSlash(Val):
    for i in range(Val):
        print("\\",end="")
# Space
def Space(Val):
    for i in range(Val):
        print(" ",end="")

# New Line
def NewLine():
    print()


def TopTrigonal(Val=0,Right=1,Left=1):
    StSp = Val//2-1
    for i in range(Val//2):
        Space(StSp-i)
        RightSlash(Right)
        Space(i*2)
        LeftSlash(Left)
        NewLine()
def BotTrigonal(Val,Right=1,Left=1):
    StSp = Val-2
    for i in range(Val//2):
        Space(i)
        LeftSlash(Right)
        Space(StSp - (i*2))
        RightSlash(Left)
        NewLine()
def Parallelogram(Val,Right=1,Left=1):
    TopTrigonal(Val,Right,Left)
    BotTrigonal(Val,Right,Left)
while(True):
    Parallelogram(20)
