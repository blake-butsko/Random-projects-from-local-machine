#05/28/2021  Hi Blake
#Everything is in SI units and weight/mass is in Kg

import math

from Turtle_fun import proj_graphic

football = 0.042857
baseball = 0.152
air_compressor_impulse = 0.0857

def distance_calc(angle=45, force=20, projectile_weight = football, impluse = air_compressor_impulse):
    a = force/projectile_weight
    V = a * impluse
    #Now we calculate the throw
    Vix = V * math.cos(math.radians(angle))
    Viy = V * math.sin(math.radians(angle))
    t = (Viy/9.8) *2
    height = Viy * (t/2)
    d = Vix * t

    # proj_graphic(d,height,angle) -> directly calls the one from turtle fun how do I use the function in this one   
    return f"The distance traveled is {round(d,2)}\nThe maximum height was {round(height,2)}\nAnd the flight time was {round(t,2)}"
 



# Its only drawing the on in Turtle

print( distance_calc(force=20) )
# print(math.sin(math.radians(45)))
# print(math.cos(math.radians(45)))