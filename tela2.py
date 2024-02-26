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

# .....................................

# import customtkinter as ctkn

# ctkn.set_appearance_mode('dark')
# # background

# janela = ctkn.CTk()
# janela.geometry('500x300')
# # janela

# def clique():
#     print('Oi')

# titulo = ctkn.CTkLabel(janela, text='Bem Vindo ao APP',text_color='red')
# titulo.pack(padx=10, pady=10)
# # janela

# login = ctkn.CTkEntry(janela, placeholder_text='Login', width=250)
# login.pack(padx=10, pady=10)

# Senha = ctkn.CTkEntry(janela, placeholder_text='Senha', width=250, show='•')
# Senha.pack(padx=10, pady=10)

# button = ctkn.CTkButton(janela, text='Entrar', command=clique)
# button.pack(padx=10,pady=10)



# janela.mainloop()