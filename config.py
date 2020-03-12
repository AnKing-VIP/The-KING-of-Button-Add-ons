# -*- coding: utf-8 -*-
# Config code written by Arthur Milchior

from aqt import mw
from aqt.utils import showWarning



userOption = None

def _getUserOption():
    global userOption
    if userOption is None:
        userOption = mw.addonManager.getConfig(__name__)

def getUserOption(key = None, default = None):
    _getUserOption()
    if key is None:
        return userOption
    if key in userOption:
        val = userOption[key]
        if isinstance(val, str):
            return val.lower()
        else:
            return val
        return 
    else:
        return default


def writeConfig():
    mw.addonManager.writeConfig(__name__, userOption)

def update(_):
    global userOption, fromName
    userOption = None
    fromName = None

mw.addonManager.setConfigUpdatedAction(__name__, update)

fromName = None
def getFromName(name):
    global fromName
    if fromName is None:
        fromName = dict()
        for dic in getUserOption("columns"):
            fromName[dic["name"]]=dic
    return fromName.get(name)

def setUserOption(key, value):
    _getUserOption()
    userOption[key] = value
    writeConfig()
