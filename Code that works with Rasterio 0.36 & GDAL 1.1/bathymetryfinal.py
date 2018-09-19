# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Tue Jul 03 01:22:26 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import numpy.ma as ma
import rasterio
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
import utm
import math
import csv
from sklearn.linear_model import LinearRegression
from sklearn import metrics


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


#Window for depth processing
class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(642, 693)
        validator = QtGui.QDoubleValidator()
        validator.setRange(-100000,100000)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 30, 523, 25))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_ir = QtGui.QLabel(self.layoutWidget_2)
        self.label_ir.setObjectName(_fromUtf8("label_ir"))
        self.horizontalLayout_2.addWidget(self.label_ir)
        self.ir_threshold = QtGui.QLineEdit(self.layoutWidget_2)
        self.ir_threshold.setObjectName(_fromUtf8("ir_threshold"))
        self.ir_threshold.textChanged.connect(self.set_ir_threshold)
        self.ir_threshold.setValidator(validator)
        self.horizontalLayout_2.addWidget(self.ir_threshold)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.histogram = QtGui.QPushButton(self.layoutWidget_2)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.histogram.clicked.connect(self.show_histogram)
        self.horizontalLayout_5.addWidget(self.histogram)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 380, 521, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.out_dir = QtGui.QLineEdit(self.layoutWidget)
        self.out_dir.setObjectName(_fromUtf8("out_dir"))
        self.out_dir.textChanged.connect(set_outdir)
        self.horizontalLayout.addWidget(self.out_dir)
        self.browse_directory = QtGui.QPushButton(self.layoutWidget)
        self.browse_directory.setObjectName(_fromUtf8("browse_directory"))
        self.horizontalLayout.addWidget(self.browse_directory)
        self.browse_directory.clicked.connect(self.browse_dir)
        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(110, 420, 404, 19))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.select_grayscale_2 = QtGui.QCheckBox(self.layoutWidget_3)
        self.select_grayscale_2.setObjectName(_fromUtf8("select_grayscale_2"))
        self.select_grayscale_2.toggled.connect(self.set_grayscale)
        self.horizontalLayout_4.addWidget(self.select_grayscale_2)
        self.select_colour_2 = QtGui.QCheckBox(self.layoutWidget_3)
        self.select_colour_2.setObjectName(_fromUtf8("select_colour_2"))
        self.select_colour_2.toggled.connect(self.set_colour)
        self.horizontalLayout_4.addWidget(self.select_colour_2)
        self.compute = QtGui.QPushButton(self.centralwidget)
        self.compute.setGeometry(QtCore.QRect(280, 570, 75, 23))
        self.compute.setObjectName(_fromUtf8("compute"))
        self.compute.clicked.connect(self.pressed_compute)
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(110, 460, 381, 80))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_8 = QtGui.QLabel(self.layoutWidget_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_9.addWidget(self.label_8)
        self.grayscale_filename_2 = QtGui.QLineEdit(self.layoutWidget_4)
        self.grayscale_filename_2.setObjectName(_fromUtf8("grayscale_filename_2"))
        self.grayscale_filename_2.textChanged.connect(grayscale_filename)
        self.horizontalLayout_9.addWidget(self.grayscale_filename_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_9 = QtGui.QLabel(self.layoutWidget_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        self.grayscale_logfile_2 = QtGui.QLineEdit(self.layoutWidget_4)
        self.grayscale_logfile_2.setObjectName(_fromUtf8("grayscale_logfile_2"))
        self.grayscale_logfile_2.textChanged.connect(log_filename)
        self.horizontalLayout_10.addWidget(self.grayscale_logfile_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_10 = QtGui.QLabel(self.layoutWidget_4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_11.addWidget(self.label_10)
        self.colour_filename_2 = QtGui.QLineEdit(self.layoutWidget_4)
        self.colour_filename_2.setObjectName(_fromUtf8("colour_filename_2"))
        self.colour_filename_2.textChanged.connect(colour_filename)
        self.horizontalLayout_11.addWidget(self.colour_filename_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.proc_label = QtGui.QLabel(self.centralwidget)
        self.proc_label.setGeometry(QtCore.QRect(230, 610, 221, 31))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proc_label.setFont(font)
        self.proc_label.setObjectName(_fromUtf8("proc_label"))
        self.proc_label.hide()
        self.pick_groundtruth = QtGui.QPushButton(self.centralwidget)
        self.pick_groundtruth.setGeometry(QtCore.QRect(210, 240, 181, 23))
        self.pick_groundtruth.setObjectName(_fromUtf8("pick_groundtruth"))
        self.pick_groundtruth.clicked.connect(self.select_groundtruth_values)
        self.layoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(50, 270, 521, 25))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_14.setMargin(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_pointsfile = QtGui.QLabel(self.layoutWidget_5)
        self.label_pointsfile.setObjectName(_fromUtf8("label_pointsfile"))
        self.horizontalLayout_14.addWidget(self.label_pointsfile)
        self.points_filename = QtGui.QLineEdit(self.layoutWidget_5)
        self.points_filename.setObjectName(_fromUtf8("points_filename"))
        self.points_filename.textChanged.connect(set_pointsfname)
        self.horizontalLayout_14.addWidget(self.points_filename)
        self.browse_points = QtGui.QPushButton(self.layoutWidget_5)
        self.browse_points.setObjectName(_fromUtf8("browse_points"))
        self.browse_points.clicked.connect(self.brwpoints)
        self.horizontalLayout_14.addWidget(self.browse_points)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 110, 521, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_georef = QtGui.QLabel(self.widget)
        self.label_georef.setObjectName(_fromUtf8("label_georef"))
        self.horizontalLayout_12.addWidget(self.label_georef)
        self.georefimg = QtGui.QLineEdit(self.widget)
        self.georefimg.setObjectName(_fromUtf8("georefimg"))
        self.georefimg.textChanged.connect(set_georefimg)
        self.horizontalLayout_12.addWidget(self.georefimg)
        self.browse_georef = QtGui.QPushButton(self.widget)
        self.browse_georef.setObjectName(_fromUtf8("browse_georef"))
        self.browse_georef.clicked.connect(self.brwgrf)
        self.horizontalLayout_12.addWidget(self.browse_georef)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(140, 190, 340, 19))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.groundtruth = QtGui.QRadioButton(self.widget1)
        self.groundtruth.setObjectName(_fromUtf8("groundtruth"))
        self.groundtruth.toggled.connect(self.selgroundtruth)
        self.horizontalLayout_13.addWidget(self.groundtruth)
        self.pointsfile = QtGui.QRadioButton(self.widget1)
        self.pointsfile.setObjectName(_fromUtf8("pointsfile"))
        self.pointsfile.toggled.connect(self.checkptsfile)
        self.horizontalLayout_13.addWidget(self.pointsfile)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.pick_groundtruth.hide()
        self.label_pointsfile.hide()
        self.points_filename.hide()
        self.browse_points.hide()
        self.colour_filename_2.hide()
        self.label_10.hide()
        self.grayscale_filename_2.hide()
        self.label_8.hide()
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
    def set_ir_threshold(self,text):
        global limit
        limit = float(text)
        self.ir_threshold.setText(text)
 
	
    def show_histogram(self):
        global img3, qcalmax1, qcalmin1
        heights,edges = np.histogram(img3,int(qcalmax1-qcalmin1+1),(qcalmin1,qcalmax1))
        edges = edges[:-1]+(edges[1]-edges[0])
        fig, ax = plt.subplots()
        ax.plot(edges,heights)
        ax.set(title='Click Once', xlabel='Pixel value', ylabel='Frequency')
        point1 = fig.ginput(1)
        lim = point1[0][0]
        self.ir_threshold.setText(str(lim))
        plt.close(fig)
		
    def set_grayscale(self):
        global isGrayscale
        if self.select_grayscale_2.isChecked() == True:
			isGrayscale = 1;
			self.grayscale_filename_2.show()
			self.label_8.show()
        else:
            isGrayscale = 0;
            self.grayscale_filename_2.hide()
            self.label_8.hide()
       
       

    def set_colour(self):
        global isColour
        if self.select_colour_2.isChecked() == True:
            isColour = 1;
            self.colour_filename_2.show()
            self.label_10.show()
        else:
            isColour = 0;
            self.colour_filename_2.hide()
            self.label_10.hide()
       
    
    def checkptsfile(self):
		global check
		if self.pointsfile.isChecked() == True:
			check = 0
			self.pick_groundtruth.hide()
			self.label_pointsfile.show()
			self.points_filename.show()
			self.browse_points.show()
			
		
	
    def selgroundtruth(self):
		global check
		if self.groundtruth.isChecked() == True:
			check = 1
			self.pick_groundtruth.show()
			self.label_pointsfile.hide()
			self.points_filename.hide()
			self.browse_points.hide()
			
			
		
    def select_groundtruth_values(self):
        global a,b,depthvals
        src = rasterio.open(grefimg) #from gui

        data = src.read()

        fig, ax = plt.subplots()
        ax.set_title('Double click on points to select GCPs')
        data = np.transpose(data,(1,2,0))
        ax.imshow(data)

        a=src.affine
        depthvals=[]

        
        fig.canvas.mpl_connect('button_press_event', self.onclick)

        plt.show()
      

    def onclick(self,event):
        global a,b,depthvals
        if event.dblclick:
			self.widget11 = QWidget()
			depth, ok = QInputDialog.getDouble(self.widget11,"Ground Truth Values","Enter the depth")
			if(ok):
						lon = a[0]*event.xdata + a[1]*event.ydata + a[2]
						lat = a[3]*event.xdata + a[4]*event.ydata + a[5]
						(xutm,yutm,zoneno,zonelet) = utm.from_latlon(lat,lon)
						depthvals.append((xutm,yutm,depth))
					
    def pressed_compute(self):
        
        if (self.select_grayscale_2.isChecked() == False)and(self.select_colour_2.isChecked() == False):
            self.showdialogcheck()
        elif (self.groundtruth.isChecked() == False)and(self.pointsfile.isChecked() == False):
			self.showdialogcheck()
        elif (check==0)and(not self.points_filename.text()):
			self.showdialogerr()
        elif (not self.grayscale_logfile_2.text())or(not self.ir_threshold.text())or(not self.georefimg.text())or (not self.out_dir.text()):
            self.showdialogerr()
        elif (self.select_grayscale_2.isChecked() == True)and(not self.grayscale_filename_2.text()):
			self.showdialogerr()
        elif (self.select_colour_2.isChecked() == True)and(not self.colour_filename_2.text()):
			self.showdialogerr()
        else:
            self.proc_label.show()
            start_depth()
            self.proc_label.hide()
            self.showdialogfin()
            sys.exit(app.exec_())

    def showdialogfin(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("The output image files have been created and saved")
        
        msg.setWindowTitle("Done")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def showdialogerr(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Fill all the details required")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def showdialogcheck(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Check at least one of the boxes")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
		
        


		

    def browse_dir(self):
        self.out_dir.setText(QFileDialog.getExistingDirectory())
        
	
    def brwgrf(self):
		self.georefimg.setText(QFileDialog.getOpenFileName()) 
	
    def brwpoints(self):
		self.points_filename.setText(QFileDialog.getOpenFileName()) 
		
	

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Depth Processing", None))
        self.label_ir.setText(_translate("MainWindow", "Enter the threshold for separating land and water in IR band ", None))
        self.histogram.setText(_translate("MainWindow", "Use Histogram ", None))
        self.label.setText(_translate("MainWindow", "Select target folder for output file", None))
        self.browse_directory.setText(_translate("MainWindow", "Browse directory", None))
        self.label_7.setText(_translate("MainWindow", "Output as:", None))
        self.select_grayscale_2.setText(_translate("MainWindow", "Grayscale map(original resolution)", None))
        self.select_colour_2.setText(_translate("MainWindow", "Colour map(less resolution)", None))
        self.compute.setText(_translate("MainWindow", "Compute", None))
        self.label_8.setText(_translate("MainWindow", "Grayscale filename      ", None))
        self.label_9.setText(_translate("MainWindow", "Grayscale log filename", None))
        self.label_10.setText(_translate("MainWindow", "Colour filename           ", None))
        self.proc_label.setText(_translate("MainWindow", "PROCESSING...", None))
        self.pick_groundtruth.setText(_translate("MainWindow", "Pick Ground truth points", None))
        self.label_pointsfile.setText(_translate("MainWindow", "Select the points file(.csv file)", None))
        self.browse_points.setText(_translate("MainWindow", "Browse file", None))
        self.label_georef.setText(_translate("MainWindow", "Select the georeferenced image", None))
        self.browse_georef.setText(_translate("MainWindow", "Browse file", None))
        self.groundtruth.setText(_translate("MainWindow", "Pick Ground truth points for depth manually", None))
        self.pointsfile.setText(_translate("MainWindow", "Select points file", None))

def start_depth():
		global targetdir,logfile,log
		logfile = targetdir + os.path.sep + logfile + ".txt"
		log = open(unicode(logfile),'w')
		log.write (str(time.clock())+ ": Depth Processing started\n")
		landcut()
		calc_rad()
		calc_depth()
		if(isColour):
			savedepthcolor()
		if(isGrayscale):
			savedepthgray()
		log.write (str(time.clock())+ ": Depth Processing ended\n")

def calc_depth():
	global depth,check,radgreen,sampledepth,img2
	if check==0:
		readpointsfile()
	get_parameters()
	get_regression()
	plot_regression_line(radgreen_train,sampledepth_train,(c,m))
	validation()
	
	#Formula for depth. Our formula: Depth= Slope*(Green Band Radiance)+Intercept NOTE: Can be changed according to bathymetric model used.
	depth = m * img2 + c

#Reads csv file containing data and loads into array	
def readpointsfile():
	global depthvals
	depthvals=[]
	pfile = csv.reader(open(pointsfname)) #get name from gui
	for row in pfile:
		depthvals.append(row)
	depthvals.pop(0)
	depthvals = [[float(s) for s in sublist] for sublist in depthvals]
	

#Obtains training and testing data from selected Ground truth points
def get_parameters():
	global depthvals,sampledepth_train,radblue_train,radgreen_train,sampledepth_test,radblue_test,radgreen_test
	i_s = []
	for i in range(len(depthvals)):
		#45 meters is the absolute maximum depth dtectable by remote sensing
		#Selects values only inside the bounds of satellite dataset
		if blue.bounds.left<=depthvals[i][0]<blue.bounds.right and blue.bounds.bottom<=depthvals[i][1]<blue.bounds.top and depthvals[i][2]<45:
			i_s.append(i)
	
	xutm = np.array([depthvals[i][0] for i in i_s],dtype = np.float64)
	xutm = np.reshape(xutm, newshape = (xutm.shape[0],1))
	yutm = np.array([depthvals[i][1] for i in i_s],dtype = np.float64)
	yutm = np.reshape(yutm, newshape = (yutm.shape[0],1))
	sampledepth = np.array([depthvals[i][2] for i in i_s],dtype = np.float64)
	sampledepth = np.reshape(sampledepth, newshape = (sampledepth.shape[0],1))
	
	b=blue.affine
	
	xdst = (b[4]*(xutm-b[2]) - b[1]*(yutm-b[5])) / (b[0]*b[4] - b[3]*b[1])
	ydst = (b[0]*(yutm-b[5]) - b[3]*(xutm-b[2])) / (b[0]*b[4] - b[3]*b[1])
	xind = np.asarray(np.floor(xdst),dtype = np.int32)
	yind = np.asarray(np.floor(ydst),dtype = np.int32)
	radblue  = np.array(img1[0,yind,xind],dtype = np.float64)
	radgreen = np.array(img2[0,yind,xind],dtype = np.float64)
	
	# [x_s,y_s] = np.where(logblue == 1.)
	# [x_s_2,y_s_2] = np.where(loggreen == 1.)
	# x_union = np.union1d(x_s,x_s_2)
	
	radblue = np.squeeze(radblue)
	radgreen = np.squeeze(radgreen)
	sampledepth = np.squeeze(sampledepth)
	
	# logblue = np.delete(logblue,x_union)
	# loggreen = np.delete(loggreen,x_union)
	# sampledepth = np.delete(sampledepth,x_union)
	
	#Splitting available data for training and testing in 3:1 ratio
	radblue_train,radblue_test = np.split(radblue,[int(0.75 * radblue.shape[0])])
	radgreen_train,radgreen_test = np.split(radgreen,[int(0.75 * radgreen.shape[0])])
	sampledepth_train,sampledepth_test = np.split(sampledepth,[int(0.75 * sampledepth.shape[0])])
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('Green band radiance')
    plt.ylabel('Sample depth')
 
    # function to show plot
    plt.show()

# Gives linear regression for the training dataset
def get_regression():
	global radgreen_train,sampledepth_train,m,c,outlier,log
	
	#Plots scatter and asks to select outliers
	fig,ax = plt.subplots()
	plt.scatter(radgreen_train, sampledepth_train, color = "m", marker = "o", s = 30)
	ax.set(title='Click to set limits to reject outliers: first right limit, then left limit', xlabel='Green band radiance', ylabel='Sample Depth')
	outlier = fig.ginput(2)
	plt.close(fig)
	
	x_inds = np.where( radgreen_train <= outlier[0][0] )
	radgreen_train = radgreen_train[x_inds]
	sampledepth_train = sampledepth_train[x_inds]

	x_inds = np.where( radgreen_train > outlier[1][0])
	radgreen_train = radgreen_train[x_inds]
	sampledepth_train = sampledepth_train[x_inds]
	
	#Calculates Linear Regression
	lr = LinearRegression(fit_intercept = True,normalize = True)
	radgreen_train = np.reshape(radgreen_train, newshape = (radgreen_train.shape[0],1))
	lr.fit(radgreen_train,sampledepth_train)
	m = lr.coef_[0]
	log.write("Regression coefficient: Slope = {}\n".format(m))
	c = lr.intercept_
	log.write("Regression coefficient: Intercept = {}\n".format(c))

#Validation of regression with the testing data and deriation of R2 value
def validation():
	global radgreen_test,sampledepth_test,m,c,log,outlier
	
	x_inds = np.where( radgreen_test <= outlier[0][0] )
	radgreen_test = radgreen_test[x_inds]
	sampledepth_test = sampledepth_test[x_inds]

	x_inds = np.where( radgreen_test > outlier[1][0])
	radgreen_test = radgreen_test[x_inds]
	sampledepth_test = sampledepth_test[x_inds]

	#Formula for depth. Our formula: Depth= Slope*(Green Band Radiance)+Intercept NOTE: Can be changed according to bathymetric model used.
	depth_pred = m*radgreen_test + c
	
	r2 = metrics.r2_score(sampledepth_test, depth_pred)
	log.write("R2 score of the analysis: {}\n".format(r2))
	
	#Displays plot between prediction and truth
	fig,ax = plt.subplots()
	plt.scatter(sampledepth_test, depth_pred)
	ax.set(title='R2 score = {}'.format(r2), xlabel='Sample depth', ylabel='Predicted Depth')

	
#Export colormap of depth values
def savedepthcolor():
	global log, targetdir, col_filename,depth
	log.write (str(time.clock())+ ": Saving colormap started\n")
	col_filename = unicode(targetdir + os.path.sep + col_filename + ".png")
	log.write ("Colormap path: " + col_filename + "\n")
	plt.figure()
	colormap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',['violet','indigo','blue','green','yellow','orange','red'],256)
	colorimg = plt.imshow(depth[0],interpolation='nearest', cmap=colormap ,origin='lower')
	plt.colorbar(colorimg,cmap=colormap)
	plt.savefig(col_filename)
	plt.show()
	

#Export scaled grayscale map of depth values
def savedepthgray():
	global log, targetdir, gray_filename, depth
	log.write (str(time.clock())+": Saving graymap started\n")
	file_name = unicode(targetdir + os.path.sep + gray_filename + ".tif")
	log.write ("Greyscale file path: " + file_name + "\n")
	depthmax = np.nanmax(depth)
	depthmin = np.nanmin(depth)
	log.write ("Max. measured depth: {} was scaled to {}\n".format(depthmax,2**bit-1))
	log.write ("Min. measured depth: {} was scaled to {}\n".format(depthmin,1))
	depth = (2**bit - 1)*(depth - depthmin)/(depthmax - depthmin) 
	depth = depth.filled(2**bit - 1)
	if bit==16:
		depth = depth.astype(np.uint16)
		type = 'uint16' 
	else:
		depth = depth.astype(np.uint8)
		type = 'uint8'
	dst = rasterio.open(file_name, 'w', driver = 'Gtiff',width = blue.width, height = blue.height, count = 1, dtype = type,crs = blue.crs, transform = blue.transform)
	dst.write(depth)
	dst.close()


        

#Main Window for taking inputs of satellite image and metadata
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(754, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.image_type = QtGui.QComboBox(self.centralwidget)
        self.image_type.setGeometry(QtCore.QRect(140, 30, 451, 22))
        self.image_type.setObjectName(_fromUtf8("image_type"))
        self.image_type.addItems(["Landsat 8", "Landsat 7", "Landsat 5", "Other"])
        self.image_type.currentIndexChanged.connect(self.change_image_type)
        
        validator = QtGui.QDoubleValidator()
        validator.setRange(-100000,100000)
        
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 80, 701, 114))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_3.addWidget(self.label_10)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.blue_filename = QtGui.QLineEdit(self.layoutWidget)
        self.blue_filename.setObjectName(_fromUtf8("blue_filename"))
        self.verticalLayout.addWidget(self.blue_filename)
        self.blue_filename.textChanged.connect(set_blue_filename)
        
        self.green_filename = QtGui.QLineEdit(self.layoutWidget)
        self.green_filename.setObjectName(_fromUtf8("green_filename"))
        self.verticalLayout.addWidget(self.green_filename)
        self.green_filename.textChanged.connect(set_green_filename)
        
        self.ir_filename_2 = QtGui.QLineEdit(self.layoutWidget)
        self.ir_filename_2.setObjectName(_fromUtf8("ir_filename_2"))
        self.verticalLayout.addWidget(self.ir_filename_2)
        self.ir_filename_2.textChanged.connect(set_ir_filename)
        
        self.meta_filename = QtGui.QLineEdit(self.layoutWidget)
        self.meta_filename.setObjectName(_fromUtf8("meta_filename"))
        self.verticalLayout.addWidget(self.meta_filename)
        self.meta_filename.textChanged.connect(set_meta_filename)
        
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.browse_blue = QtGui.QPushButton(self.layoutWidget)
        self.browse_blue.setObjectName(_fromUtf8("browse_blue"))
        self.verticalLayout_2.addWidget(self.browse_blue)
        self.browse_blue.clicked.connect(self.select_blue_file)
        
        self.browse_green = QtGui.QPushButton(self.layoutWidget)
        self.browse_green.setObjectName(_fromUtf8("browse_green"))
        self.verticalLayout_2.addWidget(self.browse_green)
        self.browse_green.clicked.connect(self.select_green_file)

        self.browse_ir = QtGui.QPushButton(self.layoutWidget)
        self.browse_ir.setObjectName(_fromUtf8("browse_ir"))
        self.verticalLayout_2.addWidget(self.browse_ir)
        self.browse_ir.clicked.connect(self.select_ir_file)

        self.browse_meta = QtGui.QPushButton(self.layoutWidget)
        self.browse_meta.setObjectName(_fromUtf8("browse_meta"))
        self.verticalLayout_2.addWidget(self.browse_meta)
        self.browse_meta.clicked.connect(self.select_meta_file)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 260, 701, 56))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.max_rad_blue = QtGui.QLineEdit(self.layoutWidget1)
        self.max_rad_blue.setObjectName(_fromUtf8("max_rad_blue"))
        
        self.max_rad_blue.setValidator(validator)
        self.max_rad_blue.textChanged.connect(set_maxrad_blue)
    
        
        self.horizontalLayout_3.addWidget(self.max_rad_blue)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.min_rad_blue = QtGui.QLineEdit(self.layoutWidget1)
        self.min_rad_blue.setObjectName(_fromUtf8("min_rad_blue"))
        self.min_rad_blue.setValidator(validator)
        self.min_rad_blue.textChanged.connect(set_minrad_blue)
        
        self.horizontalLayout_4.addWidget(self.min_rad_blue)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.max_pixel_blue = QtGui.QLineEdit(self.layoutWidget1)
        self.max_pixel_blue.setObjectName(_fromUtf8("max_pixel_blue"))
        self.max_pixel_blue.setValidator(validator)
        self.max_pixel_blue.textChanged.connect(set_maxpix_blue)
        
        self.horizontalLayout_6.addWidget(self.max_pixel_blue)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.min_pixel_blue = QtGui.QLineEdit(self.layoutWidget1)
        self.min_pixel_blue.setObjectName(_fromUtf8("min_pixel_blue"))
        self.min_pixel_blue.setValidator(validator)
        self.min_pixel_blue.textChanged.connect(set_minpix_blue)
        
        self.horizontalLayout_7.addWidget(self.min_pixel_blue)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 350, 701, 56))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.max_rad_green = QtGui.QLineEdit(self.layoutWidget_2)
        self.max_rad_green.setObjectName(_fromUtf8("max_rad_green"))
        self.max_rad_green.setValidator(validator)
        self.max_rad_green.textChanged.connect(set_maxrad_green)
        
        self.horizontalLayout_12.addWidget(self.max_rad_green)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_12 = QtGui.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_13.addWidget(self.label_12)
        self.min_rad_green = QtGui.QLineEdit(self.layoutWidget_2)
        self.min_rad_green.setObjectName(_fromUtf8("min_rad_green"))
        self.min_rad_green.setValidator(validator)
        self.min_rad_green.textChanged.connect(set_minrad_green)
        
        self.horizontalLayout_13.addWidget(self.min_rad_green)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_13 = QtGui.QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_15.addWidget(self.label_13)
        self.max_pixel_green = QtGui.QLineEdit(self.layoutWidget_2)
        self.max_pixel_green.setObjectName(_fromUtf8("max_pixel_green"))
        self.max_pixel_green.setValidator(validator)
        self.max_pixel_green.textChanged.connect(set_maxpix_green)
        
        self.horizontalLayout_15.addWidget(self.max_pixel_green)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_14 = QtGui.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_16.addWidget(self.label_14)
        self.min_pixel_green = QtGui.QLineEdit(self.layoutWidget_2)
        self.min_pixel_green.setObjectName(_fromUtf8("min_pixel_green"))
        self.min_pixel_green.setValidator(validator)
        self.min_pixel_green.textChanged.connect(set_minpix_green)

        myFont=QtGui.QFont()
        myFont.setBold(True)
        
        self.horizontalLayout_16.addWidget(self.min_pixel_green)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_15.setFont(myFont)

        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 330, 81, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_16.setFont(myFont)

        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 430, 523, 25))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        '''self.ir_threshold = QtGui.QLineEdit(self.layoutWidget2)
        self.ir_threshold.setObjectName(_fromUtf8("ir_threshold"))
        self.ir_threshold.setValidator(validator)
        self.ir_threshold.textChanged.connect(set_ir_threshold)
        
        self.horizontalLayout_2.addWidget(self.ir_threshold)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.histogram = QtGui.QPushButton(self.layoutWidget2)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.horizontalLayout_5.addWidget(self.histogram)'''
        self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 210, 194, 20))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_9 = QtGui.QLabel(self.layoutWidget3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        self.datatype_8 = QtGui.QRadioButton(self.layoutWidget3)
        self.datatype_8.setObjectName(_fromUtf8("datatype_8"))
        self.datatype_8.toggled.connect(self.set_datatype_8)

        self.max_rad_blue.hide()
        self.min_rad_blue.hide()
        self.max_pixel_blue.hide()
        self.min_pixel_blue.hide()
        self.max_rad_green.hide()
        self.min_rad_green.hide()
        self.max_pixel_green.hide()
        self.min_pixel_green.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_10.show()
        self.browse_meta.show()
        self.meta_filename.show()

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(280, 490, 191, 51))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_18.setMargin(0)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.dii = QtGui.QPushButton(self.widget)
        self.dii.setObjectName(_fromUtf8("dii"))
        self.dii.setText("WCC")
        self.dii.clicked.connect(self.pressed_dii)
        self.horizontalLayout_18.addWidget(self.dii)
        self.seldepth = QtGui.QPushButton(self.widget)
        self.seldepth.setObjectName(_fromUtf8("seldepth"))
        self.seldepth.setText("Depth")
        self.seldepth.clicked.connect(self.pressed_depth)
        self.horizontalLayout_18.addWidget(self.seldepth)

        
        self.horizontalLayout_10.addWidget(self.datatype_8)
        self.datatype_16 = QtGui.QRadioButton(self.layoutWidget3)
        self.datatype_16.setObjectName(_fromUtf8("datatype_16"))
        self.datatype_16.toggled.connect(self.set_datatype_16)
        self.horizontalLayout_10.addWidget(self.datatype_16)
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtGui.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 21))
        # self.menubar.setObjectName(_fromUtf8("menubar"))
        # self.menuMenu = QtGui.QMenu(self.menubar)
        # self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        # self.actionNew = QtGui.QAction(MainWindow)
        # self.actionNew.setObjectName(_fromUtf8("actionNew"))
        # self.actionSave = QtGui.QAction(MainWindow)
        # self.actionSave.setObjectName(_fromUtf8("actionSave"))
        # self.actionExit = QtGui.QAction(MainWindow)
        # self.actionExit.setObjectName(_fromUtf8("actionExit"))
        # self.menuMenu.addAction(self.actionNew)
        # self.menuMenu.addAction(self.actionSave)
        # self.menuMenu.addSeparator()
        # self.menuMenu.addAction(self.actionExit)
        # self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def select_blue_file(self):
		self.blue_filename.setText(QFileDialog.getOpenFileName())
	
    def select_green_file(self):
		self.green_filename.setText(QFileDialog.getOpenFileName())
		
    def select_ir_file(self):
		self.ir_filename_2.setText(QFileDialog.getOpenFileName())
    		
    def select_meta_file(self):
		self.meta_filename.setText(QFileDialog.getOpenFileName())
    def set_datatype_8(self):
                if self.datatype_8.isChecked() == True:
                   
                    set_radio(8)
    def set_datatype_16(self):
                if self.datatype_16.isChecked() == True:
                    set_radio(16)
                   
    def change_image_type(self):
                if self.image_type.currentText()=="Other":
                    self.show_for_other()
                    
                else:
                    self.val_hide()
                    
    def show_for_other(self):
                self.max_rad_blue.show()
                self.min_rad_blue.show()
                self.max_pixel_blue.show()
                self.min_pixel_blue.show()
                self.max_rad_green.show()
                self.min_rad_green.show()
                self.max_pixel_green.show()
                self.min_pixel_green.show()
                self.label_2.show()
                self.label_3.show()
                self.label_4.show()
                self.label_5.show()
                self.label_11.show()
                self.label_12.show()
                self.label_13.show()
                self.label_14.show()
                self.label_15.show()
                self.label_16.show()
                
                self.label_10.hide()
                self.browse_meta.hide()
                self.meta_filename.hide()
    #def read_data_other(self):
        
    def val_hide(self):
        self.max_rad_blue.hide()
        self.min_rad_blue.hide()
        self.max_pixel_blue.hide()
        self.min_pixel_blue.hide()
        self.max_rad_green.hide()
        self.min_rad_green.hide()
        self.max_pixel_green.hide()
        self.min_pixel_green.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_14.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.label_10.show()
        self.browse_meta.show()
        self.meta_filename.show()
        
        
    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Fill in all the required values")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    def showdialog1(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Specify the file names")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    def showdialogcheck(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Check at least one of the boxes")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    def pressed_dii(self):
        global isColour,isGrayscale
        isColour = 0
        isGrayscale = 0
        if (not self.blue_filename.text())or(not self.green_filename.text())or(not self.ir_filename_2.text()):
                self.showdialog1()
        elif (self.datatype_8.isChecked() == False)and(self.datatype_16.isChecked() == False):
			self.showdialogcheck()
                
        else:
            if  self.image_type.currentText()=="Other":
                               
                if (not self.max_rad_blue.text())or(not self.min_rad_blue.text())or(not self.max_pixel_blue.text())or(not self.min_pixel_blue.text()):
                    self.showdialog()
                elif (not self.max_rad_green.text())or(not self.min_rad_green.text())or(not self.max_pixel_green.text())or(not self.min_pixel_green.text()):
                    self.showdialog()
                else:
                    imgread()
                    self.window = QtGui.QMainWindow()
                    self.ui_2= Ui_MainWindow2()
                    self.ui_2.setupUi(self.window)
                    self.window.show()
                    
            else:
                if not self.meta_filename.text():
                    self.showdialog1()
                else:
                    fileread()
                    imgread()
                    self.window = QtGui.QMainWindow()
                    self.ui_2= Ui_MainWindow2()
                    self.ui_2.setupUi(self.window)
                    self.window.show()
    def pressed_depth(self):
        #sys.exit(app.exec_())
        global isColour,isGrayscale
        isColour = 0
        isGrayscale = 0
       
        if (not self.blue_filename.text())or(not self.green_filename.text())or(not self.ir_filename_2.text()):
                self.showdialog1()
        elif (self.datatype_8.isChecked() == False)and(self.datatype_16.isChecked() == False):
			self.showdialogcheck()        
        else:
            if  self.image_type.currentText()=="Other":
                               
                if (not self.max_rad_blue.text())or(not self.min_rad_blue.text())or(not self.max_pixel_blue.text())or(not self.min_pixel_blue.text()):
                    self.showdialog()
                elif (not self.max_rad_green.text())or(not self.min_rad_green.text())or(not self.max_pixel_green.text())or(not self.min_pixel_green.text()):
                    self.showdialog()
                else:
                    imgread()
                    self.window3 = QtGui.QMainWindow()
                    self.ui_3= Ui_MainWindow3()
                    self.ui_3.setupUi(self.window3)
                    self.window3.show()
                    
            else:
                if not self.meta_filename.text():
                    self.showdialog1()
                else:
                    fileread()
                    imgread()
                    self.window3 = QtGui.QMainWindow()
                    self.ui_3= Ui_MainWindow3()
                    self.ui_3.setupUi(self.window3)
                    self.window3.show()
        
       
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Bathymetry Tool", None))
        self.label_6.setText(_translate("MainWindow", "Select the blue band image", None))
        self.label_8.setText(_translate("MainWindow", "Select the green band image", None))
        self.label_7.setText(_translate("MainWindow", "Select the NIR band image", None))
        self.label_10.setText(_translate("MainWindow", "Select the metadata file", None))
        self.browse_blue.setText(_translate("MainWindow", "Browse file", None))
        self.browse_green.setText(_translate("MainWindow", "Browse file", None))
        self.browse_ir.setText(_translate("MainWindow", "Browse file", None))
        self.browse_meta.setText(_translate("MainWindow", "Browse file", None))
        self.label_2.setText(_translate("MainWindow", "Maximum Radiance value", None))
        self.label_3.setText(_translate("MainWindow", "Minimum Radiance value", None))
        self.label_4.setText(_translate("MainWindow", "Maximum Pixel value       ", None))
        self.label_5.setText(_translate("MainWindow", "Minimum Pixel value       ", None))
        self.label_11.setText(_translate("MainWindow", "Maximum Radiance value", None))
        self.label_12.setText(_translate("MainWindow", "Minimum Radiance value", None))
        self.label_13.setText(_translate("MainWindow", "Maximum Pixel value       ", None))
        self.label_14.setText(_translate("MainWindow", "Minimum Pixel value        ", None))
        self.label_15.setText(_translate("MainWindow", "Blue Band", None))
        self.label_16.setText(_translate("MainWindow", "Green Band", None))
        #self.label.setText(_translate("MainWindow", "Enter the threshold for separating land and water in IR band ", None))
        #self.histogram.setText(_translate("MainWindow", "Use Histogram ", None))
        self.label_9.setText(_translate("MainWindow", "Image type:       ", None))
        self.datatype_8.setText(_translate("MainWindow", "8 bit", None))
        self.datatype_16.setText(_translate("MainWindow", "16 bit", None))
        # self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        # self.actionNew.setText(_translate("MainWindow", "New", None))
        # self.actionSave.setText(_translate("MainWindow", "Save", None))
        # self.actionExit.setText(_translate("MainWindow", "Exit", None))

def set_blue_filename(text):
		global bluefile 
		bluefile = text
		
def set_green_filename(text):
		global greenfile
		greenfile = text
def set_ir_filename(text):
		global nirfile 
		nirfile = text
def set_meta_filename(text):
		global meta 
		meta = text
def set_maxrad_blue(text):
                global radmax1
                radmax1 = float(text)
                
def set_minrad_blue(text):
                global radmin1
                radmin1 = float(text)
               
def set_maxpix_blue(text):
                global qcalmax1
                qcalmax1 = float(text)
               
def set_minpix_blue(text):
                global qcalmin1
                qcalmin1 = float(text)
                
def set_maxrad_green(text):
                global radmax2
                radmax2 = float(text)
               
def set_minrad_green(text):
                global radmin2
                radmin2 = float(text)
               
def set_maxpix_green(text):
                global qcalmax2
                qcalmax2 = float(text)
                
def set_minpix_green(text):
                global qcalmin2
                qcalmin2 = float(text)
                
def set_radio(n):
    global bit
    bit=n

#Starting point of WCC	
def start_dinv():
        global targetdir,logfile,log
        logfile = targetdir + os.path.sep + logfile + ".txt"
        log = open(unicode(logfile),'w')
        log.write (str(time.clock())+ ": DII Processing started\n")
        landcut()
        calc_rad()
        calc_log()
        wcc()
        if(isColour):
			savediicolor()
        if(isGrayscale):
			savediigray()
        log.write (str(time.clock())+ ": DII Processing ended\n")

#Differtiates metadata between LandSat 5,7 and 8		
def fileread():
	global metafile,meta
	metafile = open(meta,"r")
	satid = "SPACECRAFT_ID"
	for line in metafile:
		if satid in line.split():
			line = line.split()
			satname = line[2].replace("\"","")
			if satname == "LANDSAT_5":
				l5read()
			elif satname == "Landsat7":
				l7read()
			elif satname == "LANDSAT_8":
				l8read()

#Assign Metadata variables for LandSat 8				
def l8read():
	global radmax1f, radmin1f, radmax2f, radmin2f, qcalmax1f, qcalmin1f, qcalmax2f, qcalmin2f, bluename, greenname, nirname
	radmax1f = "RADIANCE_MAXIMUM_BAND_2"
	radmin1f = "RADIANCE_MINIMUM_BAND_2"
	radmax2f = "RADIANCE_MAXIMUM_BAND_3"
	radmin2f = "RADIANCE_MINIMUM_BAND_3"
	qcalmax1f = "QUANTIZE_CAL_MAX_BAND_2"
	qcalmin1f = "QUANTIZE_CAL_MIN_BAND_2"
	qcalmax2f = "QUANTIZE_CAL_MAX_BAND_3"
	qcalmin2f = "QUANTIZE_CAL_MIN_BAND_3"
	pickdata()

#Assign Metadata variables for LandSat 7	
def l7read():
	global radmax1f, radmin1f, radmax2f, radmin2f, qcalmax1f, qcalmin1f, qcalmax2f, qcalmin2f, bluename, greenname, nirname
	qcalmax1f = "QCALMAX_BAND1"
	qcalmin1f = "QCALMIN_BAND1"
	qcalmax2f = "QCALMAX_BAND2"
	qcalmin2f = "QCALMIN_BAND2"
	radmax1f = "LMAX_BAND1"
	radmin1f = "LMIN_BAND1"
	radmax2f = "LMAX_BAND2"
	radmin2f = "LMIN_BAND2"
	pickdata()

#Assign Metadata variables for LandSat 5	
def l5read():
	global radmax1f, radmin1f, radmax2f, radmin2f, qcalmax1f, qcalmin1f, qcalmax2f, qcalmin2f, bluename, greenname, nirname
	qcalmax1f = "QUANTIZE_CAL_MAX_BAND_1"
	qcalmin1f = "QUANTIZE_CAL_MIN_BAND_1"
	qcalmax2f = "QUANTIZE_CAL_MAX_BAND_2"
	qcalmin2f = "QUANTIZE_CAL_MIN_BAND_2"
	radmax1f = "RADIANCE_MAXIMUM_BAND_1"
	radmin1f = "RADIANCE_MINIMUM_BAND_1"
	radmax2f = "RADIANCE_MAXIMUM_BAND_2"
	radmin2f = "RADIANCE_MINIMUM_BAND_2"
	pickdata()

#Picks data from metadata file
def pickdata():
	global qcalmax1, qcalmin1, qcalmax2, qcalmin2, radmax1, radmin1, radmax2, radmin2, bluefile, greenfile, nirfile,metafile
	global radmax1f, radmin1f, radmax2f, radmin2f, qcalmax1f, qcalmin1f, qcalmax2f, qcalmin2f, bluename, greenname, nirname
	for line in metafile:
		if qcalmax1f in line.split():
			line = line.split()
			qcalmax1 = line[2]
		elif qcalmin1f in line.split():
			line = line.split()
			qcalmin1 = line[2]
		elif qcalmax2f in line.split():
			line = line.split()
			qcalmax2 = line[2]
		elif qcalmin2f in line.split():
			line = line.split()
			qcalmin2 = line[2]
		elif radmax1f in line.split():
			line = line.split()
			radmax1 = line[2]
		elif radmin1f in line.split():
			line = line.split()
			radmin1 = line[2]
		elif radmax2f in line.split():
			line = line.split()
			radmax2 = line[2]
		elif radmin2f in line.split():
			line = line.split()
			radmin2 = line[2]
			
	qcalmax1 = float(qcalmax1)
	qcalmax2 = float(qcalmax2)
	qcalmin1 = float(qcalmin1)
	qcalmin2 = float(qcalmin2)
	radmax1 = float(radmax1)
	radmax2 = float(radmax2)
	radmin1 = float(radmin1)
	radmin2 = float(radmin2)

#Loads Satellite Images into numpy arrays	
def imgread():
	global blue,green,ir,img1,img2,img3
	blue = rasterio.open(unicode(bluefile))
	green = rasterio.open(unicode(greenfile))
	nir = rasterio.open(unicode(nirfile))
	
	global img1,img2,img3
	img1 = blue.read()
	img2 = green.read()
	img3 = nir.read()

#Land Masking from all 3 bands	
def landcut():
	global log
	log.write (str(time.clock())+ ": Land clipping started\n")
	log.write ("Threshold DN value for land-sea separation: {}\n".format(limit))
	global img3,img1,img2
	img3 = ma.masked_less_equal(img3,0)
	img3 = ma.masked_greater(img3,limit)
	img3 = img3.filled(2**bit - 1)
	img3 = ma.masked_less_equal(img3,limit)
	img3 = img3.filled(0)
	img3 = ma.masked_greater(img3,limit)
	img3 = img3.filled(1)
	
	img1 = ma.masked_array(img1,mask=img3)
	img1 = ma.masked_equal(img1,0)
	img2 = ma.masked_array(img2,mask=img3)
	img2 = ma.masked_equal(img2,0)

#Pixel Radiance Calculation & Atmospheric Correction	
def calc_rad():
	global log, qcalmax1, qcalmin1, qcalmax2, qcalmin2, radmax1, radmin1, radmax2, radmin2,img1,img2
	log.write (str(time.clock())+  (": Conversion to radiance started\n"))
	
	img1 = ((radmax1) -  (radmin1))*(img1 - (qcalmin1))/((qcalmax1) - (qcalmin1)) 
	img2 = ((radmax2) -  (radmin2))*(img2 - (qcalmin2))/((qcalmax2) - (qcalmin2)) 

#Pixel log value calculation	
def calc_log():
	global img1,img2,radmax1,radmax2,log
	log.write (str(time.clock())+  (": Conversion to radiance started\n"))
	
	img1 = img1.filled(2*radmax1)
	img1 = ma.masked_less_equal(img1,0)
	img1 = img1.filled(1)
	img1 = ma.masked_equal(img1,2*radmax1)
	img2 = img2.filled(2*radmax2)
	img2 = ma.masked_less_equal(img2,0)
	img2 = img2.filled(1)
	img2 = ma.masked_equal(img2,2*radmax2)
	img1 = np.log(img1)
	img2 = np.log(img2)

#Water Column Correction	
def wcc():
        global log, img1,img2
	log.write (str(time.clock())+  (": Water Column Correction started\n"))
	sigma1 = np.var(img1)
	log.write ("Variance of blue band: {}\n".format(sigma1))
	sigma2 = np.var(img2)
	log.write ("Variance of green band: {}\n".format(sigma2))
	mean1 = np.mean(img1)
	log.write ("Mean of blue band: {}\n".format(mean1))
	mean2 = np.mean(img2)
	log.write ("Mean of green band: {}\n".format(mean2))
	
	mean3 = np.mean(img1 * img2)
	cov = mean3 - (mean1 * mean2)
	log.write ("Covariance of both bands: {}\n".format(cov))
	a = (sigma1 - sigma2)/(2*cov)
	att = a + (a**2 + 1)**0.5
	log.write ("Ratio of attenuation coefficients (k_blue/k_green): {}\n".format(att))
	
	global dinv
	dinv = img1 - (att * img2)

#Export colormap of depth invariant index values
def savediicolor():
	global log, targetdir, col_filename
	log.write (str(time.clock())+ ": Saving colormap started\n")
	col_filename = unicode(targetdir + os.path.sep + col_filename + ".png")
	log.write ("Colormap path: " + col_filename + "\n")
	plt.figure()
	colormap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',['violet','indigo','blue','green','yellow','orange','red'],256)
	colorimg = plt.imshow(dinv[0],interpolation='nearest', cmap=colormap ,origin='lower')
	plt.colorbar(colorimg,cmap=colormap)
	plt.savefig(col_filename)
	plt.show()
	

#Export scaled grayscale map of depth invariant index values
def savediigray():
	global log, targetdir, gray_filename, dinv
	log.write (str(time.clock())+": Saving graymap started\n")
	file_name = unicode(targetdir + os.path.sep + gray_filename + ".tif")
	log.write ("Greyscale file path: " + file_name + "\n")
	dinvmax = np.nanmax(dinv)
	dinvmin = np.nanmin(dinv)
	log.write ("Max. measured depth invariant index: {} was scaled to {}\n".format(dinvmax,2**bit-1))
	log.write ("Min. measured depth invariant index: {} was scaled to {}\n".format(dinvmin,1))
	dinv = (2**bit - 1)*(dinv - dinvmin)/(dinvmax - dinvmin) 
	dinv = dinv.filled(2**bit - 1)
	if bit==16:
		dinv = dinv.astype(np.uint16)
		type = 'uint16' 
	else:
		dinv = dinv.astype(np.uint8)
		type = 'uint8'
	dst = rasterio.open(file_name, 'w', driver = 'Gtiff',width = blue.width, height = blue.height, count = 1, dtype = type,crs = blue.crs, transform = blue.transform) 
	dst.write(dinv)
	dst.close()

	
#Window for Depth Invariant Index Processing
class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(601, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 100, 521, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.out_dir = QtGui.QLineEdit(self.widget)
        self.out_dir.setObjectName(_fromUtf8("out_dir"))
        self.out_dir.textChanged.connect(set_outdir)
        self.horizontalLayout.addWidget(self.out_dir)
        self.browse_directory = QtGui.QPushButton(self.widget)
        self.browse_directory.setObjectName(_fromUtf8("browse_directory"))
        self.horizontalLayout.addWidget(self.browse_directory)
        '''self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 90, 291, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.browse_directory = QtGui.QPushButton(self.layoutWidget)
        self.browse_directory.setObjectName(_fromUtf8("browse_directory"))'''
        self.browse_directory.clicked.connect(self.browse_dir)
        validator = QtGui.QDoubleValidator()
        validator.setRange(-100000,100000)
        self.horizontalLayout.addWidget(self.browse_directory)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 30, 523, 25))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ir_threshold = QtGui.QLineEdit(self.layoutWidget_2)
        self.ir_threshold.setObjectName(_fromUtf8("ir_threshold"))
        self.ir_threshold.setValidator(validator)
        self.ir_threshold.textChanged.connect(self.set_ir_threshold)
        
        self.horizontalLayout_2.addWidget(self.ir_threshold)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.histogram = QtGui.QPushButton(self.layoutWidget_2)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.histogram.clicked.connect(self.show_histogram)
        
        self.horizontalLayout_5.addWidget(self.histogram)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 180, 404, 19))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.select_grayscale = QtGui.QCheckBox(self.widget)
        self.select_grayscale.setObjectName(_fromUtf8("select_grayscale"))
        self.select_grayscale.toggled.connect(self.set_grayscale)
        
        self.horizontalLayout_3.addWidget(self.select_grayscale)
        self.select_colour = QtGui.QCheckBox(self.widget)
        self.select_colour.setObjectName(_fromUtf8("select_colour"))
        self.select_colour.toggled.connect(self.set_colour)
        
        self.horizontalLayout_3.addWidget(self.select_colour)
        self.compute = QtGui.QPushButton(self.centralwidget)
        self.compute.setGeometry(QtCore.QRect(260, 370, 75, 23))
        self.compute.setObjectName(_fromUtf8("compute"))
        self.compute.clicked.connect(self.pressed_compute)
        
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(90, 260, 381, 80))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.grayscale_filename = QtGui.QLineEdit(self.widget1)
        self.grayscale_filename.setObjectName(_fromUtf8("grayscale_filename"))
        self.grayscale_filename.textChanged.connect(grayscale_filename)
        
        self.horizontalLayout_6.addWidget(self.grayscale_filename)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.grayscale_logfile = QtGui.QLineEdit(self.widget1)
        self.grayscale_logfile.setObjectName(_fromUtf8("grayscale_logfile"))
        self.grayscale_logfile.textChanged.connect(log_filename)

        self.horizontalLayout_7.addWidget(self.grayscale_logfile)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.colour_filename = QtGui.QLineEdit(self.widget1)
        self.colour_filename.setObjectName(_fromUtf8("colour_filename"))
        self.colour_filename.textChanged.connect(colour_filename)
        self.proc_label = QtGui.QLabel(self.centralwidget)
        self.proc_label.setGeometry(QtCore.QRect(210, 410, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proc_label.setFont(font)
        self.proc_label.setObjectName(_fromUtf8("proc_label"))
        self.proc_label.hide()
        
        self.horizontalLayout_8.addWidget(self.colour_filename)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def pressed_compute(self):
        if (not self.grayscale_logfile.text())or(not self.ir_threshold.text())or (not self.out_dir.text()):
            self.showdialogerr()
        elif (self.select_grayscale.isChecked() == False)and(self.select_colour.isChecked() == False):
			self.showdialogcheck()
        elif (self.select_grayscale.isChecked() == True)and(not self.grayscale_filename.text()):
			self.showdialogerr()
        elif (self.select_colour.isChecked() == True)and(not self.colour_filename.text()):
			self.showdialogerr()
        else:
            self.proc_label.show()
            start_dinv()
            self.proc_label.hide()
            self.showdialogfin()
            sys.exit(app.exec_())

    def showdialogfin(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("The output image files have been created and saved")
        
        msg.setWindowTitle("Done")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def showdialogerr(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Fill all the details required")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def showdialogcheck(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Check at least one of the boxes")
        
        msg.setWindowTitle("Error")
        
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
	
   
    
	
    def set_grayscale(self):
        global isGrayscale
        if self.select_grayscale.isChecked() == True:
            isGrayscale = 1;
            self.grayscale_filename.show()
            self.label_4.show()
        else:
            isGrayscale = 0;
            self.grayscale_filename.hide()
            self.label_4.hide()
       

    def set_colour(self):
        global isColour
        if self.select_colour.isChecked() == True:
            isColour = 1;
            self.colour_filename.show()
            self.label_6.show()
        else:
            isColour = 0;
            self.colour_filename.hide()
            self.label_6.hide()

    def browse_dir(self):
        global targetdir
        targetdir = QFileDialog.getExistingDirectory()
        self.out_dir.setText(targetdir)
        
        

    def set_ir_threshold(self,text):
                global limit
                limit = float(text)
                
                self.ir_threshold.setText(text)
    def show_histogram(self):
        global img3, qcalmax1, qcalmin1
        heights,edges = np.histogram(img3,int(qcalmax1-qcalmin1+1),(qcalmin1,qcalmax1))
        edges = edges[:-1]+(edges[1]-edges[0])
        fig, ax = plt.subplots()
        ax.plot(edges,heights)
        ax.set(title='Click Once', xlabel='Pixel value', ylabel='Frequency')
        point1 = fig.ginput(1)
        lim = point1[0][0]
        self.ir_threshold.setText(str(lim))
        plt.close(fig)
        
            

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Water Column Correction", None))
        self.label.setText(_translate("MainWindow", "Select target folder for output file", None))
        self.browse_directory.setText(_translate("MainWindow", "Browse directory", None))
        self.label_2.setText(_translate("MainWindow", "Enter the threshold for separating land and water in IR band ", None))
        self.histogram.setText(_translate("MainWindow", "Use Histogram ", None))
        self.label_3.setText(_translate("MainWindow", "Output as:", None))
        self.select_grayscale.setText(_translate("MainWindow", "Grayscale map(original resolution)", None))
        self.select_colour.setText(_translate("MainWindow", "Colour map(less resolution)", None))
        self.compute.setText(_translate("MainWindow", "Compute", None))
        self.label_4.setText(_translate("MainWindow", "Grayscale filename      ", None))
        self.label_5.setText(_translate("MainWindow", "Grayscale log filename", None))
        self.label_6.setText(_translate("MainWindow", "Colour filename           ", None))
        self.proc_label.setText(_translate("MainWindow", "PROCESSING...", None))


def grayscale_filename(text):
    global gray_filename
    gray_filename = text
    

def colour_filename(text):
    global col_filename
    col_filename = text
    

def log_filename(text):
    global logfile
    logfile = text
	
def set_outdir(text):
	global targetdir
	targetdir = unicode(text)

def set_georefimg(text):
	global grefimg
	grefimg = unicode(text)

def set_pointsfname(text):
	global pointsfname
	pointsfname = unicode(text)
    
    




if __name__ == "__main__":
    import sys
    global log
    time1 = time.clock()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    time2 = time.clock()
    log.write( "Time taken is " + str(time2 - time1) + "\n")
    log.close()



    
    
