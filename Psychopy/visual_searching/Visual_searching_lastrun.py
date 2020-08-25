#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.2),
    on August 25, 2020, at 18:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.2'
expName = 'Visual_searching'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='F:\\psychopy\\visual_seaching\\Visual_searching_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instru_text = visual.TextStim(win=win, name='instru_text',
    text='Click the hexagon as quickly as possible. press the mouse button to start.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instru_mouse = event.Mouse(win=win)
x, y = [None, None]
instru_mouse.mouseClock = core.Clock()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
y_pos = [-400,-300,-200,-100,0,100,200,300,400]
x_pos = [-400,-300,-200,-100,0,100,200,300,400]
target = visual.Polygon(
    win=win, name='target',units='pix', 
    edges=6, size=(20, 20),
    ori=30, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
distract_1 = visual.Polygon(
    win=win, name='distract_1',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
distract_2 = visual.Polygon(
    win=win, name='distract_2',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
distract_3 = visual.Polygon(
    win=win, name='distract_3',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
distract_4 = visual.Polygon(
    win=win, name='distract_4',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-5.0, interpolate=True)
distract_5 = visual.Polygon(
    win=win, name='distract_5',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-6.0, interpolate=True)
distract_6 = visual.Polygon(
    win=win, name='distract_6',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-7.0, interpolate=True)
distract_7 = visual.Polygon(
    win=win, name='distract_7',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)
distract_8 = visual.Polygon(
    win=win, name='distract_8',units='pix', 
    edges=5, size=(20, 20),
    ori=0, pos=[0,0],
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1.0, depth=-9.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('search_conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the instru_mouse
    gotValidClick = False  # until a click is received
    if trials.thisN % 5 != 0 :
        continueRoutine = False
    # keep track of which components have finished
    instrComponents = [instru_text, instru_mouse]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instru_text* updates
        if instru_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instru_text.frameNStart = frameN  # exact frame index
            instru_text.tStart = t  # local t and not account for scr refresh
            instru_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instru_text, 'tStartRefresh')  # time at next scr refresh
            instru_text.setAutoDraw(True)
        # *instru_mouse* updates
        if instru_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instru_mouse.frameNStart = frameN  # exact frame index
            instru_mouse.tStart = t  # local t and not account for scr refresh
            instru_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instru_mouse, 'tStartRefresh')  # time at next scr refresh
            instru_mouse.status = STARTED
            instru_mouse.mouseClock.reset()
            prevButtonState = instru_mouse.getPressed()  # if button is down already this ISN'T a new click
        if instru_mouse.status == STARTED:  # only update if started and not finished!
            buttons = instru_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('instru_text.started', instru_text.tStartRefresh)
    trials.addData('instru_text.stopped', instru_text.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('instru_mouse.started', instru_mouse.tStart)
    trials.addData('instru_mouse.stopped', instru_mouse.tStop)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [polygon]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon.started', polygon.tStartRefresh)
    trials.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    shuffle(x_pos)
    shuffle(y_pos)
    target.setPos((x_pos[0],y_pos[0]))
    target.setFillColor(target_color)
    distract_1.setOpacity(opacity_1)
    distract_1.setPos((x_pos[1], y_pos[1]))
    distract_2.setOpacity(opacity_2)
    distract_2.setPos((x_pos[2], y_pos[2]))
    distract_3.setOpacity(opacity_3)
    distract_3.setPos((x_pos[3], y_pos[3]))
    distract_4.setOpacity(opacity_4)
    distract_4.setPos((x_pos[4], y_pos[4]))
    distract_5.setOpacity(opacity_5)
    distract_5.setPos((x_pos[5], y_pos[5]))
    distract_6.setOpacity(opacity_6)
    distract_6.setPos((x_pos[6], y_pos[6]))
    distract_7.setOpacity(opacity_7)
    distract_7.setPos((x_pos[7], y_pos[7]))
    distract_8.setOpacity(opacity_8)
    distract_8.setPos((x_pos[8], y_pos[8]))
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    mouse.clicked_pos = []
    gotValidClick = False  # until a click is received
    mouse.mouseClock.reset()
    # keep track of which components have finished
    trialComponents = [target, distract_1, distract_2, distract_3, distract_4, distract_5, distract_6, distract_7, distract_8, mouse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        
        # *distract_1* updates
        if distract_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_1.frameNStart = frameN  # exact frame index
            distract_1.tStart = t  # local t and not account for scr refresh
            distract_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_1, 'tStartRefresh')  # time at next scr refresh
            distract_1.setAutoDraw(True)
        
        # *distract_2* updates
        if distract_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_2.frameNStart = frameN  # exact frame index
            distract_2.tStart = t  # local t and not account for scr refresh
            distract_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_2, 'tStartRefresh')  # time at next scr refresh
            distract_2.setAutoDraw(True)
        
        # *distract_3* updates
        if distract_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_3.frameNStart = frameN  # exact frame index
            distract_3.tStart = t  # local t and not account for scr refresh
            distract_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_3, 'tStartRefresh')  # time at next scr refresh
            distract_3.setAutoDraw(True)
        
        # *distract_4* updates
        if distract_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_4.frameNStart = frameN  # exact frame index
            distract_4.tStart = t  # local t and not account for scr refresh
            distract_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_4, 'tStartRefresh')  # time at next scr refresh
            distract_4.setAutoDraw(True)
        
        # *distract_5* updates
        if distract_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_5.frameNStart = frameN  # exact frame index
            distract_5.tStart = t  # local t and not account for scr refresh
            distract_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_5, 'tStartRefresh')  # time at next scr refresh
            distract_5.setAutoDraw(True)
        
        # *distract_6* updates
        if distract_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_6.frameNStart = frameN  # exact frame index
            distract_6.tStart = t  # local t and not account for scr refresh
            distract_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_6, 'tStartRefresh')  # time at next scr refresh
            distract_6.setAutoDraw(True)
        
        # *distract_7* updates
        if distract_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_7.frameNStart = frameN  # exact frame index
            distract_7.tStart = t  # local t and not account for scr refresh
            distract_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_7, 'tStartRefresh')  # time at next scr refresh
            distract_7.setAutoDraw(True)
        
        # *distract_8* updates
        if distract_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            distract_8.frameNStart = frameN  # exact frame index
            distract_8.tStart = t  # local t and not account for scr refresh
            distract_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distract_8, 'tStartRefresh')  # time at next scr refresh
            distract_8.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                            mouse.clicked_pos.append(obj.pos)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('target.started', target.tStartRefresh)
    trials.addData('target.stopped', target.tStopRefresh)
    trials.addData('distract_1.started', distract_1.tStartRefresh)
    trials.addData('distract_1.stopped', distract_1.tStopRefresh)
    trials.addData('distract_2.started', distract_2.tStartRefresh)
    trials.addData('distract_2.stopped', distract_2.tStopRefresh)
    trials.addData('distract_3.started', distract_3.tStartRefresh)
    trials.addData('distract_3.stopped', distract_3.tStopRefresh)
    trials.addData('distract_4.started', distract_4.tStartRefresh)
    trials.addData('distract_4.stopped', distract_4.tStopRefresh)
    trials.addData('distract_5.started', distract_5.tStartRefresh)
    trials.addData('distract_5.stopped', distract_5.tStopRefresh)
    trials.addData('distract_6.started', distract_6.tStartRefresh)
    trials.addData('distract_6.stopped', distract_6.tStopRefresh)
    trials.addData('distract_7.started', distract_7.tStartRefresh)
    trials.addData('distract_7.stopped', distract_7.tStopRefresh)
    trials.addData('distract_8.started', distract_8.tStartRefresh)
    trials.addData('distract_8.stopped', distract_8.tStopRefresh)
    # store data for trials (TrialHandler)
    if len(mouse.x): trials.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): trials.addData('mouse.clicked_name', mouse.clicked_name[0])
    if len(mouse.clicked_pos): trials.addData('mouse.clicked_pos', mouse.clicked_pos[0])
    trials.addData('mouse.started', mouse.tStart)
    trials.addData('mouse.stopped', mouse.tStop)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
