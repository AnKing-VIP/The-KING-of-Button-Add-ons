# -*- coding: utf-8 -*-

import aqt
from aqt import utils
from aqt.utils import closeTooltip
from aqt.qt import *


# custom method for deleting the tooltip, since there were problems
# with the handling of global variables by an add-on
def customCloseTooltip(tooltipLabel):
    if tooltipLabel:
        try:
            tooltipLabel.deleteLater()
        except:
            # already deleted as parent window closed
            pass
        tooltipLabel = None
utils.customCloseTooltip = customCloseTooltip


# modified method to alter the background color of the tooltip label
def tooltipWithColour(msg, color, x=0, y=20, xref=1, period=3000, parent=None, width=0, height=0):
    global _tooltipTimer, _tooltipLabel
    class CustomLabel(QLabel):
        silentlyClose = True
        def mousePressEvent(self, evt):
            evt.accept()
            self.hide()
    closeTooltip()
    aw = parent or aqt.mw.app.activeWindow() or aqt.mw
    lab = CustomLabel("""\
<center><table cellpadding=1>
<tr>
<td>%s</td>
</tr>
</table></center>""" % msg, aw)
    lab.setFrameStyle(QFrame.Panel)
    lab.setLineWidth(0)
    lab.setWindowFlags(Qt.ToolTip)
    
    # adjust height if user configured custom height
    
    if (width>0):
        lab.setFixedWidth(width)
    if (height>0):
        lab.setFixedHeight(height)
    
    p = QPalette()
    p.setColor(QPalette.Window, QColor(color))
    p.setColor(QPalette.WindowText, QColor("#000000"))
    lab.setPalette(p)
    lab.show()
    lab.move(QPoint(x - int(round(lab.width() * 0.5 * xref, 0)), y))
    
    def handler():
        customCloseTooltip(lab)
    
    t = QTimer(aqt.mw)
    t.setSingleShot = True
    t.timeout.connect(handler)
    t.start(period)
    
    _tooltipLabel = lab
utils.tooltipWithColour = tooltipWithColour
