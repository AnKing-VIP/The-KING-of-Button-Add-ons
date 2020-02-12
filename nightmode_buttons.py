# -*- coding: utf-8 -*-

# Original code Copyright: (c) 2018 hkr <hkrysg@gmail.com>
# Modified by The AnKing 
### Youtube: www.ankingmed.com
### Facebook/Instagram: @ankingmed
### Patreon (get individualized Anki help): www.patreon.com/ankingmed

from anki.hooks import wrap
from aqt import mw
from aqt.reviewer import Reviewer
import os
import shutil


this_script_dir = os.path.dirname(__file__)
user_files_dir = os.path.join(this_script_dir, 'user_files')
user_css_path = os.path.join(user_files_dir, 'user_bottom_buttons.css')
default_css_path = os.path.join(this_script_dir, 'default_bottom_buttons.css')

# user_filesにuser_bottom_buttons.cssが無かったらdefault_bottom_buttons.cssをリネームしてコピーする
if not os.path.isfile(user_css_path):
    os.makedirs(user_files_dir, exist_ok=True)  # user_filesが存在しない場合の対策
    shutil.copyfile(default_css_path, user_css_path)


with open(user_css_path, encoding='utf-8') as f:
    bottom_buttons_css = f.read()


# css文字列をバッククォートで囲む
# css中の改行を削除しなくてO.K.
# シングルクォートとダブルクォートが混在していてもO.K.
js_append_css = f"$('head').append(`<style>{bottom_buttons_css}</style>`);"


def reviewer_initWeb_wrapper(*args, **kwargs):
    mw.reviewer.bottom.web.eval(js_append_css)


Reviewer._initWeb = wrap(Reviewer._initWeb, reviewer_initWeb_wrapper)
