
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
x=['Anger','Depression','Fatigue','Vigour','Tension','Confusion']
y1=[53.090681,67.76034553,7.197155714,3.641539031,8.722815008,24.58746401]
male = [((element/165) * 100) for element in y1]
y2=[36.07190585,46.60872397,5.965768923,0.691085978,6.273306259,21.38920875]
female = [((element/117) * 100) for element in y2]
X_axis = np.arange(len(x))
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
plt.rcParams.update({'font.family':'Times New Roman'})
plt.rcParams.update({'font.size': 12})
plt.bar(X_axis - 0.2, male, 0.4, label = 'Male',color='blue')
plt.bar(X_axis + 0.2, female, 0.4, label = 'Female',color='pink')
plt.xticks(X_axis, x)
plt.legend()
#plt.savefig('f2.eps',format='eps',dpi=1200,facecolor='w',bbox_inches='tight')
plt.show()