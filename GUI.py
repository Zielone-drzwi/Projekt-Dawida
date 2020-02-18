from PyQt5 import  QtWidgets, uic
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())* 1.23))

app  = QtWidgets.QApplication([])
dlg = uic.loadUi("test.ui")

dlg.pushButton.clicked.connect(Convert)

dlg.tableWidget.setRowCount(4)
dlg.tableWidget.setColumnCount(2)
dlg.show()
app.exec()