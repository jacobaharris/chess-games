from stockfish import Stockfish


def main():
    stockfish = Stockfish(path="/usr/local/Cellar/stockfish/15/bin/stockfish",
                          depth=25,
                          parameters={"Hash":128,"Threads":4})
    fens = open('/Users/admin/Desktop/chess-games/FENeval.txt','r')
    fenlist = []
    for line in fens:
        entry = line.rstrip('\n')
        entry = list(line.split(":"))
        fenlist.append(entry)
    fens.close()
    for i in fenlist:
        if len(i) == 2:
            stockfish.set_fen_position(i[0])
            stockeval = stockfish.get_evaluation()
            i.append(stockeval['type'])
            i.append(stockeval['value'])
    with open('/Users/admin/Desktop/chess-games/FENeval.txt','w') as f:
        for l in fenlist:
            print(l, file = f)
main()
