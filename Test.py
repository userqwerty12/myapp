from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
import sqlite3


#Кол-во вопросов
num = 1
#Шаблон вопрос
a = 'Вопрос '
#Кол-во правильных ответов
tru = 0


#Первый вопрос
quest1 = 'Качество изображения монитора определяется:'

#Варианты ответа на первый вопрос
answer1_1 = 'Способом подключения'
answer1_2 = 'Разрешающей способностью *'
answer1_3 = 'Типом видеокарты'

#Номер правильного ответа
options1 = 2


#Второй вопрос
quest2 = 'Дисковод - это устройство для:'

#Варианты ответа на второй вопрос
answer2_1 = 'Чтения/записи данных с внешнего носителя *'
answer2_2 = 'Обработки команд исполняемой программы'
answer2_3 = 'Хранения команд исполняемой программы'

#Номер правильного ответа
options2 = 1


#Третий вопрос
quest3 = 'Какие устройства относятся к устройствам ввода информации?'

#Варианты ответа на третий вопрос
answer3_1 = 'Принтер, сканер, клавиатура'
answer3_2 = 'Графический планшет, клавиатура, микрофон, сканер *'
answer3_3 = 'Монитор, сканер, клавиатура'

#Номер правильного ответа
options3 = 2


#Четвёртый вопрос
quest4 = 'Что хранится в ячейках оперативной памяти?'

#Варианты ответа на четвёртый вопрос
answer4_1 = 'Микрочипы'
answer4_2 = 'Модули памяти'
answer4_3 = 'Двоичный код длиной 8 знаков *'

#Номер правильного ответа
options4 = 3


#Пятый вопрос
quest5 = 'Для долговременного хранения пользовательской информации служит:'

#Варианты ответа на пятый вопрос
answer5_1 = 'Процессор'
answer5_2 = 'Оперативная память'
answer5_3 = 'Внешняя память *'

#Номер правильного ответа
options5 = 3


#Шестой вопрос
quest6 = 'Свойство постоянного запоминающегося устройства (ПЗУ):'

#Варианты ответа на шестой вопрос
answer6_1 = 'Энергонезависимость'
answer6_2 = 'Возможность перезаписи информации'
answer6_3 = 'Только чтение информации *'

#Номер правильного ответа
options6 = 3


#Седьмой вопрос
quest7 = 'Устройство для визуального воспроизведения символьной и графической информации:'

#Варианты ответа на седьмой вопрос
answer7_1 = 'Клавиатура'
answer7_2 = 'Монитор *'
answer7_3 = 'Процессор'

#Номер правильного ответа
options7 = 2


#Восьмой вопрос
quest8 = 'Как называется устройство, используемое для печати на листах больших размеров:'

#Варианты ответа на восьмой вопрос
answer8_1 = 'Плоттер *'
answer8_2 = 'Монитор'
answer8_3 = 'Принтер'

#Номер правильного ответа
options8 = 1


#Девятый вопрос
quest9 = 'При выключении компьютера вся информация теряется:'

#Варианты ответа на девятый вопрос
answer9_1 = 'На жестком диске'
answer9_2 = 'В оперативной памяти *'
answer9_3 = 'На CD-ROM диске'

#Номер правильного ответа
options9 = 2


#Десятый вопрос
quest10 = 'Какое устройство не находятся в системном блоке?'

#Варианты ответа на десятый вопрос
answer10_1 = 'Жесткий диск'
answer10_2 = 'Видеокарта'
answer10_3 = 'Мышь *'

#Номер правильного ответа
options10 = 3


#Функции
def question():
	#Глобальные переменные
	global lbl1, lbl2, rad1, rad2, rad3, btn1, selected, options

	#Условие для первого вопроса
	if num == 1:
		#Текст первого вопроса
		quest = quest1

		#Текс вариантов ответа на первый вопрос
		answer1 = answer1_1
		answer2 = answer1_2
		answer3 = answer1_3

		#Список виджетов которые надо удалить
		delete = [lbl, btn]

		#Процесс удаления виджетов
		for i in range(len(delete)):
			delete[i].destroy()

		#Номер правильного ответа
		options = options1

	#Условие для второго вопроса
	elif num > 1:

		#Список виджетов которые надо удалить
		delete = [lbl1, lbl2, rad1, rad2, rad3, btn1]

		#Процесс удаления виджетов
		for i in range(len(delete)):
			delete[i].destroy()

		if num == 2:

			#Текст второго вопроса
			quest = quest2

			#Текс вариантов ответа на второй вопрос
			answer1 = answer2_1
			answer2 = answer2_2
			answer3 = answer2_3

			#Номер правильного ответа
			options = options2

		elif num == 3:

			#Текст второго вопроса
			quest = quest3

			#Текс вариантов ответа на второй вопрос
			answer1 = answer3_1
			answer2 = answer3_2
			answer3 = answer3_3

			#Номер правильного ответа
			options = options3

		elif num == 4:

			#Текст второго вопроса
			quest = quest4

			#Текс вариантов ответа на второй вопрос
			answer1 = answer4_1
			answer2 = answer4_2
			answer3 = answer4_3

			#Номер правильного ответа
			options = options4

		elif num == 5:

			#Текст второго вопроса
			quest = quest5

			#Текс вариантов ответа на второй вопрос
			answer1 = answer5_1
			answer2 = answer5_2
			answer3 = answer5_3

			#Номер правильного ответа
			options = options5

		elif num == 6:

			#Текст второго вопроса
			quest = quest6

			#Текс вариантов ответа на второй вопрос
			answer1 = answer6_1
			answer2 = answer6_2
			answer3 = answer6_3

			#Номер правильного ответа
			options = options6

		elif num == 7:

			#Текст второго вопроса
			quest = quest7

			#Текс вариантов ответа на второй вопрос
			answer1 = answer7_1
			answer2 = answer7_2
			answer3 = answer7_3

			#Номер правильного ответа
			options = options7

		elif num == 8:

			#Текст второго вопроса
			quest = quest8

			#Текс вариантов ответа на второй вопрос
			answer1 = answer8_1
			answer2 = answer8_2
			answer3 = answer8_3

			#Номер правильного ответа
			options = options8

		elif num == 9:

			#Текст второго вопроса
			quest = quest9

			#Текс вариантов ответа на второй вопрос
			answer1 = answer9_1
			answer2 = answer9_2
			answer3 = answer9_3

			#Номер правильного ответа
			options = options9

		elif num == 10:

			#Текст второго вопроса
			quest = quest10

			#Текс вариантов ответа на второй вопрос
			answer1 = answer10_1
			answer2 = answer10_2
			answer3 = answer10_3

			#Номер правильного ответа
			options = options10


	#Виджет вывода текста "Номер вопроса"
	lbl1 = Label(window, text=a + str(num), font=("", 15))
	#Настрока параметров виджета
	lbl1.place(relx=.5, rely=.1, anchor='c')

	#Виджет вывода текста "Текст вопроса"
	lbl2 = Label(window, text=quest, font=("Lucida Grande", 12))
	#Настрока параметров виджета
	lbl2.place(relx=.2, rely=.3, anchor='w')

	#
	selected = IntVar()

	#РадиоКнопки "Варианты выбора"
	rad1 = Radiobutton(window, text=answer1, value=1, variable=selected)  
	rad2 = Radiobutton(window, text=answer2, value=2, variable=selected)
	rad3 = Radiobutton(window, text=answer3, value=3, variable=selected)
	#Настрока параметров виджетов
	rad1.place(relx=.2, rely=.4, anchor='w')
	rad2.place(relx=.2, rely=.5, anchor='w')
	rad3.place(relx=.2, rely=.6, anchor='w')

	#Виджет кнопки
	btn1 = Button(window, text='Далее', command=click)
	#Настрока параметров виджета
	btn1.place(relx=.5, rely=.9, anchor='c', height=30, width=130)


def click():
	global num

	#Изменение номера вопроса
	num += 1

	#Если ответ правильный
	if selected.get() == options:
		Bull = 'True'
		#Сохранение в БД правильного ответа
		c.execute("INSERT INTO Test VALUES (null, ?)", (Bull, ))
		conn.commit()
		
		if num > 10:
			exit()

		else:
			link()
		

	#Если ответ не неправильный
	elif selected.get() != options:
		Bull = 'False'
		#Сохранение в БД неправильного ответа
		c.execute("INSERT INTO Test VALUES (null, ?)", (Bull, ))
		conn.commit()
		
		if num > 10:
			exit()

		else:
			link()


def exit():
	if num > 10:
		#Список виджетов которые надо удалить
		delete = [lbl1, lbl2, rad1, rad2, rad3, btn1]

		#Процесс удаления виджетов
		for i in range(len(delete)):
			delete[i].destroy()

		#Вывод таблицы
		def Info(pillar, table):
			global tru

			for value in c.execute(f"SELECT {pillar} FROM {table}"):
				if value == ('True',):
					tru += 1


		Info('answer', 'Test')

		procent = int(10 * tru / 10)

		#Виджет вывода текста 
		lbl = Label(window, text=f'Результат: {procent} из 10', font=("", 15))
		#Настрока параметров виджета
		lbl.place(relx=.5, rely=.5, anchor='c')

		#Удаление таблицы
		c.execute("DROP table Test")
		conn.commit()

def link():
	command = question()


#Подключение к БД
conn = sqlite3.connect('test.db')
c = conn.cursor()

#Создание таблицы
c.execute("""CREATE TABLE IF NOT EXISTS Test
	                  (id INTEGER PRIMARY KEY AUTOINCREMENT, answer text NOT NULL)
	               """)

# Сохранение в БД
conn.commit()


#Создание окна
window = Tk()
#Название окна
window.title("TEST")
#Разрешение окна
window.geometry('600x350')
#window.resizable(False, False)
window.minsize(1200, 600)

#Виджет вывода текста
lbl = Label(window, text='Устройство компьютера', font=("", 15))
#Настрока параметров виджета
lbl.place(relx=.5, rely=.4, anchor='c')

#Виджет кнопки
btn = Button(window, text='Начать', command=question)
#Настрока параметров виджета
btn.place(relx=.5, rely=.5, anchor='c', height=30, width=130)

#Цикл окна
window.mainloop()