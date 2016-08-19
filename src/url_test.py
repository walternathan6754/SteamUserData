# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:52:24 2016

@author: Nathan
"""

import time

import pandas
from f_steam_user import get_games

steam_id = 76561198136945326

test_user = pandas.DataFrame()

start=time.time()
for i in range(100):
    try:
        next_user = get_games(steam_id + i)
    except ValueError as err:
        continue
    test_user = test_user.append(pandas.DataFrame(next_user, index=[0]), ignore_index=True)
    
print test_user

end=time.time()
print end - start

print test_user.sum()

test2 = test_user.sum()
test2.sort(ascending=False)
test2 = test2[0:30]

print
print
print test2

test2.plot.bar()

