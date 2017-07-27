# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 10:40:08 2017

@author: yc180
modiefied from issp_TrialGen.py 


"""
def fillerGen(SRmapping_par, SRmapping_mag, taskColorRGB):
#    SRmapping = ['g','j','g','j']
#    taskColorRGB = ['#ff0000','#0000ff']

    import pandas as pd
    import numpy as np
    import random
    import copy
#    import csv
    
    
    def myShuffle(ss):
        random.shuffle(ss)    
        return copy.copy(ss) 
    
    header = ['bkId','trialType','task','taskColor','taskStim','swProb','corrAns']
    practiceM = pd.DataFrame(np.ones([48,len(header)], dtype=int)*999,columns=header)
    initTask = myShuffle([1,2])   # 1 = parity, 2 = magnitude
    
    practiceM.loc[:,'taskStim']  = myShuffle([1,2,3,4,6,7,8,9]*2) + myShuffle([1,2,3,4,6,7,8,9]*2) + myShuffle([1,2,3,4,6,7,8,9]*2)
    practiceM.loc[:,'swProb']    = 'sw50%'
    practiceM.loc[:,'trialType'] = ['repeat']*32 + myShuffle(['switch','repeat']*8)
    practiceM.loc[:,'task']      = [initTask[0]]*16 + [initTask[1]]*16 + [0]*16
    practiceM.loc[:,'bkId']      = [0]*16 + [1]*16 + [2]*16
    
    # fill in the correct task for bkId==2
    currentTask = practiceM.loc[31,'task']
    for r in range(32,len(practiceM)):
        practiceM.loc[r,'task'] = currentTask if practiceM.loc[r,'trialType']=='repeat' else 3-currentTask
        currentTask = practiceM.loc[r,'task']
    
    
    # formal filler task
    fillerMat = pd.DataFrame(np.empty([0,len(header)], dtype=int),columns=header)
    stimSet = myShuffle([1,3]) + myShuffle([2,4]) + myShuffle([6,8]) + myShuffle([7,9]) 
    swProbList = [80,20]*4  # swProb
    trPerStim = 20
    
    
    for i in range(len(stimSet)):
        condMat = pd.DataFrame(np.ones([20,len(header)],dtype=int)*9999,columns=header)  # 20 trials per stim 
        NrSw  = trPerStim*swProbList[i]/100
        NrRep = trPerStim-NrSw
        condMat.loc[:,'taskStim']  = stimSet[i]
        condMat.loc[:,'trialType'] = ['switch']*NrSw + ['repeat']*NrRep
        condMat.loc[:,'swProb']    = 'sw' + str(swProbList[i]) + '%'
        fillerMat = fillerMat.append(condMat, ignore_index=True)
    
    while 1:
        fillerMat = fillerMat.sample(frac=1).reset_index(drop=True)
        currentTask = random.choice([1,2])
        for tr in range(len(fillerMat)):
            fillerMat.loc[tr,'task'] = currentTask if fillerMat.loc[tr,'trialType']==0 else 3-currentTask
            currentTask = fillerMat.loc[tr,'task']
            nrT1=sum(fillerMat['task']==1)
            nrT2=sum(fillerMat['task']==2)
        stimT1CNT=[]
        
        for s in [1,2,3,4,6,7,8,9]:
            stimT1CNT.append(sum((fillerMat.loc[:,'taskStim']==s) & (fillerMat.loc[:,'task']==1)))
        stimT1CNTexp = trPerStim/2 
        
        if (nrT1==nrT2) & (sum(abs(np.array(stimT1CNT)-stimT1CNTexp)<=2)==8):
            break
    
    fillerMat.loc[:,'bkId'] = [3]*80 + [4]*80
    fillerMat = practiceM.append(fillerMat, ignore_index=True)
            
        
    for r in range(len(fillerMat)):
        if fillerMat.loc[r,'task'] ==1:  # parity  [odd, even, high, low]
            fillerMat.loc[r,'corrAns']= SRmapping_par[0] if fillerMat.loc[r,'taskStim']%2==1 else SRmapping_par[1]
        else: # magnitude
            fillerMat.loc[r,'corrAns']= SRmapping_mag[0] if fillerMat.loc[r,'taskStim']>5 else SRmapping_mag[1]
    
    
    fillerMat.loc[:,'taskColor']= fillerMat.loc[:,'task']
    fillerMat.loc[:,'taskColor']= fillerMat.loc[:,'taskColor'].replace(1,taskColorRGB[0])
    fillerMat.loc[:,'taskColor']= fillerMat.loc[:,'taskColor'].replace(2,taskColorRGB[1])
    fillerMat.loc[:,'task']= fillerMat.loc[:,'task'].replace(1,'par')
    fillerMat.loc[:,'task']= fillerMat.loc[:,'task'].replace(2,'mag')
    
    fillerMat.trialType = pd.Categorical(fillerMat.trialType, categories=['repeat','switch'],ordered=True)
    fillerMat.swProb    = pd.Categorical(fillerMat.swProb, categories=['sw20%','sw80%'],ordered=True)
    
    return fillerMat

