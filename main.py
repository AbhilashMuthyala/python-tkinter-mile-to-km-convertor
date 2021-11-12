
from tkinter import *

# text entry
# button
# label widget

def button_clicked():
    input_text = entry.get()
    display_label.config(text=float(input_text)*1.6)

window = Tk()
window.title("Mile to kilometer convertor")
window.minsize(width=500,height=300)

label1 = Label(text='is equal to')
label1.grid(row=1,column=0)

entry = Entry(text='0')
entry.grid(row=0,column=2)

display_label = Label(text="0")
display_label.grid(row=1,column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2,column=2)

label2 = Label(text='Miles')
label2.grid(row=0,column=3)

label2 = Label(text='Km')
label2.grid(row=1,column=3)

window.mainloop()


