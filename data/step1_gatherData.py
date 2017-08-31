# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:43:14 2017

@author: yc180

"""

import os
from copy import copy 
import pandas as pd
import numpy as np

version  = 'v2'

#currentDir = os.getcwd()
currentDir = os.path.dirname(os.path.realpath(__file__))
dataDir = currentDir + os.sep + 'csv' + os.sep + version + os.sep

#%% Do a quick first past to exclude sbj whose stroop task accuracy is too low <75%
if version == 'v1':
    sbjList = range(1,21)  # 1-20
else:
    sbjList = range(21,41)  # 21-40
        
goodSbjList=[]
taskName='stroop'
for S in sbjList:   
    f = dataDir + 'stroop' + '_' +str(S) +  '.csv'
    df = pd.read_csv(f)
    if df.sbjACC.mean()>0.75:
        goodSbjList.append(S)   

#%%
taskNameList = ['stroop','sourceMem']

for taskName in taskNameList:
    gpResult = pd.DataFrame(np.empty((0,0),dtype=int))
    
    for S in goodSbjList:
        f = dataDir + taskName + '_' +str(S) +  '.csv'
        df = pd.read_csv(f)
        df.drop(df.columns[[0,1]],axis=1,inplace=True)
        df['blockType'] = pd.Categorical(df.blockType, categories=['easy','hard'], ordered=True)
        df['trialType'] = pd.Categorical(df.trialType, categories=['con','inc'], ordered=True)
        df['sbjRT2'] = copy(df.sbjRT)  # use sbjRT2 to store the original and modify sbjRT
        df.loc[df.sbjRT2 <= 0.25, 'sbjRT']= np.nan
        df.loc[df.sbjACC == 0, 'sbjRT'] = np.nan
    
        sbjMeans = df.groupby(['blockType','trialType']).sbjACC.mean()*100
        mRT = df.groupby(['blockType','trialType']).sbjRT.mean()*1000  # correct trial RTs
        sbjMeans=pd.concat([sbjMeans,mRT],axis=1)
        sbjMeans['sbjId']=S           
        gpResult = pd.concat([gpResult,sbjMeans], axis=0)

    # output group DataFrame
   
    gpResult.reset_index(inplace=True)
    gpResult.to_pickle('gp_' + taskName + '_' + version +'.pkl')



#%%
excludeSbj=[]
taskName='memory'
gpResult = pd.DataFrame(np.empty((0,0),dtype=int))
for S in goodSbjList:    
    f = dataDir + taskName + '_' +str(S) +  '.csv'
    df = pd.read_csv(f)
    df.drop(df.columns[[0,1]],axis=1,inplace=True)
    df['blockType'] = pd.Categorical(df.blockType, categories=['easy','hard','new'], ordered=True)
    df['trialType'] = pd.Categorical(df.trialType, categories=['con','inc','new'], ordered=True)
    df['sbjResp'] = pd.Categorical(df.sbjResp, categories=['defNew','probNew','probOld','defOld'], ordered=True)    
    # figure memory accuracy        
    df.loc[df.sbjResp<='probNew','sbjRespCat']= 'new'
    df.loc[df.sbjResp>'probNew','sbjRespCat'] = 'old'
    df.loc[df.sbjResp.cat.codes==-1,'sbjRespCat']=None
    df.sbjACC=0
    df.loc[df.sbjRespCat == df.corrAns,'sbjACC']=1
    
    CR_rate = df[df.blockType=='new'].sbjACC.mean()*100
    if CR_rate <50:
        excludeSbj.append(S)
    
    # memory accuracy
    sbjMeans = df.groupby(['blockType','trialType']).sbjACC.mean()*100
    mRT = df.groupby(['blockType','trialType']).sbjRT.mean()*1000
    sbjMeans=pd.concat([sbjMeans,mRT],axis=1)
    sbjMeans['sbjId']=S    
    
    #prob detection accuracy 
    df2 = copy(df.loc[df.probetrial.notnull(),:])
    df2['probeACC']=0
    df2.loc[(df2.probetrial=='tone1.wav') & (df2.probeResp=='y'),'probeACC']=1
    df2.loc[(df2.probetrial=='tone2.wav') & (df2.probeResp=='n'),'probeACC']=1
    probeACC = df2.groupby(['blockType','trialType']).probeACC.mean()*100 
    probeRT  = df2.groupby(['blockType','trialType']).probeRT.mean()*1000
    sbjMeans=pd.concat([sbjMeans,probeACC,probeRT],axis=1)
    
    gpResult = pd.concat([gpResult,sbjMeans], axis=0)
# output group DataFrame
gpResult.reset_index(inplace=True)
gpResult.to_pickle('gp_memory_'  + version + '.pkl')


#%%
taskName='filler'
gpResult = pd.DataFrame(np.empty((0,0),dtype=int))
for S in goodSbjList: 
    f = dataDir + taskName + '_' +str(S) +  '.csv'
    df = pd.read_csv(f)
    df.drop(df.columns[0],axis=1,inplace=True)  # for this.. somehow only the first column is unamed..
    df=df.loc[df.bkId>=3]
    df['swProb'] = pd.Categorical(df.swProb, categories=['sw20%','sw80%'], ordered=True)
    df['trialType'] = pd.Categorical(df.trialType, categories=['repeat','switch'], ordered=True)     
    
    sbjMeans = df.groupby(['swProb','trialType']).sbjACC.mean()*100
    mRT = df.groupby(['swProb','trialType']).sbjRT.mean()*1000
    sbjMeans=pd.concat([sbjMeans,mRT],axis=1)
    sbjMeans['sbjId']=S    
    gpResult = pd.concat([gpResult,sbjMeans], axis=0)

# output group DataFrame
gpResult.reset_index(inplace=True)    
gpResult.to_pickle('gp_filler_' + version + '.pkl')



if version=='v1':
    excludeSbj.append(11)
    excludeSbj.append(12)
else:
    excludeSbj.append(21)
    excludeSbj.append(26)

#%% use excludeSbj to clean up pkl 

if len(excludeSbj)>0:
    taskNameList = ['stroop','sourceMem','memory','filler']
    for taskName in taskNameList:        
        gpResult = pd.read_pickle('gp_' + taskName + '_' + version + '.pkl')
        for S in excludeSbj:
            gpResult.drop(gpResult[gpResult.sbjId==S].index, axis=0, inplace=True)
        gpResult.reset_index(inplace=True)
        gpResult.to_pickle('gp_' + taskName + '_' + version + '.pkl')
        
        