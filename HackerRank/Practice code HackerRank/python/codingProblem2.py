aliceArray = [3,4,5]
bobArray = [1,2,9]
aliceScore = 0
bobScore = 0
scoreBoard = []

for x,y in zip(aliceArray,bobArray):
    if(x>y):
        aliceScore +=1
    elif(x==y):
        pass
    else:
        bobScore +=1

scoreBoard.append(aliceScore);
scoreBoard.append(bobScore);
print(scoreBoard)
