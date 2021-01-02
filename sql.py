import sys

from PyQt5.QtWidgets import (
    QApplication,QWidget,QLabel,QPushButton,
    QMainWindow,QStackedWidget,QFileDialog,QDesktopWidget,
    QTableWidget,QTableWidgetItem,QVBoxLayout,
    )

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sqlite3
from pathlib import Path

class Win(QMainWindow):
    def __init__ (self):
        super(Win,self).__init__()
        self.gui()
        self.center()


    def gui(self):

        widget = QWidget()
        self.b = QPushButton("Load")
        self.b.clicked.connect(self.load_table)



        self.table=QTableWidget()
        self.table.setMaximumSize(670,470)

        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        vbox.addWidget(self.b)

        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.setWindowTitle("SQl View")
        self.setWindowIcon(QIcon("sqlite3.png"))
        self.setFixedSize(700,500)
        self.show()


    def center(self):
        frame = self.frameGeometry()
        desk = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(desk)
        self.move(frame.topLeft())

    def load_table(self):
        path=Path()
        file_name = QFileDialog.getOpenFileName(self,"Open File",str(path))
        if file_name[0]:
            s=sqlite3.connect(file_name[0])
            cur = s.cursor()
            cur.execute("select username,password,email from auth_user")
            data = cur.fetchall()
            self.table.setRowCount(len(data)+1)
            self.table.setColumnCount(3)
            self.table.setItem(0,0,QTableWidgetItem("Username"))
            self.table.setItem(0,1,QTableWidgetItem("Password"))
            self.table.setItem(0,2,QTableWidgetItem("Email"))
            i=1
            for row in data:
                self.table.setItem(i,0,QTableWidgetItem(row[0]))
                self.table.setItem(i,1,QTableWidgetItem(row[1]))
                self.table.setItem(i,2,QTableWidgetItem(row[2]))
                i+=1


if __name__ == "__main__":
    app=QApplication(sys.argv)
    master = Win()
    sys.exit(app.exec_())
