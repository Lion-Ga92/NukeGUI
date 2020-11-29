import tkinter

class GUI_pre_arm1:

    def __init__(self):
        self = self

    def GUI2_outlay(self):
        self.window2= tk.Tk()
        self.window2.title("NUCLEAR LAUNCH CODES SIMULATOR")
        self.frame_a2 = tk.Frame(master=self.window2)
        self.frame_a2.pack()
        self.frame_b2 = tk.Frame(master=self.window2, bg="red")
        self.frame_b2.pack()
        self.frame_c2 = tk.Frame(master=self.window2, bg="red")
        self.frame_c2.pack()
        self.frame_d2 = tk.Frame(master=self.window2, bg="red")
        self.frame_d2.place(x=920, y=878)
        self.frame_e2 = tk.Frame(master=self.window2, bg="red")
        self.frame_e2.place(x=920, y=928)
        self.frame_f2 = tk.Frame(master=self.window2, bg="red")
        self.frame_f2.place(x=1050, y=928)

        self.lbl_CAN = tk.Label(master=self.frame_a2, text="#####COMMAND ACCESS NETWORK#####", fg="white", bg="Black")
        self.lbl_CAN.pack()
        self.lbl_Pelot = tk.Label(master=self.frame_a2, text="*LA PELOTA PRE-ARMING SEQUENCE*", fg="white", bg="Dimgray")
        self.lbl_Pelot.pack()
        
        self.Text_main = tk.Text(master=self.frame_b2, bg="Orange", fg="Black")
        self.Text_main.pack(padx=25, pady=15)

        self.Bttn_one = tk.Button(master=self.frame_d2, text="1", width=3, height=1, fg="red", bg="yellow")
        self.Bttn_two = tk.Button(master=self.frame_d2, text="2", width=3, height=1, fg="red", bg="yellow")
        self.Bttn_three = tk.Button(master=self.frame_d2, text="3",width=3, height=1, fg="red", bg="yellow")
        self.Bttn_one.grid(row=1, column=1)
        self.Bttn_two.grid(row=1, column=2)
        self.Bttn_three.grid(row=1, column=3) 
        
        
        self.ENT_fordata2 = tk.Entry(master=self.frame_c2, state="normal", bg="Gainsboro")
        self.ENT_fordata2.pack(padx=50, pady=15)

        self.Ent_bttn2 = tk.Button(master=self.frame_c2,text="Enter", command='''check_permission''', width=6)
        self.Ent_bttn2.pack(padx=10, pady=10)

        self.Bttn_bypass2 = tk.Button(master=self.frame_e2, text="bypass", command='by_pass_lock_1',fg="red", bg="yellow")
        self.Bttn_bypas2s.pack()
        self.Bttn_input2 = tk.Button(master=self.frame_f2, text="Start", command='dialogue_one', fg="red", bg="yellow")
        self.Bttn_inpu2t.pack()
        self.root.mainloop()