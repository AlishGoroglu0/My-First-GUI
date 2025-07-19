from tkinter import *

Count = 0

def label_appear():
    global Count
    if Count >= 10:
        lab2.pack()
    elif Count <= -10:
        lab2.pack()
    else: 
        lab2.pack_forget()

def count_up():
    global Count
    Count += 1
    lab.config(text=f"現在の数は{Count}です")
    label_appear()
def count_down():
    global Count
    Count -= 1
    lab.config(text=f"現在の数は{Count}です")
    label_appear()


window = Tk()
window.geometry("500x500")
window.config(background="gray")




but = Button(text="1つ増える" , font=("Arial" , 30 , "bold"), cursor="dot",
            activebackground="green", activeforeground="white" , command=count_up)
but2 = Button(text="1つ減る" , font=("Arial" , 30 , "bold"), cursor="dot",
            activebackground="red", activeforeground="white" , command=count_down)
lab = Label(text=f"現在の数は{Count}です" ,
            font=("Arial" , 40 , "bold"), padx=5 , pady=5,
            relief="solid", bd=6,
            cursor="arrow",)
lab2 = Label(text=f"あなたの数字は10で割り切れます{Count}です" ,
            font=("Arial" , 40 , "bold"), padx=5 , pady=5,
            relief="solid", bd=6,
            cursor="arrow",)

lab.pack()
but.pack()
but2.pack()

window.mainloop()