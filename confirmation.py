# -*- coding: utf-8 -*-

"""
This is a modification of the Answer Confirmation add-on for Anki by Albert Lyubarsky
I do not take credit for any of the original code.

License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
"""


from anki.hooks import wrap
import aqt
from aqt.reviewer import Reviewer
from aqt.utils import tooltip
from aqt import utils
from aqt.qt import *
from .config import getUserOption
from .nmcheck import isnightmode


# Ancillary answer card method to show the tooltip when user answered a card.
# There have been compatibility issues with other add-ons, which override this method.

def answerCard_before(self, ease) :
    # get the ease which was selected
    answerButtons = self._answerButtonList()
    cB = [item for item in answerButtons if item[0] == ease] #cB: clickedButtons, should always be just one
    
    # load the display time
    time = getUserOption("confirmation time")
    

    # determine the position for the label #idk why the +7 offset is needed, but only this brings exact values
    if getUserOption("button width") == "S":
        x1 = -125 + 7 + getUserOption("confirmation x-offset")
        x2 = -50 + 7 + getUserOption("confirmation x-offset")
        x3 = 25 + 7 + getUserOption("confirmation x-offset")
        x4 = 100 + 7 + getUserOption("confirmation x-offset")
        width = 62
    elif getUserOption("button width") == "M":
        x1 = -162 + 7 + getUserOption("confirmation x-offset")
        x2 = -65.33 + 7 + getUserOption("confirmation x-offset")
        x3 = 31.33 + 7 + getUserOption("confirmation x-offset")
        x4 = 128 + 7 + getUserOption("confirmation x-offset")
        width = 87      
    elif getUserOption("button width") == "L":
        x1 = -224 + 7 + getUserOption("confirmation x-offset")
        x2 = -88.66 + 7 + getUserOption("confirmation x-offset")
        x3 = 46.66 + 7 + getUserOption("confirmation x-offset")
        x4 = 182 + 7 + getUserOption("confirmation x-offset")
        width = 125                

    if getUserOption("button height") == "S":   
        height = 26
        y = -36 - getUserOption("confirmation y-offset") 
    elif getUserOption("button height") == "M":   
        height = 41
        y = -51 - getUserOption("confirmation y-offset")  
    elif getUserOption("button height") == "L":   
        height = 61
        y = -71 - getUserOption("confirmation y-offset") 


    aw = aqt.mw.app.activeWindow() or aqt.mw
    xref = 0
    
    # apply values
    x1 = aw.mapToGlobal(QPoint(x1+int(round(aw.width()/2, 0)), 0)).x()
    x2 = aw.mapToGlobal(QPoint(x2+int(round(aw.width()/2, 0)), 0)).x()
    x3 = aw.mapToGlobal(QPoint(x3+int(round(aw.width()/2, 0)), 0)).x()
    x4 = aw.mapToGlobal(QPoint(x4+int(round(aw.width()/2, 0)), 0)).x()        
    xref = 1
    
    y = aw.mapToGlobal(QPoint(0, y+aw.height())).y()
    
    if (x1 < 0):
        x1 = 0
    if (y < 0):
        y = 0

    if isnightmode():
        AgainColor = getUserOption("Nightmode_AgainColor")
        HardColor = getUserOption("Nightmode_HardColor")
        GoodColor = getUserOption("Nightmode_GoodColor")
        EasyColor = getUserOption("Nightmode_EasyColor")
    else:
        AgainColor = getUserOption("AgainColor")
        HardColor = getUserOption("HardColor")
        GoodColor = getUserOption("GoodColor")
        EasyColor = getUserOption("EasyColor")                        

    #set font size options
    if getUserOption("button font size") == "S":
        FONTSIZE = ""
    elif getUserOption("button font size") == "M":
        FONTSIZE = "font-size: 16px;"
    elif getUserOption("button font size") == "L":
        FONTSIZE = "font-size: 20px;"

    # show tooltip in according color
    if len(cB) > 0 :
        # display the tooltip in an according color
        if (cB[0][1]=="Again" or "Again" in cB[0][1]):
            utils.tooltipWithColour(("<div style='color:#3a3a3a;%s'>Again</div>" % (FONTSIZE)), AgainColor, x=x1, y=y, xref=xref, period=time, width=width, height=height)
        elif (cB[0][1]=="Hard" or "Hard" in cB[0][1]):
            utils.tooltipWithColour(("<div style='color:#3a3a3a;%s'>Hard</div>" % (FONTSIZE)), HardColor, x=x2, y=y, xref=xref, period=time, width=width, height=height)
        elif (cB[0][1]=="Good" or "Good" in cB[0][1]):
            utils.tooltipWithColour(("<div style='color:#3a3a3a;%s'>Good</div>" % (FONTSIZE)), GoodColor, x=x3, y=y, xref=xref, period=time, width=width, height=height)
        elif (cB[0][1]=="Easy" or "Easy" in cB[0][1]):
            utils.tooltipWithColour(("<div style='color:#3a3a3a;%s'>Easy</div>" % (FONTSIZE)), EasyColor, x=x4, y=y, xref=xref, period=time, width=width, height=height)
        else:
            # default behavior for unforeseen cases
            tooltip(cB[0][1])


if getUserOption("confirmation", True):
    Reviewer._answerCard  = wrap(Reviewer._answerCard, answerCard_before, "before")
    Reviewer.CustomAnswerCard = answerCard_before
