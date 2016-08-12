import numpy as np
import matplotlib.pyplot as plt

halo='m0290'
z=0
out=94
 
#thermal
#mass,rvir=np.loadtxt('/Users/aquirk/Rockstar/T{}_S/out_{}.list'.format(halo,out), usecols=(2,5,), unpack=True)
#Mc=np.amax(mass) #mass of central halo 
#n=np.argmax(mass) #index of central halo 
#Rc=rvir[n]*.72*10**-3 #in Mpc

#mass,distance=np.loadtxt('/Users/aquirk/Rockstar/T{}_S/nocentral_mass{}.txt'.format(halo,z), unpack=True)
#uniquemasses=[]
#unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
#for i in range(len(distance)):
#        if distance[i]!=distance[-1]:
#                if distance[i+1]-distance[i]>.0005:
#                        uniquemasses.append(mass[i])
#			unique_distances.append(distance[i])
#        if distance[i]==distance[-1]:
#                if distance[-1]-distance[-2]>.0005:
#                        uniquemasses.append(mass[-1])
#			unique_distances.append(distance[i])

#closemassesT=[]
#for i in range(len(uniquemasses)):
#        if (.3)>unique_distances[i]:
#                closemassesT.append(np.log10(uniquemasses[i]))

#Snow Plow
mass,rvir=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/out_{}.list'.format(halo,out), usecols=(2,5,), unpack=True)
Mc=np.amax(mass) #mass of central halo 
n=np.argmax(mass) #index of central halo 
Rc=rvir[n]*.72*10**-3 #in Mpc

mass,distance=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/nocentral_mass{}.txt'.format(halo,z), unpack=True) 

closemassesS=[]
for i in range(len(mass)):
        if (.3)>distance[i]:
                closemassesS.append(np.log10(mass[i]))

#no AGN
#mass,rvir=np.loadtxt('/Users/aquirk/Rockstar/N{}_S/out_{}.list'.format(halo,out), usecols=(2,5,), unpack=True)
#Mc=np.amax(mass) #mass of central halo 
#n=np.argmax(mass) #index of central halo 
#Rc=rvir[n]*.72*10**-3 #in Mpc

#mass,distance=np.loadtxt('/Users/aquirk/Rockstar/N{}_S/mass{}.txt'.format(halo,z), unpack=True)

#closemassesN=[]
#for i in range(len(mass)):
#        if (10*Rc)>distance[i]:
#                closemassesN.append(np.log10(mass[i]))

bins=np.linspace(8,12,16)
#plt.hist(closemassesT, bins, color='b', alpha=.5, label='Thermal')
plt.hist(closemassesS, bins, color='r', alpha=.5, label='Snow Plow')
#plt.hist(closemassesN, alpha=.5, color='g', label='no AGN')
#plt.title('{}- Stellar Mass Distribution within 10*R_vir  z={}'.format(halo,z))
plt.xlabel('log(M_sat)')
plt.ylabel('N_sat')
plt.legend()
plt.savefig('/Users/aquirk/savedplots/massdistrib{}_{}.ps'.format(halo,z))
print('massdistrib{}_{}.ps'.format(halo,z))

