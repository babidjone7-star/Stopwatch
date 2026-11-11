from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import QTime, QTimer 
from TimerDesigns import Ui_Dialog
import sys

class TimerApp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.total_seconds = 0
        self.timers  = QTimer()
        self.timers.timeout.connect(self.update)
        self.ui.StartButton.clicked.connect(self.starta)
        self.ui.ResetButton.clicked.connect(self.reset)
        self.ui.StopButton.clicked.connect(self.stopb)
    def update(self):
        self.total_seconds -= 1
        if self.total_seconds <= 0:
            self.timers.stop()
            self.ui.TimeLabel.setText("Время вышло!")
            self.ui.Timer.setTime(QTime(0, 0, 0)) 
            return
        h = self.total_seconds // 3600
        m = (self.total_seconds % 3600) // 60
        s = self.total_seconds % 60
        time_str = f"{h:02d}:{m:02d}:{s:02d}"
        self.ui.TimeLabel.setText(time_str)
    def starta(self):
        t = self.ui.Timer.time()
        self.total_seconds = t.hour() * 3600 + t.minute() * 60 + t.second()
        self.timers.start(1000)
        self.ui.TimeLabel.setText("Отсчет пошел...")
    def stopb(self):
        self.timers.stop()
        self.ui.TimeLabel.setText("Пауза...")  
    def reset(self):
        self.timers.stop()
        self.ui.Timer.setTime(QTime(0,0,0))
        self.ui.TimeLabel.setText("Готов к работе..")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    TimeApp = TimerApp()
    TimeApp.show()
    sys.exit(app.exec())