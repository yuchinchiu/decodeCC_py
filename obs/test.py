#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.1),
    on July 20, 2017, at 11:13
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# YCC: include paths to bin in order to create a subject specific trial sequence
binDir   = _thisDir + os.sep + u'bin'
sys.path.append(binDir)
from trialGen import trialGen
from random import choice
respMapping      = choice([[1,2],[2,1]])  # if [1,2] = press g for natural, press j for manmade
SRkey = np.where(np.array(respMapping)==1,'g','j')

trialGen(respMapping)   # output 3 csv for later use 

# Store info about the experiment session
expName = u'stroop_practice'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_' % (expName, expInfo['participant'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

taskInstruction = u'If the object is natural, press ' + SRkey[0].title()+ '\n\nIf the object is man-made, press ' + SRkey[1].title()

# Initialize components for Routine "Ins"
InsClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text = taskInstruction,
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

# Initialize components for Routine "blockIns"
blockInsClock = core.Clock()
bkIns = visual.TextStim(win=win, name='bkIns',
    text='default text',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
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

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Ins"-------

# update component parameters for each repeat
ins_response = event.BuilderKeyResponse()
ins_response.status == NOT_STARTED
Instruction.setAutoDraw(True)
continueRoutine = True

# -------Start Routine "Ins"-------
while continueRoutine:
    # *ins_response* updates
    if ins_response.status == NOT_STARTED:
        ins_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ins_response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ins_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed, end the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins"-------
Instruction.setAutoDraw(False)
# the Routine "Ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials_practice.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

trialCNT =-1

for thisTrial in trials:
    trialCNT = trialCNT+1
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [blank]
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if t >= 0.0 and blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank.tStart = t
            blank.frameNStart = frameN  # exact frame index
            blank.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank.status == STARTED and t >= frameRemains:
            blank.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # Break #####################################################
    if trialCNT == 80:    # total =160
        # ------Prepare to start Routine "Ins"-------
        t = 0
        InsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        Instruction.setText(breakMsg)
        ins_response = event.BuilderKeyResponse()
        # keep track of which components have finished
        InsComponents = [Instruction, ins_response]
        for thisComponent in InsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Ins"-------
        while continueRoutine:
            # get current time
            t = InsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Instruction* updates
            if t >= 0.0 and Instruction.status == NOT_STARTED:
                # keep track of start time/frame for later
                Instruction.tStart = t
                Instruction.frameNStart = frameN  # exact frame index
                Instruction.setAutoDraw(True)
            
            # *ins_response* updates
            if t >= 0.0 and ins_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                ins_response.tStart = t
                ins_response.frameNStart = frameN  # exact frame index
                ins_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(ins_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if ins_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if ins_response.keys == []:  # then this was the first keypress                
                        ins_response.keys = theseKeys[0]  # just the first key pressed
                        ins_response.rt = ins_response.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Ins"-------
        for thisComponent in InsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Ins" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
    # #####################################################
    
    # only show blockIns every 10 trials
    
    if trialCNT%10 == 0:
        # ------Prepare to start Routine "blockIns"-------
        t = 0
        blockInsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        bkIns.setText(blockType)
        # keep track of which components have finished
        blockInsComponents = [bkIns]
        for thisComponent in blockInsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
    
        # -------Start Routine "blockIns"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blockInsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame        
            
            # *bkIns* updates
            if t >= 0.0 and bkIns.status == NOT_STARTED:
                # keep track of start time/frame for later
                bkIns.tStart = t
                bkIns.frameNStart = frameN  # exact frame index
                bkIns.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if bkIns.status == STARTED and t >= frameRemains:
                bkIns.setAutoDraw(False)
        
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockInsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
        
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
        
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
    
        # -------Ending Routine "blockIns"-------
        for thisComponent in blockInsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)


    # #####################################################
    
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    target.setImage(targetStim)
    distractor.setSound(distractorStim, secs=1.0)
    response = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [target, distractor, response]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if t >= 0.0 and target.status == NOT_STARTED:
            # keep track of start time/frame for later
            target.tStart = t
            target.frameNStart = frameN  # exact frame index
            target.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if target.status == STARTED and t >= frameRemains:
            target.setAutoDraw(False)
        # start/stop distractor
        if t >= 0.0 and distractor.status == NOT_STARTED:
            # keep track of start time/frame for later
            distractor.tStart = t
            distractor.frameNStart = frameN  # exact frame index
            distractor.play()  # start the sound (it finishes automatically)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if distractor.status == STARTED and t >= frameRemains:
            distractor.stop()  # stop the sound (if longer than duration)
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response.status == STARTED and t >= frameRemains:
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['g', 'j', 'escape'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if response.keys == []:  # then this was the first keypress
                    response.keys = theseKeys[0]  # just the first key pressed
                    response.rt = response.clock.getTime()
                    # was this 'correct'?
                    if (response.keys == str(corrAns)) or (response.keys == corrAns):
                        response.corr = 1
                    else:
                        response.corr = 0
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    distractor.stop()  # ensure sound has stopped at end of routine
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response.corr = 1  # correct non-response
        else:
           response.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('response.keys',response.keys)
    trials.addData('response.corr', response.corr)
    if response.keys != None:  # we had a response
        trials.addData('response.rt', response.rt)
    thisExp.nextEntry()







# ------Prepare to start Routine "Feedback"-------
t = 0
InsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

Instruction.setText(u'Your mean accuracy was ' + str(np.ceil(np.mean(acc)*100)) + '%\n\nYou have finished the practice.\n\nPlease call the experimenter.')
ins_response = event.BuilderKeyResponse()
# keep track of which components have finished
InsComponents = [Instruction, ins_response]
for thisComponent in InsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Ins"-------
while continueRoutine:
    # get current time
    t = InsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instruction* updates
    if t >= 0.0 and Instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruction.tStart = t
        Instruction.frameNStart = frameN  # exact frame index
        Instruction.setAutoDraw(True)
    
    # *ins_response* updates
    if t >= 0.0 and ins_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        ins_response.tStart = t
        ins_response.frameNStart = frameN  # exact frame index
        ins_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ins_response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ins_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            if ins_response.keys == []:  # then this was the first keypress                
                ins_response.keys = theseKeys[0]  # just the first key pressed
                ins_response.rt = ins_response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ins"-------
for thisComponent in InsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
#thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
