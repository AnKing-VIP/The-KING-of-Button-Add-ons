# -*- coding: utf-8 -*-

from anki.utils import pointVersion

old_anki = pointVersion() < 20

if not old_anki:
    from aqt.theme import theme_manager


def isnightmode():
    if old_anki:
        return False
    else:
        return theme_manager.night_mode
