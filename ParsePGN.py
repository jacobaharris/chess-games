import chess.pgn
import csv

def main():
    PGN = open('/Users/admin/Desktop/chess-games/data.pgn')
    FEN = open('/Users/admin/Desktop/chess-games/FEN.txt','w')
    current = chess.pgn.read_game(PGN)
    board = current.board()
    pgnType = type(current)
    fens = dict()
    with open('/Users/admin/Desktop/chess-games/games.csv','w',newline='')as games:
        gameWriter = csv.writer(games)
        while type(current)==pgnType:
            board.reset()
            gameID = current.headers['Site'].replace('https://lichess.org/','')
            #write to game.txt
            gameInfo = [gameID,
                        current.headers['UTCDate'],
                        current.headers['UTCTime'],
                        current.headers['TimeControl'],
                        current.headers['Termination'],
                        current.headers['Result'],
                        current.headers['White'],
                        current.headers['WhiteElo'],
                        current.headers['WhiteRatingDiff'],
                        current.headers['Black'],
                        current.headers['BlackElo'],
                        current.headers['BlackRatingDiff']]
            gameWriter.writerow(gameInfo)
            #write to FEN.txt, update fens
            for move in current.mainline_moves():
                board.push(move)
                tempFEN = board.fen()
                FEN.write(str(gameID)+','+str(tempFEN)+'\n')
                if tempFEN in fens:
                    fens[tempFEN] += 1
                else:
                    fens[tempFEN] = 1
            current = chess.pgn.read_game(PGN)
    with open('/Users/admin/Desktop/chess-games/FENeval.txt','w') as f:
        for key,value in fens.items():
            f.write('%s:%s\n'%(key,value))
    PGN.close()
    FEN.close()
    f.close()
main()
