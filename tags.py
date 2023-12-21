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
        ft = tkFont.Font(family='Times',size=13)
        GMessage_36["font"] = ft
        GMessage_36["fg"] = "#741288"
        GMessage_36["justify"] = "center"
        GMessage_36["text"] = "THANK YOU"
        GMessage_36.place(x=160,y=400,width=250,height=30)

        GMessage_23=tk.Message(root)
        GMessage_23["bg"] = "#a319ad"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_23["font"] = ft
        GMessage_23["fg"] = "#333333"
        GMessage_23["justify"] = "center"
        GMessage_23["text"] = "Tell us how which services do you need"
        GMessage_23["relief"] = "raised"
        GMessage_23.place(x=100,y=90,width=500,height=60)

        GButton_846=tk.Button(root)
        GButton_846["bg"] = "#aa23cc"
        ft = tkFont.Font(family='Times',size=10)
        GButton_846["font"] = ft
        GButton_846["fg"] = "#000000"
        GButton_846["justify"] = "center"
        GButton_846["text"] = "Device scan"
        GButton_846.place(x=190,y=160,width=207,height=44)
        GButton_846["command"] = self.GButton_846_command

        GButton_946=tk.Button(root)
        GButton_946["bg"] = "#d732bf"
        ft = tkFont.Font(family='Times',size=10)
        GButton_946["font"] = ft
        GButton_946["fg"] = "#000000"
        GButton_946["justify"] = "center"
        GButton_946["text"] = "File Scan"
        GButton_946.place(x=200,y=220,width=195,height=45)
        GButton_946["command"] = self.GButton_946_command

    def GButton_72_command(self):
        print("command")


    def GRadio_977_command(self):
        print("command")


    def GCheckBox_679_command(self):
        print("command")


    def GButton_846_command(self):
        print("command")


    def GButton_946_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
