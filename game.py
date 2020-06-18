from tkinter import *
from random import choices


colors = []
done = []
def choice(b,n):
    globals()[str(n)].config(bg=b, state=DISABLED)
    colors.append(b)
    done.append(n)
    # print(colors)
    if len(colors) == 2 and colors[0] == colors[1]:
        lb1.config(text="Good")
        globals()[str(n)].config(state=DISABLED)
        colors.clear()
        done.append(str(n))
    elif len(colors) == 2 and colors[0] != colors[1]:
        lb1.config(text="Bad")
        colors.clear()
        for i in done[-2:]:
            globals()[str(i)].config(bg="white", state=NORMAL)
    else:
        lb1.config(text="Wait")
    
    print(done)
    # print(b, n)
    # print(colors)

sec = 3 
def start():
    global sec
    if sec > 0:
        lb1.config(text=str(sec))
        window.after(1000, start)
    else:
        for i in list:
            globals()[str(i)].config(bg="white", state=NORMAL)
        lb1.config(text="Time over")
    sec -= 1


window = Tk()
window.title("Игра")
window.geometry('700x780')

colorlist = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
list = []
for a in range(1,4):
    for i in range(1,5):
        globals()['btn'+str(i)+str(a)] = Button(window, width=13, height=6, state=DISABLED)
        color = choices(colorlist)
        name = 'btn'+str(i)+str(a)
        globals()['btn'+str(i)+str(a)].config(bg=color, command=lambda b=color, n=name: choice(b,n))
        globals()['btn'+str(i)+str(a)].grid(column=i, row=a)
        list.append('btn'+str(i)+str(a))

lb1 = Label(window, text=str(sec), font=("gabriola", 30))
lb1.grid(column=4, row=0)

start()

window.mainloop()

