class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + ' is available from '+ self.start_time +' '+ self.end_time

  def calculate_bill(self, purchased_items):
    i = 0
    for x in purchased_items:
      i += self.items[x]
    i += i * 0.0575
    return round(i,2)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

    # for x in self.menus:
    #   if 'am' in x.start_time:
    #     am_range = range(x.start_time)

  def __repr__(self):
    return self.address

  def available_menu(self, time):
    for x in self.menus:
      # if time in range()

# range needs two ints so you can seperate the string from the int or cast in the string representation in Menu

# brunch = Menu('Brunch menu',
# {
#     'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
#     }, '11 am', '4 pm')

early_bird = Menu('Early-Bird menu', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, '3 pm', '6 pm')

dinner = Menu('Dinner menu',{'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, '5 pm', '11 pm')

kids = Menu('Kids menu',{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, '11 am', '9 pm')

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])

flagship_store = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids])

print(brunch)
print( early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']) )

x = '11 am'
print(x.split())

