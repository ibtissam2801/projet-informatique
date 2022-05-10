Mon IA : Shika.py
Matricules: 195163 195190

Nous avons créé une intelligence artificielle pour othello portant le nom de shika. En ce qui concerne notre stratégie de jeu, nous voulions à la base opter pour une stratégie qui se baserait sur le fait de retourner le plus de pions possibles à chaque tour. Mais après plusieurs recherches, nous nous sommes rendu compte que ce n'était pas une bonne idée car un pion peut potentiellement retourner jusqu'à 18 autres pions et donc renverser le cours de la partie. C'est pour cela que notre stratégie se base plutot sur l'acquisition de pions stables. La stabilité d'un pion dans le jeu Othello est définie par la probabilité qu'il a de se retourner au fil de la partie. Nous avons distingué 3 types de stabilité différents qu'on a chacuns fait correspondre à un score.

    1) Stable --> Ce pion ne sera jamais retourné ! Ex.: les coins ----> 15 points
    2) Semi-stable --> Il est possible que ce pion soit retourné au fil de la partie. EX. les bords et le centre ---> 10 points 
    3) Instable --> Ce pion peut être retourné à l'instant même ou l'adversaire va jouer. Ex. : le 6x6 ---> 5 points

Ensuite, en expérimentant plusieurs fois le jeu nous avons attribué un score à chacune des positons du plateau et nous en avons fait un tableau. Notre fonction Bestmove se charge de parcourir la liste des coups legaux et de les faire correspondre avec leur score. Ensuite, elle les compare entre eux et retourne la position qui correspond au score maximale.(une fonction possiblemove se charge de determiner les coups legaux).

Toutes nos fonctions sont regroupées dans un fichier que nous avons appelé game.py. Nous avons importé ce dernier dans le code de notre intelligence artificielle.
Nous avons également importé d'autres bibliothèques tel que le socket car notre IA communique en réseau avec le serveur du jeu. Le contenu des messages se fait sous le format JSON nous devions donc également importer la bibliotheque JSON. Et enfin,nous utilisons la bibliothèque pytest pour effectuer des test unitaires.