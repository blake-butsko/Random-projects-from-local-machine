#project in codecademy.     started on 4/5/2021.    finished 4/5/2021.
import random

money = 100
card_deck = []
for c in range(4):
  card_deck.extend(range(1,14))
wheel = [*range(-1,37)]
#Write your game of chance functions here
#have print statements reesult, if you won/lost, how much money won
#have an additonal function called in all functions that calculates money lost/earned based on odds
#saving money between runs

def coinflip(bet, choice):
  print("\n")
  global money
  if random.random() > 0.5: val = "heads"
  else: val = "tails"
  if choice.lower() == val: money += bet; print("You won", bet, "dollars!")
  else: money += -bet; print("Sorry, you lost", bet, "dollars")
  print("your total is now", money,"dollars")

def Cho_Han(bet, choice):
  print("\n")
  global money
  dice_sum = random.randint(1,6) + random.randint(1,6)
  if (dice_sum % 2) == 0: sum_val = "even"
  else: sum_val = "odd"
  if choice.lower() == sum_val: money += bet; print("You won", bet,"dollars!")
  else: money += -bet; print("Sorry, you lost", bet, "dollars")
  print("your total is now", money,"dollars")

def war(bet):
  print("\n")
  global money
  x = 0
  while x < 26:
    player = random.choice(card_deck)
    card_deck.remove(player)
    opponent = random.choice(card_deck)
    card_deck.remove(opponent)
    if player > opponent: money += bet; print("You won", bet,"dollars!");print("your total is now", money,"dollars"); return 
    elif player == opponent: print("You tied!"); print("The tie was", player, "and", opponent)
    else: money += -bet; print("Sorry, you lost", bet, "dollars"); print("your total is now", money,"dollars"); return
    x += 1


def roulette(bet, guess):
  print("\n")
  global money
  if len(guess) < 3: int(guess)

  value = random.choice(wheel)
  if value % 2 == 0: parity = "even"
  else: parity = "odd"

  if value == 0 or value == 00: money += -bet; print("Sorry, you hit Zero"); print("your total is now", money,"dollars"); return
  elif guess == value: money += (bet*35); print("You won the jackpot!!",bet*35,"dollars"); return
  elif str(guess).lower() == parity: money += bet; print("You won", bet,"dollars!"); print("your total is now", money,"dollars"); return
  else: money += -bet; print("Sorry, you lost", bet, "dollars"); print("your total is now", money,"dollars"); return

def 


#directly test value == 0 or value == 00:


#Call your game of chance functions here

# coinflip(50, "heads")
# Cho_Han(30, "Even")
# war(20)

# for c in range(10):
#     roulette(int(input("Please enter a bet ")), input("Please place your guess for roulette "))

