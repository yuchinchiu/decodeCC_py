# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 14:34:13 2017

@author: yc180
"""

#%%
from copy import copy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_pickle('gp_stroop.pkl')
overallM=df.groupby('sbjId').sbjACC.mean()
fig, axs = plt.subplots(1,2,figsize=(16,5))
sns.factorplot(x='blockType',y = 'sbjACC', data=df, hue='trialType', ax=axs[0])
sns.factorplot(x='blockType',y = 'sbjRT', data=df, hue='trialType',ax=axs[1])
axs[0].set_title("Stroop Task mean ACC")
axs[1].set_title("Stroop Task mean RT")
plt.show()


#%%
df = pd.read_pickle('gp_memory.pkl')
df2= copy(df.loc[df.blockType!='new'])
df2.blockType=pd.Categorical(df2.blockType, categories=['easy','hard'], ordered=True)
df2.trialType=pd.Categorical(df2.trialType, categories=['con','inc'], ordered=True)

fig = plt.figure(figsize=(10,5))
sns.factorplot(x='blockType',y = 'sbjACC', data=df2, hue='trialType')
plt.ylim(0,100)
plt.title('Memory accuracy')



#%%
df = pd.read_pickle('gp_sourceMem.pkl')
fig = plt.figure(figsize=(10,5))
sns.factorplot(x='blockType',y = 'sbjACC', data=df, hue='trialType')
plt.ylim(30,60)
plt.title('Source memory accuracy')
plt.show()



# =============================================================================
# #%%
# df = pd.read_pickle('gp_filler.pkl')
# fig,axs  = plt.subplots(1,2,figsize=(16,5))
# axs[0].set_title("ISSP Task mean ACC")
# sns.factorplot(x='swProb',y = 'sbjACC', data=df, hue='trialType', ax=axs[0])
# axs[1].set_title("ISSP Task mean RT")
# sns.factorplot(x='swProb',y = 'sbjRT', data=df, hue='trialType',ax=axs[1])
# 
# =============================================================================
