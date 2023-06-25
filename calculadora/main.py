from tkinter import *
from tkinter import ttk
import py

# cores
cor1 = '#232423'  #  preto
cor2 = '#404040'  #  cinzento
cor3 = '#efffff'  #  branco
cor4 = '#ffac40'  #  laranja
cor5 = '#38576b'  #  azul
cor6 = '#eceff1'  # cinzento claro


janela = Tk()
janela.title('Calculadora')
janela.geometry('235x330')
janela.resizable(height=False, width=False)
janela.config(background=cor1)
janela.iconbitmap('calculadora\icon.ico')

# Criar frames
frame_tela = Frame(janela, width=235, height=70, background=cor2)
frame_tela.grid(row=0, column=0)

frame_quadro = Frame(janela, width=235, height=330)
frame_quadro.grid(row=1)


todos_valores = ''

# Criar label
valor_texto = StringVar()


# Criar funcao
def entrada(a):
    global todos_valores

    todos_valores += str(a)
    # passar o valor para a tela
    valor_texto.set(todos_valores)


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=3, padx=8, anchor=E, relief=FLAT, justify=RIGHT, font=('Ivy 18'), background=cor2, foreground=cor3)
app_label.place(x=0, y=0)



# Criar botoes

b1 = Button(frame_quadro, command=limpar, text='C', width=11, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_quadro, command=lambda: entrada('%'), text='%', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(frame_quadro, command=lambda: entrada('/'), text='/', width=5, height=2, background=cor4, foreground=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

b4 = Button(frame_quadro, command=lambda: entrada('7'), text='7', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame_quadro, command=lambda: entrada('8'), text='8', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(frame_quadro, command=lambda: entrada('9'), text='9', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(frame_quadro, command=lambda: entrada('*'),text='*', width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, foreground=cor3)
b7.place(x=176, y=52)

b8 = Button(frame_quadro, command=lambda: entrada('4'), text='4', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frame_quadro, command=lambda: entrada('5'), text='5', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(frame_quadro, command=lambda: entrada('6'),text='6', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(frame_quadro, command=lambda: entrada('-'), text='-', width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, foreground=cor3)
b11.place(x=176, y=104)

b12 = Button(frame_quadro, command=lambda: entrada('1'), text='1', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frame_quadro, command=lambda: entrada('2'), text='2', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(frame_quadro, command=lambda: entrada('3'), text='3', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(frame_quadro, command=lambda: entrada('+'), text='+', width=5, height=2, background=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, foreground=cor3)
b15.place(x=176, y=156)

b16 = Button(frame_quadro, command=lambda: entrada('0'), text='0', width=11, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frame_quadro, command=lambda: entrada('.'), text='.', width=5, height=2, background=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18 = Button(frame_quadro, command=calcular, text='=', width=5, height=2, background=cor4, foreground=cor3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)


janela.mainloop()