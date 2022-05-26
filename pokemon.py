# 5/25/2021 Blake Butsko      (Approx. date)
from random import randint


x_axis = {'Normal':0,'Fighting':1,'Flying':2,'Poison':3,'Ground':4,'Rock':5,'Bug':6,'Ghost':7,'Steel':8,'Fire':9,'Water':10,'Grass':11,'Electric':12,'Psychic':13,'Ice':14,'Dragon':15,'Dark':16,'Fairy':17}
effectiveness_chart = {'Normal':[1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1],
'Fighting':[2,1,0.5,0.5,1,2,0.5,0,2,1,1,1,1,0.5,2,1,2,0.5],
'Flying':[1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1],
'Poison':[1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2], 
'Ground':[1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1],
'Rock':[1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1],
'Bug':[1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5],
'Ghost':[0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1],
'Steel':[1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2],
'Fire':[1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1],
'Water':[1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1],
'Grass':[1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1],
'Electric':[1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1],
'Psychic':[1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1],
'Ice':[1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1],
'Dragon':[1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0],
'Dark':[1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5],
'Fairy':[1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]}

stat_keys = ['stat_health','stat_attack' ,'stat_defense' ,'stat_sp_attack' ,'stat_sp_defense' ,'stat_sp_defense'] #Might mess with things if so put it in the obj 
# Put these variables in the class if they need to be brought across different files, they're up here right now because I felt like it be a way to have every instance of the class bring them
# over


class Pokemon:
  def __init__(self, name, level, type, ko, base_stats_list):#base_stats_list is a list used to calculate the stats for the pokemon (randomness is applied by IV and maybe another random value)

    def iv_generator():
      x = randint(1,100)
      if x <= 10: return randint(1,10)
      elif x <=71: return randint(11,25)
      elif x <=97: return randint(26,30)
      else: return 31

    self.iv_health = iv_generator()
    self.iv_attack = iv_generator()
    self.iv_defense = iv_generator()
    self.iv_sp_attack = iv_generator()
    self.iv_sp_defense = iv_generator()
    self.iv_speed = iv_generator()

    base_stats = dict(zip(stat_keys, base_stats_list))

    def stat_calculator():     # (self.iv_health,)   #Check If it's for health bc that's a different formula
      pass  
      # 

    # Stats            #Those are not the actual stats they will have to be calculated using the base stats but keep them for now to get things working

    self.stat_health = base_stats['stat_health']
    self.stat_attack = stat_calculator(self.iv_attack, base_stats['stat_attack'])
    self.stat_defense = base_stats['stat_defense']
    self.stat_sp_attack = base_stats['stat_sp_attack']
    self.stat_sp_defense = base_stats['stat_sp_defense'] 
    self.stat_speed = base_stats['stat_sp_defense']

    # self.iv = #formula to calculate IV 

    self.name = name.title()
    self.level = level
    self.current_health = self.stat_health
    self.type = type
    self.is_knocked_out = ko


  def lose_health(self, amount):
    self.current_health -= amount
    if self.current_health < 0: self.current_health = 0
    if self.current_health == 0: 
      self.is_knocked_out = True
      print(self.name,'has fainted'); return
    print(self.name,'now has',self.current_health,'health')

  def gain_health(self, amount):
    if self.is_knocked_out: 
      print(self.name,'is knocked out'); return
    self.current_health += amount
    if self.current_health > self.stat_health:
      self.current_health = self.stat_health
    print(self.name,'now has',self.current_health,'health')

  def revive(self, amount): 
    self.is_knocked_out = False
    self.current_health += amount

  def level_up(self):
    #Called when pokemon hits the level of experience -> base stats will be recalulated 
    pass
  def evolve(self, new_base_stats):
    #set base_stats_list = new_base_stats, it will also have to call level_up, and new_move
    pass

  def new_move(self, move):
    #Gives pokemon new move which if current_moves == 4 it will option to replace one of the moves or not learn it
    pass

  def effectiveness(self, attack, defender):
    effect = 1
    for x in defender.type:
        effect *= effectiveness_chart[attack.att_type][x_axis[x]]
    return effect

  def attack(self, attack, defender): #Attack are the stats(power, speed, etc.) and (2: Second update) We can just make who goes first on the speed stat of the pokemon
      return ((((((2*self.level)/5)+2)*(attack.power * defender.defense))/50)+2) * self.effectiveness(attack.att_type, defender.type) * attack.crit_chance

class Moves:
  def __init__(self, att_type, power, accuracy, crit_chance):
    self.type = att_type
    self.power = power
    self.accuracy = accuracy
    self.crit_chance = crit_chance
    # see if you have to make a function for crit chance


class Trainer:  
  def __init__(self, name, pokemon_party):
    self.name = name
    self.pokemon_party = [pokemon_party]
  def add_pokemon(self, pokemon):
    self.pokemon_party.append(pokemon)
  def use_potion(self, pokemon, potion_value): #I'm just having the only item be a potion for now so this method will eventually be use item and will take the item as a parameter then call item.effect or something along those lines
    pokemon.gain_health(potion_value)
  def catch_pokemon(self, pokemon, Pokeball): #Will have a chance to catch a wild pokemon based on pokemon health and ball type
    # if pokemon in all.pokemon_party #find out how to check all instances of that object varible
    # Pokeball.type
    pass

# charmander = Pokemon('Charmander', 10, ['Fire'], 58, 58, False)
# squirtle = Pokemon('squirtler', 10, ['Water'], 60, 60, False )
bulbasaur = Pokemon('bulbasaur', 10, ['Grass', 'Poison'], False, [45,49,49,65,65,45])

print(bulbasaur.current_health)

# from random import choice
# test = ['A'] * 5 + ['B'] * 5 + ['C'] * 90
# print (random.choice(test))
print (randint(1,100))

# print(charmander.effectiveness('Fire', bulbasaur.type))   #Using Pokemon type rather than attack type so it is a list and can't be put as a key so it we be casted as a string

#implement fainting either as a method or check the boolean at the start of most methods so the pokemon can't use moves after it's fainted (if you decide check at methods take it in as an arguement then if ko: print('Your pokemon can't do that it's knocked out'; end))

# could make stats iterable and update them that way

# Have IV's be herditary if you want to do breeding





# Scrapped the .title() for pokemon.type but you could do a comprehensive for loop



# for x in bulbasaur.type:
#     print(x, type(x))

# test = 'grass, poison'
# print([test])
# print(type([test]))


# charmander.lose_health(200)
# # print(charmander.current_health)
# # print(charmander.is_knocked_out)
# charmander.gain_health(200)
# charmander.revive(10)
# charmander.gain_health(200)












# import csv

# with open(r'C:\Users\blake\OneDrive\Desktop\Visual Studio Python\Effectiveness_Chart.csv') as eff_chart:
#     eff = csv.reader(eff_chart, delimiter=' ', quotechar='|')
#     for row in eff:
#         print(', '.join(row))
















# x_axis = {'Normal':0,'Fighting':1,'Flying':2,'Poison':3,'Ground':4,'Rock':5,'Bug':6,'Ghost':7,'Steel':8,'Fire':9,'Water':10,'Grass':11,'Electric':12,'Psychic':13,'Ice':14,'Dragon':15,'Dark':16,'Fairy':17}

# effectiveness = {'Normal':[1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1],
# 'Fighting':[2,1,0.5,0.5,1,2,0.5,0,2,1,1,1,1,0.5,2,1,2,0.5],
# 'Flying':[1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1],
# 'Poison':[1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2], 
# 'Ground':[1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1],
# 'Rock':[1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1],
# 'Bug':[1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5],
# 'Ghost':[0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1],
# 'Steel':[1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2],
# 'Fire':[1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1],
# 'Water':[1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1],
# 'Grass':[1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1],
# 'Electric':[1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1],
# 'Psychic':[1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1],
# 'Ice':[1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1],
# 'Dragon':[1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0],
# 'Dark':[1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5],
# 'Fairy':[1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]}

# ~~~~~~~~ Recycling Bin ~~~~~~~~

# temp = [[1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1],
# [2,1,0.5,0.5,1,2,0.5,0,2,1,1,1,1,0.5,2,1,2,0.5],
# [1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1],
# [1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2],
# [1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1],
# [1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1],
# [1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5],
# [0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1],
# [1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2],
# [1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1],
# [1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1],
# [1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1],
# [1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1],
# [1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1],
# [1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1],
# [1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0],
# [1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5],
# [1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]]