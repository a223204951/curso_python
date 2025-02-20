'''
Clase Team: Equipo 
'''

from athlete import Athlete
from sport import Sport

class Team:
    '''
    Clase para representar un equipo
    '''
    def __init__(self, name:str, sport:Sport, players:list):
        '''
        Constructor de la clase
        '''
        self.name = name
        self.sport = sport
        self.players = players
    
    def __str__(self):
        '''
        Representación en cadena de la clase
        '''
        return f"Team: {self.name}, Sport: {repr(self.sport)}, Players: {self.players}"
    
    def __repr__(self):
        '''
        Representación en cadena de la clase
        '''
        return f"Team(Name = '{self.name}', Sport = {self.sport}, Players = {self.players})"
    
    def to_json(self)->dict:
        '''
        Método que convierte la clase a un diccionario
        '''
        return {
            "Name": self.name,
            "Sport": self.sport.to_json(),
            "Players": [p.to_json() for p in self.players]
        }

if __name__ == "__main__":
    a1 = Athlete("Michael Jordan")
    a2 = Athlete("Kobe Bryant")
    a3 = Athlete("Lebron James")
    a4 = Athlete("Stephen Curry")
    a5 = Athlete("Shaquille O'Neal")
    s = Sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers", s, [a1, a2, a3, a4, a5])
    print(lakers)
    print(repr(lakers))
    print(lakers.to_json())