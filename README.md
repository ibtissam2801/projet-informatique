Mon IA : Shika.py

Nous avons créer une IA du nom de shika possèdant une stratégie simple permettant de battre RANDOM.
Le principe même est d'attribué des poids en fonction des positions sur le plateau 
En jouant à othello maintes fois, nous avons conclu que certaines positions étaient beaucoup plus favorables à d'autres
Pour commencer, les coins nous permettent




Explication des bibliothèques 
Notre premier import est json: cette bibliothèque nous permet d'envoyer et de recevoir les messages du server sous format json
ensuite nous importons socket, qui lui, nous permet simplement de faire les connexions réseaux
puis vient le import game. cette bibliothèque nous permet d'appeler le fichier python que nous avons renommé game où nous avons décider de