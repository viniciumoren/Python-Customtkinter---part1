import tkinter

janela = tkinter.Tk()
janela.geometry('500x300')

def ola():
    print('Oi tudo bem !!!')

titulo = tkinter.Label(janela, text='Bem vindo ao APP !')
titulo.pack(padx=10, pady=10)

botao = tkinter.Button(janela,text='Calcular', command=ola)
botao.pack(padx=10,pady=10)



janela.mainloop()