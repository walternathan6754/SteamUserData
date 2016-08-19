# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:02:39 2016

@author: Nathan
"""

import urllib2      

# function recieves steam_id number
# and returns a dictionary containing all 
# owned games with hours played
def get_games(steam_id):
    keyword_name = '"name"'
    keyword_hours = '"hours_forever"'
    keyword_seperator = '","'
    my_steam = urllib2.urlopen('http://steamcommunity.com/profiles/' + str(steam_id) + '/games/?tab=all')
    
    steam_data = my_steam.read()

    start = steam_data.find('rgGames = [') + 10
    finish = steam_data.find('var rgChangingGames') - 4

    games = steam_data[start:finish]
    
    if games.find('name') == -1:
        raise ValueError('Private Accout or no games')
    
    location = 0
    list_of_games = []

    while location < finish:
        next_game = games.find(keyword_name, location)
        if next_game == -1:
            break
        else:
            next_game = next_game + 8
            
        game = games[next_game:games.find(keyword_seperator, next_game)]

        game_hours = games.find(keyword_hours, next_game)
        if game_hours == -1:
            hours = 0
        else:
            game_hours = game_hours + 17
            hours = games[game_hours:games.find(keyword_seperator, game_hours)]
            hours = float(hours.replace(',',''))
            
        list_of_games.append([game,hours])
        location = next_game
            
    list_of_games = dict(list_of_games)
    
    my_steam.close()
    
    return list_of_games