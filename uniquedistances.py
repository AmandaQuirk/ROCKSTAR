import numpy as np

halo='m0858'
model='S' #T, S, or N
out='94'

mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/{}{}_S/out_{}_4x.list'.format(model,halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass) #mass of central halo 
n=np.argmax(mass) #index of central halo 
Xc=x[n] #units of Mpc/h
Yc=y[n]
Zc=z[n]
Rc=rvir[n]*.72*10**-3 #Mpc

#print(Mc)

distance=[] #will contain the distances of all halos to central halo with the lines of cade below
for i in range(len(mass)):
        d=(np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2)) #in Mpc
        distance.append(d)
	print(mass[i],distance[i])

distance=sorted(distance)
unique_distances=[] #this eliminates 'double counted' halos (within .05 kpc of each other) 
for i in range(len(distance)):
        if distance[i]!=distance[-1]:
                if distance[i+1]-distance[i]>.0005:
                        unique_distances.append(distance[i])
        if distance[i]==distance[-1]:
                if distance[-1]-distance[-2]>.0005:
                        unique_distances.append(distance[i])

print(unique_distances)


