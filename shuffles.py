from __future__ import division
__author__ = 'Horea Christian'

import numpy as np

def australian(deck_size=52):
    deck = tasmanian(deck_size=deck_size, down_nr=1)
    return deck

    
def tasmanian(deck_size=52, down_nr=2):
    deck = np.arange(deck_size)+1
    discard=True
    while len(deck) > down_nr:
	if discard:
	    deck = np.delete(deck, np.arange(down_nr))
	    discard = False
	else:
	    under = deck[0]
	    deck = np.delete(deck,0)
	    deck = np.hstack((deck,under))
	    discard = True
    if not discard:
	under = deck[0]
	deck = np.delete(deck,0)
	deck = np.hstack((deck,under))
    return deck[-1]
    
def texas(deck_size=52, down_nr=2):
    deck = np.arange(deck_size)+1
    discard=False
    while len(deck) > down_nr:
	if discard:
	    deck = np.delete(deck, np.arange(down_nr))
	    discard = False
	else:
	    under = deck[0]
	    deck = np.delete(deck,0)
	    deck = np.hstack((deck,under))
	    discard = True
    if not discard:
	under = deck[0]
	deck = np.delete(deck,0)
	deck = np.hstack((deck,under))
    return deck[-1]

