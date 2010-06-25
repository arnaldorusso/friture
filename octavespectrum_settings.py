#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2009 Timoth?Lecomte

# This file is part of Friture.
#
# Friture is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# Friture is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Friture.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui, QtCore

# shared with octavespectrum.py
DEFAULT_SPEC_MIN = -140
DEFAULT_SPEC_MAX = 0
DEFAULT_WEIGHTING = 1 #A

class OctaveSpectrum_Settings_Dialog(QtGui.QDialog):
	def __init__(self, parent, logger):
		QtGui.QDialog.__init__(self, parent)
		
		self.parent = parent
		self.logger = logger
		
		self.setWindowTitle("Spectrum settings")
		
		self.formLayout = QtGui.QFormLayout(self)

		self.spinBox_specmin = QtGui.QSpinBox(self)
		self.spinBox_specmin.setKeyboardTracking(False)
		self.spinBox_specmin.setMinimum(-200)
		self.spinBox_specmin.setMaximum(200)
		self.spinBox_specmin.setProperty("value", DEFAULT_SPEC_MIN)
		self.spinBox_specmin.setObjectName("spinBox_specmin")
		self.spinBox_specmin.setSuffix(" dB")

		self.spinBox_specmax = QtGui.QSpinBox(self)
		self.spinBox_specmax.setKeyboardTracking(False)
		self.spinBox_specmax.setMinimum(-200)
		self.spinBox_specmax.setMaximum(200)
		self.spinBox_specmax.setProperty("value", DEFAULT_SPEC_MAX)
		self.spinBox_specmax.setObjectName("spinBox_specmax")
		self.spinBox_specmax.setSuffix(" dB")
		
		self.comboBox_weighting = QtGui.QComboBox(self)
		self.comboBox_weighting.setObjectName("weighting")
		self.comboBox_weighting.addItem("None")
		self.comboBox_weighting.addItem("A")
		self.comboBox_weighting.addItem("B")
		self.comboBox_weighting.addItem("C")
		self.comboBox_weighting.setCurrentIndex(DEFAULT_WEIGHTING)

		self.formLayout.addRow("Min:", self.spinBox_specmin)
		self.formLayout.addRow("Max:", self.spinBox_specmax)
		self.formLayout.addRow("Middle-ear weighting:", self.comboBox_weighting)
		
		self.setLayout(self.formLayout)

		self.connect(self.spinBox_specmin, QtCore.SIGNAL('valueChanged(int)'), self.parent.setmin)
		self.connect(self.spinBox_specmax, QtCore.SIGNAL('valueChanged(int)'), self.parent.setmax)
		self.connect(self.comboBox_weighting, QtCore.SIGNAL('currentIndexChanged(int)'), self.parent.setweighting)

	# method
	def saveState(self, settings):
		settings.setValue("Min", self.spinBox_specmin.value())
		settings.setValue("Max", self.spinBox_specmax.value())
		settings.setValue("weighting", self.comboBox_weighting.currentIndex())

	# method
	def restoreState(self, settings):
		(colorMin, ok) = settings.value("Min", DEFAULT_SPEC_MIN).toInt()
		self.spinBox_specmin.setValue(colorMin)
		(colorMax, ok) = settings.value("Max", DEFAULT_SPEC_MAX).toInt()
		self.spinBox_specmax.setValue(colorMax)
		(weighting, ok) = settings.value("weighting", DEFAULT_WEIGHTING).toInt()
		self.comboBox_weighting.setCurrentIndex(weighting)
