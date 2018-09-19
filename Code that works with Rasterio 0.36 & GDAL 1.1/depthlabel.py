# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pointsdepth.ui'
#
# Created: Fri Jul 13 04:41:20 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
import matplotlib.pyplot as plt
import rasterio
import utm
from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(498, 211)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.OK = QtGui.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(210, 140, 75, 23))
        self.OK.setObjectName(_fromUtf8("OK"))
        self.OK.clicked.connect(self.pressed_ok)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 80, 441, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_dir = QtGui.QLabel(self.widget)
        self.label_dir.setObjectName(_fromUtf8("label_dir"))
        self.horizontalLayout.addWidget(self.label_dir)
        self.targetdir = QtGui.QLineEdit(self.widget)
        self.targetdir.setObjectName(_fromUtf8("targetdir"))
        self.targetdir.textChanged.connect(set_dir)
        self.horizontalLayout.addWidget(self.targetdir)
        self.brwfolder = QtGui.QPushButton(self.widget)
        self.brwfolder.setObjectName(_fromUtf8("brwfolder"))
        self.brwfolder.clicked.connect(self.sel_folder)
        self.horizontalLayout.addWidget(self.brwfolder)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 20, 321, 22))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_fname = QtGui.QLabel(self.widget1)
        self.label_fname.setObjectName(_fromUtf8("label_fname"))
        self.horizontalLayout_2.addWidget(self.label_fname)
        self.points_fname = QtGui.QLineEdit(self.widget1)
        self.points_fname.setObjectName(_fromUtf8("points_fname"))
        self.points_fname.textChanged.connect(set_fname)
        self.horizontalLayout_2.addWidget(self.points_fname)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(30, 50, 441, 25))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.widget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.textChanged.connect(set_georef)
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.widget2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.sel_file)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def pressed_ok(self):
		make_pointsfile()
		sys.exit(app.exec_())
    def sel_folder(self):
		self.targetdir.setText(QFileDialog.getExistingDirectory())
    def sel_file(self):
		self.lineEdit.setText(QFileDialog.getOpenFileName())

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Module for making CSV files of Ground Depth data", None))
        self.OK.setText(_translate("MainWindow", "OK", None))
        self.label_dir.setText(_translate("MainWindow", "Target Directory", None))
        self.brwfolder.setText(_translate("MainWindow", "Browse", None))
        self.label_fname.setText(_translate("MainWindow", " Points Filename", None))
        self.label.setText(_translate("MainWindow", "Georeferenced image", None))
        self.pushButton.setText(_translate("MainWindow", "Browse", None))


def set_dir(text):
	global outdir
	outdir = unicode(text)
	
def set_fname(text):
	global fname
	fname = unicode(text)

def set_georef(text):
	global georefimg
	georefimg = unicode(text)

def make_pointsfile():
	global widget11,a,depthvals
	src = rasterio.open(georefimg) #from gui
	#blue = rasterio.open('../')
	data = src.read()

	fig, ax = plt.subplots()
	ax.set_title('Double click on points to select GCPs')

	data = np.transpose(data,(1,2,0))

	ax.imshow(data)

	app = QtGui.QApplication(sys.argv)
	widget11 = QtGui.QWidget()

	a=src.affine
	#b=blue.affine
	depthvals=[]
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
	out_fname = unicode(outdir + os.path.sep + fname + ".csv")
	plt.show()

	points=open(out_fname,"w")
	points.write("x_utm,y_utm,depth,\n")
	for pt in depthvals:
		points.write("{},{},{}\n".format(pt[0],pt[1],pt[2]))
	points.close()
	
def onclick(event):
    global widget11,a,depthvals
    if event.dblclick:
		depth, ok = QInputDialog.getDouble(widget11,"Ground Truth Values","Enter the depth")
		if(ok):
						lon = a[0]*event.xdata + a[1]*event.ydata + a[2]
						lat = a[3]*event.xdata + a[4]*event.ydata + a[5]

						(xutm,yutm,zoneno,zonelet) = utm.from_latlon(lat,lon)

						# xdst = (b[4]*(xutm-b[2]) - b[1]*(yutm-b[5])) / (b[0]*b[4] - b[3]*b[1])
						# ydst = (b[0]*(yutm-b[5]) - b[3]*(xutm-b[2])) / (b[0]*b[4] - b[3]*b[1])
						# xind = int(math.floor(xdst))
						# yind = int(math.floor(ydst))
						print (xutm,yutm,depth)
						depthvals.append((xutm,yutm,depth))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

