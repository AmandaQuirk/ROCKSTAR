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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
	if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies and the central
		close_masses.append(mass[i])
for i in range(len(close_masses)):
	if 0.5<close_masses[i]/Mc:
		SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP215_y1=(float(len(SP_interval1)))#/len(close_masses))
SP215_y2=(float(len(SP_interval2)))#/len(close_masses))
SP215_y3=(float(len(SP_interval3)))#/len(close_masses))
SP215_y4=(float(len(SP_interval4)))#/len(close_masses))
SP215_y5=(float(len(SP_interval5)))#/len(close_masses))
SP215_y6=(float(len(SP_interval6)))#/len(close_masses))

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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T215_y1=(float(len(T_interval1)))#/len(close_masses))
T215_y2=(float(len(T_interval2)))#/len(close_masses))
T215_y3=(float(len(T_interval3)))#/len(close_masses))
T215_y4=(float(len(T_interval4)))#/len(close_masses))
T215_y5=(float(len(T_interval5)))#/len(close_masses))
T215_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP259_y1=(float(len(SP_interval1)))#/len(close_masses))
SP259_y2=(float(len(SP_interval2)))#/len(close_masses))
SP259_y3=(float(len(SP_interval3)))#/len(close_masses))
SP259_y4=(float(len(SP_interval4)))#/len(close_masses))
SP259_y5=(float(len(SP_interval5)))#/len(close_masses))
SP259_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T259_y1=(float(len(T_interval1)))#/len(close_masses))
T259_y2=(float(len(T_interval2)))#/len(close_masses))
T259_y3=(float(len(T_interval3)))#/len(close_masses))
T259_y4=(float(len(T_interval4)))#/len(close_masses))
T259_y5=(float(len(T_interval5)))#/len(close_masses))
T259_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP190_y1=(float(len(SP_interval1)))#/len(close_masses))
SP190_y2=(float(len(SP_interval2)))#/len(close_masses))
SP190_y3=(float(len(SP_interval3)))#/len(close_masses))
SP190_y4=(float(len(SP_interval4)))#/len(close_masses))
SP190_y5=(float(len(SP_interval5)))#/len(close_masses))
SP190_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T190_y1=(float(len(T_interval1)))#/len(close_masses))
T190_y2=(float(len(T_interval2)))#/len(close_masses))
T190_y3=(float(len(T_interval3)))#/len(close_masses))
T190_y4=(float(len(T_interval4)))#/len(close_masses))
T190_y5=(float(len(T_interval5)))#/len(close_masses))
T190_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP329_y1=(float(len(SP_interval1)))#/len(close_masses))
SP329_y2=(float(len(SP_interval2)))#/len(close_masses))
SP329_y3=(float(len(SP_interval3)))#/len(close_masses))
SP329_y4=(float(len(SP_interval4)))#/len(close_masses))
SP329_y5=(float(len(SP_interval5)))#/len(close_masses))
SP329_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T329_y1=(float(len(T_interval1)))#/len(close_masses))
T329_y2=(float(len(T_interval2)))#/len(close_masses))
T329_y3=(float(len(T_interval3)))#/len(close_masses))
T329_y4=(float(len(T_interval4)))#/len(close_masses))
T329_y5=(float(len(T_interval5)))#/len(close_masses))
T329_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP380_y1=(float(len(SP_interval1)))#/len(close_masses))
SP380_y2=(float(len(SP_interval2)))#/len(close_masses))
SP380_y3=(float(len(SP_interval3)))#/len(close_masses))
SP380_y4=(float(len(SP_interval4)))#/len(close_masses))
SP380_y5=(float(len(SP_interval5)))#/len(close_masses))
SP380_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T380_y1=(float(len(T_interval1)))#/len(close_masses))
T380_y2=(float(len(T_interval2)))#/len(close_masses))
T380_y3=(float(len(T_interval3)))#/len(close_masses))
T380_y4=(float(len(T_interval4)))#/len(close_masses))
T380_y5=(float(len(T_interval5)))#/len(close_masses))
T380_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP408_y1=(float(len(SP_interval1)))#/len(close_masses))
SP408_y2=(float(len(SP_interval2)))#/len(close_masses))
SP408_y3=(float(len(SP_interval3)))#/len(close_masses))
SP408_y4=(float(len(SP_interval4)))#/len(close_masses))
SP408_y5=(float(len(SP_interval5)))#/len(close_masses))
SP408_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T408_y1=(float(len(T_interval1)))#/len(close_masses))
T408_y2=(float(len(T_interval2)))#/len(close_masses))
T408_y3=(float(len(T_interval3)))#/len(close_masses))
T408_y4=(float(len(T_interval4)))#/len(close_masses))
T408_y5=(float(len(T_interval5)))#/len(close_masses))
T408_y6=(float(len(T_interval6)))#/len(close_masses))

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
#snow plow m0501
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0501_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
if 300>=(distance*(10**3)) and mass!=Mc: #elimnates far away galaxies
	close_masses.append(mass)
if 0.5<close_masses/Mc:# and 1>=close_masses[i]/Mc:
	SP_interval6.append(close_masses)
if 0.2<close_masses/Mc:# and 0.5>=close_masses[i]/Mc:
	SP_interval5.append(close_masses)
if 0.1<close_masses/Mc:# and 0.2>=close_masses[i]/Mc:
	SP_interval4.append(close_masses)
if 0.05<close_masses/Mc:# and 0.1>=close_masses[i]/Mc:
	SP_interval3.append(close_masses)
if 0.02<close_masses/Mc:# and 0.05>=close_masses[i]/Mc:
	SP_interval2.append(close_masses)
if 0.01<close_masses/Mc:# and 0.02>=close_masses[i]/Mc:
	SP_interval1.append(close_masses)
SP501_y1=(float(len(SP_interval1)))#/len(close_masses))
SP501_y2=(float(len(SP_interval2)))#/len(close_masses))
SP501_y3=(float(len(SP_interval3)))#/len(close_masses))
SP501_y4=(float(len(SP_interval4)))#/len(close_masses))
SP501_y5=(float(len(SP_interval5)))#/len(close_masses))
SP501_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T501_y1=(float(len(T_interval1)))#/len(close_masses))
T501_y2=(float(len(T_interval2)))#/len(close_masses))
T501_y3=(float(len(T_interval3)))#/len(close_masses))
T501_y4=(float(len(T_interval4)))#/len(close_masses))
T501_y5=(float(len(T_interval5)))#/len(close_masses))
T501_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP763_y1=(float(len(SP_interval1)))#/len(close_masses))
SP763_y2=(float(len(SP_interval2)))#/len(close_masses))
SP763_y3=(float(len(SP_interval3)))#/len(close_masses))
SP763_y4=(float(len(SP_interval4)))#/len(close_masses))
SP763_y5=(float(len(SP_interval5)))#/len(close_masses))
SP763_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T763_y1=(float(len(T_interval1)))#/len(close_masses))
T763_y2=(float(len(T_interval2)))#/len(close_masses))
T763_y3=(float(len(T_interval3)))#/len(close_masses))
T763_y4=(float(len(T_interval4)))#/len(close_masses))
T763_y5=(float(len(T_interval5)))#/len(close_masses))
T763_y6=(float(len(T_interval6)))#/len(close_masses))

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
#snow plow m0858
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0858_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
if 300>=(distance*(10**3)) and mass!=Mc: #elimnates far away galaxies
	close_masses.append(mass)
if 0.5<close_masses/Mc:# and 1>=close_masses[i]/Mc:
	SP_interval6.append(close_masses)
if 0.2<close_masses/Mc:# and 0.5>=close_masses[i]/Mc:
	SP_interval5.append(close_masses)
if 0.1<close_masses/Mc:# and 0.2>=close_masses[i]/Mc:
	SP_interval4.append(close_masses)
if 0.05<close_masses/Mc:# and 0.1>=close_masses[i]/Mc:
	SP_interval3.append(close_masses)
if 0.02<close_masses/Mc:# and 0.05>=close_masses[i]/Mc:
        SP_interval2.append(close_masses)
if 0.01<close_masses/Mc:# and 0.02>=close_masses[i]/Mc:
	SP_interval1.append(close_masses)
SP858_y1=(float(len(SP_interval1)))#/len(close_masses))
SP858_y2=(float(len(SP_interval2)))#/len(close_masses))
SP858_y3=(float(len(SP_interval3)))#/len(close_masses))
SP858_y4=(float(len(SP_interval4)))#/len(close_masses))
SP858_y5=(float(len(SP_interval5)))#/len(close_masses))
SP858_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T858_y1=(float(len(T_interval1)))#/len(close_masses))
T858_y2=(float(len(T_interval2)))#/len(close_masses))
T858_y3=(float(len(T_interval3)))#/len(close_masses))
T858_y4=(float(len(T_interval4)))#/len(close_masses))
T858_y5=(float(len(T_interval5)))#/len(close_masses))
T858_y6=(float(len(T_interval6)))#/len(close_masses))

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
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP209_y1=(float(len(SP_interval1)))#/len(close_masses))
SP209_y2=(float(len(SP_interval2)))#/len(close_masses))
SP209_y3=(float(len(SP_interval3)))#/len(close_masses))
SP209_y4=(float(len(SP_interval4)))#/len(close_masses))
SP209_y5=(float(len(SP_interval5)))#/len(close_masses))
SP209_y6=(float(len(SP_interval6)))#/len(close_masses))
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T209_y1=(float(len(T_interval1)))#/len(close_masses))
T209_y2=(float(len(T_interval2)))#/len(close_masses))
T209_y3=(float(len(T_interval3)))#/len(close_masses))
T209_y4=(float(len(T_interval4)))#/len(close_masses))
T209_y5=(float(len(T_interval5)))#/len(close_masses))
T209_y6=(float(len(T_interval6)))#/len(close_masses))

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
mass,distance=np.loadtxt('/Users/aquirk/Rockstar/Sm0290_S/mass0.txt', unpack=True) #uses unique distances file
Mc=np.amax(mass) #mass of central halo 
close_masses=[] #will contain masses of galaxies that passed the below radius cut
for i in range(len(mass)):
        if 300>=(distance[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(mass[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                SP_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                SP_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                SP_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                SP_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                SP_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                SP_interval1.append(close_masses[i])
SP290_y1=(float(len(SP_interval1)))#/len(close_masses))
SP290_y2=(float(len(SP_interval2)))#/len(close_masses))
SP290_y3=(float(len(SP_interval3)))#/len(close_masses))
SP290_y4=(float(len(SP_interval4)))#/len(close_masses))
SP290_y5=(float(len(SP_interval5)))#/len(close_masses))
SP290_y6=(float(len(SP_interval6)))#/len(close_masses))
#thermal m0209
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
for i in range(len(unique_distances)):
        if 300>=(unique_distances[i]*(10**3)) and mass[i]!=Mc: #elimnates far away galaxies
                close_masses.append(unique_masses[i])
for i in range(len(close_masses)):
        if 0.5<close_masses[i]/Mc:# and 1>=close_masses[i]/Mc:
                T_interval6.append(close_masses[i])
        if 0.2<close_masses[i]/Mc:# and 0.5>=close_masses[i]/Mc:
                T_interval5.append(close_masses[i])
        if 0.1<close_masses[i]/Mc:# and 0.2>=close_masses[i]/Mc:
                T_interval4.append(close_masses[i])
        if 0.05<close_masses[i]/Mc:# and 0.1>=close_masses[i]/Mc:
                T_interval3.append(close_masses[i])
        if 0.02<close_masses[i]/Mc:# and 0.05>=close_masses[i]/Mc:
                T_interval2.append(close_masses[i])
        if 0.01<close_masses[i]/Mc:# and 0.02>=close_masses[i]/Mc:
                T_interval1.append(close_masses[i])
T290_y1=(float(len(T_interval1)))#/len(close_masses))
T290_y2=(float(len(T_interval2)))#/len(close_masses))
T290_y3=(float(len(T_interval3)))#/len(close_masses))
T290_y4=(float(len(T_interval4)))#/len(close_masses))
T290_y5=(float(len(T_interval5)))#/len(close_masses))
T290_y6=(float(len(T_interval6)))#/len(close_masses))

#plotting
N=11
x=[0.015, 0.04, 0.085, 0.15, 0.4, 0.85]
y_SP1=SP215_y1+SP259_y1+SP190_y1+SP290_y1+SP329_y1+SP380_y1+SP408_y1+SP501_y1+SP763_y1+SP209_y1+SP858_y1
y_SP2=SP215_y2+SP259_y2+SP190_y2+SP290_y2+SP329_y2+SP380_y2+SP408_y2+SP501_y2+SP763_y2+SP209_y2+SP858_y2
y_SP3=SP215_y3+SP259_y3+SP190_y3+SP290_y3+SP329_y3+SP380_y3+SP408_y3+SP501_y3+SP763_y3+SP209_y3+SP858_y3
y_SP4=SP215_y4+SP259_y4+SP190_y4+SP290_y4+SP329_y4+SP380_y4+SP408_y4+SP501_y4+SP763_y4+SP209_y4+SP858_y4
y_SP5=SP215_y5+SP259_y5+SP190_y5+SP290_y5+SP329_y5+SP380_y5+SP408_y5+SP501_y5+SP763_y5+SP209_y5+SP858_y5
y_SP6=SP215_y6+SP259_y6+SP190_y6+SP290_y6+SP329_y6+SP380_y6+SP408_y6+SP501_y6+SP763_y6+SP209_y6+SP858_y6
y_SP=[float(y_SP1)/N, float(y_SP2)/N, float(y_SP3)/N, float(y_SP4)/N, float(y_SP5)/N, float(y_SP6)/N]
y_T1=T215_y1+T259_y1+T190_y1+T290_y1+T329_y1+T380_y1+T408_y1+T501_y1+T763_y1+T209_y1+T858_y1
y_T2=T215_y2+T259_y2+T190_y2+T290_y2+T329_y2+T380_y2+T408_y2+T501_y2+T763_y2+T209_y2+T858_y2
y_T3=T215_y3+T259_y3+T190_y3+T290_y3+T329_y3+T380_y3+T408_y3+T501_y3+T763_y3+T209_y3+T858_y3
y_T4=T215_y4+T259_y4+T190_y4+T290_y4+T329_y4+T380_y4+T408_y4+T501_y4+T763_y4+T209_y4+T858_y4
y_T5=T215_y5+T259_y5+T190_y5+T290_y5+T329_y5+T380_y5+T408_y5+T501_y5+T763_y5+T209_y5+T858_y5
y_T6=T215_y6+T259_y6+T190_y6+T290_y6+T329_y6+T380_y6+T408_y6+T501_y6+T763_y6+T209_y6+T858_y6
y_T=[float(y_T1)/N, float(y_T2)/N, float(y_T3)/N, float(y_T4)/N, float(y_T5)/N, float(y_T6)/N]
error_SP1=float(np.std([SP215_y1,SP259_y1,SP190_y1,SP290_y1,SP329_y1,SP380_y1,SP408_y1,SP501_y1,SP763_y1,SP209_y1,SP858_y1]))/N
error_SP2=float(np.std([SP215_y2,SP259_y2,SP190_y2,SP290_y2,SP329_y2,SP380_y2,SP408_y2,SP501_y2,SP763_y2,SP209_y2,SP858_y2]))/N
error_SP3=float(np.std([SP215_y3,SP259_y3,SP190_y3,SP290_y3,SP329_y3,SP380_y3,SP408_y3,SP501_y3,SP763_y3,SP209_y3,SP858_y3]))/N
error_SP4=float(np.std([SP215_y4,SP259_y4,SP190_y4,SP290_y4,SP329_y4,SP380_y4,SP408_y4,SP501_y4,SP763_y4,SP209_y4,SP858_y4]))/N
error_SP5=float(np.std([SP215_y5,SP259_y5,SP190_y5,SP290_y5,SP329_y5,SP380_y5,SP408_y5,SP501_y5,SP763_y5,SP209_y5,SP858_y5]))/N
error_SP6=float(np.std([SP215_y6,SP259_y6,SP190_y6,SP290_y6,SP329_y6,SP380_y6,SP408_y6,SP501_y6,SP763_y6,SP209_y6,SP858_y6]))/N
error_SP=[error_SP1, error_SP2, error_SP3, error_SP4, error_SP5, error_SP6]
error_T1=float(np.std([T215_y1,T259_y1,T190_y1,T290_y1,T329_y1,T380_y1,T408_y1,T501_y1,T763_y1,T209_y1,T858_y1]))/N
error_T2=float(np.std([T215_y2,T259_y2,T190_y2,T290_y2,T329_y2,T380_y2,T408_y2,T501_y2,T763_y2,T209_y2,T858_y2]))/N
error_T3=float(np.std([T215_y3,T259_y3,T190_y3,T290_y3,T329_y3,T380_y3,T408_y3,T501_y3,T763_y3,T209_y3,T858_y3]))/N
error_T4=float(np.std([T215_y4,T259_y4,T190_y4,T290_y4,T329_y4,T380_y4,T408_y4,T501_y4,T763_y4,T209_y4,T858_y4]))/N
error_T5=float(np.std([T215_y5,T259_y5,T190_y5,T290_y5,T329_y5,T380_y5,T408_y5,T501_y5,T763_y5,T209_y5,T858_y5]))/N
error_T6=float(np.std([T215_y6,T259_y6,T190_y6,T290_y6,T329_y6,T380_y6,T408_y6,T501_y6,T763_y6,T209_y6,T858_y6]))/N
error_T=[error_T1, error_T2, error_T3, error_T4, error_T5, error_T6]
x_R=[0.85,0.4,0.15,0.085,0.04,0.015]
y_R=[0.29,0.88,1.4,2.17,3.1,3.67]
R_err=[0.03,0.02,0.05,0.05,0.08,0.11]
y_RS=[0.21,0.47,0.63,1.13,1.82,2.32]
RS_err=[0.02,0.05,0.06,0.07,0.08,0.12]
y_Ra=[0.11,0.23,0.38,0.64,1.05,1.26]
Ra_err=[0.01,0.02,0.02,0.03,0.05,0.06]
rc('axes', linewidth=2)
rcParams['xtick.major.size']=8
rcParams['xtick.major.width']=2
rcParams['xtick.minor.size']=4
rcParams['xtick.minor.width']=2
rcParams['ytick.major.size']=8
rcParams['ytick.major.width']=2
rcParams['ytick.minor.size']=4
rcParams['ytick.minor.width']=2
plt.minorticks_on()
plt.errorbar(x_R, y_R, R_err, color='k', linestyle='--', linewidth=2, label='Ruiz et al E galaxies')
plt.errorbar(x_R, y_RS, RS_err, color='k', linestyle='-.', linewidth=2, label='Ruiz et al So galaxies')

plt.errorbar(x_R, y_Ra, Ra_err, color='k', linestyle=':', linewidth=2, label='Ruiz et al Sa galaxies')

plt.errorbar(x, y_SP, error_SP, color='r', linewidth=2, label='Snow Plow')
plt.errorbar(x, y_T, error_T, color='b', linewidth=2, label='Thermal')
plt.tick_params(labelsize=16)
plt.xscale('log')
plt.xlim(0.01,2)
plt.xlabel(r'$M_{sat}/M_{host}$', fontsize=18)
plt.ylabel(r'$N_{sat}(>M_{sat}/M_{host})/N_{host}$', fontsize=18)
plt.legend()
plt.savefig('/Users/aquirk/savedplots/stacked_mass_number.ps')
