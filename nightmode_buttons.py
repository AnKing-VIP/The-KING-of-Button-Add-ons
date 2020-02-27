# -*- coding: utf-8 -*-

# Created by: The AnKing
### Website: https://www.ankingmed.com  (Includes 40+ recommended add-ons)
### Youtube: https://www.youtube.com/theanking
### Instagram/Facebook: @ankingmed
### Patreon: https://www.patreon.com/ankingmed (Get individualized help)

#TODO add font-weight? 

from anki.hooks import wrap
from aqt import mw
from aqt.reviewer import Reviewer
import os
import shutil
from .config import getUserOption

# Nightmode
from anki import version as anki_version
old_anki = tuple(int(i) for i in anki_version.split(".")) < (2, 1, 20)
if old_anki:
    class Object():
        pass
    theme_manager = Object()
    theme_manager.night_mode = False
else:
    from aqt.theme import theme_manager

#Main config options
BORDERRADIUS = getUserOption("border radius")
if getUserOption("answer button width") == "Full":
    if getUserOption("button width") == "S":
        ANSWERWIDTH = 280
    elif getUserOption("button width") == "M":
        ANSWERWIDTH = 375
    elif getUserOption("button width") == "L":
        ANSWERWIDTH = 530
else:
    ANSWERWIDTH = 120

if getUserOption("button width") == "S":
    WIDTH = 42
elif getUserOption("button width") == "M":
    WIDTH = 82
elif getUserOption("button width") == "L":
    WIDTH = 122

if getUserOption("button height") == "S":
    HEIGHT = 25
elif getUserOption("button height") == "M":
    HEIGHT = 40
elif getUserOption("button height") == "L":
    HEIGHT = 60

if getUserOption("button color") == "colors":
    if theme_manager.night_mode:
        AGAINBUTTON = getUserOption("Nightmode_AgainColor")
        HARDBUTTON = getUserOption("Nightmode_HardColor")
        GOODBUTTON = getUserOption("Nightmode_GoodColor")
        EASYBUTTON = getUserOption("Nightmode_EasyColor")
    else:
        AGAINBUTTON = getUserOption("AgainColor")
        HARDBUTTON = getUserOption("HardColor")
        GOODBUTTON = getUserOption("GoodColor")
        EASYBUTTON = getUserOption("EasyColor")            
else:
    if theme_manager.night_mode:
        AGAINBUTTON = "inherit"
        HARDBUTTON = "inherit"
        GOODBUTTON = "inherit"
        EASYBUTTON = "inherit"
    else:
        AGAINBUTTON = "#fff"
        HARDBUTTON = "#fff"
        GOODBUTTON = "#fff"
        EASYBUTTON = "#fff"        
#add hover effects
if getUserOption("button color") == "hover":
    if theme_manager.night_mode:
        AGAINHOVER = getUserOption("Nightmode_AgainColor")
        HARDHOVER = getUserOption("Nightmode_HardColor")
        GOODHOVER = getUserOption("Nightmode_GoodColor")
        EASYHOVER = getUserOption("Nightmode_EasyColor")
        TEXT = "#3a3a3a"
        BACKGROUND = "#c0c0c0"   
    else:
        AGAINHOVER = getUserOption("AgainColor")
        HARDHOVER = getUserOption("HardColor")
        GOODHOVER = getUserOption("GoodColor")
        EASYHOVER = getUserOption("EasyColor") 
        TEXT = "#c0c0c0"
        BACKGROUND = "#3a3a3a"         
                
    HOVEREFFECT = ('''
    /* the "Good" button */  
    #defease:hover {
        background-color: %s!important;
        color: #3a3a3a!important;
    }    
    button[onclick*="ease1"]:not(#defease):hover {
        background-color: %s!important;
        color: #3a3a3a!important;
    }   
    button[onclick*="ease2"]:not(#defease):hover {
        background-color: %s!important;
        color: #3a3a3a!important;        
    }  
    button[onclick*="ease3"]:not(#defease):hover,
    button[onclick*="ease4"]:not(#defease):hover {
        background-color: %s!important;
        color: #3a3a3a!important;
    }  
    /* the "Edit", "More" and "Answer" buttons */
    button[onclick*="edit"]:hover, 
    button[onclick*="more"]:hover,
    #ansbut:hover {
        background-color: %s!important;
        color: %s!important;
    }    
    ''' % (GOODHOVER, AGAINHOVER, HARDHOVER, EASYHOVER, BACKGROUND, TEXT))
else:
    HOVEREFFECT = ""

if getUserOption("button font size") == "S":
    FONTSIZE = ""
elif getUserOption("button font size") == "M":
    FONTSIZE = '''
    #defease, #ansbut,
    button[onclick*="ease1"]:not(#defease), 
    button[onclick*="ease2"]:not(#defease),
    button[onclick*="ease3"]:not(#defease),
    button[onclick*="ease4"]:not(#defease), 
    button[onclick*="edit"],
    button[onclick*="more"] { font-size: 16px; } 
    '''
elif getUserOption("button font size") == "L":
    FONTSIZE = '''
    #defease, #ansbut,
    button[onclick*="ease1"]:not(#defease), 
    button[onclick*="ease2"]:not(#defease),
    button[onclick*="ease3"]:not(#defease),
    button[onclick*="ease4"]:not(#defease), 
    button[onclick*="edit"],
    button[onclick*="more"] { font-size: 20px; } 
    '''    

#add colors to the text and black for 'colors' mode
if getUserOption("button color") != "colors":
    if theme_manager.night_mode:
        AGAINCOLOR = getUserOption("Nightmode_AgainColor")
        HARDCOLOR = getUserOption("Nightmode_HardColor")
        GOODCOLOR = getUserOption("Nightmode_GoodColor")
        EASYCOLOR = getUserOption("Nightmode_EasyColor")      
    else:
        AGAINCOLOR = getUserOption("AgainColor")
        HARDCOLOR = getUserOption("HardColor")
        GOODCOLOR = getUserOption("GoodColor")
        EASYCOLOR = getUserOption("EasyColor")            
    CARDCOLOR = ('''
    /* the "Good" button */
    #defease {
        color: %s!important;
    }      
    /* the "Again" button */
    button[onclick*="ease1"]:not(#defease) {
        color: %s!important;
    }    
    /* the "Hard" button */
    button[onclick*="ease2"]:not(#defease) {
        color: %s!important;  
    }
    /* the "Easy" button */
    button[onclick*="ease3"]:not(#defease),
    button[onclick*="ease4"]:not(#defease) {
        color: %s!important;
    }                     
    ''' % (GOODCOLOR, AGAINCOLOR, HARDCOLOR, EASYCOLOR))
else:
    CARDCOLOR = '''
    /* the "Good" button */
    #defease {
        color: #3a3a3a!important;
    }      
    /* the "Again" button */
    button[onclick*="ease1"]:not(#defease) {
        color: #3a3a3a!important;
    }    
    /* the "Hard" button */
    button[onclick*="ease2"]:not(#defease) {
        color: #3a3a3a!important; 
    }           
    /* the "Easy" button */
    button[onclick*="ease3"]:not(#defease),
    button[onclick*="ease4"]:not(#defease) {
        color: #3a3a3a!important;
    }      
    '''

#main css
bottom_buttons_css = ('''
/* All buttons at the bottom of the review screen
   (including the "Edit" and "More" button) */
button {
    height: %spx;
    border: solid 1px rgba(0, 0, 0, 0.2);
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
    background-color: #3a3a3a!important;
}

/* the "Show Answer" button */
#ansbut {
    width: %spx !important;
    text-align: center;
}
/* All rating buttons */
#middle button {
    width: %spx;
    text-align: center !important;
}

/* the "Good" button */
#defease {
    background-color: %s!important;
    text-align: center;
}

/* the "Again" button */
button[onclick*="ease1"]:not(#defease) {
    text-align: center;
    background-color: %s!important;
    text-align: center;
}

/* the "Hard" button */
button[onclick*="ease2"]:not(#defease) {
    background-color: %s!important;
    text-align: center;
}

/* the "Easy" button */
button[onclick*="ease3"]:not(#defease),
button[onclick*="ease4"]:not(#defease) {
    background-color: %s!important;
    text-align: center;
}

/* the "Edit" button */
button[onclick*="edit"] {
    text-align: center;

}

/* the "More" button */
button[onclick*="more"] {
    text-align: center;
}

%s
%s
%s
''' % (HEIGHT, BORDERRADIUS, ANSWERWIDTH, WIDTH, GOODBUTTON, AGAINBUTTON, HARDBUTTON, EASYBUTTON, HOVEREFFECT, CARDCOLOR, FONTSIZE))



# add css
js_append_css = f"$('head').append(`<style>{bottom_buttons_css}</style>`);"


def reviewer_initWeb_wrapper(*args, **kwargs):
    mw.reviewer.bottom.web.eval(js_append_css)


Reviewer._initWeb = wrap(Reviewer._initWeb, reviewer_initWeb_wrapper)
