import pytest
import game

def test_bestmove():
    assert game.bestmove((3,9,63)) == 63
    assert game.bestmove((3,8,35)) == 8
    pass
def test_possibleMove():
    pass
def test_willBeTaken():
    pass
    assert game.willBeTaken((-2)) 
        