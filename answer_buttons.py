# -*- coding: utf-8 -*-
# refined thanks to ijgnord

#TODO add font-weight? 

from anki.hooks import wrap
from aqt import mw
from aqt.reviewer import Reviewer

from .config import getUserOption
from .nmcheck import isnightmode


#Main config options
BORDERRADIUS = getUserOption("border radius")


if getUserOption("answer button width") == "full":
    if getUserOption("button width") == "l":
        ANSWERWIDTH = 530
    elif getUserOption("button width") == "m":
        ANSWERWIDTH = 375
    else:
        ANSWERWIDTH = 280
else:
    ANSWERWIDTH = 120


if getUserOption("button width") == "l":
    WIDTH = 122
elif getUserOption("button width") == "m":
    WIDTH = 82
else:  # getUserOption("button width") == "s" OR other cases
    WIDTH = 42


if getUserOption("button height") == "l":
    HEIGHT = 60
elif getUserOption("button height") == "m":
    HEIGHT = 40
else:  #  getUserOption("button height") == "s" OR other cases
    HEIGHT = 25


# set background color of buttons
if getUserOption("button color") == "colors":
    if isnightmode():
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
    if isnightmode():
        AGAINBUTTON = HARDBUTTON = GOODBUTTON = EASYBUTTON = "inherit"
    else:
        AGAINBUTTON = HARDBUTTON = GOODBUTTON = EASYBUTTON = "#fff"


# add hover effects
HOVEREFFECT = ""
if getUserOption("button color") == "hover":
    if isnightmode():
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
                
    HOVEREFFECT = '''
    /* the "Good" button */  
    #defease:hover {
        background-color: %(GOODHOVER)s!important;
        color: #3a3a3a!important;
    }    
    button[onclick*="ease1"]:not(#defease):hover {
        background-color: %(AGAINHOVER)s!important;
        color: #3a3a3a!important;
    }   
    button[onclick*="ease2"]:not(#defease):hover {
        background-color: %(HARDHOVER)s!important;
        color: #3a3a3a!important;        
    }  
    button[onclick*="ease3"]:not(#defease):hover,
    button[onclick*="ease4"]:not(#defease):hover {
        background-color: %(EASYHOVER)s!important;
        color: #3a3a3a!important;
    }  
    /* the "Edit", "More" and "Answer" buttons */
    button[onclick*="edit"]:hover, 
    button[onclick*="more"]:hover,
    #ansbut:hover {
        background-color: %(BACKGROUND)s!important;
        color: %(TEXT)s!important;
    }    
    ''' % {
        "GOODHOVER": GOODHOVER,
        "AGAINHOVER": AGAINHOVER,
        "HARDHOVER": HARDHOVER,
        "EASYHOVER": EASYHOVER,
        "BACKGROUND": BACKGROUND,
        "TEXT": TEXT,
    }


customfontsize = '''
#defease, #ansbut,
button[onclick*="ease1"]:not(#defease), 
button[onclick*="ease2"]:not(#defease),
button[onclick*="ease3"]:not(#defease),
button[onclick*="ease4"]:not(#defease), 
button[onclick*="edit"],
button[onclick*="more"] { font-size: %spx; } 
'''
if getUserOption("button font size") == "l":
    FONTSIZE = customfontsize % "20"
elif getUserOption("button font size") == "m":
    FONTSIZE = customfontsize % "16"
if getUserOption("button font size") == "s":
    FONTSIZE = ""


#set font color (when background is colored the font must be black)
if getUserOption("button color") == "colors":
    GOODCOLOR = AGAINCOLOR = HARDCOLOR = EASYCOLOR = "#3a3a3a"
else:
    if isnightmode():
        AGAINCOLOR = getUserOption("Nightmode_AgainColor")
        HARDCOLOR = getUserOption("Nightmode_HardColor")
        GOODCOLOR = getUserOption("Nightmode_GoodColor")
        EASYCOLOR = getUserOption("Nightmode_EasyColor")
    else:
        AGAINCOLOR = getUserOption("AgainColor")
        HARDCOLOR = getUserOption("HardColor")
        GOODCOLOR = getUserOption("GoodColor")
        EASYCOLOR = getUserOption("EasyColor")

if getUserOption("outline") == "no":
    OUTLINE = "outline:none;"
else:
    OUTLINE = ""    

#main css
bottom_buttons_css = """
/* All buttons at the bottom of the review screen
   (including the "Edit" and "More" button) */
button {
    height: %(HEIGHT)spx;
    border: solid 1px rgba(100, 100, 100, 0.2)!important;
    border-top: solid 0.5px #878787!important;  
    border-radius: %(BORDERRADIUS)spx !important;
    -webkit-appearance: none;
    cursor: pointer;
    margin: 2px 6px 6px !important;
    box-shadow: 0px 0px 1.5px .2px #000000 !important;
    -webkit-box-shadow: 0px 0px 1.5px .2px #000000 !important;
    %(OUTLINE)s
}
.nightMode button {
    box-shadow: 0px 0px 1.5px .5px #000000 !important;
    -webkit-box-shadow: 0px 0px 2.5px .5px #000000 !important;
    background: #3a3a3a !important;
}

/* the "Show Answer" button */
#ansbut {
    width: %(ANSWERWIDTH)spx !important;
    text-align: center;
}
/* All rating buttons */
#middle button {
    width: %(WIDTH)spx;
    text-align: center !important;
}

/* the "Good" button */
#defease {
    color: %(GOODCOLOR)s !important;
    background: %(GOODBUTTON)s !important;
    text-align: center;
}

/* the "Again" button */
button[onclick*="ease1"]:not(#defease) {
    color: %(AGAINCOLOR)s !important;
    background: %(AGAINBUTTON)s !important;
    text-align: center;
}

/* the "Hard" button */
button[onclick*="ease2"]:not(#defease) {
    color: %(HARDCOLOR)s !important;
    background: %(HARDBUTTON)s !important;
    text-align: center;
}

/* the "Easy" button */
button[onclick*="ease3"]:not(#defease),
button[onclick*="ease4"]:not(#defease) {
    color: %(EASYCOLOR)s !important;
    background: %(EASYBUTTON)s !important;
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

%(HOVEREFFECT)s
%(FONTSIZE)s
""" % {
    "HEIGHT": HEIGHT,
    "BORDERRADIUS": BORDERRADIUS,
    "OUTLINE": OUTLINE,
    "ANSWERWIDTH": ANSWERWIDTH,
    "WIDTH": WIDTH,
    "GOODCOLOR": GOODCOLOR,
    "AGAINCOLOR": AGAINCOLOR,
    "HARDCOLOR": HARDCOLOR,
    "EASYCOLOR": EASYCOLOR,
    "GOODBUTTON": GOODBUTTON,
    "AGAINBUTTON": AGAINBUTTON,
    "HARDBUTTON": HARDBUTTON,
    "EASYBUTTON": EASYBUTTON,
    "HOVEREFFECT": HOVEREFFECT,
    "FONTSIZE": FONTSIZE,
}



# add css
js_append_css = f"$('head').append(`<style>{bottom_buttons_css}</style>`);"

def reviewer_initWeb_wrapper(func):
    def _initWeb(*args, **kwargs):
        func(*args, **kwargs)
        mw.reviewer.bottom.web.eval(js_append_css)
    return _initWeb

mw.reviewer._initWeb = reviewer_initWeb_wrapper(mw.reviewer._initWeb)
