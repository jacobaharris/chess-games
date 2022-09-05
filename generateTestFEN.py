import random

#create a sample list of FENs to test different versions of Stockfish
def main():
    #open FENeval and get list of unique FENs
    fens = open('/Users/admin/Desktop/chess-games/FENeval.txt','r')
    fenList = []
    for line in fens:
        fenList.append(line.split(':')[0])
    fens.close()
    #create a list of FENs randomly selected without repitition
    randList = []
    sampleNum = 50
    randFEN = []
    while len(randList)<sampleNum:
        a = random.randint(0,len(fenList)-1)
        if a in randList:
            continue
        else:
            randList.append(a)
            randFEN.append(fenList[a])
    with open('/Users/admin/Desktop/chess-games/sampleFEN.txt','w') as f:
        for i in randFEN:
            print(i,file=f)
main()
