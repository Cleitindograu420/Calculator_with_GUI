import customtkinter

calculo = ""
fonte_texto = ("Arial", 30, "bold")
fonte_btn = ("Arial", 20)
off_white = "#EEEEEE"
dark_gray = "#636363"



def add_calculo(symbol):
    global calculo
    calculo += str(symbol)
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)


def eval_calculo():
    global calculo
    try:
        calculo = str(eval(calculo))
        texto.delete(1.0, "end")
        texto.insert(1.0, calculo)

    except:
        clear_field()
        texto.insert(1.0, "ERROR")


def clear_field():
    global calculo
    calculo = ""
    texto.delete(1.0, "end")


janela = customtkinter.CTk()

janela.geometry("300x500")
janela.title("Calculator")


texto = customtkinter.CTkTextbox(janela)
texto.pack(fill='x', padx=5, pady=5)


btnframe = customtkinter.CTkFrame(janela)
btnframe.columnconfigure(0, weight=1)
btnframe.columnconfigure(1, weight=1)
btnframe.columnconfigure(2, weight=1)
btnframe.columnconfigure(3, weight=1)

btnac = customtkinter.CTkButton(btnframe, text="AC", font=fonte_btn, bg_color=dark_gray, fg_color=off_white, command=lambda: clear_field())
btnac.grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btnplusmin = customtkinter.CTkButton(btnframe, text="+/-", font=fonte_btn)
btnplusmin.grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btncent = customtkinter.CTkButton(btnframe, text="%", font=fonte_btn, command=lambda: add_calculo("/100"))
btncent.grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btnplus = customtkinter.CTkButton(btnframe, text="+", font=fonte_btn, command=lambda: add_calculo("+"))
btnplus.grid(row=3, column=3, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btnmin = customtkinter.CTkButton(btnframe, text="-", font=fonte_btn, command=lambda: add_calculo("-"))
btnmin.grid(row=2, column=3, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btndiv = customtkinter.CTkButton(btnframe, text="÷", font=fonte_btn, command=lambda: add_calculo("/"))
btndiv.grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btnmult = customtkinter.CTkButton(btnframe, text="×", font=fonte_btn, command=lambda: add_calculo("*"))
btnmult.grid(row=1, column=3, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btnequ = customtkinter.CTkButton(btnframe, text="=", font=fonte_btn, command=lambda: eval_calculo())
btnequ.grid(row=4, column=3, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btndot = customtkinter.CTkButton(btnframe, text=".", font=fonte_btn, command=lambda: add_calculo("."))
btndot.grid(row=4, column=2, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn0 = customtkinter.CTkButton(btnframe, text="0", font=fonte_btn, command=lambda: add_calculo(0))
btn0.grid(row=4, column=0, columnspan=2, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn1 = customtkinter.CTkButton(btnframe, text="1", font=fonte_btn, command=lambda: add_calculo(1))
btn1.grid(row=3, column=0, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn2 = customtkinter.CTkButton(btnframe, text="2", font=fonte_btn, command=lambda: add_calculo(2))
btn2.grid(row=3, column=1, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn3 = customtkinter.CTkButton(btnframe, text="3", font=fonte_btn, command=lambda: add_calculo(3))
btn3.grid(row=3, column=2, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn4 = customtkinter.CTkButton(btnframe, text="4", font=fonte_btn, command=lambda: add_calculo(4))
btn4.grid(row=2, column=0, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn5 = customtkinter.CTkButton(btnframe, text="5", font=fonte_btn, command=lambda: add_calculo(5))
btn5.grid(row=2, column=1, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn6 = customtkinter.CTkButton(btnframe, text="6", font=fonte_btn, command=lambda: add_calculo(6))
btn6.grid(row=2, column=2, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn7 = customtkinter.CTkButton(btnframe, text="7", font=fonte_btn, command=lambda: add_calculo(7))
btn7.grid(row=1, column=0, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn8 = customtkinter.CTkButton(btnframe, text="8", font=fonte_btn, command=lambda: add_calculo(8))
btn8.grid(row=1, column=1, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btn9 = customtkinter.CTkButton(btnframe, text="9", font=fonte_btn, command=lambda: add_calculo(9))
btn9.grid(row=1, column=2, sticky=customtkinter.W + customtkinter.E + customtkinter.S)

btnframe.pack(fill='x')

janela.mainloop()
