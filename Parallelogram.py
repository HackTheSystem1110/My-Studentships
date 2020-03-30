
# Right Slash
def RightSlash():
    print("/",end="") # End is None


# Left Slash
def LeftSlash():
    print("\\",end="") # End is none and \\ for Reverse-Slash "\" is SyntaxError
# Space
def Space(Val):
    for i in range(Val):
        print(" ",end="") # End is None

# New Line
def NewLine():
    print() # Simple Jump to New Line


def TopTrigonal(Val=20):
    StSp = Val//2-1 #StartSpace
    for i in range(Val//2):
        Space(StSp-i)
        RightSlash()
        Space(i*2)
        LeftSlash()
        NewLine()
def BotTrigonal(Val=20):
    StSp = Val-2 #Start-Space
    for i in range(Val//2):
        Space(i)
        LeftSlash()
        Space(StSp - (i*2))
        RightSlash()
        NewLine()
def Parallelogram(): # Make The Common-Caller
    TopTrigonal() # Make Top of Parallelogram
    BotTrigonal() # Make Bot of Parallelogram
Parallelogram() # Make 20 Value Parallelogram...
