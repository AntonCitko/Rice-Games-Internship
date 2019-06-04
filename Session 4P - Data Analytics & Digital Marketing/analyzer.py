from PyQt5 import QtCore, QtWidgets, QtGui, uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
            plt.xlabel("Count of Sessions")
            plt.ylabel("Sessions")
            
        if self.option == "acqusition-overview-a.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            plt.bar(data["Default Channel Grouping"], data["Users"])
            plt.xlabel("Channel Grouping")
            plt.ylabel("Number of Users")
            
        if self.option == "audience-overview.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            data["Day Index"] = pd.to_datetime(data["Day Index"])
            data["cum_tot"] = data["Users"].cumsum()
            
            plt.xticks(rotation = 90)
            plt.plot(data["Day Index"], data["cum_tot"])
            plt.xlabel("Day")
            plt.ylabel("Cumulative Number of Users")
            
        if self.option == "location-b.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            plt.bar(data.loc[data["Users"] > 50, "Country"], data.loc[data["Users"] > 50, "Users"])
            plt.xticks(rotation = 90)
            plt.xlabel("Country")
            plt.ylabel("Number of Users")
            
        if self.option == "location-a.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            plt.bar(data.loc[data["Users"] > 10, "Country"], data.loc[data["Users"] > 10, "Users"])
            plt.xticks(rotation = 90)
            plt.xlabel("Country")
            plt.ylabel("Number of Users")

        if self.option == "acquisition-overview-b.csv":
            data = pd.read_csv(self.option, skiprows = 5, thousands = ",")
            data.drop(data.tail(1).index,inplace=True)
            
            plt.bar(data["Default Channel Grouping"], data["Users"])
            plt.xlabel("Channel Grouping")
            plt.ylabel("Number of Users")

        if self.option == "cohort-analysis.csv":
            data = pd.read_csv(self.option, skiprows = 11, thousands = ",", header = 0)
            data = data.iloc[0,2:10]
            data = data.apply(lambda x : x.strip("%"))
            data = data.astype(float)
            
            plt.plot(range(0, len(data)), data)
            plt.xlabel("Day")
            plt.ylabel("Overall User Retention (% Return)")

        self.canvas.draw()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    
    sys.exit(app.exec_())

