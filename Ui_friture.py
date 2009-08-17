# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'friture.ui'
#
# Created: Mon Aug 17 17:37:06 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 573)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_startstop = QtGui.QPushButton(self.centralwidget)
        self.pushButton_startstop.setCheckable(True)
        self.pushButton_startstop.setChecked(True)
        self.pushButton_startstop.setAutoDefault(True)
        self.pushButton_startstop.setObjectName("pushButton_startstop")
        self.horizontalLayout_2.addWidget(self.pushButton_startstop)
        self.comboBox_inputDevice = QtGui.QComboBox(self.centralwidget)
        self.comboBox_inputDevice.setObjectName("comboBox_inputDevice")
        self.horizontalLayout_2.addWidget(self.comboBox_inputDevice)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabelLevel = QtGui.QLabel(self.centralwidget)
        self.LabelLevel.setObjectName("LabelLevel")
        self.verticalLayout.addWidget(self.LabelLevel)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_rms = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_rms.setFont(font)
        self.label_rms.setObjectName("label_rms")
        self.gridLayout_2.addWidget(self.label_rms, 0, 0, 1, 1)
        self.label_peak = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_peak.sizePolicy().hasHeightForWidth())
        self.label_peak.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_peak.setFont(font)
        self.label_peak.setObjectName("label_peak")
        self.gridLayout_2.addWidget(self.label_peak, 0, 2, 1, 1)
        self.meter = qsynthMeter(self.groupBox)
        self.meter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.meter.setFrameShadow(QtGui.QFrame.Raised)
        self.meter.setObjectName("meter")
        self.gridLayout_2.addWidget(self.meter, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.PlotZoneUp = TimePlot(self.centralwidget)
        self.PlotZoneUp.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PlotZoneUp.setFrameShadow(QtGui.QFrame.Raised)
        self.PlotZoneUp.setObjectName("PlotZoneUp")
        self.horizontalLayout.addWidget(self.PlotZoneUp)
        self.PlotZoneSpect = SpectPlot(self.centralwidget)
        self.PlotZoneSpect.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PlotZoneSpect.setFrameShadow(QtGui.QFrame.Raised)
        self.PlotZoneSpect.setObjectName("PlotZoneSpect")
        self.horizontalLayout.addWidget(self.PlotZoneSpect)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.PlotZoneImage = ImagePlot(self.centralwidget)
        self.PlotZoneImage.setFrameShape(QtGui.QFrame.StyledPanel)
        self.PlotZoneImage.setFrameShadow(QtGui.QFrame.Raised)
        self.PlotZoneImage.setObjectName("PlotZoneImage")
        self.gridLayout = QtGui.QGridLayout(self.PlotZoneImage)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addWidget(self.PlotZoneImage)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_freqscale = QtGui.QComboBox(self.centralwidget)
        self.comboBox_freqscale.setObjectName("comboBox_freqscale")
        self.comboBox_freqscale.addItem(QtCore.QString())
        self.comboBox_freqscale.addItem(QtCore.QString())
        self.horizontalLayout_3.addWidget(self.comboBox_freqscale)
        self.comboBox_fftsize = QtGui.QComboBox(self.centralwidget)
        self.comboBox_fftsize.setObjectName("comboBox_fftsize")
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.comboBox_fftsize.addItem(QtCore.QString())
        self.horizontalLayout_3.addWidget(self.comboBox_fftsize)
        self.spinBox_specmin = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_specmin.setKeyboardTracking(False)
        self.spinBox_specmin.setMinimum(-200)
        self.spinBox_specmin.setMaximum(200)
        self.spinBox_specmin.setProperty("value", QtCore.QVariant(-100))
        self.spinBox_specmin.setObjectName("spinBox_specmin")
        self.horizontalLayout_3.addWidget(self.spinBox_specmin)
        self.spinBox_specmax = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_specmax.setKeyboardTracking(False)
        self.spinBox_specmax.setMinimum(-200)
        self.spinBox_specmax.setMaximum(200)
        self.spinBox_specmax.setProperty("value", QtCore.QVariant(-20))
        self.spinBox_specmax.setObjectName("spinBox_specmax")
        self.horizontalLayout_3.addWidget(self.spinBox_specmax)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_fftsize.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Friture", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_startstop.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelLevel.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Input levels", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rms.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_peak.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_freqscale.setItemText(0, QtGui.QApplication.translate("MainWindow", "Linear", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_freqscale.setItemText(1, QtGui.QApplication.translate("MainWindow", "Logarithmic", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(0, QtGui.QApplication.translate("MainWindow", "32", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(1, QtGui.QApplication.translate("MainWindow", "64", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(2, QtGui.QApplication.translate("MainWindow", "128", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(3, QtGui.QApplication.translate("MainWindow", "256", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(4, QtGui.QApplication.translate("MainWindow", "512", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(5, QtGui.QApplication.translate("MainWindow", "1024", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(6, QtGui.QApplication.translate("MainWindow", "2048", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(7, QtGui.QApplication.translate("MainWindow", "4096", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(8, QtGui.QApplication.translate("MainWindow", "8192", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fftsize.setItemText(9, QtGui.QApplication.translate("MainWindow", "16384", None, QtGui.QApplication.UnicodeUTF8))

from timeplot import TimePlot
from qsynthmeter import qsynthMeter
from spectplot import SpectPlot
from imageplot import ImagePlot
