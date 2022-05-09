import json
import socket
import game

# on est le client IA
s = socket.socket() 
address = ('localhost',3000) # port du prof
s.connect(address)
request = {
      "request": "subscribe",
      "port": 8887,     # numero de port choisi par nous 
      "name": "shika",
      "matricules": ["195163", "195190"]
   }
message = json.dumps(request).encode() # message qu'on envoie au serveur qui contient les données d'inscription
s.send(message)
reponse = s.recv(2048).decode() # on ecoute la reponse du serveur
print("reponse:", reponse)
s.close()

#les roles s'inversent, on devient le serveur jeu

s = socket.socket() 
s.bind(('0.0.0.0',8887))
s.listen()
while True:
    client,address=s.accept()
    with client :
        message = json.loads(client.recv(2048).decode()) 
        print(message)

        if message == {'request': 'ping'}:
            client.send(json.dumps({'response':'pong'}).encode()) 
# dictionnaire qu on transforme en json avec dumps puis qu on transforme en binaire avec encode pour pouvoire l'envoyer au client
    
        else:
            etat = message['state'] #liste pour recuper la clé state du dictionnaire
            possibleMoves = game.possibleMoves(etat)
            the_move_played = game.bestmove(possibleMoves)
            print ('shika: ')
            print (possibleMoves)
            print(the_move_played)
            
            client.send(json.dumps( {
            "response": "move",
             "move": the_move_played ,
             "message": "let's play"
            }).encode())




       
