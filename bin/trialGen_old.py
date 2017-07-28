# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:06:39 2017
@author: yc180

"""
    #respMapping=[1,2]
    #repetition=2
    
def trialGen(respMapping,repetition):
        
    import numpy as np
    import copy
    import random
    import csv        
    
    
    def myShuffle(ss):
        random.shuffle(ss)    
        return copy.copy(ss)
    ############################################
    col        = dict(bkId=0, blockType=1, trialType=2, stimSet=3, stim=4, stimCat=5, audioType=6, response=7, target=8, distractor=9)
    
    stimSetList = [1,2,3]
    random.shuffle(stimSetList)  # shuffle array elements in place    
    spMat  = np.empty([0,len(col)], dtype=int)  # 160 unique stim
       
    
    ############################################
    # construct Stroop trials
    t1 = list(np.arange(1,41,1))
    t2 = list(np.arange(41,81,1))  # must treat it as a list to concatenate them easily, see line 61
    
    
    # shuffle stimuli to be assigned to each condition
    con_nat = myShuffle(t1)
    con_man = myShuffle(t2)
    inc_nat = myShuffle(t1)
    inc_man = myShuffle(t2)
    
    bkType = random.choice([[1,0]*8, [0,1]*8])    
    
    for miniBk in range(len(bkType)):
        block = np.ones([10,len(col)], dtype=int)*9999  # 10 trials per block, 11 columns (trial attributes)
        block[:,col['bkId']] = miniBk
        
        if bkType[miniBk]==0:
            block[:, col['stim']]      = np.array(con_nat[:5] + con_man[:5])            
            block[:, col['stimSet']]   = stimSetList[0]
            block[:, col['trialType']] = np.array(myShuffle([0]*4 + [1]*1) + myShuffle([0]*4 + [1]*1))  # 0 = congruent, 1 = incongruent
            block[:, col['blockType']] = 0  # mostly congruent
            con_nat[:5]=[]
            con_man[:5]=[]
        else:
            block[:, col['stim']]      = np.array(inc_nat[:5] + inc_man[:5])
            block[:, col['stimSet']]   = stimSetList[1]
            block[:, col['trialType']] = np.array(myShuffle([1]*4 + [0]*1) + myShuffle([1]*4 + [0]*1))  # 0 = congruent, 1 = incongruent
            block[:, col['blockType']] = 1  # mostly Incongruent
            inc_nat[:5]=[]
            inc_man[:5]=[]
                    
        # common things
        block[:, col['stimCat']]   = np.array([1]*5 + [2]*5) # 1 = natural, 2 = manmade
        block[:, col['response']]  = np.array([respMapping[0]]*5 + [respMapping[1]]*5)
        block[:, col['audioType']] = np.array([1]*5 + [2]*5)  # copy the stimCat.. all congruent labels            
        replaceIdx= [i for i, j in enumerate(block[:, col['trialType']]) if j == 1] # find the incongrent ones
        block[replaceIdx, col['audioType']] = 3-block[replaceIdx, col['audioType']]                
        np.random.shuffle(block)
        spMat = np.concatenate((spMat,block), axis =0)
    
        # Shuffle trials but keep trialtype thing.. for rep 2 or more
        spMat1 = copy.copy(spMat)
        # spMat1 will be concatenated with.. and will be the final spMat
        # spMat is the original one and will not be changed
    for rep in range(0,repetition-1,1):
        newBkList=myShuffle(range(0,16,1))
        spMat_new  = np.empty([0,len(col)], dtype=int) 
        for bk in newBkList:
            miniBk=miniBk+1
            block = copy.copy(spMat[spMat[:, col['bkId']]==bk,:])
            np.random.shuffle(block)
            block[:, col['bkId']] = miniBk
            spMat_new = np.concatenate((spMat_new,block), axis =0)
        # 
        spMat1 = np.concatenate((spMat1, spMat_new), axis =0)
    
    
    
    
    # trialMat 160 x 8  Stroop , also serve as "memory-old"
    
    ############################################
    
    # Memory new items
    new_nat = myShuffle(t1)
    new_man = myShuffle(t2)
        
    memMat    = np.empty([0,len(col)],dtype=int)
    block_old = copy.copy(spMat)
    block_old[:,col['response']]  = 0 # 0 = old item, 1 = new item
    block_old[:,col['audioType']] = 9999
    # select some trials to present tone and present probe questions, use 'distractor' column to mark those trials
    block_old[:,8]=range(0,len(block_old),1)
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==0) & (block_old[:,col['trialType']]==0) & (block_old[:,col['stimCat']]==1),8])[0:6], 9]=[1,1,1,2,2,2]  # MC-congurent x 12
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==0) & (block_old[:,col['trialType']]==0) & (block_old[:,col['stimCat']]==2),8])[0:6], 9]=[1,1,1,2,2,2]  
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==0) & (block_old[:,col['trialType']]==1) & (block_old[:,col['stimCat']]==1),8])[0:2], 9]=[1,2]  # MC-incongruent x 4
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==0) & (block_old[:,col['trialType']]==1) & (block_old[:,col['stimCat']]==2),8])[0:2], 9]=[1,2]  
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==1) & (block_old[:,col['trialType']]==1) & (block_old[:,col['stimCat']]==1),8])[0:6], 9]=[1,1,1,2,2,2]  # MIC-congurent x 12
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==1) & (block_old[:,col['trialType']]==1) & (block_old[:,col['stimCat']]==2),8])[0:6], 9]=[1,1,1,2,2,2]   
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==1) & (block_old[:,col['trialType']]==0) & (block_old[:,col['stimCat']]==1),8])[0:2], 9]=[1,2]  # MIC-incongruent x 4
    block_old[myShuffle(block_old[(block_old[:,col['blockType']]==1) & (block_old[:,col['trialType']]==0) & (block_old[:,col['stimCat']]==2),8])[0:2], 9]=[1,2]  
    
    block_new = np.ones([80,len(col)], dtype=int)*9999
    block_new[:,col['stim']]      = np.array(new_nat + new_man)
    block_new[:,col['stimCat']]   = np.array([1]*40 + [2]*40) # 1 = natural, 2 = manmade    
    block_new[:,col['stimSet']]   = stimSetList[2]
    block_new[:,col['blockType']] = 2
    block_new[:,col['trialType']] = 2
    block_new[:,col['response']]  = 1
    block_new[:,col['bkId']]  = 99   # record 1-16 for old item and set 9999 for new item
    
    memMat = np.concatenate((memMat, block_old, block_new), axis =0)
    np.random.shuffle(memMat)
    #memMat[:,col['bkId']] = np.array([16]*120 + [17]*120)   ## 0-15 Stroop Task, 16, 17 Memory task
    
    #return (spMat,memMat, col)
    
    ########### spMat1 is the real trial matrix. spMat is only 1 repetition
    spMat_char = np.array(spMat1,dtype='U25')
    spMat_char[:,col['distractor']]=copy.copy(spMat_char[:,col['audioType']])
    spMat_char[:,col['distractor']]=np.char.replace(spMat_char[:,col['distractor']], '1', 'natural.wav')
    spMat_char[:,col['distractor']]=np.char.replace(spMat_char[:,col['distractor']], '2', 'manmade.wav')
    
    spMat_char[:,col['response']]=np.char.replace(spMat_char[:,col['response']], '1', 'g')
    spMat_char[:,col['response']]=np.char.replace(spMat_char[:,col['response']], '2', 'j')
    
    spMat_char[:,col['trialType']]=np.char.replace(spMat_char[:,col['trialType']], '1', 'inc')
    spMat_char[:,col['trialType']]=np.char.replace(spMat_char[:,col['trialType']], '0', 'con')
    
    spMat_char[:,col['blockType']]=np.char.replace(spMat_char[:,col['blockType']], '1', 'hard')
    spMat_char[:,col['blockType']]=np.char.replace(spMat_char[:,col['blockType']], '0', 'easy')
    
    spMat_char[:,col['stimCat']]=np.char.replace(spMat_char[:,col['stimCat']], '1', 'nat')
    spMat_char[:,col['stimCat']]=np.char.replace(spMat_char[:,col['stimCat']], '2', 'man')
    
    
    for r in range(len(spMat_char)):
        spMat_char[r,col['target']] = 'images\\set' + spMat_char[r,col['stimSet']] + '\\' + spMat_char[r,col['stim']] + '.jpg'
    
    
    # output to a csv file
    
    
    header = ['bkId','blockType','trialType','stimCat','targetStim','distractorStim','corrAns']
    with open('trials_stroop.csv', 'wb') as csvfile:
        trialMat = csv.writer(csvfile, delimiter=',')
        trialMat.writerow(header)
        for r in range(len(spMat_char)):
            trialMat.writerow([spMat_char[r,col['bkId']], spMat_char[r,col['blockType']], spMat_char[r,col['trialType']], spMat_char[r,col['stimCat']], 
                               spMat_char[r,col['target']], spMat_char[r,col['distractor']], spMat_char[r,col['response']]])
        
    # save another csv for memory task
    memMat_char = np.array(memMat,dtype='U25')
    memMat_char[:,col['blockType']]=np.char.replace(memMat_char[:,col['blockType']], '1', 'hard')
    memMat_char[:,col['blockType']]=np.char.replace(memMat_char[:,col['blockType']], '0', 'easy')
    memMat_char[:,col['blockType']]=np.char.replace(memMat_char[:,col['blockType']], '2', 'new')
    
    memMat_char[:,col['trialType']]=np.char.replace(memMat_char[:,col['trialType']], '1', 'inc')
    memMat_char[:,col['trialType']]=np.char.replace(memMat_char[:,col['trialType']], '0', 'con')
    memMat_char[:,col['trialType']]=np.char.replace(memMat_char[:,col['trialType']], '2', 'new')
    
    memMat_char[:,col['stimCat']]=np.char.replace(memMat_char[:,col['stimCat']], '1', 'nat')
    memMat_char[:,col['stimCat']]=np.char.replace(memMat_char[:,col['stimCat']], '2', 'man')
    
    
    memMat_char[:,col['distractor']]=np.char.replace(memMat_char[:,col['distractor']], '1', 'tone1.wav')
    memMat_char[:,col['distractor']]=np.char.replace(memMat_char[:,col['distractor']], '2', 'tone2.wav')
    memMat_char[:,col['distractor']]=np.char.replace(memMat_char[:,col['distractor']], '9999', 'NaN')
    
    
    for r in range(len(memMat_char)):
        memMat_char[r,col['target']] = 'images\\set' + memMat_char[r,col['stimSet']] + '\\' + memMat_char[r,col['stim']] + '.jpg'
        
    header = ['blockType','trialType','stimCat','origBkId', 'targetStim','corrAns','probetrial']
    with open('trials_memory.csv', 'wb') as csvfile:
        trialMat2 = csv.writer(csvfile, delimiter=',')
        trialMat2.writerow(header)
        for r in range(len(memMat_char)):
            trialMat2.writerow([memMat_char[r,col['blockType']], memMat_char[r,col['trialType']], memMat_char[r,col['stimCat']], memMat_char[r,col['bkId']], 
                                memMat_char[r,col['target']], memMat_char[r,col['response']],memMat_char[r,col['distractor']]])
     
    
    
    ## generate some practice trials
    bkTypePractice=[0,1] # two blocks, one mostly congruent, 2nd mostly incongruent
    practiceMat  = np.empty([0,len(col)], dtype=int)  # 160 unique stim    
    
    for miniBk in range(len(bkTypePractice)):
        block = np.ones([8,len(col)], dtype=int)*9999  # 10 trials per block, 10 columns (trial attributes)
        block[:,col['bkId']]       = miniBk
        block[:, col['stim']]      = np.array(myShuffle([1,2,3,4]) + myShuffle([5,6,7,8]))
        block[:, col['stimSet']]   = 4
        if bkTypePractice[miniBk]==0:			
            block[:, col['trialType']] = np.array(myShuffle([0]*3 + [1]*1) + myShuffle([0]*3 + [1]*1))  # 0 = congruent, 1 = incongruent
        else:
            block[:, col['trialType']] = np.array(myShuffle([0]*1 + [1]*3) + myShuffle([0]*1 + [1]*3))  # 0 = congruent, 1 = incongruent
    
        block[:, col['blockType']] = bkTypePractice[miniBk]  # 
        block[:, col['stimCat']]   = np.array([1]*4 + [2]*4) # 1 = natural, 2 = manmade
        block[:, col['response']]  = np.array([respMapping[0]]*4 + [respMapping[1]]*4)
        block[:, col['audioType']] = np.array([1]*4 + [2]*4)  # copy the stimCat.. all congruent labels            
        replaceIdx= [i for i, j in enumerate(block[:, col['trialType']]) if j == 1] # find the incongrent ones
        block[replaceIdx, col['audioType']] = 3-block[replaceIdx, col['audioType']]                
        np.random.shuffle(block)
        practiceMat = np.concatenate((practiceMat,block), axis =0)
    
    practiceMat_char = np.array(practiceMat,dtype='U25')
    practiceMat_char[:,col['distractor']]=copy.copy(practiceMat_char[:,col['audioType']])
    practiceMat_char[:,col['distractor']]=np.char.replace(practiceMat_char[:,col['distractor']], '1', 'natural.wav')
    practiceMat_char[:,col['distractor']]=np.char.replace(practiceMat_char[:,col['distractor']], '2', 'manmade.wav')
    	
    practiceMat_char[:,col['blockType']]=np.char.replace(practiceMat_char[:,col['blockType']], '1', 'hard')
    practiceMat_char[:,col['blockType']]=np.char.replace(practiceMat_char[:,col['blockType']], '0', 'easy')
    	
    practiceMat_char[:,col['trialType']]=np.char.replace(practiceMat_char[:,col['trialType']], '1', 'inc')
    practiceMat_char[:,col['trialType']]=np.char.replace(practiceMat_char[:,col['trialType']], '0', 'con')    
    	
    practiceMat_char[:,col['stimCat']]=np.char.replace(practiceMat_char[:,col['stimCat']], '1', 'nat')
    practiceMat_char[:,col['stimCat']]=np.char.replace(practiceMat_char[:,col['stimCat']], '2', 'man')	
    practiceMat_char[:,col['response']]=np.char.replace(practiceMat_char[:,col['response']], '1', 'g')
    practiceMat_char[:,col['response']]=np.char.replace(practiceMat_char[:,col['response']], '2', 'j')
    
    for r in range(len(practiceMat_char)):
        practiceMat_char[r,col['target']] = 'images\\set' + practiceMat_char[r,col['stimSet']] + '\\' + practiceMat_char[r,col['stim']] + '.jpg'
        
    header = ['bkId','blockType','trialType','stimCat','targetStim','distractorStim','corrAns']
    with open('trials_practice.csv', 'wb') as csvfile:
        trialMat3 = csv.writer(csvfile, delimiter=',')
        trialMat3.writerow(header)
        for r in range(len(practiceMat_char)):
            trialMat3.writerow([practiceMat_char[r,col['bkId']], practiceMat_char[r,col['blockType']], practiceMat_char[r,col['trialType']], practiceMat_char[r,col['stimCat']], 
                               practiceMat_char[r,col['target']], practiceMat_char[r,col['distractor']], practiceMat_char[r,col['response']]])
    
    
    
    
    
    # test the source memory.. shuffle all trails 
    
    sourceMem = copy.copy(spMat_char[0:160,:])
    sourceMem[:,col['response']] = copy.copy(sourceMem[:,col['blockType']])
    sourceMem[:,col['response']] = np.char.replace(sourceMem[:,col['response']],'easy','e')
    sourceMem[:,col['response']] = np.char.replace(sourceMem[:,col['response']],'hard','h')
    np.random.shuffle(sourceMem)
    header = ['orig_bkId','blockType','trialType','stimCat','targetStim','distractorStim','corrAns']
    with open('trials_sourceMem.csv', 'wb') as csvfile:
        trialMat = csv.writer(csvfile, delimiter=',')
        trialMat.writerow(header)
        for r in range(len(sourceMem)):
            trialMat.writerow([sourceMem[r,col['bkId']], sourceMem[r,col['blockType']], sourceMem[r,col['trialType']], sourceMem[r,col['stimCat']], 
                               sourceMem[r,col['target']], sourceMem[r,col['distractor']], sourceMem[r,col['response']]])
    
    
