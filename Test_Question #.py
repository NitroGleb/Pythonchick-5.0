from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QRadioButton,QLabel,QVBoxLayout,QHBoxLayout,QMessageBox,QGroupBox,QPushButton,QBoxLayout
from random import shuffle

#def win():
    #bqy1 = QMessageBox()
    #bqy1.setText('ПРЕКРАСНО')
    #bqy1.exec_()

#def lose():
    #wqn1 = QMessageBox()
    #wqn1.setText('НИЧТОЖНО!')
    #wqn1.exec_()

app = QApplication([])
window = QWidget()
window.resize(400,200)

btn_OK = QPushButton('Ответить')
text = QLabel('В каком году убили Александра 2 ?')
RadioGroupBox = QGroupBox('Варианты ответов на данный вопрос перед вами.ВЫБИРАЙ.')
rainer = QRadioButton('1918')
rainer2 = QRadioButton('1147')
rainer3 = QRadioButton('1881')
rainer4 = QRadioButton('2022')
w1 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

h1.addWidget(rainer)
h1.addWidget(rainer2)
h2.addWidget(rainer3)
h2.addWidget(rainer4)
w1.addLayout(h1)
w1.addLayout(h2)

RadioGroupBox.setLayout(w1)

layout_line = QVBoxLayout()
layout_line = QHBoxLayout()
layout_line = QHBoxLayout()

layout_line.addStretch(1)
layout_line.addWidget(btn_OK,stretch=2)

layout_card = QVBoxLayout()
layout_card.addWidget(btn_OK,alignment=Qt.AlignmentFlag.AlignCenter)
layout_card.addWidget(RadioGroupBox,alignment=Qt.AlignmentFlag.AlignCenter)
layout_card.addWidget(text,alignment=Qt.AlignmentFlag.AlignCenter)

w1.addWidget(text,alignment=Qt.AlignmentFlag.AlignCenter)
h1.addWidget(rainer,alignment=Qt.AlignmentFlag.AlignCenter)
h1.addWidget(rainer2,alignment=Qt.AlignmentFlag.AlignCenter)
h2.addWidget(rainer3,alignment=Qt.AlignmentFlag.AlignCenter)
h2.addWidget(rainer4,alignment=Qt.AlignmentFlag.AlignCenter)

w1.addLayout(h1)
w1.addLayout(h2)
RadioGroupBox.setLayout(w1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('Ты прав или нет?')
lb_correct = QLabel('Ответ будет тут')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct,alignment=Qt.AlignCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QVBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(text,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line1.addWidget(RadioGroupBox)
layout_line1.addWidget(btn_OK,stretch=2)
layout_line1.addWidget(AnsGroupBox)

class Question():
    def __init__(self,question,wrong1,wrong2,right_answer,wrong3):
        self.question = question
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.right_answer = right_answer
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В каком году убили Александра 2 ?','1918','1147','1881','2022'))

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    #else:
        #next_question()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    text.setText('Please, answer on the other questions')
    btn_OK.setText('Next question')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    text.setText('В каком году убили Александра 2 ?')
    btn_OK.setText('Ответить')

    RadioGroupBox.setExclusive(False)
    rainer.setChecked(False)
    rainer2.setChecked(False)
    rainer3.setChecked(False)
    rainer4.setChecked(False)
    RadioGroupBox.setExclusive(True)

answers = [rainer,rainer2,rainer3,rainer4]

def ask(q: Question):
    shuffle(answers)
    answers[2].setText(q.right_answer)
    answers[0].setText(q.wrong1)
    answers[1].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_result.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_correct.setText(res)
    show_result()

def check_answer():
    if answers[2].isChecked():
        show_correct('Верно')
    else:
        if answers[0].isChecked() or answers[1].isChecked() or answers[3].isChecked():
            show_correct('Неверно')

#def next_question():
    #window.cur_question = window.cur_question 
    #if window.cur_question >= len(question_list):
        #window.cur_question = 0
    #q = question_list[window.cur_question]
    #ask(q)

btn_OK.clicked.connect(click_OK)
AnsGroupBox.hide()
#btn_OK.clicked.connect(win)
#btn_OK.clicked.connect(lose)
#window.setLayout(layout_card)
#window.setWindowTitle('Memo Card')
window.setLayout(layout_line1)
window.show()
app.exec_()
