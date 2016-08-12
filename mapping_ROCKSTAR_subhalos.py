import pygad
import numpy as np
import matplotlib.pyplot as plt

halo='m0190'

#snowplow
location='/Volumes/simdisk3/choi/Fiducial_MrAGN/' 

model='Snow Plow' #Thermal, Snow Plow, no AGN
modelID='S' #T, S, N
out=94 #snap number-- corresponds to redshift
redshift=0
extrafactor=1 #1 for z=0,1 and 1/(1+redshift) for z=2
#YOU HAVE TO CHANGE THE NUMBER MANUALLY FOR PYGAD READ IN FILES

s= pygad.Snap('{}{}/snap_{}_sf_x_2x_094'.format(location,halo,halo), load_double_prec=True)
s.to_physical_units()

#below centers code on GADGET center so that pygad can read the units of the snapshot 
with open('{}{}/info_094.txt'.format(location,halo)) as inFile:
        for line in inFile:
                if line.startswith('center'):
                        for char in line:
                                if char in "[]":
                                        line=line.replace(char,'')
                        center=line.split(' ')
                        center=filter(None, center)
			center=np.array([float(center[1]), float(center[2]), float(center[3])])
                        center=center*s.time/0.72 #this line converts to physical units to match the units of the rest of the data- FALSE. This is the only way to seem to get pygad to read the units from the info file, but it makes the center too big by a factor of 1/(.72^2). I correct for this below

pygad.Translation(-center).apply(s)

#stars
mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/{}{}_S/out_{}.list'.format(modelID,halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass) #mass of central halo found by ROCKSTAR
n=np.argmax(mass) #index of central halo found by ROCKSTAR
Xc=x[n] #units of Mpc/h
Yc=y[n]
Zc=z[n]
Rc=rvir[n]

constant=(.72*10**3)/(1+redshift) #for converting to ckpc from Mpc/h_o
Rockcenter=np.array([float(Xc*constant), float(Yc*constant), float(Zc*constant)]) #this gives ROCKSTAR's center, from which the subhalos will be based and plotted, ckpc
deltax=(extrafactor)*(Rockcenter[0]-(center[0]*(.72**2))) #difference between GADGET and ROCKSTAR center
deltay=(extrafactor)*(Rockcenter[1]-(center[1]*(.72**2))) #ckpc
#print(Rockcenter)
#print(center*(.72**2))
#print(deltax)
#print(deltay)

#fig, ((ax1,ax2), (ax3,ax4))=plt.subplots(nrows=2,ncols=2)
fig=plt.figure(figsize=(8,8))
ax = [fig.add_subplot(2,2,i+1) for i in range(4)]

#arrays for circle coordinates
newcenterx=[]
newcentery=[]
radius=[]
centralx=[]
centraly=[]

#below all units should be ckpc/h**2
for i in range(len(mass)): #below narrows down which ROCKSTAR halos are plotted
        r=((np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2))*10**3)
        if Mc==mass[i]:
		centralx.append((((Xc*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2)))
		centraly.append((((Yc*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
	if Mc != mass[i] and (Mc/400)<mass[i] and 800>r: #(Mc/400)<mass[i] and  
                newcenterx.append((((x[i]*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2))) #here I correct for the center units discrepancy above- the additive constants are for the difference between the GADGET center and the ROCKSTAR center
                newcentery.append((((y[i]*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
		radius.append((rvir[i])*.1)

#highlight the center galaxy
centercircle1=plt.Circle((centralx[0],centraly[0]), Rc*.1, color='red', fill=False)
ax[0].add_artist(centercircle1)				

for i in range(len(newcenterx)):
	circle1=plt.Circle((newcenterx[i],newcentery[i]), radius[i], color='white', fill=False)
	ax[0].add_artist(circle1) 

pygad.plotting.image(s.stars, qty='mass', cmap='BlackBlue', showcbar=False, cbartitle='Stars', fontcolor='w', fontsize=10, extent='300 kpc', ax=ax[0])

#DARK MATTER
mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/{}{}_D/out_{}.list'.format(modelID,halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass) #mass of central halo found by ROCKSTAR
n=np.argmax(mass) #index of central halo found by ROCKSTAR
Xc=x[n] #units of Mpc/h
Yc=y[n]
Zc=z[n]
Rc=rvir[n]

constant=(.72*10**3)/(1+redshift) #for converting to ckpc from Mpc/h_o
Rockcenter=np.array([float(Xc*constant), float(Yc*constant), float(Zc*constant)]) #this gives ROCKSTAR's center, from which the subhalos will be based and plotted, ckpc
deltax=(extrafactor)*(Rockcenter[0]-(center[0]*(.72**2))) #difference between GADGET and ROCKSTAR center
deltay=(extrafactor)*(Rockcenter[1]-(center[1]*(.72**2))) #ckpc
#print(Rockcenter)
#print(center*(.72**2))
#print(deltax)
#print(deltay)

#arrays for circle coordinates
newcenterx=[]
newcentery=[]
radius=[]
centralx=[]
centraly=[]

#below all units should be ckpc/h**2
for i in range(len(mass)): #below narrows down which ROCKSTAR halos are plotted
        r=((np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2))*10**3)
        if Mc==mass[i]:
                centralx.append((((Xc*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2)))
                centraly.append((((Yc*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
        if Mc != mass[i] and (Mc/400)<mass[i] and 800>r: #(Mc/400)<mass[i] and  
                newcenterx.append((((x[i]*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2))) #here I correct for the center units discrepancy above- the additive constants are for the difference between the GADGET center and the ROCKSTAR center
                newcentery.append((((y[i]*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
                radius.append((rvir[i])*.1)

#highlight the center galaxy
centercircle1=plt.Circle((centralx[0],centraly[0]), Rc*.1, color='red', fill=False)
ax[1].add_artist(centercircle1)

for i in range(len(newcenterx)):
        circle1=plt.Circle((newcenterx[i],newcentery[i]), radius[i], color='white', fill=False)
        ax[1].add_artist(circle1)

pygad.plotting.image(s.dm, qty='mass', cmap='BlackBlue', showcbar=False, cbartitle='DM', fontcolor='w', fontsize=10, extent='300 kpc', ax=ax[1])

#thermal
location='/Volumes/Happy/Choi15/MrAGN/'

model='Thermal' #Thermal, Snow Plow, no AGN
modelID='T' #T, S, N
out=94 #snap number-- corresponds to redshift
redshift=0
extrafactor=1 #1 for z=0,1 and 1/(1+redshift) for z=2
#YOU HAVE TO CHANGE THE NUMBER MANUALLY FOR PYGAD READ IN FILES

s= pygad.Snap('{}{}/snap_{}_sf_x_2x_094'.format(location,halo,halo), load_double_prec=True)
s.to_physical_units()

#below centers code on GADGET center so that pygad can read the units of the snapshot 
with open('{}{}/info_094.txt'.format(location,halo)) as inFile:
        for line in inFile:
                if line.startswith('center'):
                        for char in line:
                                if char in "[]":
                                        line=line.replace(char,'')
                        center=line.split(' ')
                        center=filter(None, center)
                        center=np.array([float(center[1]), float(center[2]), float(center[3])])
                        center=center*s.time/0.72 #this line converts to physical units to match the units of the rest of the data- FALSE. This is the only way to seem to get pygad to read the units from the info file, but it makes the center too big by a factor of 1/(.72^2). I correct for this below

pygad.Translation(-center).apply(s)

#stars
mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/{}{}_S/out_{}.list'.format(modelID,halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass) #mass of central halo found by ROCKSTAR
n=np.argmax(mass) #index of central halo found by ROCKSTAR
Xc=x[n] #units of Mpc/h
Yc=y[n]
Zc=z[n]
Rc=rvir[n]

constant=(.72*10**3)/(1+redshift) #for converting to ckpc from Mpc/h_o
Rockcenter=np.array([float(Xc*constant), float(Yc*constant), float(Zc*constant)]) #this gives ROCKSTAR's center, from which the subhalos will be based and plotted, ckpc
deltax=(extrafactor)*(Rockcenter[0]-(center[0]*(.72**2))) #difference between GADGET and ROCKSTAR center
deltay=(extrafactor)*(Rockcenter[1]-(center[1]*(.72**2))) #ckpc
#print(Rockcenter)
#print(center*(.72**2))
#print(deltax)
#print(deltay)

#arrays for circle coordinates
newcenterx=[]
newcentery=[]
radius=[]
centralx=[]
centraly=[]

#below all units should be ckpc/h**2
for i in range(len(mass)): #below narrows down which ROCKSTAR halos are plotted
        r=((np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2))*10**3)
        if Mc==mass[i]:
                centralx.append((((Xc*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2)))
                centraly.append((((Yc*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
        if Mc != mass[i] and (Mc/400)<mass[i] and 800>r: #(Mc/400)<mass[i] and  
                newcenterx.append((((x[i]*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2))) #here I correct for the center units discrepancy above- the additive constants are for the difference between the GADGET center and the ROCKSTAR center
                newcentery.append((((y[i]*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
                radius.append((rvir[i])*.1)

#highlight the center galaxy
centercircle1=plt.Circle((centralx[0],centraly[0]), Rc*.1, color='red', fill=False)
ax[2].add_artist(centercircle1)

for i in range(len(newcenterx)):
        circle1=plt.Circle((newcenterx[i],newcentery[i]), radius[i], color='white', fill=False)
        ax[2].add_artist(circle1)

pygad.plotting.image(s.stars, qty='mass', cmap='BlackBlue', showcbar=False, cbartitle='Stars', fontcolor='w', fontsize=10, extent='300 kpc', ax=ax[2])

#DARK MATTER
mass,rvir, x,y,z=np.loadtxt('/Users/aquirk/Rockstar/{}{}_D/out_{}.list'.format(modelID,halo,out), usecols=(2,5,8,9,10,), unpack=True)
Mc=np.amax(mass) #mass of central halo found by ROCKSTAR
n=np.argmax(mass) #index of central halo found by ROCKSTAR
Xc=x[n] #units of Mpc/h
Yc=y[n]
Zc=z[n]
Rc=rvir[n]

constant=(.72*10**3)/(1+redshift) #for converting to ckpc from Mpc/h_o
Rockcenter=np.array([float(Xc*constant), float(Yc*constant), float(Zc*constant)]) #this gives ROCKSTAR's center, from which the subhalos will be based and plotted, ckpc
deltax=(extrafactor)*(Rockcenter[0]-(center[0]*(.72**2))) #difference between GADGET and ROCKSTAR center
deltay=(extrafactor)*(Rockcenter[1]-(center[1]*(.72**2))) #ckpc
#print(Rockcenter)
#print(center*(.72**2))
#print(deltax)
#print(deltay)

#arrays for circle coordinates
newcenterx=[]
newcentery=[]
radius=[]
centralx=[]
centraly=[]

#below all units should be ckpc/h**2
for i in range(len(mass)): #below narrows down which ROCKSTAR halos are plotted
        r=((np.sqrt(((Xc*.72)-(x[i]*.72))**2+((Yc*.72)-(y[i]*.72))**2+((Zc*.72)-(z[i]*.72))**2))*10**3)
        if Mc==mass[i]:
                centralx.append((((Xc*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2)))
                centraly.append((((Yc*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
        if Mc != mass[i] and (Mc/400)<mass[i] and 800>r: #(Mc/400)<mass[i] and  
                newcenterx.append((((x[i]*constant)-Rockcenter[0])/(.72**2))+(deltax/(.72**2))) #here I correct for the center units discrepancy above- the additive constants are for the difference between the GADGET center and the ROCKSTAR center
                newcentery.append((((y[i]*constant)-Rockcenter[1])/(.72**2))+(deltay/(.72**2)))
                radius.append((rvir[i])*.1)

#highlight the center galaxy
centercircle1=plt.Circle((centralx[0],centraly[0]), Rc*.1, color='red', fill=False)
ax[3].add_artist(centercircle1)

for i in range(len(newcenterx)):
        circle1=plt.Circle((newcenterx[i],newcentery[i]), radius[i], color='white', fill=False)
        ax[3].add_artist(circle1)

pygad.plotting.image(s.dm, qty='mass', cmap='BlackBlue', showcbar=False, cbartitle='DM', fontcolor='w', fontsize=10, extent='300 kpc', ax=ax[3])

#fig.suptitle('{} {}  z={} '.format(halo, model, redshift), y=0.68)
for a in ax:
    a.set_xticklabels([])
    a.set_yticklabels([])
    a.set_aspect('equal')
plt.subplots_adjust(wspace=0, hspace=0) #removes space between plots
plt.savefig('/Users/aquirk/savedplots/{}_{}_{}.ps'.format(modelID, halo, redshift), bbox_inches='tight')
print('/Users/aquirk/savedplots/{}_{}_{}.ps'.format(modelID, halo, redshift))
