from stockfish import Stockfish


def main():
    stockfish = Stockfish(path="/usr/local/Cellar/stockfish/15/bin/stockfish",
                          depth=25,
                          parameters={"Hash":128,"Threads":4})
    
main()
