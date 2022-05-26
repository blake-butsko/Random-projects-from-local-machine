#problem one
import math
# print( (1.08*10**31)*(300**3)*math.exp( -1.12/((8.62*10**-5)*300) ) )
# x = (1.08*10**31)*(300**3)*math.exp( -1.12/((8.62*10**-5)*300) )
# x = round(x,5)
# print("ni is equal to ",math.sqrt(x))
def intrinstic_carrier_denstiy_si(T, B = 1.08*10**31,EG = 1.12):
    x = (B)*(T**3)*math.exp( -EG/((8.62*10**-5)*T) )
    print("ni^2 = ","{:e}".format(x))
    print("ni = ","{:e}".format( math.sqrt(x) ))

def intrinstic_carrier_denstiy_ge(T, B = 2.31*10**30,EG = 0.66):
    x = (B)*(T**3)*math.exp( -EG/((8.62*10**-5)*T) )
    print("ni^2 = ","{:e}".format(x))
    print("ni = ","{:e}".format( math.sqrt(x) ))



print('silicon')
intrinstic_carrier_denstiy_si(500)
print('germanium')
intrinstic_carrier_denstiy_ge(500)