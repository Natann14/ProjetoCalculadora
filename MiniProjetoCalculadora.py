import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title('Calculadora')

#janela.geometry("400x400+500+100")
janela.resizable(False, False)

#janela.minsize(width=200 , height=200)
#janela.maxsize(600, 600) existem essas formas de escrita 

#cor botões numericos 
bgnum = '#343838'   
fgnum = 'white'

#cor botões não numericos
bgnaonum = '#00dffc' 
fgnaonum = 'white'

#fonte dos botões
fonte = 'verdana 15 italic'

#variavel que armazenha os numeros digitados pelo usuario
todos_valores = ''

#função responsavel por coletar entrada do usuario
def pegar_entrada(botao_apertado):
    global todos_valores
    todos_valores = todos_valores + str(botao_apertado)
    #enviando o valor para a telinha
    valor_texto.set(todos_valores)

#função para calcular valores
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#apagar tudo na tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#apagar ultimo caractere na tela
def exc_ultimo():
    global todos_valores
    todos_valores = todos_valores[:-1]
    valor_texto.set(todos_valores)

#Representa o display da calculadora
# 
# variavel auxiliar
valor_texto = StringVar()

telinha = tk.Label(textvariable=valor_texto, width=8, height=3, bg='white', fg= 'black', justify='right', anchor='e', font='verdana 15') #relief='solid', borderwidth=4
telinha.grid(row=0, columnspan=4, sticky='we')


#botoes não numericos
btAC = tk.Button(text='AC', command=limpar_tela, background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btEXC = tk.Button(text='←', command=exc_ultimo, background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btporc = tk.Button(text='%', command= lambda: pegar_entrada('%'), background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btdiv = tk.Button(text='÷', command= lambda: pegar_entrada('/'), background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btmult = tk.Button(text='×', command= lambda: pegar_entrada('*'), background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btsub = tk.Button(text='-', command= lambda: pegar_entrada('-'), background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btsom = tk.Button(text='+', command= lambda: pegar_entrada('+'), background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btigu = tk.Button(text='=', command= calcular, background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
#btseta = tk.Button(text='', background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
btponto = tk.Button(text='.', command= lambda: pegar_entrada('.'), background=f'{bgnaonum}', foreground=f'{fgnaonum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)

#numericos
texto0 = tk.Button(text='0', command= lambda: pegar_entrada('0'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto1 = tk.Button(text='1', command= lambda: pegar_entrada('1'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto2 = tk.Button(text='2', command= lambda: pegar_entrada('2'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto3 = tk.Button(text='3', command= lambda: pegar_entrada('3'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto4 = tk.Button(text='4', command= lambda: pegar_entrada('4'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto5 = tk.Button(text='5', command= lambda: pegar_entrada('5'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto6 = tk.Button(text='6', command= lambda: pegar_entrada('6'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto7 = tk.Button(text='7', command= lambda: pegar_entrada('7'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto8 = tk.Button(text='8', command= lambda: pegar_entrada('8'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)
texto9 = tk.Button(text='9', command= lambda: pegar_entrada('9'), background=f'{bgnum}', foreground=f'{fgnum}', width= 5, font=f'{fonte}', relief='solid', borderwidth=0.5)

#Grids numericos
texto7.grid(row=3, column=0)
texto8.grid(row=3, column=1)
texto9.grid(row=3, column=2)
texto4.grid(row=4, column=0)
texto5.grid(row=4, column=1)
texto6.grid(row=4, column=2)
texto1.grid(row=5, column=0)
texto2.grid(row=5, column=1)
texto3.grid(row=5, column=2)
texto0.grid(row=6, column=0, columnspan=2, sticky='nswe')
#Grids não numericos
btAC.grid(row=2, column=0)
btEXC.grid(row=2, column=1)
btporc.grid(row=2, column=2)
btdiv.grid(row=2, column=3)
btmult.grid(row=3, column=3)
btsub.grid(row=4, column=3)
btsom.grid(row=5, column=3)
btigu.grid(row=6, column=3)
#btseta.grid(row=6, column=0)
btponto.grid(row=6, column=2)

janela.mainloop()