from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextBrowser, QPushButton
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtGui import QMovie
import sys
from CIPHER import MainThread

class VoiceAssistantUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CIPHER Voice Assistant")
        self.setGeometry(200, 100, 800, 500)

        # Voice animation
        self.animation_label = QLabel(self)
        self.animation_label.setGeometry(300, 50, 200, 200)
        self.movie = QMovie("glow.gif")  # Make sure you have a glowing GIF
        self.animation_label.setMovie(self.movie)
        self.movie.start()

        # Real-time output display
        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(100, 300, 600, 150)

        # Date/Time
        self.time_label = QLabel(self)
        self.time_label.setGeometry(650, 10, 150, 30)
        self.update_time()
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        # Listen button
        self.listen_btn = QPushButton("🎙️ Speak", self)
        self.listen_btn.setGeometry(350, 260, 100, 30)
        self.listen_btn.clicked.connect(self.handle_speech)

        # Cipher logic thread
        self.cipher = MainThread()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        current_date = QDate.currentDate().toString("dd MMM yyyy")
        self.time_label.setText(f"{current_time} | {current_date}")

    def handle_speech(self):
        self.text_browser.append("🎤 Listening...")
        command = self.cipher.listen_Command()
        self.text_browser.append(f"🧠 You said: {command}")
        self.cipher.process_command(command)

    def speak_output(self, text):
        self.text_browser.append(f"🗣️ {text}")

# Hook output redirection
def redirect_stdout_to_gui(ui):
    class Stream:
        def write(self, msg):
            ui.speak_output(msg)
        def flush(self):
            pass
    sys.stdout = Stream()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoiceAssistantUI()
    redirect_stdout_to_gui(window)
    window.show()
    sys.exit(app.exec_())
