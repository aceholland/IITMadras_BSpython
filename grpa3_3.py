#Print the Manhattan distance of the bot from the origin. 
x,y=0,0
move=input()
while move.lower()!="stop":
    if move.lower()=="up":
        y+=1
    if move.lower()=="down":
        y-=1
    if move.lower()=="left":
        x-=1
    if move.lower()=="right":
        x+=1

    move=input()

dist= abs(x)+abs(y)
print (dist)