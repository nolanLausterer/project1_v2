from PyQt5.QtWidgets import *
from gui import *
from PyQt5.QtGui import QPixmap

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.label_9.setHidden(True)
        self.label_5.setHidden(True)
        self.label_7.setHidden(True)
        self.label_6.setHidden(True)
        self.textBrowser.setHidden(True)
        self.pushButton.clicked.connect(lambda: self.calculate())
        self.pushButton_2.clicked.connect(lambda: self.clear())
        '''
        This function constructs the GUI object and assigns the initial values
        '''

    def gradeScale(self, percent: int) -> float:
        points = 0
        if percent >= 93:
            points = 4.0
        elif percent >= 90:
            points = 3.67
        elif percent >= 87:
            points = 3.33
        elif percent >= 83:
            points = 3.0
        elif percent >= 80:
            points = 2.67
        elif percent >= 77:
            points = 2.33
        elif percent >= 73:
            points = 2.00
        elif percent >= 70:
            points = 1.67
        elif percent >= 67:
            points = 1.33
        elif percent >= 63:
            points = 1.0
        elif percent >= 60:
            points = .67
        else:
            points = 0

        '''
        This function accepts a percentage and returns the corresponding grade point average 
        for the passed value  
        
        :param percent: percent number value.
        '''
        return points


    def calculate(self):
        classNum = self.spinBox.value()
        grade = 0
        try:
            if classNum == 1:
                grade = self.gradeScale(int(self.lineEdit_2.text()))
            if classNum == 2:
                grade = (self.gradeScale(int(self.lineEdit_2.text())) + self.gradeScale(int(self.lineEdit_10.text()))) / classNum
            if classNum == 3:
                grade = (self.gradeScale(int(self.lineEdit_2.text())) + self.gradeScale(int(self.lineEdit_10.text())) + self.gradeScale(int(self.lineEdit_11.text())) ) / classNum

            if classNum == 4:
                grade = (self.gradeScale(int(self.lineEdit_2.text())) + self.gradeScale(int(self.lineEdit_10.text())) + self.gradeScale(int(self.lineEdit_11.text())) + self.gradeScale(int(self.lineEdit_12.text())) ) / classNum

            if classNum == 5:
                grade = (self.gradeScale(int(self.lineEdit_2.text())) + self.gradeScale(int(self.lineEdit_10.text())) + self.gradeScale(int(self.lineEdit_11.text())) + self.gradeScale(int(self.lineEdit_12.text())) + self.gradeScale(int(self.lineEdit_13.text())) ) / classNum

            if classNum == 6:
                grade = (self.gradeScale(int(self.lineEdit_2.text())) + self.gradeScale(int(self.lineEdit_10.text())) + self.gradeScale(int(self.lineEdit_11.text())) + self.gradeScale(int(self.lineEdit_12.text())) + self.gradeScale(int(self.lineEdit_13.text())) + self.gradeScale(int(self.lineEdit_14.text())) ) / classNum

            if classNum == 7:
                grade = (self.gradeScale(int(self.lineEdit_2.text())) + self.gradeScale(int(self.lineEdit_10.text())) + self.gradeScale(int(self.lineEdit_11.text())) + self.gradeScale(int(self.lineEdit_12.text())) + self.gradeScale(int(self.lineEdit_13.text())) + self.gradeScale(int(self.lineEdit_14.text())) + self.gradeScale(int(self.lineEdit_15.text())) ) / classNum

            if grade >= 3.5:
                self.label_7.setHidden(False)
                self.label_7.setPixmap(QtGui.QPixmap("Green_Smile_edit.png"))
            elif grade >= 2.5:
                self.label_7.setHidden(False)
                self.label_7.setPixmap(QtGui.QPixmap("yellow_edit.png"))
            else:
                self.label_7.setHidden(False)
                self.label_7.setPixmap(QtGui.QPixmap("red_sad.jpeg"))
                # sad smiley

            self.textBrowser.setHidden(True)
            self.label_9.setHidden(False)
            self.label_5.setHidden(False)
            self.label_6.setHidden(False)
            self.label_6.setText(f' {grade:.2f}')
            name = self.lineEdit_9.text()
            self.label_9.setText(f'Hello, {name}')


        except ValueError:
            self.textBrowser.setHidden(False)
            self.clear()
        '''
            This function calculates the GPA and outputs the corresponding graphics to the calculator
        '''

    def clear(self):
        self.lineEdit_2.setText('')
        #self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_14.setText('')
        self.lineEdit_15.setText('')
        self.spinBox.setValue(1)
        self.label_9.setHidden(True)
        self.label_5.setHidden(True)
        self.label_7.setHidden(True)
        self.label_6.setHidden(True)

        '''
            This function clears the inputs and outputs when the calculator is reset 
        '''