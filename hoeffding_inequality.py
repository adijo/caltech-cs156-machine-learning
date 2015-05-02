"""
Simulation for verification of Hoeffding's inequality
in the ML course offered by
Yaser Abu-Mostafa from Caltech. 
"""

from random import randrange, choice
import pandas as pd 
import numpy as np 
from ggplot import *

def experiment():
    """
    Simulates experiment and 
    returns v1, vrand and vmin
    """
    coins = {x : {'heads' : 0, 'tails' : 0} for x in range(1, 1001)}
    outcomes = [0, 1]
    for coin in coins:
        for i in range(10):
            outcome = choice(outcomes)
            if outcome == 1:
                coins[coin]['heads'] += 1
            else:
                coins[coin]['tails'] += 1
    c_1 = 1
    c_rand = randrange(1, 1001)
    min_heads = coins[1]['heads']
    min_coin = 1
    for coin in coins:
        if coins[coin]['heads'] < min_heads:
            min_heads = coins[coin]['heads']
            min_coin = coin
    c_min = min_coin
    v_1 = coins[c_1]['heads']/10.0
    v_rand = coins[c_rand]['heads']/10.0
    v_min = coins[c_min]['heads']/10.0
    return (v_1, v_rand, v_min)

def simulate():
    v_1_dstr = []
    v_rand_dstr = []
    v_min_dstr = []

    for i in range(1000):
        res = experiment()
        v_1_dstr.append(res[0])
        v_rand_dstr.append(res[1])
        v_min_dstr.append(res[2])
    df = pd.DataFrame()
    df['v_1'] = v_1_dstr
    df['v_rand'] = v_rand_dstr
    df['v_min'] = v_min_dstr
    df = pd.melt(df)
    plt = ggplot(aes(x = 'value', color = 'variable'), data = df) + \
    geom_density()
    plt.__repr__()
    

simulate()

