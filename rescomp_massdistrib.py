import numpy as np
import matplotlib.pyplot as plt

halo='m0858'
z=0
out=94

#Snow Plow- high resolution
mass,rvir=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/out_{}_4x.list'.format(halo,out), usecols=(2,5,), unpack=True)
Mch=np.amax(mass) #mass of central halo

mass,distance=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/nocentral_mass{}_4x.txt'.format(halo,z), unpack=True)

closemassesS_4x=[]
for i in range(len(mass)):
        if (.3)>distance[i]:
                closemassesS_4x.append(np.log10(0.72*mass[i]))

#Snow Plow- low resolution
mass,rvir=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/out_{}.list'.format(halo,out), usecols=(2,5,), unpack=True)
Mcl=np.amax(mass) #mass of central halo 

#mass,distance=np.loadtxt('/Users/aquirk/Rockstar/S{}_S/nocentral_mass{}.txt'.format(halo,z), unpack=True)

#for no satellites
mass=[]
distance=[]
closemassesS=[]
#for i in range(len(mass)):
if (.3)>distance:
	closemassesS.append(np.log10(0.72*mass))

x=np.log10(0.01*0.72*Mch)
#plotting
ax, fig=plt.subplots()
axes = plt.gca()
ax.set_rasterized(True)
axes.annotate(r'$R < 300 kpc$', xy=(10.25, 3), fontsize=16)
axes.annotate(r'$M_{host} \sim 1.9 \times 10^{11} M_{\odot}$', xy=(10.25, 2.65), fontsize=16)
plt.plot((x,x), (0,4), color='k', linestyle='--',linewidth=2)
axes.set_yticks([0,1,2,3,4])
bins=np.linspace(8,12,16)
plt.hist(closemassesS_4x, bins, hatch='\\', fill=False, label='high resolution')
plt.hist(closemassesS, bins, hatch='/', fill=False, label='low resolution')
plt.xlabel(r'$log(M_{sat})$', fontsize=18)
plt.ylabel(r'$N_{sat}$', fontsize=20)
for axis in ['top','bottom','left','right']:
        axes.spines[axis].set_linewidth(2)
axes.tick_params(axis='x',which='minor',bottom='off')
plt.tick_params(which='both', width=2)
plt.tick_params(which='major', length=7)
plt.tick_params(which='minor', length=4)
plt.tick_params(labelsize=16)
plt.legend()
plt.savefig('/Users/aquirk/savedplots/comp_massdistrib{}_{}.ps'.format(halo,z))
print('comp_massdistrib{}_{}.ps'.format(halo,z))
