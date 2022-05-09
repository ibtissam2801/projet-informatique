class GameEnd(Exception):
	def __init__(self, lastState):
		self.__state = lastState

	@property
	def state(self):
		return self.__state

	def __str__(self):
		return 'Game Over'

class GameWin(GameEnd):
	def __init__(self, winner, lastState):
		super().__init__(lastState)
		self.__winner = winner

	@property
	def winner(self):
		return self.__winner

	def __str__(self):
		return super().__str__() + ': {} win the game'.format(self.winner)

class BadMove(Exception):
	pass

class GameDraw(GameEnd):
	def __init__(self, lastState):
		super().__init__(lastState)

	def __str__(self):
		return super().__str__() + ': Draw'

class GameLoop(GameDraw):
	def __init__(self, lastState):
		super().__init__(lastState)

	def __str__(self):
		return super().__str__() + ': Stopped because of lopping behavior'

class BadGameInit(Exception):
	pass


from unittest import removeResult

import copy

directions = [
    ( 0,  1),
    ( 0, -1),
    ( 1,  0),
    (-1,  0),
    ( 1,  1),
    (-1,  1),
    ( 1, -1),
    (-1, -1)
]

def add(p1, p2):
    l1, c1 = p1
    l2, c2 = p2
    return l1 + l2, c1 + c2

def coord(index):
    return index // 8, index % 8

def index(coord):
    l, c = coord
    return l*8+c

def isInside(coord):
    l, c = coord
    return 0 <= l < 8 and 0 <= c < 8

def walk(start, direction):
    current = start
    while isInside(current):
        current = add(current, direction)
        yield current

def isGameOver(state):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    res = False
    if len(possibleMoves(state)) == 0:
        state['current'] = otherIndex
        if  len(possibleMoves(state)) == 0:
            res = True
    state['current'] = playerIndex
    return res

def willBeTaken(state, move):
    playerIndex = state['current']
    otherIndex = (playerIndex+1)%2

    if not (0 <= move < 64):
        raise BadMove('Your must be between 0 inclusive and 64 exclusive')

    if move in state['board'][0] + state['board'][1]:
        raise BadMove('This case is not free')

    board = []
    for i in range(2):
        board.append(set((coord(index) for index in state['board'][i])))

    move = coord(move)

    cases = set()
    for direction in directions:
        mayBe = set()
        for case in walk(move, direction):
            if case in board[otherIndex]:
                mayBe.add(case)
            elif case in board[playerIndex]:
                cases |= mayBe
                break
            else:
                break

    if len(cases) == 0:
        raise BadMove('Your move must take opponent\'s pieces')
    
    return [index(case) for case in cases]

def possibleMoves(state):
    res = []
    for move in range(64):
        try:
            willBeTaken(state, move)
            res.append(move)
        except BadMove:
            pass
    return res

def Othello(players):
    # 00 01 02 03 04 05 06 07
    # 08 09 10 11 12 13 14 15
    # 16 17 18 19 20 21 22 23
    # 24 25 26 27 28 29 30 31
    # 32 33 34 35 36 37 38 39
    # 40 41 42 43 44 45 46 47
    # 48 49 50 51 52 53 54 55
    # 56 57 58 59 60 61 62 63

    state = {
        'players': players,
        'current': 0,
        'board': [
            [28, 35],
            [27, 36]
        ]
    }

    def next(state, move):
        newState = copy.deepcopy(state)
        playerIndex = state['current']
        otherIndex = (playerIndex+1)%2

        if len(possibleMoves(state)) > 0 and move is None:
            raise BadMove('You cannot pass your turn if there are possible moves')

        if move is not None:
            cases = willBeTaken(state, move)

            newState['board'][playerIndex].append(move)

            for case in cases:
                newState['board'][otherIndex].remove(case)
                newState['board'][playerIndex].append(case)
            
        newState['current'] = otherIndex

        if isGameOver(newState):
            if len(newState['board'][playerIndex]) > len(newState['board'][otherIndex]):
                winner = playerIndex
            elif len(newState['board'][playerIndex]) < len(newState['board'][otherIndex]):
                winner = otherIndex
            else:
                raise GameDraw(newState)
            raise GameWin(winner, newState)
        
        return newState

    return state, next

def bestmove(possibleMoves):
    listpoids = [
    15,   15,  10,  10,  10,   10,    15, 15,
    15,    5,   5,   5,    5,   5,    5,  15,
    10,    5,  10,  10,   10,  10,    5,  10, 
    10,    5,  10,  10,   10,  10,    5,  10,
    10,    5,  10,  10,   10,  10,    5,  10,
    10,    5,  10,  10,   10,  10,    5,  10,
    15,    5,   5,   5,    5,   5,    5,  15,
    15,   15,  10,  10,   10,  10,   15,  15,
]
    for elem in possibleMoves:
        pmax=0
        if (pmax<listpoids[elem]):
            pmax=listpoids[elem]
            elemMax=elem
        
    return elemMax

Game = Othello

if __name__ == '__main__':
    state, next = Game(['LUR', 'HSL'])

    move = 26

    print(next(state, move))
