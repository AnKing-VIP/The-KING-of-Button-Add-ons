# OriginalAuthor: C9HDN

# Modified by: The AnKing
### Website: www.ankingmed.com  (Includes 40+ recommended add-ons)
### Youtube: www.youtube.com/theanking
### Instagram/Facebook: @ankingmed
### Patreon: www.patreon.com/ankingmed (Get individualized help)

#-------------Configuration------------------
from aqt import mw
if getattr(getattr(mw, "addonManager", None), "getConfig", None): #Anki 2.1
    config = mw.addonManager.getConfig(__name__)
else:
    #----- Modify here (Anki 2.0) ------
    config = dict(AgainColor = '#ff6961', HardColor = '#ffb861', GoodColor = '#61ffb8', EasyColor = '#61a8ff')


# Get reviewer class
from aqt.reviewer import Reviewer

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


# Replace _answerButtonList method
def answerButtonList(self):
    if theme_manager.night_mode:
        AgainCustom = "<font color='"         + config['Nightmode_AgainColor'] + "'>"
        HardCustom = "<font color='"         + config['Nightmode_HardColor'] + "'>"
        GoodCustom = "<font color='"         + config['Nightmode_GoodColor'] + "'>"
        EasyCustom = "<font color='"         + config['Nightmode_EasyColor'] + "'>"   
    else:             
        AgainCustom = "<font color='"         + config['AgainColor'] + "'>"
        HardCustom = "<font color='"         + config['HardColor'] + "'>"
        GoodCustom = "<font color='"         + config['GoodColor'] + "'>"
        EasyCustom = "<font color='"         + config['EasyColor'] + "'>"  
        
    l = ((1, AgainCustom + _("Again") + "</font>"),)
    cnt = self.mw.col.sched.answerButtons(self.card)
    if cnt == 2:
        return l + ((2, GoodCustom + _("Good") + "</font>"),)
    elif cnt == 3:
        return l + ((2, GoodCustom + _("Good") + "</font>"), (3, EasyCustom + _("Easy") + "</font>"))
    else:
        return l + ((2, HardCustom + _("Hard") + "</font>"), (3, GoodCustom + _("Good") + "</font>"), (4, EasyCustom + _("Easy") + "</font>"))

Reviewer._answerButtonList = answerButtonList