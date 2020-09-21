from math import exp
def f(x):
     return x*exp(-x)
f(0.1)
f(10)

#f(0.1)= 0.09048374180359596
#f(10)= 0.0004539999299762484856
from math import exp
def f(x):
 return x*exp(-x)
# Numerically Integrate f(x) from 0 to 50
intgrl=0.0
x=0
xmax=50
dx=0.1
while x<xmax:
 intgrl+=dx*f(x)
 x+=dx
print("Integral=",intgrl,"error=",abs(1-intgrl)) 
Integral= 0.9991670831680466 error= 0.0008329168319534119
