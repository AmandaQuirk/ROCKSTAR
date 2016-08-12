import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
from pylab import *

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]

#snow plow m0215
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0215_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
	if (0.01*Mc)<=mass[i]:
		big_masses.append(mass[i])
		big_distances.append(distance[i])
for i in range(len(big_masses)):
	if 0<big_distances[i] and .05>big_distances[i]:
		SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
	if big_distances[i]<0.15 and big_masses[i]!=Mc:
		SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP215_y1=np.sum(SP_interval1)
SP215_y2=np.sum(SP_interval2)
SP215_y3=np.sum(SP_interval3)
SP215_y4=np.sum(SP_interval4)
SP215_y5=np.sum(SP_interval5)
SP215_y6=np.sum(SP_interval6)
#print(SP_interval1, SP_interval2, SP_interval3, SP_interval4, SP_interval5, SP_interval6)
#print(big_masses, big_distances)
#print(SP215_y1, SP215_y2, SP215_y3, SP215_y4, SP215_y5, SP215_y6)
#thermal m0215
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0215_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
		big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T215_y1=np.sum(T_interval1)
T215_y2=np.sum(T_interval2)
T215_y3=np.sum(T_interval3)
T215_y4=np.sum(T_interval4)
T215_y5=np.sum(T_interval5)
T215_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0259
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0259_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP259_y1=np.sum(SP_interval1)
SP259_y2=np.sum(SP_interval2)
SP259_y3=np.sum(SP_interval3)
SP259_y4=np.sum(SP_interval4)
SP259_y5=np.sum(SP_interval5)
SP259_y6=np.sum(SP_interval6)
#thermal m0259
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0259_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T259_y1=np.sum(T_interval1)
T259_y2=np.sum(T_interval2)
T259_y3=np.sum(T_interval3)
T259_y4=np.sum(T_interval4)
T259_y5=np.sum(T_interval5)
T259_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0290
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0290_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP290_y1=np.sum(SP_interval1)
SP290_y2=np.sum(SP_interval2)
SP290_y3=np.sum(SP_interval3)
SP290_y4=np.sum(SP_interval4)
SP290_y5=np.sum(SP_interval5)
SP290_y6=np.sum(SP_interval6)
#thermal m0290
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0290_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T290_y1=np.sum(T_interval1)
T290_y2=np.sum(T_interval2)
T290_y3=np.sum(T_interval3)
T290_y4=np.sum(T_interval4)
T290_y5=np.sum(T_interval5)
T290_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0190
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0190_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP190_y1=np.sum(SP_interval1)
SP190_y2=np.sum(SP_interval2)
SP190_y3=np.sum(SP_interval3)
SP190_y4=np.sum(SP_interval4)
SP190_y5=np.sum(SP_interval5)
SP190_y6=np.sum(SP_interval6)
#thermal m0190
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0190_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T190_y1=np.sum(T_interval1)
T190_y2=np.sum(T_interval2)
T190_y3=np.sum(T_interval3)
T190_y4=np.sum(T_interval4)
T190_y5=np.sum(T_interval5)
T190_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0329
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0329_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP329_y1=np.sum(SP_interval1)
SP329_y2=np.sum(SP_interval2)
SP329_y3=np.sum(SP_interval3)
SP329_y4=np.sum(SP_interval4)
SP329_y5=np.sum(SP_interval5)
SP329_y6=np.sum(SP_interval6)
#thermal m0329
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0329_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T329_y1=np.sum(T_interval1)
T329_y2=np.sum(T_interval2)
T329_y3=np.sum(T_interval3)
T329_y4=np.sum(T_interval4)
T329_y5=np.sum(T_interval5)
T329_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0380
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0380_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP380_y1=np.sum(SP_interval1)
SP380_y2=np.sum(SP_interval2)
SP380_y3=np.sum(SP_interval3)
SP380_y4=np.sum(SP_interval4)
SP380_y5=np.sum(SP_interval5)
SP380_y6=np.sum(SP_interval6)
#thermal m0380
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0380_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T380_y1=np.sum(T_interval1)
T380_y2=np.sum(T_interval2)
T380_y3=np.sum(T_interval3)
T380_y4=np.sum(T_interval4)
T380_y5=np.sum(T_interval5)
T380_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0408
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0408_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP408_y1=np.sum(SP_interval1)
SP408_y2=np.sum(SP_interval2)
SP408_y3=np.sum(SP_interval3)
SP408_y4=np.sum(SP_interval4)
SP408_y5=np.sum(SP_interval5)
SP408_y6=np.sum(SP_interval6)
#thermal m0408
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0408_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T408_y1=np.sum(T_interval1)
T408_y2=np.sum(T_interval2)
T408_y3=np.sum(T_interval3)
T408_y4=np.sum(T_interval4)
T408_y5=np.sum(T_interval5)
T408_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow 501
SP501_y1=np.sum(SP_interval1)
SP501_y2=np.sum(SP_interval2)
SP501_y3=np.sum(SP_interval3)
SP501_y4=np.sum(SP_interval4)
SP501_y5=np.sum(SP_interval5)
SP501_y6=np.sum(SP_interval6)
#thermal m0501
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0501_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T501_y1=np.sum(T_interval1)
T501_y2=np.sum(T_interval2)
T501_y3=np.sum(T_interval3)
T501_y4=np.sum(T_interval4)
T501_y5=np.sum(T_interval5)
T501_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0763
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0763_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP763_y1=np.sum(SP_interval1)
SP763_y2=np.sum(SP_interval2)
SP763_y3=np.sum(SP_interval3)
SP763_y4=np.sum(SP_interval4)
SP763_y5=np.sum(SP_interval5)
SP763_y6=np.sum(SP_interval6)
#thermal m0763
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0763_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T763_y1=np.sum(T_interval1)
T763_y2=np.sum(T_interval2)
T763_y3=np.sum(T_interval3)
T763_y4=np.sum(T_interval4)
T763_y5=np.sum(T_interval5)
T763_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plow m0209
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0209_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(mass)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(mass[i])
                big_distances.append(distance[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                SP_interval1.append(0.72*big_masses[i]) #the 0.72 converts units to Msun
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                SP_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                SP_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                SP_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                SP_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                SP_interval6.append(0.72*big_masses[i])
SP209_y1=np.sum(SP_interval1)
SP209_y2=np.sum(SP_interval2)
SP209_y3=np.sum(SP_interval3)
SP209_y4=np.sum(SP_interval4)
SP209_y5=np.sum(SP_interval5)
SP209_y6=np.sum(SP_interval6)
#thermal m0209
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0209_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T209_y1=np.sum(T_interval1)
T209_y2=np.sum(T_interval2)
T209_y3=np.sum(T_interval3)
T209_y4=np.sum(T_interval4)
T209_y5=np.sum(T_interval5)
T209_y6=np.sum(T_interval6)

SP_interval1=[]
SP_interval2=[]
SP_interval3=[]
SP_interval4=[]
SP_interval5=[]
SP_interval6=[]
T_interval1=[]
T_interval2=[]
T_interval3=[]
T_interval4=[]
T_interval5=[]
T_interval6=[]
#snow plot m0858
SP858_y1=np.sum(SP_interval1)
SP858_y2=np.sum(SP_interval2)
SP858_y3=np.sum(SP_interval3)
SP858_y4=np.sum(SP_interval4)
SP858_y5=np.sum(SP_interval5)
SP858_y6=np.sum(SP_interval6)
#thermal m0858
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Tm0858_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
unique_masses=[]
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_masses.append(mass[i])
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_masses.append(mass[-1])
                        unique_distances.append(distance[i])
big_masses=[] #will contain the masses of galaxies that pass the mass cut
big_distances=[] #will contain the distances of galaxies that pass the mass cut
for i in range(len(unique_masses)):
        if (0.01*Mc)<=mass[i]:
                big_masses.append(unique_masses[i])
                big_distances.append(unique_distances[i])
for i in range(len(big_masses)):
        if 0<big_distances[i] and .05>big_distances[i]:
                T_interval1.append(0.72*big_masses[i])
        if 0.1>big_distances[i] and big_masses[i]!=Mc:
                T_interval2.append(0.72*big_masses[i])
        if 0.15>big_distances[i] and big_masses[i]!=Mc:
                T_interval3.append(0.72*big_masses[i])
        if 0.2>big_distances[i] and big_masses[i]!=Mc:
                T_interval4.append(0.72*big_masses[i])
        if 0.25>big_distances[i] and big_masses[i]!=Mc:
                T_interval5.append(0.72*big_masses[i])
        if 0.3>big_distances[i] and big_masses[i]!=Mc:
                T_interval6.append(0.72*big_masses[i])
T858_y1=np.sum(T_interval1)
T858_y2=np.sum(T_interval2)
T858_y3=np.sum(T_interval3)
T858_y4=np.sum(T_interval4)
T858_y5=np.sum(T_interval5)
T858_y6=np.sum(T_interval6)

#plotting 
N=11
x=[25,75,125,175,225,275]
SP_y1=SP215_y1+SP259_y1+SP190_y1+SP290_y1+SP329_y1+SP380_y1+SP408_y1+SP501_y1+SP763_y1+SP209_y1+SP858_y1
SP_y2=SP215_y2+SP259_y2+SP190_y2+SP290_y2+SP329_y2+SP380_y2+SP408_y2+SP501_y2+SP763_y2+SP209_y2+SP858_y2
SP_y3=SP215_y3+SP259_y3+SP190_y3+SP290_y3+SP329_y3+SP380_y3+SP408_y3+SP501_y3+SP763_y3+SP209_y3+SP858_y3
SP_y4=SP215_y4+SP259_y4+SP190_y4+SP290_y4+SP329_y4+SP380_y4+SP408_y4+SP501_y4+SP763_y4+SP209_y4+SP858_y4
SP_y5=SP215_y5+SP259_y5+SP190_y5+SP290_y5+SP329_y5+SP380_y5+SP408_y5+SP501_y5+SP763_y5+SP209_y5+SP858_y5
SP_y6=SP215_y6+SP259_y6+SP190_y6+SP290_y6+SP329_y6+SP380_y6+SP408_y6+SP501_y6+SP763_y6+SP209_y6+SP858_y6
T_y1=T215_y1+T259_y1+T190_y1+T290_y1+T329_y1+T380_y1+T408_y1+T501_y1+T763_y1+T209_y1+T858_y1
T_y2=T215_y2+T259_y2+T190_y2+T290_y2+T329_y2+T380_y2+T408_y2+T501_y2+T763_y2+T209_y2+T858_y2
T_y3=T215_y3+T259_y3+T190_y3+T290_y3+T329_y3+T380_y3+T408_y3+T501_y3+T763_y3+T209_y3+T858_y3
T_y4=T215_y4+T259_y4+T190_y4+T290_y4+T329_y4+T380_y4+T408_y4+T501_y4+T763_y4+T209_y4+T858_y4
T_y5=T215_y5+T259_y5+T190_y5+T290_y5+T329_y5+T380_y5+T408_y5+T501_y5+T763_y5+T209_y5+T858_y5
T_y6=T215_y6+T259_y6+T190_y6+T290_y6+T329_y6+T380_y6+T408_y6+T501_y6+T763_y6+T209_y6+T858_y6
y_SP=[float(SP_y1)/(N*(10**10)), float(SP_y2)/(N*(10**10)), float(SP_y3)/(N*(10**10)), float(SP_y4)/(N*(10**10)), float(SP_y5)/(N*(10**10)), float(SP_y6)/(N*(10**10))]
y_T=[float(T_y1)/(N*(10**10)), float(T_y2)/(N*(10**10)), float(T_y3)/(N*(10**10)), float(T_y4)/(N*(10**10)), float(T_y5)/(N*(10**10)), float(T_y6)/(N*(10**10))]
error_SP1=float(np.std([SP215_y1,SP259_y1,SP190_y1,SP290_y1,SP329_y1,SP380_y1,SP408_y1,SP501_y1,SP763_y1,SP209_y1,SP858_y1]))/(N*(10**10))
error_SP2=float(np.std([SP215_y2,SP259_y2,SP190_y2,SP290_y2,SP329_y2,SP380_y2,SP408_y2,SP501_y2,SP763_y2,SP209_y2,SP858_y2]))/(N*(10**10))
error_SP3=float(np.std([SP215_y3,SP259_y3,SP190_y3,SP290_y3,SP329_y3,SP380_y3,SP408_y3,SP501_y3,SP763_y3,SP209_y3,SP858_y3]))/(N*(10**10))
error_SP4=float(np.std([SP215_y4,SP259_y4,SP190_y4,SP290_y4,SP329_y4,SP380_y4,SP408_y4,SP501_y4,SP763_y4,SP209_y4,SP858_y4]))/(N*(10**10))
error_SP5=float(np.std([SP215_y5,SP259_y5,SP190_y5,SP290_y5,SP329_y5,SP380_y5,SP408_y5,SP501_y5,SP763_y5,SP209_y5,SP858_y5]))/(N*(10**10))
error_SP6=float(np.std([SP215_y6,SP259_y6,SP190_y6,SP290_y6,SP329_y6,SP380_y6,SP408_y6,SP501_y6,SP763_y6,SP209_y6,SP858_y6]))/(N*(10**10))
error_SP=[error_SP1, error_SP2, error_SP3, error_SP4, error_SP5, error_SP6]
error_T1=float(np.std([T215_y1,T259_y1,T190_y1,T290_y1,T329_y1,T380_y1,T408_y1,T501_y1,T763_y1,T209_y1,T858_y1]))/(N*(10**10))
error_T2=float(np.std([T215_y2,T259_y2,T190_y2,T290_y2,T329_y2,T380_y2,T408_y2,T501_y2,T763_y2,T209_y2,T858_y2]))/(N*(10**10))
error_T3=float(np.std([T215_y3,T259_y3,T190_y3,T290_y3,T329_y3,T380_y3,T408_y3,T501_y3,T763_y3,T209_y3,T858_y3]))/(N*(10**10))
error_T4=float(np.std([T215_y4,T259_y4,T190_y4,T290_y4,T329_y4,T380_y4,T408_y4,T501_y4,T763_y4,T209_y4,T858_y4]))/(N*(10**10))
error_T5=float(np.std([T215_y5,T259_y5,T190_y5,T290_y5,T329_y5,T380_y5,T408_y5,T501_y5,T763_y5,T209_y5,T858_y5]))/(N*(10**10))
error_T6=float(np.std([T215_y6,T259_y6,T190_y6,T290_y6,T329_y6,T380_y6,T408_y6,T501_y6,T763_y6,T209_y6,T858_y6]))/(N*(10**10))
error_T=[error_T1, error_T2, error_T3, error_T4, error_T5, error_T6]

rc('axes', linewidth=2)
rcParams['xtick.major.size']=8
rcParams['xtick.major.width']=2
rcParams['xtick.minor.size']=4
rcParams['xtick.minor.width']=2
rcParams['ytick.major.size']=8
rcParams['ytick.major.width']=2
rcParams['ytick.minor.size']=4
rcParams['ytick.minor.width']=2
plt.ylim(0,4)
plt.yticks([0,1,2,3,4])
plt.minorticks_on()
plt.errorbar(x, y_SP, error_SP, color='r', linewidth=2, label='Snow Plow')
plt.errorbar(x, y_T, error_T, color='b', linewidth=2, label='Thermal')
plt.tick_params(labelsize=16)
plt.xlabel(r'$R_{search}(kpc)$', fontsize=18)
plt.ylabel(r'$M_{sat}/N_{host}(\times 10^{10}M_{\odot})$', fontsize=18)
plt.legend(loc=4)
plt.savefig('/Users/aquirk/savedplots/stacked_stellar_mass.ps')
