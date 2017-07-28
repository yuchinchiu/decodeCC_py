#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Memory recognition task: 240 trials + occasional probe trials (32)
Memory judgement is fixed 2 sec, probe q is until response is made

"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os  # handy system and path functions
import sys  # to get file system encoding

import pandas as pd
import numpy as np


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# YCC: 
M = pd.read_csv('trials_memory.csv')
M.loc[:,'sbjResp']= None
M.loc[:,'sbjRT']  = np.nan
M.loc[:,'sbjACC'] =np.nan

M.loc[:,'probeResp']  = None
M.loc[:,'probeRT']    = np.nan
M.loc[:,'probeACC']   = np.nan


# Store info about the experiment session
expName = u'memory'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expName, expInfo['participant'])

logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

mem_SRmapping=['0','1'][int('99')%2]  # see line 110
# 0: [v,b,n,m] => defNew, probNew,probOld,defOld
# 1: [v,b,n,m] => defOld, probOld,probNew,defNew


# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Ins"
taskInstruction = u'Your task now is to judge whether you have seen the presented image before by using the keys provided.\n\nThe keys will stay on the screen\n\nPress Space to start.'
InsClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text = taskInstruction,
    font=u'Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine 'probeTrial'
probeQuestion= u"Did you hear a tone in the previous trial?\nIf yes, press 'y', If no, press 'n'"
probeClock = core.Clock()
probe = visual.TextStim(win=win, name='probe',
    text = probeQuestion,
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);
    
# Initialize components for Routine "ITI"
ITIClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
target = visual.ImageStim(
    win=win, name='target',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

distractor = sound.Sound('A', secs=-1)
distractor.setVolume(1)

SRmapping = visual.ImageStim(
    win=win, name='SRmapping',
    image=u'images\T3_RespMapping' + mem_SRmapping +'.jpg', mask=None,
    ori=0, pos=(0, -0.7), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Task Instructions #############################

ins_response = event.BuilderKeyResponse()
ins_response.status == NOT_STARTED
Instruction.setAutoDraw(True)
continueRoutine = True
while continueRoutine:
    
    # *ins_response* updates
    if ins_response.status == NOT_STARTED:
        ins_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ins_response.clock.reset)
        event.clearEvents(eventType='keyboard')
    if ins_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if "escape" in theseKeys:
            core.quit()
        if len(theseKeys) > 0:  # at least one key was pressed, end the routine
            continueRoutine = False
    
    if continueRoutine:
        win.flip()
    else:
        break
Instruction.setAutoDraw(False)
routineTimer.reset()   # use this line, when the routine ends with subject making a key press

# Trial Loop ############################################
for trialCNT in range(0,len(M),1):

    # ITI ###############################################
    blank.setAutoDraw(True)
    event.clearEvents(eventType='keyboard')
    continueRoutine = True
    routineTimer.add(0.500000) # This is countdown timer
    while continueRoutine:        
        if event.getKeys(keyList=["escape"]):
            core.quit()
        if routineTimer.getTime() > 0:
            win.flip()
        else:            
            break
            
    blank.setAutoDraw(False)

    # Break #############################################
    if (trialCNT>1) & (trialCNT%80 == 0) & (trialCNT<len(M)):    # total =240
        Instruction.setText("Take a break here and press Space to continue")
        ins_response = event.BuilderKeyResponse()
        ins_response.status == NOT_STARTED
        Instruction.setAutoDraw(True)
        continueRoutine = True
        while continueRoutine:
            if ins_response.status == NOT_STARTED:
                ins_response.status = STARTED
                win.callOnFlip(ins_response.clock.reset)
                event.clearEvents(eventType='keyboard')
            if ins_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
            if "escape" in theseKeys:
                core.quit()
            if len(theseKeys) > 0:  # at least one key was pressed, end the routine
                continueRoutine = False    
            if continueRoutine:
                win.flip()
            else:
                break
        Instruction.setAutoDraw(False)
        routineTimer.reset()  # use this line, when the routine ends with subject making a key press
    
    # trial routine ########################################
    continueRoutine = True
    target.setImage(M.loc[trialCNT,'targetStim'])    
    target.setAutoDraw(True)
    SRmapping.setAutoDraw(True)
    if ~(M.probetrial.isnull()[trialCNT]):  # IS NOT NULL
        distractor.setSound(M.loc[trialCNT,'probetrial'], secs=1)
        distractor.play()    
    response = event.BuilderKeyResponse()
    response.status == NOT_STARTED
    response.keys = []

    routineTimer.add(2.000000)
    while continueRoutine and routineTimer.getTime() > 0:
        if response.status == NOT_STARTED:
            response.status = STARTED
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b', 'n', 'm'])
            if "escape" in theseKeys:
                core.quit()
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    M.loc[trialCNT,'sbjResp'] = theseKeys[0] # just the first key pressed
                    M.loc[trialCNT,'sbjRT']   = response.clock.getTime()
        if routineTimer.getTime() > 0:
            win.flip()
        else:
            break
    target.setAutoDraw(False)
    SRmapping.setAutoDraw(False)
    if ~(M.probetrial.isnull()[trialCNT]):        
        distractor.stop()
    response.status = STOPPED
    # ###################################################################
    
    # if this is a probeTrial, present the probe question 
    if ~(M.probetrial.isnull()[trialCNT]):        
        probe_response = event.BuilderKeyResponse()
        probe_response.status == NOT_STARTED
        probe.setAutoDraw(True)
        continueRoutine = True       
        while continueRoutine:            
            # *ins_response* updates
            if probe_response.status == NOT_STARTED:
                probe_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(probe_response.clock.reset)
                event.clearEvents(eventType='keyboard')
            if probe_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                if "escape" in theseKeys:
                    core.quit()
                if len(theseKeys) > 0:  # at least one key was pressed, end the routine
                    if probe_response.keys == []:  # then this was the first keypress
                        M.loc[trialCNT,'probeResp'] = theseKeys[0]  # just the first key pressed
                        M.loc[trialCNT,'probeRT']  = response.clock.getTime()
                    continueRoutine = False  # exit once a response is logged
            if continueRoutine:
                win.flip()
            else:
                break
        probe.setAutoDraw(False)
        routineTimer.reset()   
    # #####################################################

# end trial loop

# 0: [v,b,n,m] => defNew, probNew,probOld,defOld
# 1: [v,b,n,m] => defOld, probOld,probNew,defNew
if mem_SRmapping=='0':
    M.sbjResp.replace('v','defNew',inplace=True)
    M.sbjResp.replace('b','probNew',inplace=True)
    M.sbjResp.replace('n','probOld',inplace=True)
    M.sbjResp.replace('m','defOld',inplace=True)
else:
    M.sbjResp.replace('m','defNew',inplace=True)
    M.sbjResp.replace('n','probNw',inplace=True)
    M.sbjResp.replace('b','probOld',inplace=True)
    M.sbjResp.replace('v','defOld',inplace=True)
    
pd.DataFrame(data=M).to_csv(filename + '.csv')


# Thank you message, end of the task
Instruction.setText("Good job, please call the experimenter.")
ins_response = event.BuilderKeyResponse()
ins_response.status == NOT_STARTED
Instruction.setAutoDraw(True)
continueRoutine = True
while continueRoutine:
    if ins_response.status == NOT_STARTED:
        ins_response.status = STARTED
        win.callOnFlip(ins_response.clock.reset)
        event.clearEvents(eventType='keyboard')
    if ins_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        if "escape" in theseKeys:
            core.quit()
        if len(theseKeys) > 0:  # at least one key was pressed, end the routine
            continueRoutine = False    
        if continueRoutine:
            win.flip()
        else:
            break
Instruction.setAutoDraw(False)
routineTimer.reset()  # use this line, when the routine ends with subject making a key press


logging.flush()
win.close()
core.quit()
