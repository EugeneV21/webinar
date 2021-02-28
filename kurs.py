from numpy import sin, cos, tan, arange, pi, append
import matplotlib.pyplot as plt
#from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import LEFT,TOP,BOTH,Button,Label,Entry,Tk,messagebox,NW,Frame,END

#Создаём окно
window = Tk()
window.title("Моделирование физического явления: тело, брошенное под углом к горизонту")

#Функция для проверки значений выпадающих списков
def Checkbox():
    global graphcolor
    global line
    global lw
    global bgcolor
    if cm1.get() == "Зелёный":
       graphcolor = 'green'
    elif cm1.get() == "Жёлтый":
        graphcolor = 'yellow'
    elif cm1.get() == "Красный":
        graphcolor = 'red'
    elif cm1.get() == "Синий":
        graphcolor = 'blue'
    elif cm1.get() == "Чёрный":
        graphcolor = 'black'
    if cm2.get() == 'Сплошной':
        line = '-'
    elif cm2.get() == 'Пунктриный':
        line = '--'
    elif cm2.get() == 'Пунктир с точкой':
        line = '-.'
    elif cm2.get() == 'Точечный':
        line = ':'
    if cm3.get() == "1":
        lw = 1
    elif cm3.get() == "3":
        lw = 3
    elif cm3.get() == "5":
        lw = 5
    elif cm3.get() == "7":
        lw = 7
    elif cm3.get() == "9":
        lw = 9
    if cm4.get() == "Белый":
        bgcolor = 'white'
    elif cm4.get() == "Жёлтый":
        bgcolor = 'yellow'
    elif cm4.get() == "Оранжевый":
        bgcolor = 'orange'
    elif cm4.get() == "Серый":
        bgcolor = 'lightgrey'
    elif cm4.get() == "Зелёный":
        bgcolor = 'green'
    messagebox.showinfo(title="Успешно", message='Установлен цвет графика: '+str(cm1.get())+
                        '\nУстановлен тип графика: '+str(cm2.get())+
                        '\nУстановлена толщина графика : '+str(cm3.get())+
                        '\nУстановлен цвет фона : '+str(cm4.get()))
    
#Фунция для оставления необходимого числа цифр после запятой
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

#Функция для проверки введённого значения: является ли оно числом
def is_numeric(s):
	try:
		float(s)
		return True
	except (ValueError, TypeError):
		return False

#Функция вывода информационных сообщений при нажатии кнопки записи угла
def btn1_click():
    global a
    a = text1.get()
    if is_numeric(a):
        if (float(a)<=0):
            messagebox.showerror(title="Ошибка ввода", message="Угол должен быть больше нуля")
        elif (float(a)>=90):
            messagebox.showerror(title="Ошибка ввода", message="Угол должен быть меньше 90 градусов")            
        else:
            a = float(a)
            messagebox.showinfo(title="Успешно", message=f'Установлен угол: {str(text1.get())}°')
            return(a)
    else:
        messagebox.showerror(title="Ошибка ввода", message="Угол должен быть числом")

#Функция вывода информационных сообщений при нажатии кнопки записи скорости
def btn2_click():
    global v0
    v0 = text2.get()
    if is_numeric(v0):
        if (float(v0)<=0):
            messagebox.showerror(title="Ошибка ввода", message="Скорость дожна быть больше нуля")
        elif(float(v0)>=299792458):
            messagebox.showerror(title="Ошибка ввода", message="К сожалению, преодолевать скорость света ещё не научились")
        else:
            v0 = float(v0)
            messagebox.showinfo(title="Успешно", message=f'Установлена скорость: {str(text2.get())} м/с')
            return(v0)
    else:
        messagebox.showerror(title="Ошибка ввода", message="Скорость должна быть числом")

#Функция создания графика       
def CreateGraph():
    global currentGraph
    v0 = text2.get()
    a = text1.get()
    if is_numeric(v0) and is_numeric(a):
        #Достаём значения из поля ввода
        a = float(text1.get())
        v0 = float(text2.get())
        if (v0 > 0) and (v0 < 299792458):
            if (a > 0) and (a < 90):
                #Убираем прошлый график из памяти
                plt.clf()
                #Производим вычисления
                g = 9.80665
                a = a*pi/180
                temp = 2*(v0*sin(a))/g
                t = arange(0, temp, 0.001)
                x = v0*cos(a)*t
                y = x*tan(a)-x**2*(g/(2*v0**2*cos(a)*cos(a)))
                h = ((v0**2*sin(a)*sin(a))/(2*g))
                s = v0*cos(a)*temp
                x = append(x, s)
                y = append(y, 0)
                #Строим график
                ax = plot.add_subplot(111)
                ax.set(ylim = [0,h*1.1], xlim = [0,s*1.1], facecolor = bgcolor)
                legend = str('Время полёта: '+str(toFixed(temp,2))+' с\nМаксимальная высота подъёма: '
                                                  +str(toFixed(h,2))+' м\nРасстояние: '+str(toFixed(s,2))+ ' м')
                ax.set_title("График траектории тела, брошенного под углом "+str(text1.get())+"° к горизонту с начальной скоростью "+str(text2.get())+" м/с", fontsize=12)
                ax.set_xlabel('Дальность полёта', fontsize=20)
                ax.set_ylabel('Высота полёта', fontsize=20)
                plt.plot(x,y,color=graphcolor,linestyle = line,linewidth=lw, label=legend)
                plt.grid(True)
                ax.legend(loc = 1, edgecolor='none', labelspacing=0, handlelength = 0)
                plot.canvas.draw()
            else:
                messagebox.showerror(title="Ошибка ввода", message="Необходимо корректно задать угол")
        else:
            messagebox.showerror(title="Ошибка ввода", message="Необходимо корректно задать начальную скорость")                 
    else:
        messagebox.showerror(title="Ошибка ввода", message="Необходимо корректно задать начальную скорость и угол") 

#Функция очистки введённых значений и выпадающих списков
def Clear():
    plt.clf()
    text1.delete(0,END)
    text2.delete(0,END)
    cm1.current(0)
    cm2.current(0)
    cm3.current(0)
    cm4.current(0)
    global graphcolor
    global line
    global lw
    global bgcolor
    graphcolor = 'green'
    line = '-'
    lw = 1
    bgcolor = 'white'
    ax = plot.add_subplot(111)
    ax.set_title("Пустой график траектории тела, брошенного под углом к горизонту с начальной скоростью", fontsize=12)
    ax.set_xlabel('Дальность полёта', fontsize=20)
    ax.set_ylabel('Высота полёта', fontsize=20)
    plt.grid(True)
    plot.canvas.draw()
    plt.clf()
    
#Задаём размеры окна и убираем возможность его изменения
window.geometry('1080x720')
window.resizable(width=False, height=False)

#Фон окна
window['bg'] = '#f5e1bf'

#Задаём области для кнопок
frame = Frame(window, bg='#f5e1bf')
frame2 = Frame(window, bg='#f5e1bf')
frame3 = Frame(window, bg='#f5e1bf')
frame4 = Frame(window, bg='#f5e1bf')
frame5 = Frame(window, bg='#f5e1bf')
frame6 = Frame(window, bg='#f5e1bf')
frame.pack(anchor=NW)
frame2.pack(anchor=NW)
frame3.pack(anchor=NW)
frame4.pack(anchor=NW)
frame5.pack(anchor=NW)
frame6.pack(anchor=NW)

#Задаём текстовое описание для ввода угла
lbl1 = Label(frame, text="Введите угол (в градусах):", width=25, height=2)  
lbl1.configure(font=("Impact", 15), fg = '#b44f1e', bg='#f5e1bf')
lbl1.pack(side=LEFT)

#Задаём форму ввода угла
text1 = Entry(frame,width=20, bg='#f5e1bf', fg = '#b44f1e')
text1.pack(side=LEFT)

lbl2 = Label(frame, text=" ")
lbl2.configure(font=("Impact", 15), fg = '#f5e1bf', bg='#f5e1bf')
lbl2.pack(side=LEFT)

#Задаём кнопку для подтверждения ввода угла
btn1 = Button(frame, text="Записать угол", fg = '#1a1918', bg='#d4a752',
              command=btn1_click, width = 20)
btn1.pack(side=LEFT)

#Задаём текстовое описание для ввода скорости
lbl3 = Label(frame2, text="Введите скорость (в м/с):", width=25, height=2)  
lbl3.configure(font=("Impact", 15), fg = '#b44f1e', bg='#f5e1bf')
lbl3.pack(side=LEFT)

#Задаём форму ввода скорости
text2 = Entry(frame2,width=20, bg='#f5e1bf', fg = '#b44f1e')
text2.pack(side=LEFT)

lbl4 = Label(frame2, text=" ")
lbl4.configure(font=("Impact", 15), fg = '#f5e1bf', bg='#f5e1bf')
lbl4.pack(side=LEFT)

#Задаём кнопку для подтверждения ввода скорости
btn2 = Button(frame2, text="Записать скорость", fg = '#1a1918', bg='#d4a752',
              command=btn2_click, width = 20)
btn2.pack(side=LEFT)

#Задаём текстовое описание выбора цвета графика
lbl5 = Label(frame, text="Выберите цвет графика: ", width=25, height=2)  
lbl5.configure(font=("Impact", 15), fg = '#b44f1e', bg='#f5e1bf')
lbl5.pack(side=LEFT)

#Задаём выпадающий список для выбора цвета графика
cm1 = Combobox(frame, values =("Зелёный","Жёлтый","Красный","Синий","Чёрный"),
               width=25, height=2, state="readonly")
cm1.pack(side = LEFT)
cm1.current(0)

#Задаём текстовое описание выбора типа графика
lbl6 = Label(frame2, text="Выберите тип графика: ", width=25, height=2)  
lbl6.configure(font=("Impact", 15), fg = '#b44f1e', bg='#f5e1bf')
lbl6.pack(side=LEFT)

#Задаём выпадающий список для выбора типа графика
cm2 = Combobox(frame2, values =("Сплошной","Пунктриный","Пунктир с точкой","Точечный"), 
               width=25, height=2, state="readonly")
cm2.pack(side = LEFT)
cm2.current(0)

#Задаём текстовое описание выбора толщины графика
lbl7 = Label(frame3, text="Выберите толщину графика: ", width=28, height=2)  
lbl7.configure(font=("Impact", 15), fg = '#b44f1e', bg='#f5e1bf')
lbl7.pack(side=LEFT)

#Задаём выпадающий список для выбора толщины графика
cm3 = Combobox(frame3, values =("1","3","5","7","9"), width=38, height=2, state="readonly")
cm3.pack(side = LEFT)
cm3.current(0)

#Задаём текстовое описание выбора цвета фона
lbl8 = Label(frame3, text="Выберите цвет фона: ", width=24, height=2)  
lbl8.configure(font=("Impact", 15), fg = '#b44f1e', bg='#f5e1bf')
lbl8.pack(side=LEFT)

#Задаём выпадающий список для выбора цвета фона
cm4 = Combobox(frame3, values =("Белый","Жёлтый","Оранжевый","Серый","Зелёный"), width=25, height=2, state="readonly")
cm4.pack(side = LEFT, padx=13)
cm4.current(0)

#Задаём кнопку построения графика
btn4 = Button(frame5, text="Построить график", fg = '#1a1918', bg='#d4a752', 
              width = 20, command=CreateGraph)
btn4.pack(side=LEFT, padx = 18)

#Задаём кнопку очищения графика
btn3 = Button(frame5, text="Очистить", fg = '#1a1918', bg='#d4a752', 
              width = 20, command=Clear)
btn3.pack(side=LEFT, padx = 18)

#Задаём кнопку применения настроек из выпадающих списков
btn5 = Button(frame5, text="Применить настройки", fg = '#1a1918', bg='#d4a752', 
              width = 20, command=Checkbox)
btn5.pack(side=LEFT, padx = 18)

#Задаём настройки графика
plot=plt.figure(figsize=(11, 5), dpi=100)
canvas = FigureCanvasTkAgg(plot, frame6)
plot_widget = canvas.get_tk_widget()
plot_widget.pack(side=LEFT, padx = 18, pady = 18)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

#Задаём начальные значения выпадающих списков, если пользователь ничего не выберет
graphcolor = 'green'
line = '-'
lw = 1
bgcolor = 'white'

window.mainloop()