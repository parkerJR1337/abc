# подключаю библиотеки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, 
QPushButton, QLabel, QButtonGroup)
from random import shuffle
from random import randint
 
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
questions_list = []
 
questions_list.append(Question('Сколько будет 2+2*2', "6", "4", '2', "12"))
questions_list.append(Question('На каком языке пишут скрипты в Unity', "C#", "C", 'C++', "F#"))
questions_list.append(Question('Сколько стран в Европе', "65", "55", '58', "64"))
questions_list.append(Question('100/10', "10", "11", '12', "9"))
questions_list.append(Question('1000-7', "zxc", "993", 'qwe', "?"))
questions_list.append(Question('bird', "Птица", "Животное", 'Самолёт', "Твиттер"))
questions_list.append(Question('Кароль', "умрёт по корооевски", "king", 'sand king', "?"))
questions_list.append(Question('Город', "Санкт-Петербург", "Волгоград", 'Москва(Этот ответ не верный)', "?"))
questions_list.append(Question('Девочки с', "Зелёными глазами", "Этот ответ даст вам 0 баллов", '?', "этот ответ не праильный"))
 
 
# создаю объект - приложение
app = QApplication([])
 
# создаю окно приложения и меняю надпись
window = QWidget()
window.setWindowTitle("Memory Card")
 
''' ИНТЕРФЕЙС приложения Memory Card '''
 
# создаем кнопку ответа и текст вопроса
btn_OK = QPushButton("Ответить")
lb_Question = QLabel("Какой национальности не существует?")
 
# создаем набор переключателей
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton("Энцы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
# расположение виджетов по лэйаутам
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
 
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
# создаем окно с резуальтатами
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("Правильно/неправильно")
lb_Correct = QLabel()
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
# развещаем виджеы в главном окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, 
alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
 
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
 
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 
# размещаем созданные строки
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=2)
layout_card.addStretch(1)
 
#########################################################
#                   Функции                             #
#########################################################
 
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")
 
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
 
def show_correct(res):
    lb_Result.setText(res)
    show_result()
 
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print_stats()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print_stats()
 
def print_stats():
    print("Статистика\n-Всего вопросов:", window.total, "\n-Правильных ответов:", window.score, "\nРейтинг:", (window.score/window.total*100), "%")
 
 
def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
 
def click_ok():
    # определяем нужно ли показывать другой вопрос
    # либо проверить ответ на этот
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()
 
window.score = 0
window.total = 0
next_question()
btn_OK.clicked.connect(click_ok)
window.setLayout(layout_card)
window.show()
app.exec()