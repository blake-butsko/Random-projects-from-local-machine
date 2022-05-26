# Blake Butsko 10/05/21
# see if you could turn it into a web version by turning it into return statements

# test_input = input("left or right young traveller: ")
# if test_input == "left":
# elif test_input =="right":
# else: print("")


# either left or right else take new input - how do I reverse it so it only runs if it's left or right
# while True:
import t_a_descriptions


stink = input("left or right young traveller: ").lower()
if stink == "left": t_a_descriptions.beginning_left()
elif stink == "right": t_a_descriptions.beginning_right()
else: print("I'm not sure I understand")
