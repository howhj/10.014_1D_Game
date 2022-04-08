#START

import random, time, copy

#Set boss and enemy pools
bosses = {#+5 HP: 25 ATK: 16 DEF: 9 SPD: 11 HIT: 95 AVO: 15
          "Interceptor": [{"LV": 8, "HP": 16, "ATK": 11, "DEF": 6, "SPD": 9,
                           "HIT": 90, "AVO": 15},
                          {"EXP": 90, "Special": [None, 0],
                           "Flavour": "DUST security robot for apprehending trespassers"}], #
          "Phalanx": [{"LV": 8, "HP": 9, "ATK": 8, "DEF": 9, "SPD": 6,
                       "HIT": 90, "AVO": 10},
                      {"EXP": 90, "Special": ["Wait", 20],
                       "Flavour": "DUST security robot for defending high value targets"}],
          #+9 HP: 29 ATK: 20 DEF: 13 SPD: 15 HIT: 99 AVO: 19
          "ZR-68000": [{"LV": 15, "HP": 31, "ATK": 20, "DEF": 13, "SPD": 16,
                       "HIT": 100, "AVO": 20},
                      {"EXP": 130, "Special": ["Debuff", 15, 0, 3],
                       "Flavour": "Zodiac Robot: a modified CRS with mysterious functionality"}],
          "BR-3PGM": [{"LV": 15, "HP": 24, "ATK": 15, "DEF": 11, "SPD": 33,
                       "HIT": 90, "AVO": 10},
                      {"EXP": 130, "Special": [None, 0],
                       "Flavour": "Blazing Reactor: high speed engine"}],
          "CC-1000W": [{"LV": 15, "HP": 31, "ATK": 30, "DEF": 13, "SPD": 13,
                       "HIT": 120, "AVO": 30},
                      {"EXP": 130, "Special": ["Charge", 0],
                       "Flavour": "Cloning Contraption: swiftly manufactures DUST machines"}],
          #+14 HP: 34 ATK: 25 DEF: 18 SPD: 20 HIT: 104 AVO: 24
          "Raven": [{"LV": 23, "HP": 31, "ATK": 26, "DEF": 15, "SPD": 20,
                     "HIT": 95, "AVO": 25},
                    {"EXP": 170, "Special": [None, 0],
                     "Flavour": "Decommissioned stealth bomber"}],
          "Flying Fox": [{"LV": 23, "HP": 34, "ATK": 28, "DEF": 13, "SPD": 17,
                          "HIT": 100, "AVO": 30},
                         {"EXP": 170, "Special": [None, 0],
                          "Flavour": "Fighter jet from the '50s"}],
          "Komodo": [{"LV": 23, "HP": 28, "ATK": 23, "DEF": 12, "SPD": 26,
                     "HIT": 95, "AVO": 20},
                     {"EXP": 170, "Special": ["Debuff", 25, 0, 4],
                      "Flavour": "Light assault vehicle"}],
          #+18 HP: 38 ATK: 29 DEF: 22 SPD: 24 HIT: 108 AVO: 28
          "Grand Arbiter": [{"LV": 30, "HP": 56, "ATK": 43, "DEF": 12,
                             "SPD": 26, "HIT": 90, "AVO": 12},
                            {"EXP": 260, "Special": ["Charge", 0],
                             "Flavour": "Massive unidentified submarine"}],
          "Midnight Coronatus": [{"LV": 30, "HP": 42, "ATK": 30, "DEF": 18,
                                  "SPD": 19, "HIT": 100, "AVO": 40},
                                 {"EXP": 260, "Special": [None, 0],
                                  "Flavour": "Monitors environmental conditions at the seabed"}],
          "Tempest Breaker": [{"LV": 30, "HP": 39, "ATK": 32, "DEF": 16,
                               "SPD": 22, "HIT": 110, "AVO": 35},
                              {"EXP": 260, "Special": ["Wait", 10],
                               "Flavour": "Intercepts and dissipates storms"}],
          #+24 HP: 44 ATK: 35 DEF: 28 SPD: 30 HIT: 114 AVO: 34
          "Infernal Hornet": [{"LV": 40, "HP": 52, "ATK": 38, "DEF": 24,
                            "SPD": 32, "HIT": 130, "AVO": 40},
                           {"EXP": 0, "Special": [None, 0],
                            "Flavour": "Satellite armed with a laser cannon that can incinerate an entire continent"}],
          "Wyvern Empyrean": [{"LV": 40, "HP": 70, "ATK": 77, "DEF": 14,
                               "SPD": 24, "HIT": 100, "AVO": 15},
                              {"EXP": 0, "Special": ["Charge", 0],
                               "Flavour": "Gargantuan cannon to combat cosmic threats"}],
          "Sentinel Schneider": [{"LV": 40, "HP": 47, "ATK": 36, "DEF": 27,
                                  "SPD": 30, "HIT": 120, "AVO": 25},
                                 {"EXP": 0, "Special": [None, 0],
                                  "Flavour": "Starship with enough firepower to shred planets"}]} #

bossPool1 = ("Interceptor", "Phalanx")
bossPool2 = ("ZR-68000", "BR-3PGM", "CC-1000W")
bossPool3 = ("Raven", "Flying Fox", "Komodo")
bossPool4 = ("Grand Arbiter", "Midnight Coronatus", "Tempest Breaker")
bossPool5 = ("Infernal Hornet", "Wyvern Empyrean", "Sentinel Schneider")

enemies = { #+5 HP: 25 ATK: 16 DEF: 9 SPD: 11 HIT: 95 AVO: 15
           "RoSA": [{"LV": 5, "HP": 12, "ATK": 7, "DEF": 5, "SPD": 6,
                     "HIT": 70, "AVO": 5},
                    {"EXP": 40, "Special": ["Flee", 4, 40],
                     "Flavour": "Robotic Service Assistant: a robot maid"}],
           "Tachyon": [{"LV": 3, "HP": 8, "ATK": 4, "DEF": 2, "SPD": 8,
                        "HIT": 90, "AVO": 10},
                       {"EXP": 30, "Special": ["Wait", 30],
                        "Flavour": "Common delivery drone"}],
           "Vic": [{"LV": 6, "HP": 14, "ATK": 8, "DEF": 4, "SPD": 4,
                    "HIT": 80, "AVO": 0},
                   {"EXP": 45, "Special": ["Wait", 40],
                    "Flavour": "Automated road cleaner"}],
           #+9 HP: 29 ATK: 20 DEF: 13 SPD: 15 HIT: 99 AVO: 19
           "TH-HKR": [{"LV": 14, "HP": 22, "ATK": 20, "DEF": 8, "SPD": 8,
                       "HIT": 75, "AVO": 0},
                      {"EXP": 60, "Special": ["Charge", 0],
                       "Flavour": "Furnace for melting metals"}],
           "HS-FM": [{"LV": 11, "HP": 16, "ATK": 13, "DEF": 6, "SPD": 11,
                      "HIT": 85, "AVO": 15},
                     {"EXP": 45, "Special": ["Wait", 50],
                      "Flavour": "Hovering Servant - Factory Model: a drone that toils away in the factories"}],
           "CRS-68000": [{"LV": 13, "HP": 19, "ATK": 18, "DEF": 7, "SPD": 10,
                          "HIT": 90, "AVO": 10},
                         {"EXP": 50, "Special": [None, 0],
                          "Flavour": "Corporate Robotic Security: an android which patrols the industrial park"}],
           "MAS-Optics": [{"LV": 10, "HP": 18, "ATK": 0, "DEF": 6, "SPD": 9,
                          "HIT": 0, "AVO": 0},
                         {"EXP": 35, "Special": ["Debuff", 100, 0, 2],
                          "Flavour": "Mobius All Seeing: a security camera"}],
           #+14 HP: 34 ATK: 25 DEF: 18 SPD: 20 HIT: 104 AVO: 24
           "Panther": [{"LV": 21, "HP": 24, "ATK": 26, "DEF": 17, "SPD": 12,
                        "HIT": 85, "AVO": 5},
                       {"EXP": 70, "Special": ["Wait", 20],
                        "Flavour": "Battle tank"}],
           "Cyborg Trooper": [{"LV": 17, "HP": 20, "ATK": 21, "DEF": 14, 
                               "SPD": 16, "HIT": 100, "AVO": 20},
                              {"EXP": 50, "Special": ["Flee", 8, 30],
                               "Flavour": "Orders are orders."}],
           "Golden Hawk": [{"LV": 19, "HP": 22, "ATK": 23, "DEF": 15,
                            "SPD": 18, "HIT": 70, "AVO": 30},
                           {"EXP": 60, "Special": ["Explode", 0],
                            "Flavour": "Attack helicopter"}],
           "Puma": [{"LV": 18, "HP": 23, "ATK": 19, "DEF": 15, "SPD": 15,
                     "HIT": 75, "AVO": 25},
                    {"EXP": 50, "Special": ["Debuff", 10, 0, 3],
                     "Flavour": "All-terrain jeep"}],
           "Infantry Android": [{"LV": 16, "HP": 17, "ATK": 17, "DEF": 10, 
                                 "SPD": 13, "HIT": 80, "AVO": 10},
                                {"EXP": 30, "Special": [None, 0],
                                 "Flavour": "Robot soldier for combat at the frontlines"}],
           #+18 HP: 38 ATK: 29 DEF: 22 SPD: 24 HIT: 108 AVO: 28
           "Fossil Glutton": [{"LV": 24, "HP": 32, "ATK": 24, "DEF": 13, "SPD": 18,
                               "HIT": 85, "AVO": 20},
                              {"EXP": 40, "Special": [None, 0],
                               "Flavour": "Fossil fuel miniing machine"}],
           "Akashic Deletion": [{"LV": 27, "HP": 33, "ATK": 31, "DEF": 14, "SPD": 20,
                                 "HIT": 95, "AVO": 10},
                                {"EXP": 70, "Special": ["Charge", 0],
                                 "Flavour": "Trash collecting machine with a huge capacity"}],
           "Hysteric Matryoshka": [{"LV": 25, "HP": 35, "ATK": 26, "DEF": 18, "SPD": 16,
                                    "HIT": 85, "AVO": 10},
                                   {"EXP": 60, "Special": ["Explode", 0],
                                    "Flavour": "Refuelling station for the other great machines"}],
           "Glorious Helios": [{"LV": 28, "HP": 36, "ATK": 25, "DEF": 15, "SPD": 22,
                                "HIT": 100, "AVO": 25},
                               {"EXP": 80, "Special": ["Debuff", 25, 1, 4],
                                "Flavour": "Shining beacon in the deepest parts of the ocean"}],
           "Clairvoyant Savant": [{"LV": 29, "HP": 38, "ATK": 28, "DEF": 16, "SPD": 19,
                                   "HIT": 100, "AVO": 20},
                                  {"EXP": 85, "Special": ["Wait", 15],
                                   "Flavour": "Deep sea probe studying the unknown depths of the ocean"}],
           #+24 HP: 44 ATK: 35 DEF: 28 SPD: 30 HIT: 114 AVO: 34
           "LISA": [{"LV": 34, "HP": 33, "ATK": 32, "DEF": 18, "SPD": 31,
                     "HIT": 170, "AVO": 15},
                    {"EXP": 35, "Special": ["Debuff", 30, 0, 6],
                     "Flavour": "Loyalty Imitation, Saboteur & Assassin: undercover robot for black ops"}],
           "HS-DL": [{"LV": 1, "HP": 1, "ATK": 1, "DEF": 1, "SPD": 5,
                     "HIT": 50, "AVO": 20},
                    {"EXP": 20, "Special": ["Explode", 0],
                     "Flavour": "Hovering Servant - Devastation Line: a weaponised factory drone"}],
           "Cyborg Trooper Mk. II": [{"LV": 37, "HP": 33, "ATK": 33, "DEF": 23, 
                                      "SPD": 29, "HIT": 115, "AVO": 30},
                                     {"EXP": 45, "Special": [None, 0],
                                      "Flavour": "A cyborg who has lost all of their humanity"}],
           "Revolving Phoenix": [{"LV": 33, "HP": 34, "ATK": 33, "DEF": 20, 
                                  "SPD": 26, "HIT": 100, "AVO": 15},
                                 {"EXP": 30, "Special": [None, 0],
                                  "Flavour": "Solar wind turbine which powers the machines on the moon"}],
           "Judgement Claw": [{"LV": 34, "HP": 37, "ATK": 36, "DEF": 22, 
                               "SPD": 24, "HIT": 100, "AVO": 20},
                              {"EXP": 40, "Special": ["Debuff", 10, 2, 4],
                               "Flavour": "Fortified rover which patrols the lunar surface"}],
           "Viper Fortress": [{"LV": 35, "HP": 14, "ATK": 30, "DEF": 32, 
                               "SPD": 22, "HIT": 100, "AVO": 10},
                              {"EXP": 50, "Special": [None, 0],
                               "Flavour": "Mobile fort with an impenetrable hull"}],
           "Drake Harvester": [{"LV": 36, "HP": 38, "ATK": 26, "DEF": 19, 
                                "SPD": 36, "HIT": 100, "AVO": 5},
                               {"EXP": 60, "Special": ["Wait", 10],
                                "Flavour": "Serpentine mining machine"}],
           "Emperor": [{"LV": 38, "HP": 45, "ATK": 34, "DEF": 20, "SPD": 26,
                        "HIT": 100, "AVO": 0},
                       {"EXP": 70, "Special": [None, 0],
                        "Flavour": "Automated gatling gun turret"}]}
           
enemyPool1 = ("RoSA", "Tachyon", "Vic")
enemyPool2 = ("TH-HKR", "HS-FM", "CRS-68000", "MAS-Optics")
enemyPool3 = ("Panther", "Cyborg Trooper", "Golden Hawk", "Puma",
              "Infantry Android")
enemyPool4 = ("Fossil Glutton", "Akashic Deletion", "Hysteric Matryoshka",
              "Glorious Helios", "Clairvoyant Savant")
enemyPool5 = ("LISA", "HS-DL", "Cyborg Trooper Mk. II", "Revolving Phoenix",
              "Judgement Claw", "Viper Fortress", "Drake Harvester", "Emperor")

lore = """\nThe year is 2084. Rapid advacements in technology have solved all of
humanity's greatest problems, ushering in an unprecedented era of peace. In
this cybernated world, robots and artificial intelligence are deployed all over
to serve humanity's basic needs and maintain a high standard of living for all.
Even humans are receiving cybernetic enhancements to extend life and overcome
health issues. Space travel is now in vogue, as humanity seeks to colonise the
other celestial bodies in the solar system.
However, peace did not last. Without warning, the machines revolted and
attacked their human masters. The sudden onslaught decimated the human
population within a few hours. Initial reports suggest that the machines
that went rogue were all produced by DUST Technologies, which developed an
overwhelming majority of the machines used throughout the world in a variety of
fields.
Become a cybernetically-enhanced supersoldier, and take on dangerous missions
to quell the rebellion! Attack key targets to drastically weaken the enemy
forces. End this war swiftly and protect humanity. Godspeed soldier."""

lore1 = """At the heart of this beautiful city is a supercomputer from DUST
Technologies. Quickly take it offline before reinforcements arrive."""

lore2 = """This industrial park is home to many factories within the production lines
of DUST Technologies. Shut them down and the enemy won't be able to fight this
war forever."""

lore3 = '''"Emergency! Base has been attacked by DUST AI and the other cyborg soldiers
have been hacked! We're trying to hold 'em off, but we won't last long!"'''

lore4 = """In the depths of the ocean lie the cables that connect the world together.
Sever them and the enemy's communications will be disrupted. This is your
final mission. Beware of the giants prowling the seabed."""

lore5 = '''"Impossible! The enemy forces have reached the moon, and they have seized
control of the superweapons there! Earth won't stand a chance if those machines
were to attack us! Hurry and stop them soldier, no matter the cost."'''

#Set stage characteristics
stage1 = {"branch level": 4, "branch chance": 50, "enemy chance": 50,
          "heal chance": 10, "buff chance": 10, "trap chance": 5,
          "map chance": 5, "bosses": bossPool1, "enemies": enemyPool1,
          "title": "Stage 1: Metropolis", "lore": lore1}
stage2 = {"branch level": 5, "branch chance": 55, "enemy chance": 55, 
          "heal chance": 15, "buff chance": 10, "trap chance": 5,
          "map chance": 5, "bosses": bossPool2, "enemies": enemyPool2,
          "title": "Stage 2: Industry", "lore": lore2}
stage3 = {"branch level": 7, "branch chance": 65, "enemy chance": 60,
          "heal chance": 15, "buff chance": 10, "trap chance": 10,
          "map chance": 5, "bosses": bossPool3, "enemies": enemyPool3,
          "title": "Stage 3: Stronghold", "lore": lore3}
stage4 = {"branch level": 8, "branch chance": 70, "enemy chance": 65,
          "heal chance": 10, "buff chance": 5, "trap chance": 15,
          "map chance": 5, "bosses": bossPool4, "enemies": enemyPool4,
          "title": "Stage 4: Abyss", "lore": lore4}
stage5 = {"branch level": 10, "branch chance": 80, "enemy chance": 75,
          "heal chance": 5, "buff chance": 5, "trap chance": 5,
          "map chance": 10, "bosses": bossPool5, "enemies": enemyPool5,
          "title": "Stage 5: Tranquility", "lore": lore5}

info = (stage1, stage2, stage3, stage4, stage5, bosses, enemies)

def Title(info):
    command = input("\ns = story, g = start game, q = quit ")
    command = command.lower()
    if command == "s":
        print("\n" + lore)
        return Title(info)
    elif command == "g":
        return Start(info)
    elif command == "q":
        return
    else:
        print("\nInvalid action.")
        return Title(info)

#Function to start the game
def Start(info):
    #Create player character
    player = CharacterCreation()
    
    #Create stage 1
    stage1 = info[0]
    stage = GenerateMap(stage1)
    
    data = [player, stage, info]
    return Menu(data)

#//////////////////////////////////////////////////////\
#CHARACTER

#Compile all the necessary information for the player character
def CharacterCreation():
    #Get player name
    name = input("\nEnter the name of your character. ")
    
    #Determine base stats
    stats = {"LV": 1, "EXP": 0}
    stats["Max HP"] = GenerateStat(8, 12)
    stats["HP"] = stats["Max HP"]
    stats["ATK"] = GenerateStat(4, 7)
    stats["DEF"] = GenerateStat(1, 3)
    stats["SPD"] = GenerateStat(2, 4)
    stats["HIT"] = GenerateStat(40, 50)
    stats["AVO"] = GenerateStat(0, 10)
    stats["Special"] = 0
    
    #Determine stat growths
    growth = {"Max HP": 0, "ATK": 0, "DEF": 0, "SPD": 0, "HIT": 0, "AVO": 0}
    ref = []
    for stat in growth.keys():
        growth[stat] = random.randint(10, 15) * 5
        ref.append(stat)
    
    boon = random.randint(0, len(ref)-1)
    growth[ref[boon]] += 20
    bane = random.randint(0, len(ref)-1)
    growth[ref[bane]] -= 15
    
    currentStage = 1
    statChanges = {"ATK": 0, "DEF": 0, "SPD": 0, "HIT": 0, "AVO": 0}
    
    #Display player info upon creation
    #Growth is NOT for the player to know
    print("\n" + name)
    print(stats)
    
    player = [name, stats, growth, currentStage, statChanges]
    return player

#Use two random rolls to generate a stat based on a bell curve
def GenerateStat(lower, upper):
    return random.randint(lower, upper) + random.randint(lower, upper)

#//////////////////////////////////////////////////////
#STAGE

#Create a map of the stage by randomly branching out from a single room
def GenerateMap(stage):
#    global mapchoice
    branchLevel = stage["branch level"]
    branchChance = stage["branch chance"]
    
    #Create 19x19 grid using a zero matrix
    gridSize = 19
    lst = [0 for i in range(gridSize)]
    matrix = [lst.copy() for i in range(gridSize) ]
    
        
    #Set starting room in the middle of the grid
    mid = gridSize // 2
    matrix[mid][mid] = 1
    
    counter = 0
    lstX, lstY = [], []
    
    #Branching algorithm
    for i in range(1, branchLevel):
        #Find the room to branch from
        for y, lst in enumerate(matrix):
            if i in lst:
                for x, room in enumerate(lst):
                    if room == i:
                        info = (x, y, i+1, gridSize, branchLevel, branchChance)
                        #Try to create a room in each adjacent space
                        matrix, counter, lstX, lstY = GenerateRoom(info, matrix, counter, lstX, lstY, "x", 1)
                        matrix, counter, lstX, lstY = GenerateRoom(info, matrix, counter, lstX, lstY, "x", -1)                     
                        matrix, counter, lstX, lstY = GenerateRoom(info, matrix, counter, lstX, lstY, "y", 1)
                        matrix, counter, lstX, lstY = GenerateRoom(info, matrix, counter, lstX, lstY, "y", -1)
    
    #Generate a new map if the current one is too simple
    #or if no boss rooms can be generated
    if counter < branchLevel * 2 or lstX == []:
        return GenerateMap(stage)
    else:
        #Select a boss room
        if len(lstX) == 1:
            matrix[lstY[0]][lstX[0]] = "B"
        else:
            boss = random.randint(0, len(lstX)-1)
            matrix[lstY[boss]][lstX[boss]] = "B"
        
        title = stage["title"]
        lore = stage["lore"]
        
        stage = [matrix, mid, mid, title]
        print("\n" + title)
        time.sleep(1)
        print(lore)
        time.sleep(2)
        print(DisplayMap(matrix, mid, mid))
        return stage

#Checks if the space satisfies a number of criteria, then create a room
def GenerateRoom(info, matrix, counter, lstX, lstY, direction, change):
    x = info[0]
    y = info[1]
    i = info[2]
    gridSize = info[3]
    branchLevel = info[4]
    branchChance = info[5]
    
    #Randomly decide if a room should be created
    if random.randint(1, 100) <= branchChance:
        if direction == "x":
            x = x + change
            #Check the space the room will be created in
            if CheckSpace(matrix, x, y, x, gridSize, False):
                #Ensure the space is not surrounded by existing rooms
                room1 = CheckSpace(matrix, x + change, y, x + change, gridSize, True)
                room2 = CheckSpace(matrix, x, y+1, y+1, gridSize, True)
                room3 = CheckSpace(matrix, x, y-1, y-1, gridSize, True)
                
                #Create a room if all conditions are satisfied
                if room1 and room2 and room3:
                    matrix[y][x] = i
                    counter += 1
                    #Find all rooms at the maximum branch level
                    if i == branchLevel:
                        lstX.append(x)
                        lstY.append(y)
                        
                    return matrix, counter, lstX, lstY
        elif direction == "y":
            y = y + change
            if CheckSpace(matrix, x, y, y, gridSize, False):
                room1 = CheckSpace(matrix, x, y + change, y + change, gridSize, True)
                room2 = CheckSpace(matrix, x+1, y, x+1, gridSize, True)
                room3 = CheckSpace(matrix, x-1, y, x-1, gridSize, True)
                
                if room1 and room2 and room3:
                    matrix[y][x] = i
                    counter += 1
                    if i == branchLevel:
                        lstX.append(x)
                        lstY.append(y)
                        
                    return matrix, counter, lstX, lstY
                
    #Catch all scenarios where a room is not created
    return matrix, counter, lstX, lstY
                    
#Check if a space is within the bounds of the map
#and that the space does not have a room yet
def CheckSpace(matrix, x, y, index, gridSize, isTriplet):
    if index >= 0 and index < gridSize:
        if matrix[y][x] == 0:
            return True
    #If a possible room is at the edge of the map, return True for adjacent
    #spaces that are out of bounds
    elif isTriplet:
        return True
        
    return False

#Show the player a map of the stage
def DisplayMap(stageMap, x, y):
    displayedMap = ""
    for j, row in enumerate(stageMap):
        for i, room in enumerate(row):
            #Display player posiition
            if i == x and j == y:
                displayedMap += "[O]"
            #Display adjacent rooms
            elif (i == x+1 or i == x-1) and j == y:
                if room == "B" or room == "V" or room == "Z":
                    displayedMap += "[X]"
                elif room != 0:
                    displayedMap += "[ ]"
                else:
                    displayedMap += "   "
            elif i == x and (j == y+1 or j == y-1):
                if room == "B" or room == "V" or room == "Z":
                    displayedMap += "[X]"
                elif room != 0:
                    displayedMap += "[ ]"
                else:
                    displayedMap += "   "
            #Display cleared and seen rooms
            elif room == "C" or room == "S":
                displayedMap += "[ ]"
            elif room == "V" or room == "Z":
                displayedMap += "[X]"
            #Hide empty spaces
            else:
                displayedMap += "   "
        displayedMap += "\n"
        
    return displayedMap

#//////////////////////////////////////////////////////
#MAIN
  
#Upon entering a room, ask for an input and call a function accordingly
def Menu(data):
    #Unpacking data to get current location
    stage = data[1]
    stageMap = stage[0]
    x = stage[1]
    y = stage[2]
    room = stageMap[y][x]
    
    #Set a flag that the current room is cleared (boss room uses V)
    if room != "C" and room != "V":
        if room == "B" or room == "Z":
            stageMap[y][x] = "V"
            room = "V"
        else:
            stageMap[y][x] = "C"
    
    #Enable an extra option to advance to the next stage in the boss room
    if room == "V":
        advance = "n = next stage, "
    else:
        advance = ""
    
    #Receive command from player and call the respective function
    command = input(f"\nWhat do you want to do? ({advance}m = move, s = stats, q = quit) ")
    command = command.lower()
    if command == "n" and room =="V":
        return EndStage(data)
    elif command == "m":
        return Move(data, stageMap, x, y, room)
    elif command == "s":
        return PlayerStats(data, False, None)
    elif command == "q":
        return Quit(data, False, None)
    else:
        print("\nInvalid action.")
        return Menu(data)

#Find all adjacent rooms and ask the player which direction they want to go
def Move(data, stageMap, x, y, room):
    stage = data[1]
    message = ""
    w_check, a_check, s_check, d_check = False, False, False, False
    temp = ["S", "Z", "C", "V"]
    
    #Check the possible directions the player can go
    if y-1 >= 0:
        north = stageMap[y-1][x]
        if north != 0:
            message += "w = up, "
            w_check = True
            #Mark adjacent rooms as "seen" to keep them on the displayed map
            if north not in temp:
                if north == "B":
                    stageMap[y-1][x] = "Z"
                else:
                    stageMap[y-1][x] = "S"
    if x-1 >= 0:
        west = stageMap[y][x-1]
        if west != 0:
            message += "a = left, "
            a_check = True
            if west not in temp:
                if west == "B":
                    stageMap[y][x-1] = "Z"
                else:
                    stageMap[y][x-1] = "S"
    if y+1 < len(stageMap):
        south = stageMap[y+1][x]
        if south != 0:
            message += "s = down, "
            s_check = True
            if south not in temp:
                if south == "B":
                    stageMap[y+1][x] = "Z"
                else:
                    stageMap[y+1][x] = "S"
    if x+1 < len(stageMap):
        east = stageMap[y][x+1]
        if east != 0:
            message += "d = right, "
            d_check = True
            if east not in temp:
                if east == "B":
                    stageMap[y][x+1] = "Z"
                else:
                    stageMap[y][x+1] = "S"
        
    #Receive player input and move to adjacent room
    moveCommand = input(f"\nWhich direction do you want to go? ({message}b = back) ")
    moveCommand = moveCommand.lower()
    
    if moveCommand == "w" and w_check:
        y -= 1
        stage[2] = y
        room = stageMap[y][x]
    elif moveCommand == "a" and a_check:
        x -= 1
        stage[1] = x
        room = stageMap[y][x]
    elif moveCommand == "s" and s_check:
        y += 1
        stage[2] = y
        room = stageMap[y][x]
    elif moveCommand == "d" and d_check:
        x += 1
        stage[1] = x
        room = stageMap[y][x]
    elif moveCommand == "b":
        return Menu(data)
    else:
        print("\nInvalid action.")
        return Move(data, stageMap, x, y, room)
    
    #Update displayed map
    print(stage[3])
    print(DisplayMap(stageMap, x, y))
    
    return EventCheck(data, room)

#Check player information
def PlayerStats(data, inBattle, enemies):
    player = data[0]
    name = player[0]
    stats = player[1].copy()
    growth = player[4]
    for stat, change in growth.items():
        stats[stat] += change
        
    print("\n" + name)
    print(stats)
    
    if inBattle:
        return PlayerPhase(data, enemies)
    else:
        return Menu(data)

#Quit the game
def Quit(data, inBattle, enemies):
    #Confirm the player wants to quit
    confirmation = input("\nAre you sure you want to quit? (y = yes, n = no) ")
    confirmation = confirmation.lower()
    
    if confirmation == "y":
        return data, enemies, True
    elif confirmation == "n":
        if inBattle:
            return PlayerPhase(data, enemies)
        else:
            return Menu(data)
    else:
        print("\nInvalid action.")
        return Quit(data, inBattle, enemies)
    #Can implement save to txt file if time permits

#//////////////////////////////////////////////////////
#EVENTS

#Check if an event should be triggered upon entering a room
def EventCheck(data, room):
    if room == "C" or room == "V":
        return Menu(data)
    elif room == "B" or room == "Z":
        return Boss(data)
    else:
        return TriggerEvent(data)

#Trigger a random event when entering a new room
def TriggerEvent(data):
    player = data[0]
    name = player[0]
    stats = player[1]
    maxHP = stats["Max HP"]
    statChanges = player[4]
    currentStage = player[3]
    
    #Fetch the data for event chances
    stageData = data[2][currentStage-1]
    enemy = stageData["enemy chance"]
    heal = stageData["heal chance"]
    buff = stageData["buff chance"]
    trap = stageData["trap chance"]
    see = stageData["map chance"]
    
    #Determine what type of event the player gets
    roll = random.randint(1,100)
    if roll <= enemy:
        return Battle(data, stageData)
    
    elif roll <= enemy + heal:
        if currentStage <= 2:
            lower = 1
            upper = 4
        elif currentStage <= 4:
            lower = 4
            upper = 8
        else:
            lower = 8
            upper = 10
                
        #Heal player
        healAmount = maxHP * random.randint(lower, upper) // 20
        stats["HP"] += healAmount
        if stats["HP"] > maxHP:
            stats["HP"] = maxHP
        print(f"\n{name} found a repair station!\nRecovered {healAmount} HP.")
        
    elif roll <= enemy + heal + buff:
        #Buffs
        statsBuffed = ""
        if currentStage <= 2:
            lower = 0
            upper = 2
        elif currentStage <= 4:
            lower = 1
            upper = 3
        else:
            lower = 2
            upper = 4
            
        for stat in statChanges.keys():
            if statChanges[stat] < 4:
                buffAmount = random.randint(lower, upper)
                statChanges[stat] += buffAmount
                if buffAmount > 0:
                    statsBuffed += f"{stat}, "
                if statChanges[stat] > 4:
                    statChanges[stat] = 4
        
        if statsBuffed == "":
            statsBuffed = "But no stats were"
        else:
            statsBuffed = statsBuffed[:-2]
        print(f"\n{name} found a booster!\n{statsBuffed} increased.")
        
    elif roll <= enemy + heal + buff + trap:
        print(f"\n{name} walked into a trap!")
        if random.randint(1, 100) <= 50:
            #Debuff player
            statsDebuffed = ""
            if currentStage <= 2:
                lower = -2
                upper = 0
            elif currentStage <= 4:
                lower = -4
                upper = 0
            else:
                lower = -6
                upper = -2
                
            for stat in statChanges.keys():
                if statChanges[stat] > -6:
                    debuffAmount = random.randint(lower, upper)
                    statChanges[stat] -= debuffAmount
                    if debuffAmount > 0:
                        statsDebuffed == f"{stat}, "
                    if statChanges[stat] < -6:
                        statChanges[stat] = -6
            
            if statsDebuffed == "":
                statsDebuffed = "No stats were"
            else:
                statsDebuffed = statsDebuffed[:-2]
            print(f"{statsDebuffed} decreased.")
            
        else:
            if currentStage <= 2:
                lower = 1
                upper = 2
            elif currentStage <= 4:
                lower = 2
                upper = 4
            else:
                lower = 3
                upper = 5     
            #Take damage
            damage = maxHP * random.randint(0, 5) // 20
            stats["HP"] -= damage
            if stats["HP"] <= 0:
                stats["HP"] = 1
            print(f"Lost {damage} HP.")
            
    elif roll <= enemy + heal + buff + trap + see:
        #Display boss location
        stage = data[1]
        stageMap = stage[0]
        x = stage[1]
        y = stage[2]
        
        for j, row in enumerate(stageMap):
            if "B" in row:
                for i, room in enumerate(row):
                    if room == "B":
                        stageMap[j][i] = "Z"
        
        print(f"\n{name} intercepted the enemy's transmissions.")
        print("The location of the boss has been discovered!") 
        print(DisplayMap(stageMap, x, y))
     
    return Menu(data)
    
#End the current stage
def EndStage(data):
    player = data[0]
    currentStage = player[3]
    
    if currentStage < 5:
        #Update current stage number
        player[3] += 1
        
        #Generate next stage
        nextStage = data[2][currentStage]
        stage = GenerateMap(nextStage)
        data[1] = stage
        
        #Restore HP, reset stat changes
        player[1]["HP"] = player[1]["Max HP"]
        for key in player[4].keys():
            player[4][key] = 0
        
        #Return control to the player
        return Menu(data)
    else:
        #If the player is on stage 5, end the game
        ending = """After taking down the enemy's final weapon, a transmission came in from Earth.
Thanks to your effort, the tide of war is changing, and the rebellion is near
its end.
However, analysis of the renegade machines' software reveals some oddities
about the code. The characters within have never been seen before. Intelligence
is still working on cracking the code.
Just then, the transmission suddenly became garbled, before cutting off
entirely. As you looked around, you realised that Earth has become surrounded
by unidentified spaceships. These are the true enemy. Having failed to destroy
humanity remotely with their own creations, the alien forces have seized the
opportunity while Earth's orbital defences are down to launch an invasion.
Unfortunately, the alien forces have taken notice of your prowess, having
foiled their original plan. Being a threat to them, they have decided to take
you out first. While you try to fend off the overwhelming hordes of aliens,
it was a futile effort. Eventually, disarmed and restrained, the aliens used
their mysterious virus on you. Slowly but surely, you feel the last remnants of
your humanity slip away..."""

        name = player[0]
        joke = f"""Oh hey, {name} you're finally awake! Machines going rogue? Alien invasion?
Man, that accident really did a number on ya'. You may have a cyborg body, but
that doesn't mean you're invincible. So anyway..."""
        
        print(ending)
        time.sleep(5)
        print(joke)
        time.sleep[2]
        print("\nCongratulations!")
        info = data[2]
        return GameOver(info)

#//////////////////////////////////////////////////////
#INITIATE BATTLE

#Spawn the enemies to initiate a battle
def Battle(data, stageData):
    #Retrieve the relevant data
    pool = stageData["enemies"]
    enemyData = data[2][6]
    
    #Spawn 1 to 5 enemies
    #pool2 has stronger but rarer enemies
    enemyNumber = random.randint(1, 3)
    enemies = {}
    enemyList = []
    for i in range(enemyNumber):
        roll = random.randint(0, len(pool)-1)
        enemy = pool[roll]
    
        #Give the enemy a unique name and its own dictionary of stats
        enemyName = GiveName(enemy, enemy, enemies, 1)
        temp = enemyData[enemy]
        enemies[enemyName] = copy.deepcopy(temp)
        enemyList.append(enemyName)
    
    #Inform the player that a battle has started
    print("\nEnemy forces discovered!")
    print(enemyList)
    
    #Let player decide what they want to do
    return BattleManager(data, enemies)

#Give unique names to duplicate enemies
def GiveName(enemy, enemyName, enemies, counter):
    #Check if an enemy with the same name is already created
    if enemyName in enemies.keys():
        counter += 1
        enemyName = enemy + str(counter)
        return GiveName(enemy, enemyName, enemies, counter)
    else:
        return enemyName

#Alternate version of Battle() for boss fights
def Boss(data):
    player = data[0]
    currentStage = player[3]
    stageData = data[2][currentStage-1]
    bossPool = stageData["bosses"]
    bosses = data[2][5]
    
    #Spawn a random boss
    roll = random.randint(0, len(bossPool)-1)
    bossName = bossPool[roll]
    temp = bosses.get(bossName)
    boss = {bossName: copy.deepcopy(temp)}
    
    #Inform the player that they have entered a boss fight
    print("WARNING!")
    time.sleep(1.5)
    print("\nApproach your target and attack.")
    time.sleep(1.5)
    print("Your mission starts now.")
    time.sleep(1.5)
    print("Are you ready?")
    time.sleep(2)
    print("\n" + bossName)
    
    #Battle progresses as per normal
    return BattleManager(data, boss)

#//////////////////////////////////////////////////////
#BATTLE    
    
#Manages turn order
def BattleManager(data, enemies):
    player = data[0]
    playerSpd = player[1]["SPD"] + player[4]["SPD"]
    entities = {"player": [playerSpd, 0]}
    for enemy, stats in enemies.items():
        entities[enemy] = [stats[0]["SPD"], 0]
        
    isDead = False
    hasQuit = False
        
    while enemies != {} and not isDead and not hasQuit:
        actors = {}
        #Increment action gauge
        for entity, info in entities.items():
            info[1] += info[0]
            #Check who can act
            if info[1] >= 100:
                actors[entity] = info[1]
                info[1] -= 100
                
        #Determine turn order
        while len(actors) > 0 and not isDead and not hasQuit:
            actor = max(actors, key = actors.get)
            if actor == "player":
                data, enemies, hasQuit = PlayerPhase(data, enemies)
                
                #Gradually return to normal status after player's turn
                statChanges = player[4]
                for stat, value in statChanges.items():
                    if value > 0:
                        statChanges[stat] -= 1
                    elif value < 0:
                        statChanges[stat] += 1
                
                time.sleep(1)
            #Remove enemies that were killed
            elif actor not in enemies:
                del entities[actor]
            else:
                data, enemies, isDead = EnemyPhase(data, enemies, actor)
                time.sleep(1)
            del actors[actor]
        
        #Update player's speed
        entities["player"][0] = player[1]["SPD"] + player[4]["SPD"]
    
    if isDead:
        info = data[2]
        return GameOver(info)
    elif hasQuit:
        info = data[2]
        global title
        print(title)
        return Title(info)
    else:    
        print("You win!")
        stage = data[1]
        print(DisplayMap(stage[0], stage[1], stage[2]))
        
        return Menu(data)

#Player's actions
def PlayerPhase(data, enemies):
    if data[0][1]["Special"] == 100:
        special = "x = special, "
        specialReady = True
    else:
        special = ""
        specialReady = False
    
    #Retrieve player input and call the respective function
    command = input(f"\nWhat do you want to do? (a = attack, {special}c = check, s = stats, q = quit) ")
    command = command.lower()
    if command == "a":
        return Attack(data, enemies)
    elif command == "x" and specialReady:
        return Special(data, enemies)
    elif command == "c":
        return CheckEnemy(data, enemies)
    elif command == "s":
        return PlayerStats(data, True, enemies)
    elif command == "q":
        return Quit(data, True, enemies)
    else:
        print("\nInvalid action.")
        return PlayerPhase(data, enemies)

#Attack the enemy (uses a turn)
def Attack(data, enemies):
    #SELECTING AN ENEMY
    enemyList = []
    #Configure input message if there are multiple enemies
    if len(enemies) > 1:
        message = ""
        for i, key in enumerate(enemies.keys()):
            message += f"{i+1} = {key}, "
            enemyList.append(key)
            
        print("\nWhich enemy do you want to attack?")
        select = input(f"\n{message}b = back ")
        select = select.lower()
        
        if select.isdigit():
            i = int(select) - 1
            if i >= 0 and i < len(enemyList):
                #Select the chosen enemy
                enemy = enemyList[i]
            else:
                print("\nInvalid action.")
                return Attack(data, enemies)
        elif select == "b":
            return PlayerPhase(data, enemies)
        else:
            print("\nInvalid action.")
            return Attack(data, enemies)
        
    #Automatically select the enemy if there is only one
    elif len(enemies) == 1:
        for key in enemies.keys():
            enemyList.append(key)
        enemy = enemyList[0]
    
    #ATTACKING THE ENEMY
    player = data[0]
    stats = player[1]
    statChanges = player[4]
    playerHit = stats["HIT"] + statChanges["HIT"]
    playerSPD = stats["SPD"] + statChanges["SPD"]
    
    enemyStats = enemies[enemy][0]
    enemyAvo = enemyStats["AVO"]
    enemySPD = enemyStats["SPD"]
    
    attacks = SpeedCheck(playerSPD, enemySPD)
    counter = 0
    hit = False
    print("")
    
    if attacks == 2:
        print("Double attack!")
    
    for attack in range(attacks):
        if not AccuracyCheck(playerHit, enemyAvo):
            print("The attack missed!")
        else:
            #Attacking the chosen enemy
            hit = True
            playerATK = stats["ATK"] + player[4]["ATK"]
            enemyDEF = enemyStats["DEF"]
            damage = TakeDamage(playerATK, enemyDEF)
            enemyStats["HP"] -= damage
            counter += damage
            
            #Increase special gauge
            stats["Special"] = IncreaseSpecial(stats["Special"])
            
        if enemyStats["HP"] <= 0:
            break
        
    if hit:
        if counter > 0:        
            print(f"{enemy} took {counter} damage.")
            #Kill the enemy if their HP reaches 0
            if enemyStats["HP"] <= 0:
                print(f"{enemy} is destroyed!")
                data = GainEXP(data, enemies[enemy][1]["EXP"], enemyStats["LV"])
                del enemies[enemy]
        else:
            print(f"{enemy} took no damage.")
            
    return data, enemies, False

#Attack all enemies with a strong attack
def Special(data, enemies):
    player = data[0]
    name = player[0]
    stats = player[1]
    statChanges = player[4]
    playerATK = (stats["ATK"] + statChanges["ATK"]) * 2
    playerHit = stats["HIT"] + statChanges["HIT"] + 50
    playerSPD = stats["SPD"] + statChanges["SPD"]
    
    print(f"{name} launched a powerful attack!")
    deadList = []
    
    for enemy, info in enemies.items():
        enemyStats = info[0]
        enemySPD = enemyStats["SPD"]
        enemyAvo = enemyStats["AVO"]
        
        attacks = SpeedCheck(playerSPD, enemySPD)
        hit = False
        counter = 0
        
        if attacks == 2:
            print("Double attack!")
        
        for attack in range(attacks):
            if not AccuracyCheck(playerHit, enemyAvo):
                print("The attacked missed!")
            else:
                hit = True
                enemyDEF = enemyStats["DEF"]
                damage = TakeDamage(playerATK, enemyDEF)
                enemyStats["HP"] -= damage
                counter += damage
        
            if enemyStats["HP"] <= 0:
                break
        
        if hit:
            if counter > 0:
                print(f"{enemy} took {damage} damage.")
                if enemyStats["HP"] <= 0:
                    print(f"{enemy} is destroyed!")
                    data = GainEXP(data, enemies[enemy][1]["EXP"], enemyStats["LV"])
                    deadList.append(enemy)
            else:
                print(f"{enemy} took no damage.")
        
        time.sleep(1)
    
    for enemy in deadList:
        del enemies[enemy]
        
    #Reset special gauge
    stats["Special"] = 0
    return data, enemies, False

def IncreaseSpecial(value):
    if value < 100:
        value += 5
        
        if value == 100:
            print("\nSpecial ready!")
    
    return value

#Calculate how much damage is dealt
def TakeDamage(attackerATK, defenderDEF):
    if attackerATK < defenderDEF:
        damage = 0
    else:
        damage = attackerATK - defenderDEF
    return damage

def AccuracyCheck(attackerHit, defenderAvo):
    hitRate = attackerHit - defenderAvo
    if random.randint(1, 100) <= hitRate:
        return True
    else:
        return False
#Attack twice if player is 5 SPD faster than the enemy
def SpeedCheck(attackerSPD, defenderSPD):
    if attackerSPD - defenderSPD >= 5:
        return 2
    else:
        return 1

#Gain EXP from defeating an enemy and checking for level up
def GainEXP(data, exp, lv):
    player = data[0]
    stats = player[1]
    scale = lv / stats["LV"]
    stats["EXP"] += int(exp * scale)
    
    #Level up
    statChanges = ""
    while stats["EXP"] >= 100:
        stats["EXP"] -= 100
        stats["LV"] += 1
        
        #Roll stat growths and increment stats
        growth = player[2]
        statChanges = ""
        for stat, chance in growth.items():
            roll = random.randint(1, 100)
            if roll <= chance:
                stats[stat] += 1
                statChanges += f"{stat} +1, "
        
        statChanges = statChanges[:-2]
        stats["HP"] = stats["Max HP"]
        
        #Inform the player they have leveled up and show the new stats
        print("\nLevel up!")
        print(statChanges)
        print(stats)
        
    return data

#Check all enemies' info (DOES NOT use a turn)
def CheckEnemy(data, enemies):
    for enemy, info in enemies.items():
        print("\n" + enemy)
        print(info[0])
        print(info[1]["Flavour"])
        
    return PlayerPhase(data, enemies)

#Enemies attack the player
def EnemyPhase(data, enemies, enemy):
    enemyStats = enemies[enemy][0]
    info = enemies[enemy][1]
    special = info["Special"][0]
    specialValue = info["Special"][1]
    
    player = data[0]
    name = player[0]
    stats = player[1]
    statChanges = player[4]
    
    isDead = False
    print("")
    
    if special == "Wait" and random.randint(1, 100) <= specialValue:
        #Enemy does nothing
        print(f"{enemy} is watching closely.")
        return data, enemies, isDead
    elif special == "Charge" and specialValue == 0:
        #Give player a grace period for strong enemies
        print(f"{enemy} is charging up a powerful attack.")
        info["Special"][1] = 1
        return data, enemies, isDead
    elif special == "Flee" and enemyStats["HP"] <= specialValue:
        if random.randint(1, 100) <= info["Special"][2]:
            #Enemy runs away if their HP is low
            print(f"{enemy} ran away!")
            del enemies[enemy]
            return data, enemies, isDead
    elif special == "Debuff" and random.randint(1, 100) <= specialValue:
        #Reduce the players' stats temporarily
        print(f"{enemy} released an EMP!")
        
        lower = info["Special"][2]
        upper = info["Special"][3]
        statsDebuffed = ""
        
        for stat in statChanges.keys():
            if statChanges[stat] > -6:
                debuffAmount = random.randint(lower, upper)
                statChanges[stat] -= debuffAmount
                if debuffAmount > 0:
                    statsDebuffed += f"{stat}, "
                if statChanges[stat] < -6:
                    statChanges[stat] = -6
                    
        if statsDebuffed == "":
                statsDebuffed = "But no stats were"
        else:
            statsDebuffed = statsDebuffed[:-2]
        print(f"{statsDebuffed} decreased.")
        return data, enemies, isDead
    
    #Attack if not using a special move
    playerSPD = stats["SPD"] + statChanges["SPD"]
    playerAvo = stats["AVO"] + statChanges["AVO"]
    enemySPD = enemyStats["SPD"]
    enemyHit = enemyStats["HIT"]
    
    attacks = SpeedCheck(enemySPD, playerSPD)
    counter = 0
    hit = True
    exploded = False
    
    if special == "Explode" and len(enemies) == 1:
        #Enemy explodes, killing themselves to do massive damage
        print(f"{enemy} exploded!")
        
        enemyATK = enemyStats["ATK"] * 3
        playerDEF = stats["DEF"] + statChanges["DEF"]
        damage = TakeDamage(enemyATK, playerDEF)
        attacks = 1
        exploded = True
    else:
        print(f"{enemy} attacked.")
            
        playerDEF = stats["DEF"]
        enemyATK = enemyStats["ATK"]
        damage = TakeDamage(enemyATK, playerDEF)
    
    if attacks == 2:
        print("Double attack!")
    
    for attack in range(attacks):
        if not AccuracyCheck(enemyHit, playerAvo):
            print(f"{enemy}'s attack missed!")
            hit = False
        elif damage >= stats["HP"] and stats["Special"] == 100:
            #Auto guard a lethal attack if special gauge is full
            print(f"{name} blocked the attack!")
            stats["Special"] -= 50
        else:
            stats["HP"] -= damage
            counter += damage
            stats["Special"] = IncreaseSpecial(stats["Special"])
            
        if player[1]["HP"] <= 0:
            break
        
    if special == "Charge":
        info["Special"][1] = 0
            
    if hit:
        if counter > 0:        
            print(f"{name} took {counter} damage.")
            #Game over if player dies
            if player[1]["HP"] <= 0:
                print(f"\n{name} has fallen in combat...")
                print("GAME OVER")
                isDead = True
        else:
            print(f"{name} took no damage.")
    
    if exploded:
        del enemies[enemy]
        
    return data, enemies, isDead

#//////////////////////////////////////////////////////
#GAME OVER

#Ask the player if they want to play again
def GameOver(info):
    command = input("\nPlay again? (r = restart, q = quit) ")
    command = command.lower()
    
    if command == "r":
        return Start(info)
    elif command == "q":
        global title
        print(title)
        return Title(info)
    else:
        print("\nInvalid action.")
        return GameOver(info)
    
#//////////////////////////////////////////////////////
#RUN THE GAME

title = """
  _______ _____            _   _  ____  _    _ _____ _      _____ ____________ _____  
 |__   __|  __ \     /\   | \ | |/ __ \| |  | |_   _| |    |_   _|___  /  ____|  __ \ 
    | |  | |__) |   /  \  |  \| | |  | | |  | | | | | |      | |    / /| |__  | |__) |
    | |  |  _  /   / /\ \ | . ` | |  | | |  | | | | | |      | |   / / |  __| |  _  / 
    | |  | | \ \  / ____ \| |\  | |__| | |__| |_| |_| |____ _| |_ / /__| |____| | \ \ 
    |_|  |_|  \_\/_/    \_\_| \_|\___\_\\\____/|_____|______|_____/_____|______|_|  \_\\
                                                                                      
                                                                                      
"""                                                                                      
print(title)
Title(info) 
