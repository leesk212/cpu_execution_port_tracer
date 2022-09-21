import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

import sys
import os

raws = pd.read_csv('sample_all.csv')
#del raws['label']
#print(df.max())

df = raws.transpose()

df_1 = df.iloc[:8,:]
ax = sns.heatmap(df_1,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 0')
plt.show()

df_2 = df.iloc[8:16,:]
ax = sns.heatmap(df_2,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 1')
plt.show()

df_3 = df.iloc[16:24,:]
ax = sns.heatmap(df_3,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 2')
plt.show()

df_4 = df.iloc[24:32,:]
ax = sns.heatmap(df_4,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 3')
plt.show()

df_5 = df.iloc[32:40,:]
ax = sns.heatmap(df_5,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 4')
plt.show()

df_6 = df.iloc[40:48,:]
ax = sns.heatmap(df_6,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 5')
plt.show()

df_7 = df.iloc[48:56,:]
ax = sns.heatmap(df_7,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 6')
plt.show()

df_8 = df.iloc[56:64,:]
ax = sns.heatmap(df_8,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 7')
plt.show()

df_8 = df.iloc[56:64,:]
ax = sns.heatmap(df_8,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 8')
plt.show()

df_8 = df.iloc[56:64,:]
ax = sns.heatmap(df_8,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 9')
plt.show()

df_8 = df.iloc[56:64,:]
ax = sns.heatmap(df_8,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 10')
plt.show()

df_8 = df.iloc[56:64,:]
ax = sns.heatmap(df_8,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax.set_xticks([0,2000,4000,6000,8000,10000]) # tICK이 잘린 순으로 작성된다.
ax.set_xticklabels(['0','2,000','4,000','6,000','8,000','10,000'],rotation=45,fontsize=8)
ax.set_yticklabels(['port 0','port 1','port 2','port 3','port 4','port 5','port 6','port 7'])
ax.set_title('Core 11')
plt.show()


#x_axis_labels = [78000,81000,0,81000,0,81000,0,81000,0,81000,0,81000,0,81000,0,81000]

#ax = sns.heatmap(raws, cbar=False, xticklabels=True ,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
ax = sns.heatmap(df,cbar=False,cmap="YlGnBu", cbar_kws = {'orientation':'horizontal'})
#ax = sns.heatmap(raws, cbar=False, cmap="YlGnBu", cbar_kws={'orientation': 'horizontal'})
#ax.set_title(indexes[selects[i]].strip(),fontsize=10,fontweight='bold')
#plt.xticks(range(len(raws.columns)),raws.columns)
#ax_divider = make_axes_locatable(ax)
#cax = ax_divider.append_axes('bottom', size = '5%', pad = '2%')
#plt.colorbar(ax.get_children()[0], cax=cax, orientation='horizontal')
#cax.xaxis.set_ticks_position('bottom')



#    ax.set_xticks(np.arange(patten_select * 3000,(patten_select + 1) * 3000,500))
   # ax.set_xticks([0,1000,2000,3000]) # tICK이 잘린 순으로 작성된다.
#    ax.set_xticklabels([0,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000])
   # ax.set_xticklabels(['0','1,000','2,000','3,000'],rotation=45,fontsize=8)

#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()

exit()


