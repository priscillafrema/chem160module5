from math import pi, cos, sqrt
dt=0.6
mass=10
period=10
omega=2*pi/period
k=mass*omega**2
tmax=period
x=+1
v=0
t=0
rms_error=0
steps=0
while t<tmax:
 f=-k*x
 a=f/mass
 x+=v*dt
 v+=a*dt
 x_exact=cos(2*pi*t/period)
 rms_error+=(x-x_exact)**2
 steps+=1
 t+=dt
print("dt=%f RMS error=%f"%(dt, sqrt(rms_error/steps)))

#dt=0.200000 RMS error=0.229347
#dt=0.400000 RMS error=0.492908
#dt=0.600000 RMS error=0.854678
#when the dt value increases, the RMS error also increases