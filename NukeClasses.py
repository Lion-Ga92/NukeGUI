import tkinter as tk


class GUI_app:
    def __init__(self):
        self = self


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

