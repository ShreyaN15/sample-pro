import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Your guardian is here ")
        #setting window size
        width=700
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_865=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_865["font"] = ft
        GLabel_865["fg"] = "#333333"
        GLabel_865["justify"] = "center"
        GLabel_865["text"] = "label"
        GLabel_865.place(x=250,y=40,width=70,height=25)

        GLineEdit_54=tk.Entry(root)
        GLineEdit_54["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_54["font"] = ft
        GLineEdit_54["fg"] = "#333333"
        GLineEdit_54["justify"] = "center"
        GLineEdit_54["text"] = "Entry"
        GLineEdit_54.place(x=260,y=110,width=70,height=25)

        GButton_72=tk.Button(root)
        GButton_72["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_72["font"] = ft
        GButton_72["fg"] = "#000000"
        GButton_72["justify"] = "center"
        GButton_72["text"] = "Button"
        GButton_72.place(x=70,y=220,width=70,height=25)
        GButton_72["command"] = self.GButton_72_command

        GRadio_977=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_977["font"] = ft
        GRadio_977["fg"] = "#333333"
        GRadio_977["justify"] = "center"
        GRadio_977["text"] = "RadioButton"
        GRadio_977.place(x=70,y=310,width=85,height=25)
        GRadio_977["command"] = self.GRadio_977_command

        GListBox_50=tk.Listbox(root)
        GListBox_50["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_50["font"] = ft
        GListBox_50["fg"] = "#333333"
        GListBox_50["justify"] = "center"
        GListBox_50.place(x=70,y=160,width=80,height=25)

        GCheckBox_679=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_679["font"] = ft
        GCheckBox_679["fg"] = "#333333"
        GCheckBox_679["justify"] = "center"
        GCheckBox_679["text"] = "CheckBox"
        GCheckBox_679.place(x=270,y=310,width=70,height=25)
        GCheckBox_679["offvalue"] = "0"
        GCheckBox_679["onvalue"] = "1"
        GCheckBox_679["command"] = self.GCheckBox_679_command

        GMessage_36=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_36["font"] = ft
        GMessage_36["fg"] = "#333333"
        GMessage_36["justify"] = "center"
        GMessage_36["text"] = "Message"
        GMessage_36.place(x=70,y=390,width=80,height=25)

    def GButton_72_command(self):
        print("command")


    def GRadio_977_command(self):
        print("command")


    def GCheckBox_679_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
