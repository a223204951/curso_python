'''
CLASE SPORT
'''
class Sport:
    '''
    Clase para representar un deporte
    '''
    def __init__(self, name:str, players:int, league:str):
        '''
        Constructor de la clase
        '''
        self.name = name
        if isinstance(players, int): #Verifica que el número de jugadores sea un entero
            self.players = players
        else:
            self.players = int(players) #Convierte el número de jugadores a entero
        self.league = league

    def __str__(self):
        '''
        Representación en cadena de la clase
        '''
        return f"Sport: {self.name}, Players: {self.players}, League: {self.league}"
    
    def __repr__(self):
        '''
        Representación en cadena de la clase
        '''
        return f"Sport(name = '{self.name}', players = {self.players}, league = '{self.league}')"
    
    def to_json(self)->dict:
        '''
        Método que convierte la clase a un diccionario
        '''
        return {
            "Name": self.name,
            "Players": self.players,
            "League": self.league
        }

if __name__ == "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nlf = Sport("Football", 11, "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Baseball", 9, "MLB")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = [nlf, lmp, mlb, lmx, nba, s]
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
        for d in lista_deportes:
            file.write(repr(d)+"\n")
    sport_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())
    #Escritura de los deportes en un archivo JSON
    import json
    archivo_json = "deportes.json"
    #Convertimos cada deporte a un formato JSON
    sports_json = [sport.to_json() for sport in sport_list]
    #Escribimos toda la lista de deportes en el archivo JSON
    with open(archivo_json, "w", encoding='utf8') as file:
        json.dump(sports_json, file, indent=4)
    # Leemos el archivo JSON
    sport_list_json = []