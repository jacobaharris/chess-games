from stockfish import Stockfish
import timeit
import random

def main():
    #create stockfish instances
    #test 1 depth at a time, want to test ~15-20 as depth
    #test different hash sizes-128,256,512
    inDepth = int(input(prompt="Input Engine Depth:"))
    stock1 = Stockfish(path="/usr/local/Cellar/stockfish/15/bin/stockfish",
                       depth=inDepth,
                       parameters={"Hash":128})
    stock2 = Stockfish(path="/usr/local/Cellar/stockfish/15/bin/stockfish",
                       depth=inDepth,
                       parameters={"Hash":256})
    stock3 = Stockfish(path='/usr/local/Cellar/stockfish/15/bin/stockfish",
                       depth=inDepth,
                       parameters={"Hash":512})
    #create list of fens to sample from
    fens = open('/Users/admin/Desktop/Lichess/FENeval.txt','r')
    fenList = []
    for line in fens:
        fenList.append(line.split(':')[0])
    fens.close()
    randList = []
    while len(randList)<10:
        a = random.randint(0,len(fensList))
        if a in randList:
            continue
        else:
            randList.append(a)
    
        
main()
