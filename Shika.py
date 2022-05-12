import json
import random
import socket
from game import possibleMoves

# on est le client IA
s = socket.socket()
address = ('localhost', 3000)  # port du prof
s.connect(address)
request = {
    "request": "subscribe",
    "port": 8880,     # numero de port choisi par nous
    "name": "shika",
    "matricules": ["195163", "195190"]
}
# message qu'on envoie au serveur qui contient les données d'inscription
message = json.dumps(request).encode()
s.send(message)
reponse = s.recv(2048).decode()  # on ecoute la reponse du serveur
print("reponse:", reponse)
s.close()

# les roles s'inversent, on devient le serveur jeu

s = socket.socket()
s.bind(('0.0.0.0', 8880))
s.listen()


def bestmove(possibleM):

# creation d'une liste avec poids arbitraire pour chaque position
    listpoids = [
        30,   5,  25,  25,   25,  25,    5, 30,
        5,    1,  10,  10,   10,  10,    1,  5,
        25,  10,  20,  15,   15,  20,   10, 25,
        25,  10,  15,  20,   20,  15,   10, 25,
        25,  10,  15,  20,   20,  15,   10, 25,
        25,  10,  20,  15,   15,  20,   10, 25,
        5,    1,   10,  10,   10,  10,   1,   5,
        30,   5,  25,  25,   25,  25,   5,  30,
    ]

    pmax = 0
    for elem in possibleM: # pour parcourt la liste de possibleMove
        if (pmax < listpoids[elem]): # elemMax contient le mouvement qui aura le poids le plus élevé

            elemMax = []
            pmax = listpoids[elem]
            elemMax.append(elem)

        elif (pmax == listpoids[elem]): #elemMax contient tout les mouvements qui ont un poids maximal

            elemMax.append(elem)

    return random.choice(elemMax)


while True:
    client, address = s.accept()
    with client:
        message = json.loads(client.recv(2048).decode())
        print(message)

        if message == {'request': 'ping'}:
            client.send(json.dumps({'response': 'pong'}).encode())
# dictionnaire qu on transforme en json avec dumps puis qu on transforme en binaire avec encode pour pouvoire l'envoyer au client

        else:
            # liste pour recuper la clé state du dictionnaire
            etat = message['state']
            possible = possibleMoves(etat)
            if possible != []:
                the_move_played = bestmove(possible)

                print('shika: ')
                print(possible)
                print(the_move_played)

                client.send(json.dumps({
                    "response": "move",
                    "move": the_move_played,
                    "message": "let's play"
                }).encode())
            else:
                the_move_played = None
                client.send(json.dumps({
                    "response": "move",
                    "move": the_move_played,
                    "message": "let's play"
                }).encode())
