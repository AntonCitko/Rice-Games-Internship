import sys

#from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5 import QtCore, QtWidgets, QtGui, uic
#from PyQt5.QtGui import QIcon


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random

import sys

import os
import glob

import pandas as pd

#getting csv files
os.chdir("/Users/Anton/Documents/GitHub/Rice-Games-Internship/Session 4P - Data Analytics & Digital Marketing")
extension = 'csv'
result = glob.glob('*.{}'.format(extension))

result = ["Make Selection"] + result

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Web Analytics'
        self.width = 800
        self.height = 800
        
        self.selected = False
        self.option = "Make Selection"
        
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QtWidgets.QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500,500)
        button.resize(140,100)
        
        _translate = QtCore.QCoreApplication.translate
        label = QtWidgets.QLabel(self)
        label.setObjectName("label")
        label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Welcome to Web Data Analyzer</span></p></body></html>"))
        label.move(230, 10)
        label.resize(400, 50)
        
        label2 = QtWidgets.QLabel(self)
        label2.setObjectName("label2")
        label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Select a file to analyze</span></p></body></html>"))
        label2.move(315, 35)
        label2.resize(400, 50)
        
        comboBox = QtWidgets.QComboBox(self)
        for x in result:      
            comboBox.addItem(x)
        comboBox.resize(300, 30)
        comboBox.move(250, 70)
        comboBox.currentIndexChanged.connect(self.selectionchange)
        
#        self.m = PlotCanvas(self, width=5, height=4)
#        self.m.move(0,300)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.plot_widget = QtWidgets.QWidget(self)
        self.plot_widget.setGeometry(0, 100, 800, 700)
        plot_box = QtWidgets.QVBoxLayout()
        plot_box.addWidget(self.canvas)
        self.plot_widget.setLayout(plot_box)
        self.figure.clf()

        self.show()
    
    def selectionchange(self,i):
          self.option = result[i]
          self.selected = True
          
          self.update()
          
          self.plot()
    
    def plot(self):
        self.figure.clf()
        if self.option == "freq-rec.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            plt.bar(data["Count of Sessions"], data["Sessions"])
            
        if self.option == "acqusition-overview-a.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            plt.bar(data["Default Channel Grouping"], data["Users"])
        
#        if self.option == "audience-overview.csv":
#            data = pd.read_csv("audience-overview.csv", skiprows = 5, thousands = ",")
#            data.drop(data.tail(1).index,inplace=True)
#    
#            plt.xticks(rotation = 90)
#            plt.plot(data["Day Index"], data["Users"])
            
        if self.option == "audience-overview.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            data["Day Index"] = pd.to_datetime(data["Day Index"])
            data["cum_tot"] = data["Users"].cumsum()
            
            plt.xticks(rotation = 90)
            plt.plot(data["Day Index"], data["cum_tot"])
            
        if self.option == "location-b.csv":
            

        if self.option == "cohort-analysis.csv":
            data = [random.random() for i in range(25)]
            ax = self.figure.add_subplot(111)
            ax.plot(data, 'r-')
            ax.set_title('PyQt Matplotlib Example')
        
        self.canvas.draw()

#class PlotCanvas(FigureCanvas):
#    def __init__(self, parent=None, width=5, height=4, dpi=100):
#        fig = Figure(figsize=(width, height), dpi=dpi)
#        self.axes = fig.add_subplot(111)
#        
#        FigureCanvas.__init__(self, fig)
#        self.setParent(parent)
#
#        FigureCanvas.setSizePolicy(self,
#                QtWidgets.QSizePolicy.Expanding,
#                QtWidgets.QSizePolicy.Expanding)
#        FigureCanvas.updateGeometry(self)
#        
#        print(parent.option)
#        self.op = parent.option
#        
#        self.plot()
#
#
#    def plot(self):
#        self.axes.clear()
#        if self.op == "Make Selection":
#            pass
#        else:
#            if self.op == "cohort-analysis.csv":
#                skip_rows = 9
#            else:
#                skip_rows = 5
#            
#            print(skip_rows)
#            print("plot function called")
#            
#            data = [random.random() for i in range(25)]
#            ax = self.figure.add_subplot(111)
#            ax.plot(data, 'r-')
#            ax.set_title('PyQt Matplotlib Example')
#            self.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    
    sys.exit(app.exec_())

