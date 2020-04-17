# -*- coding: utf-8 -*-

from aqt.toolbar import BottomBar
import aqt.editor
from aqt.editor import Editor


from .config import getUserOption
from .nmcheck import isnightmode


BORDERRADIUS = getUserOption("border radius")


#add hover effects
if getUserOption("button color") == "hover":
    if isnightmode():
        TEXT = "#3a3a3a"
        BACKGROUND = "#c0c0c0"   
    else:
        TEXT = "#c0c0c0"
        BACKGROUND = "#3a3a3a"   
    HOVEREFFECT = ('''
    /* the "Edit", "More" and "Answer" buttons */
    button:hover {
        background-color: %s!important;
        color: %s!important;
    }    
    ''' % (BACKGROUND, TEXT))
else:
    HOVEREFFECT = ""        


if getUserOption("style main screen buttons", True):
    BottomBar._centerBody = (""" 
    <style> 
    /* All buttons at the bottom of the review screen
    (including the "Edit" and "More" button) */
    button {
        height: 22px;
        border: solid 1px rgba(100, 100, 100, 0.2)!important;
        border-top: solid 0.5px #878787!important;
        border-radius: %spx!important;
        -webkit-appearance: none;
        cursor: pointer;
        margin: 2px 6px 6px !important;
        box-shadow: 0px 0px 1.5px .2px #000000!important;
        -webkit-box-shadow: 0px 0px 1.5px .2px #000000!important;
    }
    .nightMode button {
        box-shadow: 0px 0px 2.5px .5px #000000!important;
        -webkit-box-shadow: 0px 0px 2.5px .5px #000000!important;
        background: #3a3a3a!important;
    }
    %s
    </style> 
    """ % (BORDERRADIUS, HOVEREFFECT)) + BottomBar._centerBody 



## If you want to style the "field" and "card" buttons in the editor, 
## delete the ''' at the beginning and end of this section
'''
aqt.editor._html += 
(""" 
    <style> 
    /* All buttons at the bottom of the review screen
    (including the "Edit" and "More" button) */
    button {
        height: %spx;
        border: solid 1px rgba(0, 0, 0, 0.2);
        border-radius: %spx!important;
        -webkit-appearance: none;
        outline: none;
        cursor: pointer;
        margin: 2px 6px 6px !important;
        box-shadow: 0px 0px 1.5px .2px #000000!important;
        -webkit-box-shadow: 0px 0px 1.5px .2px #000000!important;
    }
    .nightMode button {
        box-shadow: 0px 0px 2.5px .5px #000000!important;
        -webkit-box-shadow: 0px 0px 2.5px .5px #000000!important;
        background-color: #3a3a3a!important;
    }
    </style> 
    """ % (HEIGHT, BORDERRADIUS))
'''