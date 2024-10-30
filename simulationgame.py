import random

class player:

    def __init__(self, name, three_rating, two_rating, free_rating, def_rtg, age):
        self.name=name
        self.three_rating = three_rating
        self.two_rating = two_rating
        self.free_rating = free_rating
        self.def_rtg = def_rtg
        self.age = age
        self.points = 0

    def playerinfo(self):
        print(self.name + " ," + str(self.age))


#                   Name        3pt 2pt FT DEF AGE

team1 = [player("LeBron James", 90, 99, 70, 90, 39),
         player("Victor Wembanyama", 80, 85, 80, 95, 20),
         player("Bronny James", 75, 70, 80, 70, 20),
         player("Michael Jordan", 85, 99, 99, 95, 33),
         player("LeBron James Miami Heat", 92, 98, 74, 93, 29)]

team2 = [player("Kevin Durant", 95, 96, 90, 85, 36),
         player("Stephen Curry", 99, 95, 95, 80, 36),
         player("Larry Bird", 95, 95, 95, 90, 30),
         player("Tex Athanas", 80, 60, 75, 60, 26),
         player("Bill Russell", 50, 99, 70, 95, 35)]

playTypes = ['3pt','2pt','ft','turnover']





def ChoosePlay():
    playType = random.randint(0,len(playTypes)-1)
    return playTypes[playType]


def ChoosePlayer(i):
    player_index = random.randint(0,4)
    if(i==0):
        return team1[player_index]
    else:
        return team2[player_index]



def simulateGame():
    #Simulation
    quarters = 4
    team1possession = True

    team1_defense = sum(defPlayer.def_rtg for defPlayer in team1)/50
    team2_defense = sum(defPlayer.def_rtg for defPlayer in team2)/50

    while(quarters>0):

        time_remaining = 720

        while(time_remaining > 0):
        
            #Run a play
            play_type = ChoosePlay()

            #Choose Player
            if(team1possession):
                current_player = ChoosePlayer(0)
            else:
                current_player = ChoosePlayer(1)

            made_shot = random.randint(0, 100)

            #Add defense for other team
            if(team1possession):
                made_shot += team2_defense
            else:
                made_shot += team1_defense
        
            #Check play type
            if(play_type == '3pt'):

                if(made_shot < (current_player.three_rating)):
                    current_player.points += 3

            elif(play_type == '2pt'):

                if(made_shot < (current_player.two_rating)):
                    current_player.points +=2

            elif(play_type == 'ft'):

                if(made_shot < (current_player.free_rating)):
                    current_player.points +=1

            #Change Possession
            team1possession = not team1possession

            #Deduct Time
            time_remaining -= random.randint(5,24)

            #Reset Quarter
            if(time_remaining <= 0):
                quarters -=1



def manySimulations(x):

    for i in range(x):
        simulateGame()
        print("Simmed game " + str(i))



    print(f"Simulated {x} Games.")
    print()

    for i in range(5):
        print(team1[i].name + ": " + str(team1[i].points/x) + " points")

    team1_points = (sum(teamPlayer.points for teamPlayer in team1)/x)

    print(f"Team 1 Points Per Game: {team1_points}")
    print()



    for i in range(5):
        print(team2[i].name + ": " + str(team2[i].points/x) + " points")

    team2_points = (sum(teamPlayer.points for teamPlayer in team2)/x)

    print(f"Team 2 Points Per Game: {team2_points}")
    print()

    print(f"Team 1: {team1_points}, Team 2: {team2_points}")


manySimulations(10)