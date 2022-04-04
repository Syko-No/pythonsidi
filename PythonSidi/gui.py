import sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget, QPushButton, QLabel, QFrame, QDialog
from PyQt5.QtGui import QPixmap
import game

up_downs = [(7,14),(8,-4),(10,18),(13,-9),(16,23),(17,-15),(22,-12),(24,-6)]
b1 = game.Board(up_downs)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,1400,600)
        self.setWindowTitle("SnakeLadder")
        
        grid = QGridLayout()
        grid2 = QGridLayout()
        grid3 = QGridLayout()

        hbox = QHBoxLayout()

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(grid2)
        hbox.addLayout(vbox)

        self.lbl = [QLabel(f"{i}") for i in range(1,26)]
        for label in self.lbl:
            label.setStyleSheet("background: grey")
        
        btn = QPushButton("Play")
        btn.clicked.connect(move)
        btn.setMaximumWidth(100)
        grid2.addWidget(btn,5,0)

        image_path = 'Atom//python//board.png'
        board = QPixmap(image_path)
        board_label = QLabel(self)
        board_label.setPixmap(board)
        hbox.addWidget(board_label)
        

        # reset = QPushButton("Reset")
        # reset.clicked.connect(self.reset_color)
        # grid2.addWidget(reset,5,1)
        # def reset():
        #     self.reset_color()
        #     game.Player.reset()
        #     win.text.setText(" ")

        self.text = QLabel()
        grid2.addWidget(self.text,5,1)
        # grid2.setColumnStretch(0,1)

        for label in self.lbl:
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setStyleSheet("background-color: grey; border: 1px solid black;")
            label.setFont
        

        def set_grid():
            grid.addWidget(self.lbl[0], 4, 0)
            grid.addWidget(self.lbl[1], 4, 1)
            grid.addWidget(self.lbl[2], 4, 2)
            grid.addWidget(self.lbl[3], 4, 3)
            grid.addWidget(self.lbl[4], 4, 4)
            grid.addWidget(self.lbl[5], 3, 4)
            grid.addWidget(self.lbl[6], 3, 3)
            grid.addWidget(self.lbl[7], 3, 2)
            grid.addWidget(self.lbl[8], 3, 1)
            grid.addWidget(self.lbl[9], 3, 0)
            grid.addWidget(self.lbl[10], 2, 0)
            grid.addWidget(self.lbl[11], 2, 1)
            grid.addWidget(self.lbl[12], 2, 2)
            grid.addWidget(self.lbl[13], 2, 3)
            grid.addWidget(self.lbl[14], 2, 4)
            grid.addWidget(self.lbl[15], 1, 4)
            grid.addWidget(self.lbl[16], 1, 3)
            grid.addWidget(self.lbl[17], 1, 2)
            grid.addWidget(self.lbl[18], 1, 1)
            grid.addWidget(self.lbl[19], 1, 0)
            grid.addWidget(self.lbl[20], 0, 0)
            grid.addWidget(self.lbl[21], 0, 1)
        
            grid.addWidget(self.lbl[22], 0, 2)
            grid.addWidget(self.lbl[23], 0, 3)
            grid.addWidget(self.lbl[24], 0, 4)
        set_grid() 
        
        self.setLayout(hbox)

        self.show()

    def change_color(self, tiles):
        if tiles == None:
            return
        win.lbl[tiles[0]-1].setStyleSheet("background: grey; border: 1px solid black;")
        win.lbl[tiles[1]-1].setStyleSheet("background: lightgreen; border: 1px solid black;")

    def reset_color(self):
        for label in self.lbl:
            label.setStyleSheet("background: grey; border: 1px solid black;")

    def win_color(self):
        for label in self.lbl:
            label.setStyleSheet("background: #FFD700; border: 1px solid black;")

p1 = game.Player("P1",b1)


def move():
    tiles = p1.play(b1)
    print(tiles)

    if tiles[0] == 1:
        win.reset_color()

    if tiles == None:
        return
    elif type(tiles) == str:
        win.text.setText(tiles)
    elif tiles[0] == 25:
        win.lbl[-1].setStyleSheet("background: lightgreen")
        win.win_color()
        win.text.setText(tiles[1])
    else:
        win.change_color(list(tiles))
        win.text.setText(tiles[2])

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
