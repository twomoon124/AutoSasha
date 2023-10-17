from tkinter import *
import winsound

root = Tk()

root.title('사샤 자동 응답기')
root.geometry("300x217")

bg = PhotoImage( file = "sasha.png")

label1 = Label(root, image = bg)
label1.place(x=0, y=0)

def konsasha_event():
    winsound.PlaySound("konsasha.wav", winsound.SND_FILENAME)

def cute_event():
    winsound.PlaySound("sasha_cute.wav", winsound.SND_FILENAME)

def saioshi_event():
    winsound.PlaySound("saioshi.wav", winsound.SND_FILENAME)

def notsubsribe_event():
    winsound.PlaySound("notsubscribe.wav", winsound.SND_FILENAME)

def unfair_event():
    winsound.PlaySound("unfair.wav", winsound.SND_FILENAME)

def donation_event():
    winsound.PlaySound("donation.wav", winsound.SND_FILENAME)

button = Button(root, text='콘사샤', command=konsasha_event, width=10)
button2 = Button(root, text='귀여워', command=cute_event, width=10)
button3 = Button(root, text='사이오시', command=saioshi_event, width=10)
button4 = Button(root, text='비구독자', command=notsubsribe_event, width=10)
button5 = Button(root, text='억울해', command=unfair_event, width=10)
button6 = Button(root, text='도네창', command=donation_event, width=10)

button.place(x=10, y=10)
button2.place(x=110, y=10)
button3.place(x=210, y=10)
button4.place(x=10, y=50)
button5.place(x=110, y=50)
button6.place(x=210, y=50)

# button.grid(row=0, column=0)
# button2.grid(row=0, column=1)
# button3.grid(row=0, column=2)
# button4.grid(row=1, column=0)
# button5.grid(row=1, column=1)
# button6.grid(row=1, column=2)

# button.pack(side=LEFT,padx=10,pady=10)
# button2.pack(side=LEFT,padx=10,pady=10)
# button3.pack(side=LEFT,padx=10,pady=10)
# button4.pack(side=LEFT,padx=10,pady=10)
# button5.pack(side=LEFT,padx=10,pady=10)
# button6.pack(side=LEFT,padx=10,pady=10)

# button['text'] = 'Button1'
# button2['text'] = 'Button2'

root.mainloop()