import matplotlib.pyplot as plt
import matplotlib as mpl
#import numpy as np
x=['Surprise','Anger','Sadness','Fear','Happiness']
y=[55.49,17.73,61.16,81.39,25.1]
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
plt.rcParams.update({'font.family':'Times'})
plt.rcParams.update({'font.size': 14})
barlist=plt.bar(x, y)
barlist[0].set_color('yellow')
barlist[1].set_color('r')
barlist[2].set_color('b')
barlist[3].set_color('orange')
barlist[4].set_color('g')
#plt.savefig('f2.eps',format='eps',dpi=1200,facecolor='w',bbox_inches='tight')
plt.show()