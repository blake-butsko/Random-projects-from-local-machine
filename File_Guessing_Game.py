#This is a trial of while: True and general use of input, written 05/02/2021 by Blake Butsko while he should be studying for finals
#I only forgot to save before running, but I also found out that if you press control then hit a number it opens the corresponding number of windows counting the current one, so control
# 3 would open 2 additional windows, you can also toggle them this way

# num = random.randint(0,100)
num = 20

for x in range (10):
   guess = int(input("Please guess a number between 0 and 100: "))
   if guess < 0 or guess > 100:
      while (guess < 0 or guess > 100):
         guess = int(input("That was outside of the range, Please guess a number between 0 and 100: "))
   if guess == num:
      print("You guessed it!!!!")
      break
   elif guess > num + 10:
      print("lower")
   elif guess < num + 10:
      print("lower")
   elif 6 < guess - num:
      print("just a little higher")
   elif 6 > num - guess:
      print("just a little lower")


# print("""

#         .--'''''''''--.
#      .'      .---.      '.
#     /    .-----------.    \\
#    /        .-----.        \\
#    |       .-.   .-.       |
#    |      /   \ /   \      |
#     \    | .-. | .-. |    /
#      '-._| | | | | | |_.-'
#          | '-' | '-' |
#           \___/ \___/
#        _.-'  /   \  `-._
#      .' _.--|     |--._ '.
#      ' _...-|     |-..._ '
#             |     |
#             '.___.'
#               | |
#              _| |_
#             /\( )/\\
#            /  ` '  \\
#           | |     | |
#           '-'     '-'
#           | |     | |
#           | |     | |
#           | |-----| |
#        .`/  |     | |/`.
#        |    |     |    |
#        '._.'| .-. |'._.'
#              \ | /
#              | | |
#              | | |
#              | | |
#             /| | |\\
#           .'_| | |_`.
#           `. | | | .'
#        .    /  |  \    .
#       /o`.-'  / \  `-.`o\\
#      /o  o\ .'   `. /o  o\\
#      `.___.'       `.___.' 

# """)