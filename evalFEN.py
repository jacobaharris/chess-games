from stockfish import Stockfish


def main():
    stockfish = Stockfish(path="/usr/local/Cellar/stockfish/15/bin/stockfish",
                          depth=18)
    stockfish.update_engine_parameters({"Hash":512})
main()
