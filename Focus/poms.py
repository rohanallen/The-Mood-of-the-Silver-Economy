import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
x=['Anger','Depression','Fatigue','Vigour','Tension','Confusion']
y=[89.16258606,114.3690705,13.16292442,4.332625085,14.9961212,45.97667274]
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
plt.rcParams.update({'font.family':'Times'})
plt.rcParams.update({'font.size': 12})
barlist=plt.bar(x, y)
barlist[0].set_color('r')
barlist[1].set_color('black')
barlist[2].set_color('b')
barlist[3].set_color('orange')
barlist[4].set_color('g')
barlist[5].set_color('pink')
#plt.savefig('f2.eps',format='eps',dpi=1200,facecolor='w',bbox_inches='tight')
plt.show()