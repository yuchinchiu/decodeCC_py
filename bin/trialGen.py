# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:06:39 2017
@author: yc180

"""
#respMapping=[1,2]
#repetition=2

def trialGen(respMapping,repetition):
    
    import pandas as pd    
    import numpy as np
    import random
    import copy
    
    SRmapping=['g','j']
    repetition = 2
    
    def myShuffle(ss):
        random.shuffle(ss)    
        return copy.copy(ss)
    
    stimSetList = [1,2,3] # set 4 = practice
    random.shuffle(stimSetList)  # shuffle array elements in place    
    
    header = ['bkId','blockType','trialType','stimCat','stimSet','targetStim','distractorStim','corrAns']
    spMat = pd.DataFrame(np.empty([0,len(header)], dtype=int),columns=header)
    
    #########################################
    
    # construct Stroop trials
    t1 = list(np.arange(1,41,1))
    t2 = list(np.arange(41,81,1))  # must treat it as a list to concatenate them easily, see line 61
    # shuffle stimuli to be assigned to each condition
    con_nat = myShuffle(t1)
    con_man = myShuffle(t2)
    inc_nat = myShuffle(t1)
    inc_man = myShuffle(t2)
    
    bkType = random.choice([['hard','easy']*8, ['easy','hard']*8])    
    
    for miniBk in range(len(bkType)):
        block = pd.DataFrame(np.ones([10,len(header)], dtype=int)*9999, columns=header)   # 10 trials per block, 11 columns (trial attributes)
        block.loc[:,'bkId']       = miniBk
        block.loc[:,'stimCat']    = ['nat']*5 + ['man']*5
        block.loc[:,'corrAns']   = [SRmapping[0]]*5 + [SRmapping[1]]*5    
        block.loc[:,'targetStim'] = con_nat[:5] + con_man[:5] if bkType[miniBk]=='easy' else inc_nat[:5] + inc_man[:5]
        block.loc[:,'stimSet']    = stimSetList[0] if bkType[miniBk]=='easy' else stimSetList[1]
        block.loc[:,'trialType']  = myShuffle(['con']*4 + ['inc']*1) + myShuffle(['con']*4 + ['inc']*1) if bkType[miniBk]=='easy' else myShuffle(['inc']*4 + ['con']*1) + myShuffle(['inc']*4 + ['con']*1)
        block.loc[:,'blockType']  = bkType[miniBk]
        if bkType[miniBk]=='easy':
            con_nat[:5]=[]
            con_man[:5]=[]
        else:
            inc_nat[:5]=[]
            inc_man[:5]=[]        
        block.loc[:,'distractorStim'] = [1]*5 + [2]*5
        block.loc[block.loc[:,'trialType']=='inc','distractorStim']=3-block.loc[block.loc[:,'trialType']=='inc','distractorStim']    
        block = block.sample(frac=1).reset_index(drop=True)
        spMat = spMat.append(block, ignore_index=True)
    
    # keey spMat as original and never modify it..
    spMat1 = copy.copy(spMat)
    for rep in range(0,repetition-1,1):
        newBkList = myShuffle(range(0,16,1))
        spMat_new  =  pd.DataFrame(np.empty([0,len(header)], dtype=int),columns=header)
        for bk in newBkList:
            miniBk = miniBk+1
            block = copy.copy(spMat.loc[spMat.loc[:, 'bkId']==bk,:])
            block = block.sample(frac=1).reset_index(drop=True)
            block.loc[:,'bkId']= miniBk            
            spMat_new = spMat_new.append(block, ignore_index=True)
    
        spMat1 = spMat1.append(spMat_new, ignore_index=True)
    
    
    spMat1.distractorStim = spMat1.distractorStim.replace(1,'natural.wav')
    spMat1.distractorStim = spMat1.distractorStim.replace(2,'manmade.wav')
    spMat1.loc[:,'targetStim'] = 'images\\set' + spMat1.loc[:,'stimSet'].astype(str) + '\\' + spMat1.loc[:,'targetStim'].astype(str) + '.jpg' 
    
    spMat1.drop('stimSet',axis=1, inplace=True)
    spMat1.to_csv('trials_stroop.csv')
    
    #########################################
    
    bkTypePractice=['easy','hard'] # two blocks, one mostly congruent, 2nd mostly incongruent
    practiceM = pd.DataFrame(np.empty([0,len(header)], dtype = int), columns=header)
    for miniBk in range(len(bkTypePractice)):
        block = pd.DataFrame(np.ones([8,len(header)], dtype=int)*9999, columns=header)   # 10 trials per block, 11 columns (trial attributes)
        block.loc[:,'bkId']       = miniBk
        block.loc[:,'stimCat']    = ['nat']*4 + ['man']*4
        block.loc[:,'corrAns']    = [SRmapping[0]]*4 + [SRmapping[1]]*4
        block.loc[:,'targetStim'] = myShuffle([1,2,3,4]) + myShuffle([5,6,7,8])
        block.loc[:,'stimSet']    = 4
        block.loc[:,'trialType']  = myShuffle(['con']*3 + ['inc']*1) + myShuffle(['con']*3 + ['inc']*1) if bkTypePractice[miniBk]=='easy' else myShuffle(['inc']*3 + ['con']*1) + myShuffle(['inc']*3 + ['con']*1)
        block.loc[:,'blockType']  = bkTypePractice[miniBk]       
        block.loc[:,'distractorStim'] = [1]*4 + [2]*4
        block.loc[block.loc[:,'trialType']=='inc','distractorStim']=3-block.loc[block.loc[:,'trialType']=='inc','distractorStim']    
        block = block.sample(frac=1).reset_index(drop=True)
        practiceM = practiceM.append(block, ignore_index=True)
    
    
    practiceM.distractorStim = practiceM.distractorStim.replace(1,'natural.wav')
    practiceM.distractorStim = practiceM.distractorStim.replace(2,'manmade.wav')
    practiceM.loc[:,'targetStim'] = 'images\\set' + practiceM.loc[:,'stimSet'].astype(str) + '\\' + practiceM.loc[:,'targetStim'].astype(str) + '.jpg' 
    
    practiceM.drop('stimSet',axis=1, inplace=True)
    practiceM.to_csv('trials_practice.csv')
    
    #########################################
    
    new_nat = myShuffle(t1)
    new_man = myShuffle(t2)
    
    header = ['blockType','trialType','stimCat','targetStim','corrAns','probetrial']
    memMat = pd.DataFrame(np.empty([0,len(header)],dtype=int),columns=header)
    
    block_old = copy.copy(spMat)
    block_old.drop(['distractorStim','bkId'],axis=1, inplace = True)
    block_old.loc[:,'corrAns'] = 'old'
    block_old.loc[:,'probetrial']=None
    
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='hard') & (block_old.loc[:,'trialType']=='inc') & (block_old.loc[:,'stimCat']=='nat')].sample(frac=.2).index,'probetrial']=[1,1,1,2,2,2]
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='hard') & (block_old.loc[:,'trialType']=='inc') & (block_old.loc[:,'stimCat']=='man')].sample(frac=.2).index,'probetrial']=[1,1,1,2,2,2]
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='hard') & (block_old.loc[:,'trialType']=='con') & (block_old.loc[:,'stimCat']=='nat')].sample(frac=.2).index,'probetrial']=[1,2]
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='hard') & (block_old.loc[:,'trialType']=='con') & (block_old.loc[:,'stimCat']=='man')].sample(frac=.2).index,'probetrial']=[1,2]
    
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='easy') & (block_old.loc[:,'trialType']=='con') & (block_old.loc[:,'stimCat']=='nat')].sample(frac=.2).index,'probetrial']=[1,1,1,2,2,2]
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='easy') & (block_old.loc[:,'trialType']=='con') & (block_old.loc[:,'stimCat']=='man')].sample(frac=.2).index,'probetrial']=[1,1,1,2,2,2]
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='easy') & (block_old.loc[:,'trialType']=='inc') & (block_old.loc[:,'stimCat']=='nat')].sample(frac=.2).index,'probetrial']=[1,2]
    block_old.loc[block_old[(block_old.loc[:,'blockType']=='easy') & (block_old.loc[:,'trialType']=='inc') & (block_old.loc[:,'stimCat']=='man')].sample(frac=.2).index,'probetrial']=[1,2]
    
    
    block_new = pd.DataFrame(np.ones([80,len(header)],dtype=int)*9999,columns=header)
    block_new.loc[:,'targetStim']   = new_nat + new_man
    block_new.loc[:,'stimCat']= ['nat']*40 + ['man']*40
    block_new.loc[:,'stimSet'] =stimSetList[2]
    block_new.loc[:,'blockType'] = 'new'
    block_new.loc[:,'trialType'] = 'new'
    block_new.loc[:,'corrAns'] = 'new'
    block_new.loc[:,'probetrial'] = None
    block_new.loc[block_new[block_new.loc[:,'stimCat']=='nat'].sample(frac=.2).index,'probetrial']=[1]*4 + [2]*4
    block_new.loc[block_new[block_new.loc[:,'stimCat']=='man'].sample(frac=.2).index,'probetrial']=[1]*4 + [2]*4
    
    
    memMat=pd.concat([block_old,block_new],axis =0)
    memMat = memMat.sample(frac=1).reset_index(drop=True)
    
    memMat.loc[:,'targetStim'] = 'images\\set' + memMat.loc[:,'stimSet'].astype(str) + '\\' + memMat.loc[:,'targetStim'].astype(str) + '.jpg' 
    memMat.probetrial = memMat.probetrial.replace(1,'tone1.wav')
    memMat.probetrial = memMat.probetrial.replace(2,'tone2.wav')
    memMat.to_csv('trials_memory.csv')
    
    #########################################
    
    
    sourceMat = copy.copy(spMat1.loc[0:159,:])
    sourceMat.loc[:,'corrAns']=copy.copy(sourceMat.loc[:,'blockType'])
    sourceMat.corrAns=sourceMat.corrAns.replace('easy','e')
    sourceMat.corrAns=sourceMat.corrAns.replace('hard','h')
    sourceMat = sourceMat.sample(frac=1).reset_index(drop=True)
    sourceMat.drop(['bkId','distractorStim'],axis=1, inplace=True)
    sourceMat.to_csv('trials_sourceMem.csv')