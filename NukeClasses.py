import tkinter as tk


class GUI_app:

    def __init__(self, root, Text_main):
        self.root = root
        self.Text_main = Text_main

    def dialogue_one(self, Text_main):
        self.Text_main.insert("1.0","+++++++++++++++++++++++++++\n")
        self.Text_main.insert("2.0", "++++++++++++++++++++++++++++++++\n")
        self.root.after(3000, loading_2)
    
    def loading_2(self):
        self.Text_main.insert("3.0", "+++++++++++++++++++++++++++++++++++++++\n")
        self.Text_main.insert("4.0", "+++++++++++++++++++=====+++++++++++++++++++++\n")
        self.root.after(3000, CAN_Alert)
    
    def CAN_Alert(self):  
        self.Text_main.insert("5.0", "==COMMAND ACCESS NETWORK SECURE SERVER==\n")
        self.Text_main.insert("6.0", "==ALERT+ ACCESS TO THIS STATION HAS BEEN DETECTED, PERMISSION QUERY WILL FOLLOW +ALERT==")
        root.after(3000, Query_challenge)

    def Query_challenge(self):
        self.Text_main.insert("7.0", "\nHostile intrusion to this system has been detected, delayanced protocols have been initiated")
        self.Text_main.insert("8.0", "There are only three allowed users to this computer, their names are:\n")
        self.root.after(3000, Allowed_users)

    def Allowed_users(self):   
        self.Text_main.insert("9.0", "[Luis], [Dania], [Zach], please type exactly as presented by the C-A-N\n")
        self.Text_main.insert("10.0", "Click bypass button to load Bypass....\n")
        self.root.after(4000, by_pass_lock)

    def by_pass_lock(self, Txt_main):
        self.Text_main.insert("11.0", "&%^*^(&(^$!@#$%^&*\n")
        self.Text_main.insert("12.0", "*&*%^#$%&^*&(**&^%$@#%^&**^^$%\n")
        self.Text_main.insert("13.0", "$%^&*()*&^%$#@%^&*(&^%$#@%^&*(^%$#@!$%^&*(\n")


    def GUI_outlay(self, root):
        self.root= tk.Tk()
        self.root.title("NUCLEAR LAUNCH CODES SIMULATOR")
        self.frame_a = tk.Frame(master=self.root)
        self.frame_a.pack()
        self.frame_b = tk.Frame(master=self.root, bg="red")
        self.frame_b.pack()
        self.frame_c = tk.Frame(master=self.root, bg="red")
        self.frame_c.pack()
        self.frame_d = tk.Frame(master=self.root, bg="red")
        self.frame_d.place(x=920, y=878)
        self.frame_e = tk.Frame(master=self.root, bg="red")
        self.frame_e.place(x=920, y=928)
        self.frame_f = tk.Frame(master=self.root, bg="red")
        self.frame_f.place(x=1050, y=928)

        self.lbl_CAN = tk.Label(master=self.frame_a, text="#####COMMAND ACCESS NETWORK#####", fg="white", bg="Black")
        self.lbl_CAN.pack()
        self.lbl_Pelot = tk.Label(master=self.frame_a, text="*LA PELOTA PRE-ARMING SEQUENCE*", fg="white", bg="Dimgray")
        self.lbl_Pelot.pack()
        
        self.Text_main = tk.Text(master=self.frame_b, bg="Orange", fg="white")
        self.Text_main.pack(padx=30, pady=15)

        self.ENT_fordata = tk.Entry(master=self.frame_c, bg="Gainsboro")
        self.ENT_fordata.pack(padx=50, pady=10)

        self.Ent_bttn = tk.Button(master=self.frame_c,text="Enter", width=6, )
        self.Ent_bttn.pack(padx=10, pady=10)

        self.Bttn_one = tk.Button(master=self.frame_d, text="1", width=3, height=1, fg="red", bg="yellow")
        self.Bttn_two = tk.Button(master=self.frame_d, text="2", width=3, height=1, fg="red", bg="yellow")
        self.Bttn_three = tk.Button(master=self.frame_d, text="3",width=3, height=1, fg="red", bg="yellow")
        self.Bttn_one.grid(row=1, column=1)
        self.Bttn_two.grid(row=1, column=2)
        self.Bttn_three.grid(row=1, column=3)

        self.Bttn_bypass = tk.Button(master=self.frame_e, text="bypass", command=by_pass_lock,fg="red", bg="yellow")
        self.Bttn_bypass.pack()
        self.Bttn_input = tk.Button(master=self.frame_f, text="Start", command= dialogue_one, fg="red", bg="yellow")
        self.Bttn_input.pack()
        
        
        root.mainloop()

