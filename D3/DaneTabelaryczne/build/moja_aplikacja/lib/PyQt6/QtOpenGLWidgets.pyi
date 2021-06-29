# The PEP 484 type hints stub file for the QtOpenGLWidgets module.
#
# Generated by SIP 6.1.0
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtWidgets
from PyQt6 import QtOpenGL
from PyQt6 import QtGui
from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QOpenGLWidget(QtWidgets.QWidget):

    class UpdateBehavior(enum.Enum):
        NoPartialUpdate = ... # type: QOpenGLWidget.UpdateBehavior
        PartialUpdate = ... # type: QOpenGLWidget.UpdateBehavior

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ..., flags: QtCore.Qt.WindowType = ...) -> None: ...

    def setTextureFormat(self, texFormat: int) -> None: ...
    def textureFormat(self) -> int: ...
    def updateBehavior(self) -> 'QOpenGLWidget.UpdateBehavior': ...
    def setUpdateBehavior(self, updateBehavior: 'QOpenGLWidget.UpdateBehavior') -> None: ...
    def paintEngine(self) -> QtGui.QPaintEngine: ...
    def metric(self, metric: QtGui.QPaintDevice.PaintDeviceMetric) -> int: ...
    def event(self, e: QtCore.QEvent) -> bool: ...
    def resizeEvent(self, e: QtGui.QResizeEvent) -> None: ...
    def paintEvent(self, e: QtGui.QPaintEvent) -> None: ...
    def paintGL(self) -> None: ...
    def resizeGL(self, w: int, h: int) -> None: ...
    def initializeGL(self) -> None: ...
    def resized(self) -> None: ...
    def aboutToResize(self) -> None: ...
    def frameSwapped(self) -> None: ...
    def aboutToCompose(self) -> None: ...
    def grabFramebuffer(self) -> QtGui.QImage: ...
    def defaultFramebufferObject(self) -> int: ...
    def context(self) -> QtGui.QOpenGLContext: ...
    def doneCurrent(self) -> None: ...
    def makeCurrent(self) -> None: ...
    def isValid(self) -> bool: ...
    def format(self) -> QtGui.QSurfaceFormat: ...
    def setFormat(self, format: QtGui.QSurfaceFormat) -> None: ...
