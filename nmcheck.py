# -*- coding: utf-8 -*-

from anki import version as anki_version

old_anki = tuple(int(i) for i in anki_version.split(".")) < (2, 1, 20)

if not old_anki:
    from aqt.theme import theme_manager


def isnightmode():
    if old_anki:
        return False
    else:
        return theme_manager.night_mode
