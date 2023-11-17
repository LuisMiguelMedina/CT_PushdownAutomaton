import tkinter as tk
from tkinter import font as tkFont
from tkinter import PhotoImage
class App:
    def __init__(self, root):
        IMAGE_PATH = "./assets/AutomatonViewModel.png"
        
        # setting title
        root.title("Autómata de pila")
        # setting window size
        width = 860
        height = 550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Titulo de la ventana
        Msg_Title = tk.Label(root)
        ft = tkFont.Font(family="Times", size=32)
        Msg_Title["font"] = ft
        Msg_Title["fg"] = "#333333"
        Msg_Title["justify"] = "center"
        Msg_Title["text"] = "Autómata de pila"
        Msg_Title.place(x=250, y=10, width=360, height=70)

        # InputBox
        InputBox = tk.Entry(root)
        InputBox["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=16)
        InputBox["font"] = ft
        InputBox["fg"] = "#333333"
        InputBox["justify"] = "center"
        InputBox["text"] = "Ingresa una cadena de texto"
        InputBox.place(x=100, y=100, width=430, height=30)

        #
        Msg_InputBox = tk.Label(root)
        ft = tkFont.Font(family="Times", size=16)
        Msg_InputBox["font"] = ft
        Msg_InputBox["fg"] = "#333333"
        Msg_InputBox["justify"] = "center"
        Msg_InputBox["text"] = "Cadena:"
        Msg_InputBox.place(x=10, y=100, width=100, height=30)

        GLabel_823 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=16)
        GLabel_823["font"] = ft
        GLabel_823["fg"] = "#333333"
        GLabel_823["justify"] = "center"
        GLabel_823["text"] = "Modelo Del Autómata De Pila"
        GLabel_823.place(x=570, y=90, width=260, height=60)

        GLabel_536 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=16)
        GLabel_536["font"] = ft
        GLabel_536["fg"] = "#333333"
        GLabel_536["justify"] = "center"
        GLabel_536["text"] = "<Enter> para continuar, <X> para salir"
        GLabel_536.place(x=250, y=480, width=350, height=30)

        GListBox_222 = tk.Listbox(root)
        GListBox_222["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        GListBox_222["font"] = ft
        GListBox_222["fg"] = "#333333"
        GListBox_222["justify"] = "center"
        GListBox_222.place(x=100, y=160, width=430, height=290)

        # Modelos de automata de pila
        image = PhotoImage(file=IMAGE_PATH)
        
        GLabel_685 = tk.Label(root, image=image)
        ft = tkFont.Font(family="Times", size=10)
        GLabel_685["font"] = ft
        GLabel_685["fg"] = "#333333"
        GLabel_685["justify"] = "center"
        GLabel_685["text"] = "ModeloDelAutomataDePila"
        GLabel_685.place(x=580, y=170, width=250, height=270)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
