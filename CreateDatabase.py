import lichess.api
from lichess.format import PGN
import json

def getToken():
    file = open('/Users/admin/Desktop/Lichess/Token.txt','r')
    token = file.read()
    return str(token)

def main():
    token = getToken()
    mygames = list(lichess.api.user_games('jacobaharris',auth=token,rated=True,
                                     format=PGN))
    mygames.reverse()
    with open('/Users/admin/Desktop/Lichess/data.pgn','w') as f:
        for i in mygames:
            print(i, file = f)
main()
