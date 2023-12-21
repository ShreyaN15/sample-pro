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
        GLabel_865["activebackground"] = "#6b1414"
        GLabel_865["activeforeground"] = "#000eff"
        GLabel_865["anchor"] = "center"
        GLabel_865["bg"] = "#31e43d"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_865["font"] = ft
        GLabel_865["fg"] = "#af26d1"
        GLabel_865["justify"] = "center"
        GLabel_865["text"] = "Your guardian is here!!"
        GLabel_865.place(x=10,y=20,width=664,height=66)

        GLineEdit_54=tk.Entry(root)
        GLineEdit_54["bg"] = "#ad14a8"
        GLineEdit_54["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_54["font"] = ft
        GLineEdit_54["fg"] = "#333333"
        GLineEdit_54["justify"] = "center"
        GLineEdit_54["text"] = "Tell us which checking we should perform"
        GLineEdit_54.place(x=70,y=110,width=464,height=30)

        GButton_72=tk.Button(root)
        GButton_72["bg"] = "#7dd137"
        ft = tkFont.Font(family='Times',size=10)
        GButton_72["font"] = ft
        GButton_72["fg"] = "#1f0505"
        GButton_72["justify"] = "center"
        GButton_72["text"] = "go to others"
        GButton_72.place(x=70,y=260,width=104,height=47)
        GButton_72["command"] = self.GButton_72_command

        GRadio_977=tk.Radiobutton(root)
        GRadio_977["bg"] = "#90f090"
        ft = tkFont.Font(family='Times',size=10)
        GRadio_977["font"] = ft
        GRadio_977["fg"] = "#8d2020"
        GRadio_977["justify"] = "left"
        GRadio_977["text"] = "safe checking"
        GRadio_977.place(x=70,y=350,width=117,height=30)
        GRadio_977["command"] = self.GRadio_977_command

        GListBox_50=tk.Listbox(root)
        GListBox_50["bg"] = "#d432e2"
        GListBox_50["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_50["font"] = ft
        GListBox_50["fg"] = "#333333"
        GListBox_50["justify"] = "center"
        GListBox_50.place(x=190,y=160,width=194,height=41)

        GCheckBox_679=tk.Checkbutton(root)
        GCheckBox_679["bg"] = "#90f090"
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_679["font"] = ft
        GCheckBox_679["fg"] = "#333333"
        GCheckBox_679["justify"] = "center"
        GCheckBox_679["text"] = "protection on"
        GCheckBox_679.place(x=310,y=350,width=102,height=30)
        GCheckBox_679["offvalue"] = "0"
        GCheckBox_679["onvalue"] = "1"
        GCheckBox_679["command"] = self.GCheckBox_679_command

        GMessage_36=tk.Message(root)
        ft = tkFont.Font(family='Times',size=19)
        GMessage_36["font"] = ft
        GMessage_36["fg"] = "#741288"
        GMessage_36["justify"] = "center"
        GMessage_36["text"] = "THANKS FOR USING OUR SERVICES"
        GMessage_36.place(x=160,y=420,width=351,height=46)

        GLabel_602=tk.Label(root)
        GLabel_602["bg"] = "#d871ec"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_602["font"] = ft
        GLabel_602["fg"] = "#1b0420"
        GLabel_602["justify"] = "center"
        GLabel_602["text"] = "File Scan"
        GLabel_602.place(x=190,y=210,width=193,height=47)

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
