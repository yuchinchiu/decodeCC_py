#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Filler task: 208 trials. Single-Single task practice and mixed task-switching
    
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

# include paths to bin in order to create a subject specific trial sequence
binDir = _thisDir + os.sep + u'bin'
sys.path.append(binDir)
from random import choice
from isspTrialGen import fillerGen


# Store info about the experiment session
expName = u'filler'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expName, expInfo['participant'])

logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


# Generate sbj trial sequences
SRmapping_full = [['g', 'j', 'g', 'j'], ['g', 'j', 'j', 'g'], ['j', 'g', 'j', 'g'], ['j', 'g', 'g', 'j']]

SRmapping_par = SRmapping_full[int(expInfo['participant'])%4][0:2]
SRmapping_mag = SRmapping_full[int(expInfo['participant'])%4][2:4]
# color assignment for odd/even and high/low task
tt = choice([0,1]) # if 0 => [red, blue], if 1 => [blue, red]
taskColorHex = ["#ff0000","#0000ff"] if tt==0 else ["#0000ff", "#ff0000"]
taskColorTxt = ["red", "blue"] if tt==0 else ["blue","red"]

M = fillerGen(SRmapping_par,SRmapping_mag, taskColorHex)
M.loc[:,'sbjResp']= None
M.loc[:,'sbjRT']  = np.nan
M.loc[:,'sbjACC'] = np.nan
iniTask = M.loc[0,'task']

provideFeedback = 1



# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=u'white', colorSpace='rgb',
    blendMode='avg', useFBO=True)

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

#YCC: load in instructions and tailor to each subject's SRmapping

lines = [line.rstrip('\n') for line in open(os.path.join(binDir, "fillerTaskIns.txt"))]
lines.append("Perform odd vs. even if numbers are in " + taskColorTxt[0])
if SRmapping_par[0]=='g':
    lines.append("Odd numbers:press "  + SRmapping_par[0].title() + "||  Even numbers:press " + SRmapping_par[1].title())
else:
    lines.append("Even numbers:press "  + SRmapping_par[1].title() + "||  Odd numbers:press " + SRmapping_par[0].title())
lines.append("Perform >5 vs. <5 if numbers are in " + taskColorTxt[1])

if SRmapping_mag[0]=='g':
    lines.append("Greater than 5:press "  + SRmapping_mag[0].title() + "||  Smaller than 5:press " + SRmapping_mag[1].title())
else:
    lines.append("Smaller than 5:press "  + SRmapping_mag[1].title() + "||  Greater than 5:press " + SRmapping_mag[0].title())
if iniTask[0]=='par':
    lines.append("You will start with doing just Odd/Even task first")
    secondTask='mag'
else:
    lines.append("You will start with greater/smaller than 5 task first")
    secondTask='par'
lines.append("")
lines.append("Memorize that task's rule and press space bar to begin")

# prepare the 2nd task Instruction
longins=''
if secondTask=='par':
    longins=longins+("Perform odd vs. even if numbers are in " + taskColorTxt[0])
    if SRmapping_par[0]=='g':
        longins=longins+("\nOdd numbers:press "  + SRmapping_par[0].title() + "||  Even numbers:press " + SRmapping_par[1].title())
    else:
        longins=longins+("\nEven numbers:press " + SRmapping_par[1].title() + "||  Odd numbers:press " + SRmapping_par[0].title())
else:
    longins=longins+("Perform >5 vs. <5 if numbers are in " + taskColorTxt[1])
    if SRmapping_mag[0]=='g':
        longins=longins+("\nGreater than 5:press "  + SRmapping_mag[0].title() + "||  Smaller than 5:press " + SRmapping_mag[1].title())
    else:
        longins=longins+("\nSmaller than 5:press "  + SRmapping_mag[1].title() + "||  Greater than 5:press " + SRmapping_mag[0].title())
longins=longins+("\n")
longins=longins+("\nRemember the rule and press space to begin")



# Initialize components for Routine "Ins"
InsClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text =None,
    font=u'Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
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
stim = visual.TextStim(win=win, name='stim',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Task Instructions #############################

ins_response = event.BuilderKeyResponse()
ins_response.status == NOT_STARTED
Instruction.status == NOT_STARTED
continueRoutine = True
# Instruction need to be update
while continueRoutine:

    if Instruction.status == NOT_STARTED:
        for t in range(len(lines)):
            if t==4 or t==5:
                insColor = taskColorHex[0]
            elif t==6 or t==7:
                insColor = taskColorTxt[1]
            else:
                insColor ='#000000'
            Instruction = visual.TextStim(win=win, name='Instruction', 
                              text=lines[t],
                              font=u'Arial',
                              pos=(0, .8 - t*.12), height=0.08, wrapWidth=2, ori=0, 
                              color=insColor, colorSpace='rgb', opacity=1,
                              depth=0.0);
            Instruction.draw()
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
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:
        break
routineTimer.reset()   # use this line, when the routine ends with subject making a key press

# ##################################################


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
    if trialCNT==16:
        Instruction.pos=(0,0)
        Instruction.setText(longins)
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
    
    if trialCNT ==32: 
        Instruction.pos=(0,0)
        Instruction.setText("Take a break here\nNext you will perform both tasks alternatively\nWhen ready press Space to continue")
        ins_response = event.BuilderKeyResponse()
        ins_response.status == NOT_STARTED
        Instruction.setAutoDraw(True)
        continueRoutine = True

        # -------Start Routine "Ins"-------
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
    stim.setColor(M.loc[trialCNT,'taskColor'], colorSpace='rgb')
    stim.setText(M.loc[trialCNT,'taskStim'])
    stim.setAutoDraw(True)	
    response = event.BuilderKeyResponse()
    response.status == NOT_STARTED
    response.keys = []
    
    routineTimer.add(1.000000)
    while continueRoutine and routineTimer.getTime() > 0:
        if response.status == NOT_STARTED:
            response.status = STARTED
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['g', 'j', 'escape'])
            if "escape" in theseKeys:
                core.quit()
            if len(theseKeys) > 0:  # at least one key was pressed				
                if response.keys == []:  # then this was the first keypress
                    M.loc[trialCNT,'sbjResp'] = theseKeys[0]  # just the first key pressed
                    M.loc[trialCNT,'sbjRT']   = response.clock.getTime()
                    # was this 'correct'?
                    if (M.loc[trialCNT,'sbjResp'] == str(M.loc[trialCNT,'corrAns'])) or (M.loc[trialCNT,'sbjResp']  == M.loc[trialCNT,'corrAns']):                        
                        M.loc[trialCNT,'sbjACC'] = 1
                        Instruction.setText("Correct")
                    else:
                        M.loc[trialCNT,'sbjACC'] = 0
                        Instruction.setText("Incorrect")
                    continueRoutine=False # end trial once a response was collected
                    
        if routineTimer.getTime() > 0:
            win.flip()
        else:
            break
    # end while
    stim.setAutoDraw(False)
    response.status = STOPPED
    if M.loc[trialCNT,'sbjResp']==None:     # if response.keys in ['', [], None]:  # No response was made
        M.loc[trialCNT,'sbjACC'] = 0
        Instruction.setText("No response")

    # provide trial feedback for practice #################    
    if provideFeedback == 1:       
        Instruction.pos=(0,0)
        Instruction.setAutoDraw(True)
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
        Instruction.setAutoDraw(False)
# end trial loop

pd.DataFrame(data=M).to_csv(filename + '.csv')

# End of task feedback #######################################
meanACC = np.ceil(M['sbjACC'].mean(skipna=True)*100)
Instruction.setText(u'Your mean accuracy was ' + str(meanACC) + '%\n\nYou have finished this part.\n\nPlease call the experimenter.')
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



logging.flush()
win.close()
core.quit()