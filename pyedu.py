from tkinter import *


expression = ""

def expression_adder(expr):
    global expression
    if expr == "=":
        expression = eval(expression)
        Lab.config(text=(f"Hello this is a basic Calculator\nYOUR EXPRESSION\n{expression}"))
    else:   
        expression += expr
        Lab.config(text=(f"Hello this is a basic Calculator\nYOUR EXPRESSION\n{expression}"))
    

window = Tk()
window.geometry("500x500")
window.config(background="gray")

Lab = Label(text=f"Hello this is a basic Calculator\nYOUR EXPRESSION\n{expression}",
            font=("helvetica", 20 , "bold") , bg="white" , fg="Orange",
            relief="raised", bd=10 , pady=10 , anchor="n"
            
            )

b_1 = Button(text="1", command=lambda: expression_adder("1"))
b_2 = Button(text="2", command=lambda: expression_adder("2"))
b_p = Button(text="+", command=lambda: expression_adder("+"))
b_e = Button(text="=", command=lambda: expression_adder("="))

Lab.pack()
b_1.pack()
b_2.pack()
b_p.pack()
b_e.pack()


window.mainloop()