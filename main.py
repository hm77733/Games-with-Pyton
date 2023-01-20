from tkinter import *
from pomodoro import Pomodoro

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
ROUND_LENGTH = 25*60
NUMBER_OF_WORK_ROUND = 2
NUMBER_OF_REST_ROUND = NUMBER_OF_WORK_ROUND -1

pom = Pomodoro()
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_clicked():
    global timer
    window.after_cancel(timer)
    tik_label['text']= ''
    pom.reset()
    timer_label['text'] = 'Timer'
    canvas.itemconfig(canvas_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_clicked():
    tik_text = pom.check_mark
    tik_label['text'] = tik_text
    timer_label.config(text='Work', fg=GREEN)
    count_down()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down():
    timer_text = pom.convert_to_min()
    canvas.itemconfig(canvas_text, text=timer_text)
    global timer
    if pom.round_is_on():
        timer = window.after(1000, count_down)
    else:
        if pom.round_number == NUMBER_OF_WORK_ROUND + NUMBER_OF_REST_ROUND+1:
            timer_label.config(text= 'Long Rest', fg=RED)
            pom.increase_tik()
            tik_text = pom.check_mark
            tik_label['text'] = tik_text
        elif pom.round_number % 2 == 0:
            pom.increase_tik()
            tik_text = pom.check_mark
            tik_label['text'] = tik_text
            timer_label.config(text='Rest', fg=PINK)
        else:
            timer_label.config(text='Work', fg=GREEN)
        if pom.round_number != NUMBER_OF_WORK_ROUND*2+1:
            timer = window.after(1000, count_down)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW )
tomato_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img, )
canvas_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 35, 'bold'), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', command=start_clicked)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset',command=reset_clicked)
reset_button.grid(row=2, column=3)

tik_label = Label(text='', fg=GREEN, font=(FONT_NAME, 23, 'bold'))
tik_label.grid(row=2, column=1)



window.mainloop()
