'''import tkinter as tk 
import sys 
import random


class GUI_pre_ARM3:
        
        def __init__(self, window4):
                self.window4 = window4
        
        
        def GUI4_outlay(self, window4):
                self.window4= tk.Tk()
                self.window4.title("NUCLEAR LAUNCH CODES SIMULATOR")
                self.frame_a4 = tk.Frame(master=self.window4)
                self.frame_a4.pack()
                self.frame_b4 = tk.Frame(master=self.window4, bg="red")
                self.frame_b4.pack()
                self.frame_c4 = tk.Frame(master=self.window4, bg="red")
                self.frame_c4.pack()
                self.frame_d4 = tk.Frame(master=self.window4, bg="red")
                self.frame_d4.place(x=920, y=878)
                self.frame_e4 = tk.Frame(master=self.window4, bg="red")
                self.frame_e4.place(x=920, y=928)
                self.frame_f4 = tk.Frame(master=self.window4, bg="red")
                self.frame_f4.place(x=1050, y=928)

                self.lbl_CAN4 = tk.Label(master=self.frame_a4, text="#####COMMAND ACCESS NETWORK#####", fg="white", bg="Black")
                self.lbl_CAN4.pack()
                self.lbl_Pelot4 = tk.Label(master=self.frame_a4, text="*LA PELOTA PRE-ARMING SEQUENCE*", fg="white", bg="Dimgray")
                self.lbl_Pelot4.pack()
        
                self.Text_main4 = tk.Text(master=self.frame_b4, bg="Orange", fg="Black", wrap="word")
                self.Text_main4.pack(padx=25, pady=15)


                def command_4bttn1():
                        self.ENT_fordata4.insert(0,"1")
        
                def command_4bttn2():
                        self.ENT_fordata4.insert(0,"2")

                def command_4bttn3():
                        self.ENT_fordata3.insert(0, "3")
                
                self.Bttn_one4 = tk.Button(master=self.frame_d4, text="1", width=3, height=1,command=command_4bttn1,fg="red", bg="yellow")
                self.Bttn_two4 = tk.Button(master=self.frame_d4, text="2", width=3, height=1,command=command_4bttn2, fg="red", bg="yellow")
                self.Bttn_three4 = tk.Button(master=self.frame_d4, text="3",width=3, height=1,command=command_4bttn3, fg="red", bg="yellow")
                self.Bttn_close4 = tk.Button(master=self.frame_d4, text="CLOSE", command=exit)
                self.Bttn_one4.grid(row=1, column=1)
                self.Bttn_two4.grid(row=1, column=2)
                self.Bttn_three4.grid(row=1, column=3) 
                self.Bttn_close4.grid(row=1, column=4)


                def dialogue_prearm4():
                        self.Text_main4.insert("1.0", "CONGRATULATIONS USER111111111 YOUR HAVE GUESSED THE LAST CODE DIGIT CORRECTLY")
                        self.Text_main4.insert(tk.END, "\n FROM THIS POINT ON YOU HAVE A MAXIMUM OF THREE ATTEMPTS PER DIGIT")
                        self.window4.after(1000, pre_arm_4dia)

                def pre_arm_4dia():
                        self.Text_main4.insert(tk.END, "\n remember that you can enter your digit attempt by clicking each")
                        self.Text_main4.insert(tk.END, "\n digit and then pressing enter to validate after it shows in entry box")
                        self.window4.after(1000, pre_arm_5dia)

                def pre_arm_5dia():
                        self.Text_main4.insert(tk.END, "\n ===============")
                        self.window3.after(1000, pre_arm_6dia)

                def pre_arm_6dia():
                        self.Text_main4.insert(tk.END, "\n ===============")
                        self.window4.after(1000, pre_arm_7dia)

                def pre_arm_7ia():
                        self.Text_main3.insert(tk.END, "\n ===============")
                        self.window3.after(1000, pre_arm_seq4)

                def pre_arm_seq4():
                        self.Text_main4.insert(tk.END, "\n CODE SEQUENCING COMPLETE:")
                        self.Text_main4.insert(tk.END, "\n PLEASE ENTER DIGIT...")


                def arm_seq3():
                        self.Text_main4.insert(tk.END, "\n [x], [x], [x]")

                        code_4 = random.randrange(1,4)

                        code_4_try = int(self.ENT_fordata4.get())

                        if code_4_try == code_4:
                                self.Text_main4.insert(tk.END, "\n Your code attempt was a success. Proceeding to final stage of pre-arming sequence")
                                self.window4.after(1000, success_Dial)

                        else:
                                self.Text_main4.insert(tk.END, "\n Your attempt has failed, UNAUTHORIZED ACCESS SUSPECTED! IF YOU ARE NOT AUTHORIZED TO USE THIS SYSTEM\n PLEASE EXIT NOW! OR TERMINATOR PROTOCOL WILL BE INITIATE!!!")
                                self.Text_main4.insert(tk.END, "\n Please enter another number digit: ")
                                self.ENT_fordata4.delete(0)
                                self.window4.after(1000, pull_for_aseq2)

                
                def arm_seq3a():
                        self.Text_main4.insert(tk.END, "\n [x], [x], [x]")
                        code_3a = random.randrange(1,4)

                        code_3a_try = int(self.ENT_fordata4.get())
                        
                        if code_3a_try== code_3a:
                                self.Text_main4.insert(tk.END, "\n Your code attempt was a success. Proceeding to final stage of pre-arming sequence")
                                self.window4.after(1000, success_Dial)

                        else:
                                self.Text_main4.insert(tk.END, "\n WARNING THIS IS YOUR SECOND FAILED ATTEMPT, PLEASE LEAVE THIS STATION OR YOU WILL BE EXTEEEEERMINATED!!!!!")
                                self.Text_main4.insert(tk.END, "\n Please enter another number digit: ")
                                self.ENT_fordata4.delete(0)
                                self.window4.after(1000, pull_for_aseq3)

                def arm_seq3b():
                        code_3b = random.randrange(1,4)

                        code_3b_try = int(self.ENT_fordata3.get())
                        
                        if code_3b_try == code_3b:
                                self.Text_main4.insert(tk.END, "\n Your code attempt was a success. Proceeding to final stage of pre-arming sequence")
                                self.window4.after(1000, Success_Dial)

                        else:
                                self.Text_main4.insert(tk.END, "\n THIS WAS YOUR LAST ATTEMPT! TERMINATOR PROTOCOLS HAVE BEEN INITIATED!\n PREPARE YOURSELF FOR MAXIMUM EXTEEERMINATION!!!")
                                self.window4.after(4000, Terminator_rick)

                def success_Dial():
                        self.Text_main4.insert(tk.END, "\n CONGRATULATIONS! YOU ARE READY TO PROCEED TO THE NEXT STAGE OF LA PELOTA PRE-ARMING SEQUENCE\n AS A FRIENDLY REMINDER ANYONE ATTEMPTNG TO ACCESS THIS SYSTEM WIHOUT PERMISSION WILL BE SUBJECTED TO THE TERMINATOR PROTOCOL\n Thanks!!")
                        self.window4.after(3000, destroy_one_3)


                def destroy_one_3():
                        self.window4.destroy()


                def Terminator_rick():
                        self.Text_main4.insert(tk.END, "\n WARNING! WARNING!! TERMINATOR PROTOCOLS HAVE BEEN INITIATED! UNAUTHORIZED ACCESS TO THIS STATION WILL BE EXTERMINATED!!\n WHILE YOU WAIT FOR EXTERMINATOR SQUAD PLEASE ENJOY THIS PLEASANT SYMPHONY BY MR. RICKY ASTLEY!!")
                        self.window4.after(2000, Terminator_roll)
                
                def Terminator_roll():
                        self.Text_main4.insert(tk.END, "\n Never gonna give you up....")
                        self.window4.after(1000, rick_finis)

                def rick_finis():
                        self.Text_main4.insert(tk.END, "\n Never gonna let you down!!!")
                        self.window4.after(5000, kill_win)

                def kill_win():
                        self.window4.destroy()


                self.ENT_fordata4 = tk.Entry(master=self.frame_c4, state="normal", bg="Gainsboro")
                self.ENT_fordata4.pack(padx=50, pady=15)

                self.Ent_bttn4 = tk.Button(master=self.frame_c4,text="Enter", command=arm_seq3, width=6)
                self.Ent_bttn4.pack(padx=10, pady=10)
                
                def pull_for_aseq2():
                        self.Ent_bttn3a = tk.Button(master=self.frame_c4,text="Enter", command=arm_seq3a, width=6)
                        self.Ent_bttn3a.place(x=150, y=79)


                def pull_for_aseq3():
                        self.Ent_bttn3b = tk.Button(master=self.frame_c4,text="Enter", command=arm_seq3a, width=6)
                        self.Ent_bttn3b.place(x=150, y=79)


                self.Bttn_bypass4 = tk.Button(master=self.frame_e4, text="Bypass", fg="red", bg="yellow")
                self.Bttn_bypass4.pack()
                self.Bttn_input4 = tk.Button(master=self.frame_f4, text="Start", command=dialogue_prearm4,fg="red", bg="yellow")
                self.Bttn_input4.pack()'''