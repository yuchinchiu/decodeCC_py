# -*- coding: utf-8 -*-
"""
Spyder Editor
@author: yc180

This file will generate a "trials_issp.csv" for the filler task. 
Need to privde filler_SRmapping for [odd, even, high, low] (e.g.,filler_SRmapping = [1,2,1,2])
and taskColorRGB (e.g., ['#ff0000','#0000ff'])

"""

def fillerGen(filler_SRmapping, taskColorRGB):   
        
           
    import os
    import numpy as np        
    import random    
    import copy
    import csv        
    
    def myShuffle(ss):
        random.shuffle(ss)    
        return copy.copy(ss) 
    
    
    col = dict(bkId=0, trialType=1, task=2, stim=3, swProb=4,response=5, taskColor=6)
    practiceMat = np.ones([48, len(col)],dtype=int)*9999
    # create a block of practice trials [single task]
    iniTask   = myShuffle([1,2])
	
    practiceMat[:,col['stim']]      = np.array(myShuffle([1,2,3,4,6,7,8,9]*2) + myShuffle([1,2,3,4,6,7,8,9]*2) + myShuffle([1,2,3,4,6,7,8,9]*2))
    practiceMat[:,col['swProb']]    = np.array([50]*len(practiceMat))
    practiceMat[:,col['trialType']] = np.array([0]*32 + myShuffle([1,0]*8))
    practiceMat[:,col['task']]      = np.array([iniTask[0]]*16 + [iniTask[1]]*16 + [0]*16)
    practiceMat[:,col['bkId']]      = np.array([0]*16 + [1]*16 + [2]*16)
	
    currentTask = practiceMat[31,col['task']]
    for r in range(32,len(practiceMat)):
        practiceMat[r,col['task']] = currentTask if practiceMat[r,col['trialType']]==0 else 3-currentTask
        currentTask = practiceMat[r,col['task']]
        
    np.savetxt("initTask.txt",iniTask)    
    ######### real filler task       
    
    fillerMat = np.empty([0,len(col)],dtype=int)
    stimSet = myShuffle([1,3]) + myShuffle([2,4]) + myShuffle([6,8]) + myShuffle([7,9]) 
    swProbList = [80,20]*4  # prob Sw
    trPerStim = 20
    
    for i in range(8):    
        condMat = np.ones([20,len(col)],dtype=int)*9999  # 20 trials per stim 
        NrSw  = trPerStim*swProbList[i]/100
        NrRep = trPerStim-NrSw
        
        condMat[:,col['stim']]       =  np.array([stimSet[i]]*trPerStim)
        condMat[:,col['trialType']]  =  np.array([1]*NrSw + [0]*NrRep)
        condMat[:,col['swProb']]     =  np.array([swProbList[i]]*trPerStim)
        
        fillerMat = np.concatenate((fillerMat,condMat), axis=0)
        
    
    
    while 1:
        np.random.shuffle(fillerMat)
        currentTask = random.choice([1,2])
        for tr in range(len(fillerMat)):
            fillerMat[tr,col['task']] = currentTask if fillerMat[tr,col['trialType']]==0 else 3-currentTask
            currentTask =  fillerMat[tr,col['task']]
        
        nrT1 = int(sum(fillerMat[:,col['task']]==1))
        nrT2 = int(sum(fillerMat[:,col['task']]==2))
        stimT1CNT=[]
        for s in [1,2,3,4,6,7,8,9]:
            stimT1CNT.append(int(sum(np.array(fillerMat[:,col['stim']]==s) & np.array(fillerMat[:,col['task']]==1))))
        stimT1CNTexp  = trPerStim/2    
        if (nrT1==nrT2) & (sum(abs(np.array(stimT1CNT)-stimT1CNTexp)<=2)==8):
            break
        
    fillerMat[:,col['bkId']] = np.asanyarray([3]*80 + [4]*80)    
    fillerMat = np.concatenate((practiceMat,fillerMat),axis=0)
    
     # trialMat good to go.. figure out correct response
    
    for r in range(len(fillerMat)):
        if fillerMat[r,col['task']]==1: # oldd/even
            if fillerMat[r,col['stim']]%2==0: # even
                fillerMat[r,col['response']]= filler_SRmapping[1] # Even
            else:
               fillerMat[r,col['response']]= filler_SRmapping[0]  # Odd
        else:  # high/low
            if fillerMat[r,col['stim']]>5: # high
               fillerMat[r,col['response']]= filler_SRmapping[2]  # high
            else:
               fillerMat[r,col['response']]= filler_SRmapping[3]  # low
    
    
    
    #return (fillerMat,col)
    
    
     # output to a csv file
    
    fillerMat_char = np.array(fillerMat, dtype=str)
    
    fillerMat_char[:,col['response']]  = np.char.replace(fillerMat_char[:,col['response']],'1','g')
    fillerMat_char[:,col['response']]  = np.char.replace(fillerMat_char[:,col['response']],'2','j')
    fillerMat_char[:,col['taskColor']] = copy.copy(fillerMat_char[:,col['task']])
    fillerMat_char[:,col['taskColor']] = np.char.replace(fillerMat_char[:,col['taskColor']],'1',taskColorRGB[0])
    fillerMat_char[:,col['taskColor']] = np.char.replace(fillerMat_char[:,col['taskColor']],'2',taskColorRGB[1])
    
    header = ['bkId','trialType','task','taskColor','taskStim','swProb','corrAns']
    
    with open('trials_issp.csv', 'wb') as csvfile:
        trialMat = csv.writer(csvfile, delimiter=',')
        trialMat.writerow(header)
        for r in range(len(fillerMat_char)):
            trialMat.writerow([fillerMat_char[r,col['bkId']], fillerMat_char[r,col['trialType']], fillerMat_char[r,col['task']], fillerMat_char[r,col['taskColor']], 
                                fillerMat_char[r,col['stim']], fillerMat_char[r,col['swProb']], fillerMat_char[r,col['response']]])
	return iniTask
