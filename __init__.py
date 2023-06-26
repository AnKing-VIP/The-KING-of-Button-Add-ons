# -*- coding: utf-8 -*-

# Created by: The AnKing
### Website: https://www.ankingmed.com  (Includes 40+ recommended add-ons)
### Youtube: https://www.youtube.com/theanking
### Instagram/Facebook: @ankingmed
### Patreon: https://www.patreon.com/ankingmed (Get individualized help)

import os

from aqt import mw

from . import answer_buttons
from . import bottom_main_buttons
from . import custom_tooltip
from . import confirmation

def replace_module_name_in_config_help():
    """Replace static add-on module name in config.md with the actual name"""

    path = os.path.join(mw.addonManager.addonsFolder(
        mw.addonManager.addonFromModule(__name__)), "config.md")
    with open(path, encoding="utf-8") as f:
        contents = f.read()
        contents = contents.replace(
            "/_addons/374005964", f"/_addons/{mw.addonManager.addonFromModule(__name__)}")
        return contents


# Make images available to the config help webview
mw.addonManager.setWebExports(__name__, r"AnKing/.*")
if hasattr(mw.addonManager, 'set_config_help_action'):
    mw.addonManager.set_config_help_action(mw.addonManager.addonFromModule(
        __name__), replace_module_name_in_config_help)
