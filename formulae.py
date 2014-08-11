from __future__ import division
__author__ = 'Horea Christian'

import numpy as np

def australian(deck_size=52):
    '''
    Based on the formula from Sullivan and Beatty 2012 DOI: 10.4236/ojdm.2012.24027   
    '''
    
    from math import log
    deck = 2*(deck_size - 2**(int(log(deck_size,2))))
    if deck == 0:
	return deck_size
    else:
	return deck
    
def tasmanian(deck_size=52, down_nr=1):
    from math import log
    #~ return (down_nr+1)*(deck_size+1 - down_nr**(int(log(deck_size,down_nr))))
    k = down_nr+1
    if deck_size ==1:
      return 1
    else:
      return ((tasmanian(deck_size-1,k)+k-1) % deck_size)+1
