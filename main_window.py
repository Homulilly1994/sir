from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox, QHBoxLayout
from matplotlib.backends.qt_compat import QtWidgets
import sys
import model

__author__ = 'makar'


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.s = 1000
        self.i = 3
        self.r = 0
        self.b = 0.09
        self.g = 0.05
        self.br = 0.003
        self.dr = 0.002
        self.f = 0.02
        self.qle = QtGui.QLineEdit(self)
        self.qle2 = QtGui.QLineEdit(self)
        self.qle3 = QtGui.QLineEdit(self)
        self.qle4 = QtGui.QLineEdit(self)
        self.qle5 = QtGui.QLineEdit(self)
        self.qle6 = QtGui.QLineEdit(self)
        self.qle7 = QtGui.QLineEdit(self)
        self.qle8 = QtGui.QLineEdit(self)
        self.create_ui()


    def about(self):
        QMessageBox.information(self, 'Information', "Tishkin Nikita\nMIEM HSE\n2015")

    def create_ui(self):
        self.setWindowTitle('virus spreding models')
        about = self.menuBar().addMenu('About')
        info = about.addAction('Info')
        info.triggered.connect(self.about)

        lbl = QtGui.QLabel(self)
        lb2 = QtGui.QLabel(self)
        lb3 = QtGui.QLabel(self)
        lb4 = QtGui.QLabel(self)
        lb5 = QtGui.QLabel(self)
        lb6 = QtGui.QLabel(self)
        lb7 = QtGui.QLabel(self)
        lb8 = QtGui.QLabel(self)
        lbl.setText("susceptibles")
        lb2.setText("infected")
        lb3.setText("recovered")
        lb4.setText("contact rate")
        lb5.setText("recover rate")
        lb6.setText("birth rate")
        lb7.setText("death rate")
        lb8.setText("loss imunity rate")
        lbl.move(lbl.width()/2-20, self.frameSize().height()/2-self.qle.height()*2.5)
        lb2.move(lbl.width()/2-20, self.frameSize().height()/2-self.qle.height()*1.5)
        lb3.move(lbl.width()/2-20, self.frameSize().height()/2-self.qle.height()*0.5)
        lb4.move(lbl.width()/2-20, self.frameSize().height()/2+self.qle.height()*0.5)
        lb5.move(lbl.width()/2-20, self.frameSize().height()/2+self.qle.height()*1.5)
        lb6.move(lbl.width()/2-20, self.frameSize().height()/2+self.qle.height()*2.5)
        lb7.move(lbl.width()/2-20, self.frameSize().height()/2+self.qle.height()*3.5)
        lb8.move(lbl.width()/2-20, self.frameSize().height()/2+self.qle.height()*4.5)

        lbl.setFixedWidth(150)
        lb2.setFixedWidth(150)
        lb3.setFixedWidth(150)
        lb4.setFixedWidth(150)
        lb5.setFixedWidth(150)
        lb6.setFixedWidth(150)
        lb7.setFixedWidth(150)
        lb8.setFixedWidth(150)

        self.qle.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2-self.qle.height()*2.5)
        self.qle2.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2-self.qle.height()*1.5)
        self.qle3.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2-self.qle.height()*0.5)
        self.qle4.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+self.qle.height()*0.5)
        self.qle5.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+self.qle.height()*1.5)
        self.qle6.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+self.qle.height()*2.5)
        self.qle7.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+self.qle.height()*3.5)
        self.qle8.move(lbl.width()+lbl.width()/2, self.frameSize().height()/2+self.qle.height()*4.5)

        self.qle.setText(str(self.s))
        self.qle2.setText(str(self.i))
        self.qle3.setText(str(self.r))
        self.qle4.setText(str(self.b))
        self.qle5.setText(str(self.g))
        self.qle6.setText(str(self.br))
        self.qle7.setText(str(self.dr))
        self.qle8.setText(str(self.f))

        self.qle.textChanged[str].connect(self.onChanged)
        self.qle2.textChanged[str].connect(self.onChanged2)
        self.qle3.textChanged[str].connect(self.onChanged3)
        self.qle4.textChanged[str].connect(self.onChanged4)
        self.qle5.textChanged[str].connect(self.onChanged5)
        self.qle6.textChanged[str].connect(self.onChanged6)
        self.qle7.textChanged[str].connect(self.onChanged7)
        self.qle8.textChanged[str].connect(self.onChanged8)

        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2-self.qle.height()*2.5, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        sld2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld2.setFocusPolicy(QtCore.Qt.NoFocus)
        sld2.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2-self.qle.height()*1.5, 100, 30)
        sld2.valueChanged[int].connect(self.changeValue2)
        sld3 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld3.setFocusPolicy(QtCore.Qt.NoFocus)
        sld3.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2-self.qle.height()*0.5, 100, 30)
        sld3.valueChanged[int].connect(self.changeValue3)
        sld4 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld4.setFocusPolicy(QtCore.Qt.NoFocus)
        sld4.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2+self.qle.height()*0.5, 100, 30)
        sld4.valueChanged[int].connect(self.changeValue4)
        sld5 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld5.setFocusPolicy(QtCore.Qt.NoFocus)
        sld5.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2+self.qle.height()*1.5, 100, 30)
        sld5.valueChanged[int].connect(self.changeValue5)
        sld6 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld6.setFocusPolicy(QtCore.Qt.NoFocus)
        sld6.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2+self.qle.height()*2.5, 100, 30)
        sld6.valueChanged[int].connect(self.changeValue6)
        sld7 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld7.setFocusPolicy(QtCore.Qt.NoFocus)
        sld7.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2+self.qle.height()*3.5, 100, 30)
        sld7.valueChanged[int].connect(self.changeValue7)
        sld8 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld8.setFocusPolicy(QtCore.Qt.NoFocus)
        sld8.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2+self.qle.height()*4.5, 100, 30)
        sld8.valueChanged[int].connect(self.changeValue8)

        button = QtGui.QPushButton('OK', self)
        button.clicked.connect(self.invalidate)
        button.setGeometry(lbl.width()+lbl.width()/2-110, self.frameSize().height()/2+self.qle.height()*5.5+50, 50, 30)
        self.invalidate()

    def changeValue(self, value):
        self.qle.setText(str(value*100))
        self.onChanged(value*100)

    def changeValue2(self, value):
        self.qle2.setText(str(value*10))
        self.onChanged2(value*10)

    def changeValue3(self, value):
        self.qle3.setText(str(value*100))
        self.onChanged3(value*100)

    def changeValue4(self, value):
        self.qle4.setText(str(value/100))
        self.onChanged4(value/100)

    def changeValue5(self, value):
        self.qle5.setText(str(value/100))
        self.onChanged5(value/100)

    def changeValue6(self, value):
        self.qle6.setText(str(value/100))
        self.onChanged6(value/100)

    def changeValue7(self, value):
        self.qle7.setText(str(value/1000))
        self.onChanged7(value/1000)

    def changeValue8(self, value):
        self.qle8.setText(str(value/100))
        self.onChanged8(value/100)

    def onChanged(self, text):
        self.s = text

    def onChanged2(self, text):
        self.i = text

    def onChanged3(self, text):
        self.r = text

    def onChanged4(self, text):
        self.b = text

    def onChanged5(self, text):
        self.g = text

    def onChanged6(self, text):
        self.br = text

    def onChanged7(self, text):
        self.dr = text

    def onChanged8(self, text):
        self.f = text

    def invalidate(self):
        grapher = model.Model(self.s, self.i, self.r, self.b, self.g, self.br, self.dr, self.f)
        grapher.create_graph()
        i_lable1 = QtGui.QLabel(self)
        myPixmap = QtGui.QPixmap('sir.png')
        myScaledPixmap = myPixmap.scaled(320, 270, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        i_lable1.setPixmap(myScaledPixmap)
        i_lable1.setGeometry(370, 105, 320, 270)
        i_lable1.show()

        i_lable2 = QtGui.QLabel(self)
        myPixmap2 = QtGui.QPixmap('sir2.png')
        myScaledPixmap2 = myPixmap2.scaled(320, 270, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        i_lable2.setPixmap(myScaledPixmap2)
        i_lable2.setGeometry(690, 105, 320, 270)
        i_lable2.show()

        i_lable3 = QtGui.QLabel(self)
        myPixmap3 = QtGui.QPixmap('sir3.png')
        myScaledPixmap3 = myPixmap3.scaled(320, 270, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        i_lable3.setPixmap(myScaledPixmap3)
        i_lable3.setGeometry(370, 350, 320, 270)
        i_lable3.show()

        i_lable4 = QtGui.QLabel(self)
        myPixmap4 = QtGui.QPixmap('sir4.png')
        myScaledPixmap4 = myPixmap4.scaled(320, 270, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        i_lable4.setPixmap(myScaledPixmap4)
        i_lable4.setGeometry(690, 350, 320, 270)
        i_lable4.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowIcon(QtGui.QIcon('icon.png'))
    window.setGeometry(0, 200, 900, 500)
    sys.exit(app.exec_())