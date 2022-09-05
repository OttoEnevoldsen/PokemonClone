# Module for fetching data from /config


import json
import os


class Pokemon():

    def __init__(self, name, types, health, attack, defence, s_attack, s_defence, speed, moves, assets):

        self.name = name
        self.types = types
        self.health = health
        self.attack = attack
        self.defence = defence
        self.s_attack = s_attack
        self.s_defence = s_defence
        self.speed = speed
        self.moves = moves
        self.assets = assets

    def __str__(self):
        
        return self.name

    def get_asset(self, file):
        
        return os.path.join(self.assets, file)


def get_pokemon(name):

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "pokemon", name + ".json"), "r") as file:
        
        data = json.loads(file.read())
        
        return Pokemon(
            data["name"], 
            data["types"], 
            data["health"], 
            data["attack"], 
            data["defence"], 
            data["s_attack"], 
            data["s_defence"], 
            data["speed"], 
            data["moves"],
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", data["assets"])
        )

def get_global():
    
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "global.json"), "r") as file:
        
        return json.loads(file.read())