import json
import socket
import random
import game

s = socket.socket() #on est le client IA
address = ('localhost',3000) #port du code du prof
s.connect(address)
request = {
      "request": "subscribe",
      "port": 8882,
      "name": "shogi",
      "matricules": ["12345", "67890"]
   }
message = json.dumps(request).encode() #message qu'on envoie au serveur qui contient les données d'inscription
s.send(message)
reponse = s.recv(2048).decode() #on ecoute la reponse du serveur
print("reponse:", reponse)
s.close()

s=socket.socket() #les roles s'inversent, on devient le serveur jeu
s.bind(('0.0.0.0',8882))#double parenthese car tuple
s.listen()
while True:
    client,address=s.accept()
    with client :
        message = json.loads(client.recv(2048).decode()) #fonction load pour decoder fichier json
        print(message)
#        client.send(json.dumps({'response':'pong'}).encode())#dictionnaire qu on transforme en json avec dumps puis qu on transforme en binaire avec encode pour pouvoire l'envoyer au client
        if message == {'request': 'ping'}:
            client.send(json.dumps({'response':'pong'}).encode())
        
        else:
            etat = message['state'] #liste pour recuper la clé state du dictionnaire
            possibleMoves = game.possibleMoves(etat)
            if possibleMoves != []:
                the_move_played = random.choice(possibleMoves)

                print ('shika: ')
                print (possibleMoves)
                print(the_move_played)
                
                client.send(json.dumps( {
                "response": "move",
                "move": the_move_played ,
                "message": "let's play"
                }).encode())
            else: 
                the_move_played = None
                client.send(json.dumps( {
                "response": "move",
                "move": the_move_played ,
                "message": "let's play"
                }).encode())




       