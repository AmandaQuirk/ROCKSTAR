import numpy as np
import matplotlib.pyplot as plt

halo='m0290'
redshift=0
out=94

fig = plt.figure()
ax = fig.add_subplot(111)
#thermal 
#mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/T{}_S/out_{}.list'.format(halo,out), usecols=(2,5,8,9,10,), unpack=True)
#Mc=np.amax(mass) #mass of central halo 
#n=np.argmax(mass) #index of central halo 
#Xc=x[n] #units of Mpc/h
#Yc=y[n]
#Zc=z[n]
#Rc=rvir[n]*.72*10**-3 #Mpc

#radii=np.logspace(-3, 0) #inner radius=10^-3 Mpc and outer radius 1 Mpc  add number of bins

#distances=[] #will contain the distances of all halos to central halo with the lines of cade below
#for i in range(len(mass)):
#        d=(np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2)) #in Mpc
#        distances.append(d)
#D=sorted(distances) #has all distances of halos to central halo in ascending order- Mpc

#unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
#for i in range(len(D)):
#	if D[i]!=D[-1]:
#		if D[i+1]-D[i]>.0005:
#			unique_distances.append(D[i])
#	if D[i]==D[-1]:
#		if D[-1]-D[-2]>.0005:
#			unique_distances.append(D[-1])
#print(D)
#print(unique_distances)

#number=[] #will have the number of halos within the given donut 
#Xcoord=[]
#Ycoord=[]
#for i in range(len(radii)): #below looks at each donut and counts how many halos are within
#	donut=[]
#	for j in range(len(unique_distances)):
#		if radii[i]!=radii[-1]:
#			if radii[i+1]>unique_distances[j] and radii[i]<unique_distances[j]:
#				donut.append(unique_distances[j])
#		if radii[i]==radii[-1]:
#			if radii[-2]<unique_distances[j] and radii[-1]>unique_distances[j]:
#				donut.append(unique_distances[j])
#	number.append(len(donut))
#	print(radii[i], number[i])
#	Xcoord.append(np.log10(radii[i]*(Rc**-1)))
#	if radii[i]!=radii[-1]:
#		denominator=(radii[i+1]**2)-(radii[i]**2)
#	if radii[i]==radii[-1]:
#		denominator=(radii[-1]**2)-(radii[-2]**2)
#	Ycoord.append((number[i]/(np.pi*Rc*denominator))+0.00001) #number density in terms of Rvir of central halo
#	print(Xcoord,Ycoord)
#plt.plot(Xcoord,Ycoord, 'b-',linewidth=2.2)
#plt.plot(Xcoord,Ycoord, 'bo',markersize=10)

#below does the same as above for the Snow Plow Feedback
mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/out_{}.list'.format(halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass)  
n=np.argmax(mass)  
Xc=x[n] 
Yc=y[n]
Zc=z[n]
Rc=rvir[n]*.72*10**-3 

radii=np.logspace(-3, 0) 

distances=[] 
for i in range(len(mass)):
        d=(np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2)) #in Mpc
        distances.append(d)
D=sorted(distances) #has all distances of halos to central halo in ascending order- Mpc

unique_distances=[] #this eliminates 'double counted' halos 
for i in range(len(D)):
        if D[i]!=D[-1]:
                if D[i+1]-D[i]>.0005:
                        unique_distances.append(D[i])
        if D[i]==D[-1]:
                if D[-1]-D[-2]>.0005:
                        unique_distances.append(D[-1])
#print(D)
#print(unique_distances)

number=[] #will have the number of halos within the given donut 
Xcoord=[]
Ycoord=[]
for i in range(len(radii)):
        donut=[]
        for j in range(len(unique_distances)):
                if radii[i]!=radii[-1]:
                        if radii[i+1]>unique_distances[j] and radii[i]<unique_distances[j]:
                                donut.append(unique_distances[j])
                if radii[i]==radii[-1]:
                        if radii[-2]<unique_distances[j] and radii[-1]>unique_distances[j]:
                                donut.append(unique_distances[j])
        number.append(len(donut))
#       print(radii[i], number[i])
        Xcoord.append(np.log10(radii[i]*(Rc**-1)))
        if radii[i]!=radii[-1]:
                denominator=(radii[i+1]**2)-(radii[i]**2)
        if radii[i]==radii[-1]:
                denominator=(radii[-1]**2)-(radii[-2]**2)
        Ycoord.append((number[i]/(np.pi*Rc*denominator))+0.00001)
#       print(Xcoord,Ycoord)
plt.plot(Xcoord,Ycoord, 'b-',linewidth=2.2, color='r')
plt.plot(Xcoord,Ycoord, 'bo',markersize=10, color='r')

#Thermal with Mass Cut
#mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/T{}_S/out_{}.list'.format(halo,out), usecols=(2,5,8,9,10,), unpack=True)
#Mc=np.amax(mass) #mass of central halo 
#n=np.argmax(mass) #index of central halo 
#Xc=x[n] #units of Mpc/h
#Yc=y[n]
#Zc=z[n]
#Rc=rvir[n]*.72*10**-3 #Mpc

#newx=[]
#newy=[]
#newz=[]
#for i in range(len(mass)):
#	if (Mc/400)<mass[i]:
#		newx.append(x[i])
#		newy.append(y[i])
#		newz.append(z[i])
#print(len(x))
#print(len(newx))

#radii=np.logspace(-3, 0) #inner radius=10^-3 Mpc and outer radius 1 Mpc  add number of bins

#distances=[] #will contain the distances of all halos to central halo with the lines of cade below
#for i in range(len(newx)):
#        d=(np.sqrt(((Xc*.72)-(newx[i]*.72))**2+((Yc*.72)-(newy[i]*.72))**2+((Zc*.72)-(newz[i]*.72))**2)) #in Mpc
#        distances.append(d)
#D=sorted(distances) #has all distances of halos to central halo in ascending order- Mpc

#unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
#for i in range(len(D)):
#        if D[i]!=D[-1]:
#                if D[i+1]-D[i]>.0005:
#                        unique_distances.append(D[i])
#        if D[i]==D[-1]:
#                if D[-1]-D[-2]>.0005:
#                        unique_distances.append(D[-1])
#print(D)
#print(unique_distances)

#number=[] #will have the number of halos within the given donut 
#Xcoord=[]
#Ycoord=[]

#for i in range(len(radii)):
#        donut=[]
#        for j in range(len(unique_distances)):
#                if radii[i]!=radii[-1]:
#                        if radii[i+1]>unique_distances[j] and radii[i]<unique_distances[j]:
#                                donut.append(unique_distances[j])
#                if radii[i]==radii[-1]:
#                        if radii[-2]<unique_distances[j] and radii[-1]>unique_distances[j]:
#                                donut.append(unique_distances[j])
#        number.append(len(donut))
#       print(radii[i], number[i])
#        Xcoord.append(np.log10(radii[i]*(Rc**-1)))
#        if radii[i]!=radii[-1]:
#                denominator=(radii[i+1]**2)-(radii[i]**2)
#        if radii[i]==radii[-1]:
#                denominator=(radii[-1]**2)-(radii[-2]**2)
#        Ycoord.append((number[i]/(np.pi*Rc*denominator))+0.00001)
#       print(Xcoord,Ycoord)
#plt.plot(Xcoord,Ycoord, 'b-',linewidth=2.2, color='k')
#plt.plot(Xcoord,Ycoord, 'bo',markersize=5, color='k')

#Snow Plow Mass Cut
mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/out_{}.list'.format(halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass) #mass of central halo 
n=np.argmax(mass) #index of central halo 
Xc=x[n] #units of Mpc/h
Yc=y[n]
Zc=z[n]
Rc=rvir[n]*.72*10**-3 #Mpc

newx=[]
newy=[]
newz=[]
for i in range(len(mass)):
        if (Mc/400)<mass[i]:
                newx.append(x[i])
                newy.append(y[i])
                newz.append(z[i])
print(len(x))
print(len(newx))

radii=np.logspace(-3, 0) #inner radius=10^-3 Mpc and outer radius 1 Mpc  add number of bins

distances=[] #will contain the distances of all halos to central halo with the lines of cade below
for i in range(len(newx)):
        d=(np.sqrt(((Xc*.72)-(newx[i]*.72))**2+((Yc*.72)-(newy[i]*.72))**2+((Zc*.72)-(newz[i]*.72))**2)) #in Mpc
        distances.append(d)
D=sorted(distances) #has all distances of halos to central halo in ascending order- Mpc

unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
for i in range(len(D)):
        if D[i]!=D[-1]:
                if D[i+1]-D[i]>.0005:
                        unique_distances.append(D[i])
        if D[i]==D[-1]:
                if D[-1]-D[-2]>.0005:
                        unique_distances.append(D[-1])
number=[] #will have the number of halos within the given donut 
Xcoord=[]
Ycoord=[]

for i in range(len(radii)):
        donut=[]
        for j in range(len(unique_distances)):
                if radii[i]!=radii[-1]:
                        if radii[i+1]>unique_distances[j] and radii[i]<unique_distances[j]:
                                donut.append(unique_distances[j])
                if radii[i]==radii[-1]:
                        if radii[-2]<unique_distances[j] and radii[-1]>unique_distances[j]:
                                donut.append(unique_distances[j])
        number.append(len(donut))
#       print(radii[i], number[i])
        Xcoord.append(np.log10(radii[i]*(Rc**-1)))
        if radii[i]!=radii[-1]:
                denominator=(radii[i+1]**2)-(radii[i]**2)
        if radii[i]==radii[-1]:
                denominator=(radii[-1]**2)-(radii[-2]**2)
        Ycoord.append((number[i]/(np.pi*Rc*denominator))+0.00001)
#       print(Xcoord,Ycoord)
plt.plot(Xcoord,Ycoord, 'b-',linewidth=2.2, color='g')
plt.plot(Xcoord,Ycoord, 'bo',markersize=6, color='g')

#no AGN
#mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/N{}_S/out_{}.list'.format(halo,out), usecols=(2,5,8,9,10,), unpack=True)
#Mc=np.amax(mass) #mass of central halo 
#n=np.argmax(mass) #index of central halo 
#Xc=x[n] #units of Mpc/h
#Yc=y[n]
#Zc=z[n]
#Rc=rvir[n]*.72*10**-3 #Mpc

#radii=np.logspace(-3, 0) #inner radius=10^-3 Mpc and outer radius 1 Mpc  add number of bins

#distances=[] #will contain the distances of all halos to central halo with the lines of cade below
#for i in range(len(mass)):
#       d=(np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2)) #in Mpc
#      distances.append(d)
#D=sorted(distances) #has all distances of halos to central halo in ascending order- Mpc

#unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
#for i in range(len(D)):
#        if D[i]!=D[-1]:
#                if D[i+1]-D[i]>.0005:
#                        unique_distances.append(D[i])
#        if D[i]==D[-1]:
#                if D[-1]-D[-2]>.0005:
#                        unique_distances.append(D[-1])
#print(D)
#print(unique_distances)

#number=[] #will have the number of halos within the given donut 
#Xcoord=[]
#Ycoord=[]
#for i in range(len(radii)): #below looks at each donut and counts how many halos are within
#        donut=[]
#        for j in range(len(unique_distances)):
#                if radii[i]!=radii[-1]:
#                        if radii[i+1]>unique_distances[j] and radii[i]<unique_distances[j]:
#                                donut.append(unique_distances[j])
#                if radii[i]==radii[-1]:
#                        if radii[-2]<unique_distances[j] and radii[-1]>unique_distances[j]:
#                                donut.append(unique_distances[j])
#        number.append(len(donut))
#       print(radii[i], number[i])
#        Xcoord.append(np.log10(radii[i]*(Rc**-1)))
#        if radii[i]!=radii[-1]:
#                denominator=(radii[i+1]**2)-(radii[i]**2)
#        if radii[i]==radii[-1]:
#                denominator=(radii[-1]**2)-(radii[-2]**2)
#        Ycoord.append((number[i]/(np.pi*Rc*denominator))+0.00001) #number density in terms of Rvir of central halo
#       print(Xcoord,Ycoord)
#plt.plot(Xcoord,Ycoord, 'b-',linewidth=2.2, color='m')
#plt.plot(Xcoord,Ycoord, 'bo',markersize=10, color='m')

#No AGN with Mass Cut
#mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/out_{}.list'.format(halo,out), usecols=(2,5,8,9,10,), unpack=True)
#Mc=np.amax(mass) #mass of central halo 
#n=np.argmax(mass) #index of central halo 
#Xc=x[n] #units of Mpc/h
#Yc=y[n]
#Zc=z[n]
#Rc=rvir[n]*.72*10**-3 #Mpc

#newx=[]
#newy=[]
#newz=[]
#for i in range(len(mass)):
#        if (Mc/400)<mass[i]:
#                newx.append(x[i])
#                newy.append(y[i])
#                newz.append(z[i])
#print(len(x))
#print(len(newx))

#radii=np.logspace(-3, 0) #inner radius=10^-3 Mpc and outer radius 1 Mpc  add number of bins

#distances=[] #will contain the distances of all halos to central halo with the lines of cade below
#for i in range(len(newx)):
#        d=(np.sqrt(((Xc*.72)-(newx[i]*.72))**2+((Yc*.72)-(newy[i]*.72))**2+((Zc*.72)-(newz[i]*.72))**2)) #in Mpc
#        distances.append(d)
#D=sorted(distances) #has all distances of halos to central halo in ascending order- Mpc

#unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
#for i in range(len(D)):
#        if D[i]!=D[-1]:
#                if D[i+1]-D[i]>.0005:
#                        unique_distances.append(D[i])
#        if D[i]==D[-1]:
#                if D[-1]-D[-2]>.0005:
#                        unique_distances.append(D[-1])
#number=[] #will have the number of halos within the given donut 
#Xcoord=[]
#Ycoord=[]

#for i in range(len(radii)):
#        donut=[]
#        for j in range(len(unique_distances)):
#                if radii[i]!=radii[-1]:
#                        if radii[i+1]>unique_distances[j] and radii[i]<unique_distances[j]:
#                                donut.append(unique_distances[j])
#                if radii[i]==radii[-1]:
#                        if radii[-2]<unique_distances[j] and radii[-1]>unique_distances[j]:
#                                donut.append(unique_distances[j])
#        number.append(len(donut))
#       print(radii[i], number[i])
#        Xcoord.append(np.log10(radii[i]*(Rc**-1)))
#        if radii[i]!=radii[-1]:
#                denominator=(radii[i+1]**2)-(radii[i]**2)
#        if radii[i]==radii[-1]:
#                denominator=(radii[-1]**2)-(radii[-2]**2)
#        Ycoord.append((number[i]/(np.pi*Rc*denominator))+0.00001)
#       print(Xcoord,Ycoord)
#plt.plot(Xcoord,Ycoord, 'b-',linewidth=2.2, color='y')
#plt.plot(Xcoord,Ycoord, 'bo',markersize=5, color='y')

#plt.title('Projected Density {} z={}'.format(halo,redshift))
plt.yscale('log')
plt.ylim(10,10**5)
plt.xlim(-2,1)
plt.ylabel('Mpc^-3') 
plt.xlabel('log(r/r_vir)')
ax.annotate('Red=Snow Plow', xy=(-.5,5.5*10**4))
#ax.annotate('Blue=Thermal', xy=(-.5,4*10**4))
#ax.annotate('Pink= No AGN', xy=(-.5,2.9*10**4))
ax.annotate('Green=Snow Plow with Mass Cut', xy=(-.5,2.1*10**4))
#ax.annotate('Black=Thermal with Mass Cut', xy=(-.5,1.5*10**4))
#ax.annotate('Yellow=No AGN with Mass Cut', xy=(-.5,1.1*10**4))
plt.savefig('/Users/aquirk/savedplots/prodensity{}_{}.ps'.format(halo,redshift))
	
