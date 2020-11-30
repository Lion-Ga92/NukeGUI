import tkinter as tk 

import random

class GUI_pre_arm2:
        
        def __init__(self, window3):
                self.window3 = window3
        
        
        def GUI3_outlay(self, window2):
                self.window3= tk.Tk()
                self.window3.title("NUCLEAR LAUNCH CODES SIMULATOR")
                self.frame_a3 = tk.Frame(master=self.window3)
                self.frame_a3.pack()
                self.frame_b3 = tk.Frame(master=self.window3, bg="red")
                self.frame_b3.pack()
                self.frame_c3 = tk.Frame(master=self.window3, bg="red")
                self.frame_c3.pack()
                self.frame_d3 = tk.Frame(master=self.window3, bg="red")
                self.frame_d3.place(x=920, y=878)
                self.frame_e3 = tk.Frame(master=self.window3, bg="red")
                self.frame_e3.place(x=920, y=928)
                self.frame_f3 = tk.Frame(master=self.window3, bg="red")
                self.frame_f3.place(x=1050, y=928)

                self.lbl_CAN3 = tk.Label(master=self.frame_a3, text="#####COMMAND ACCESS NETWORK#####", fg="white", bg="Black")
                self.lbl_CAN3.pack()
                self.lbl_Pelot3 = tk.Label(master=self.frame_a3, text="*LA PELOTA PRE-ARMING SEQUENCE*", fg="white", bg="Dimgray")
                self.lbl_Pelot3.pack()
        
                self.Text_main3 = tk.Text(master=self.frame_b3, bg="Orange", fg="Black")
                self.Text_main3.pack(padx=25, pady=15)


                def command_3bttn1():
                        self.ENT_fordata3.insert(0, 1)
        
                def command_3bttn2():
                        self.ENT_fordata3.insert(0, 2)

                def command_3bttn3():
                        self.ENT_fordata3.insert(0, 3)
                
                self.Bttn_one3 = tk.Button(master=self.frame_d3, text="1", width=3, height=1,command=command_3bttn1,fg="red", bg="yellow")
                self.Bttn_two3 = tk.Button(master=self.frame_d3, text="2", width=3, height=1,command=command_3bttn2, fg="red", bg="yellow")
                self.Bttn_three3 = tk.Button(master=self.frame_d3, text="3",width=3, height=1,command=command_3bttn3, fg="red", bg="yellow")
                self.Bttn_one3.grid(row=1, column=1)
                self.Bttn_two3.grid(row=1, column=2)
                self.Bttn_three3.grid(row=1, column=3) 


                def dialogue_prearm2():
                        self.Text_main3.insert("1.0", "CONGRATULATIONS USER YOUR HAVE GUESSED THE LAST CODE DIGIT CORRECTLY")
                        self.Text_main3.insert(tk.END, "\n FROM THIS POINT ON YOU HAVE A MAXIMUM OF THREE ATTEMPTS PER DIGIT")
                        self.window3.after(1000, pre_arm_2dia)

                def pre_arm_2dia():
                        self.Text_main3.insert(tk.END, "\n remember that you can enter your digit attempt by clicking each")
                        self.Text_main3.insert(tk.END, "\n digit and then pressing enter to validate after it shows in entry box")
                        self.window3.after(1000, pre_arm_3dia)

                def pre_arm_3dia():
                        self.Text_main3.insert(tk.END, "\n ===============")
                        self.window3.after(1000, pre_arm_4dia)

                def pre_arm_4dia():
                        self.Text_main3.insert(tk.END, "\n ===============")
                        self.window3.after(1000, pre_arm_5dia)

                def pre_arm_5dia():
                        self.Text_main3.insert(tk.END, "\n ===============")
                        self.window3.after(1000, pre_arm_seq2)

                def pre_arm_seq2():
                        self.Text_main3.insert(tk.END, "\n CODE SEQUENCING COMPLETE:")
                        self.Text_main3.insert(tk.END, "\n PLEASE ENTER DIGIT...")


                def arm_seq():
                        self.Text_main3.insert(tk.END, "\n [x], [x], [x]")

                        code_2 = random.randrange(1,3)

                        code_2_try = self.ENT_fordata3.get()

                        if code_2_try == code_2:
                                self.Text_main3.insert(tk.END, "\n Your code attempt was a 11111111success. Proceeding to next digit")
                                self.window3.after(1000, destroy_one_3)

                        else:
                                self.Text_main3.insert(tk.END, "\n Your digit attempt was1111111111 wrong, please try again")
                                self.Text_main3.insert(tk.END, "\n Please enter another number digit: ")
                                self.ENT_fordata3.delete(0)
                                self.window3.after(1000, pull_for_aseq2)

                
                def arm_seq2():
                        self.Text_main3.insert(tk.END, "\n [x], [x], [x]")
                        code_2a = random.randrange(1,3)

                        code_2a_try = self.ENT_fordata3.get()
                        
                        if code_2a_try == code_2a:
                                self.Text_main3.insert(tk.END, "\n Your code attempt was 2222222222a success. Proceeding to next digit")
                                self.window3.after(1000, destroy_one_3)

                        else:
                                self.Text_main3.insert(tk.END, "\n Your digit attempt was2222222222222 wrong, please try again")
                                self.Text_main3.insert(tk.END, "\n Please enter another number digit: ")
                                self.ENT_fordata3.delete(0)
                                self.window3.after(1000, pull_for_aseq3)

                def arm_seq3():
                        self.Text_main3.insert(tk.END, "\n [x], [x], [x]")
                        self.ENT_fordata3.delete(0)
                        code_2b = random.randrange(1,3)

                        code_2b_try = self.ENT_fordata3.get()
                        
                        if code_2b_try == code_2b:
                                self.Text_main3.insert(tk.END, "\n Your code attempt was33333333333 a success. Proceeding to next digit")
                                self.window3.after(1000, destroy_one_3)

                        else:
                                self.Text_main3.insert(tk.END, "\n Your digit attempt was333333333333 wrong, please try again")
                                self.window3.destroy()

        
                self.ENT_fordata3 = tk.Entry(master=self.frame_c3, state="normal", bg="Gainsboro")
                self.ENT_fordata3.pack(padx=50, pady=15)

                self.Ent_bttn3 = tk.Button(master=self.frame_c3,text="Enter", command=arm_seq, width=6)
                self.Ent_bttn3.pack(padx=10, pady=10)
                
                def pull_for_aseq2():
                        self.Ent_bttn3a = tk.Button(master=self.frame_c3,text="Enter", command=arm_seq2, width=6)
                        self.Ent_bttn3a.place(x=150, y=79)


                def pull_for_aseq3():
                        self.Ent_bttn3b = tk.Button(master=self.frame_c3,text="Enter", command=arm_seq3, width=6)
                        self.Ent_bttn3b.place(x=150, y=79)


                self.Bttn_bypass3 = tk.Button(master=self.frame_e3, text="Bypass", fg="red", bg="yellow")
                self.Bttn_bypass3.pack()
                self.Bttn_input3 = tk.Button(master=self.frame_f3, text="Start", command=dialogue_prearm2,fg="red", bg="yellow")
                self.Bttn_input3.pack()
                self.window3.mainloop()

pre_arm2 = GUI_pre_arm2("window3")
pre_arm2.GUI3_outlay("window3")