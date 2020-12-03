import tkinter as tk
import sys

import random

class GUI_pre_arm1:

    def __init__(self, window2):
        self.window2 = window2

    def GUI2_outlay(self, window2):
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

        self.lbl_CAN2 = tk.Label(master=self.frame_a2, text="#####COMMAND ACCESS NETWORK#####", fg="white", bg="Black")
        self.lbl_CAN2.pack()
        self.lbl_Pelot2 = tk.Label(master=self.frame_a2, text="*LA PELOTA PRE-ARMING SEQUENCE*", fg="white", bg="Dimgray")
        self.lbl_Pelot2.pack()
        
        self.Text_main2 = tk.Text(master=self.frame_b2, bg="Orange", fg="Black", wrap="word")
        self.Text_main2.pack(padx=25, pady=15)


        '''self.Bttn_one2 = tk.Button(master=self.frame_d2, text="1", width=3, height=1, fg="red", bg="yellow")
        self.Bttn_two2 = tk.Button(master=self.frame_d2, text="2", width=3, height=1, fg="red", bg="yellow")
        self.Bttn_three2 = tk.Button(master=self.frame_d2, text="3",width=3, height=1, fg="red", bg="yellow")
        self.Bttn_one2.grid(row=1, column=1)
        self.Bttn_two2.grid(row=1, column=2)
        self.Bttn_three2.grid(row=1, column=3''' 

        def dialogue_start():
            self.Text_main2.insert("1.0",  "=====WHEN TEXT REACHES BOTTOM OF SCREEN PLEASE SCROLL DOWN==\n")
            self.window2.after(1000, dialogue_2)

        def dialogue_2():
            self.Text_main2.insert(tk.END, "===============================\n")
            self.window2.after(1000, dialogue3)

        def dialogue3():   
            self.Text_main2.insert(tk.END, "===============================\n")
            self.window2.after(1000, dialogue4)

        def dialogue4(): 
            self.Text_main2.insert(tk.END, "====COMMAND ACCESS NETWORK=====\n")
            self.Text_main2.insert(tk.END, "==NUCLEAR LAUNCH SYSTEMS INTERFACE==\n")
            self.window2.after(1000, welcome_msg)

        def welcome_msg():
            self.Text_main2.insert(tk.END, "====WELCOME USER====\n")
            self.Text_main2.insert(tk.END, "====preparing Protocols to Launch ICBM's of the Nuclear Triad====\n")
            self.window2.after(1000, load_1)

        def load_1(): 
            self.Text_main2.insert(tk.END, "====\n")
            self.window2.after(1000, load2)

        def load2(): 
            self.Text_main2.insert(tk.END, "========\n")
            self.window2.after(1000, load3)

        def load3():
            self.Text_main2.insert(tk.END, "============\n")
            self.window2.after(5000, sys_ready_msg)
        
        def sys_ready_msg():
            self.Text_main2.insert(tk.END, "SYSTEM READY\n")
            self.window2.after(100, instructions_one)

        def instructions_one():
            self.Text_main2.insert(tk.END, "THE COMMAND ACCESS NETWORK NUCLEAR LAUNCH SYSTEMS INTERFACE")
            self.window2.after(1000, instructions_two)

        def instructions_two():
            self.Text_main2.insert(tk.END, "\nIS A COMMAND LINE TOOL CARRIED IN THE portfolio device known as")
            self.window2.after(1000, instructions_three)

        def instructions_three():
            self.Text_main2.insert(tk.END,  "\nla pelota', in order to prevent unauthorized access to La pelota ")
            self.window2.after(1000, instructions_4)

        def instructions_4():
            self.Text_main2.insert(tk.END, "\n a 3 digit cypher code is implemented. The values that one") 
            self.window2.after(1000, instructions_5)
        
        def instructions_5():
            self.Text_main2.insert(tk.END, "\n can enter are either 1 or 2 . BE ADVISED THOUGH that this is the system")
            self.window2.after(1000, instructions_6)
        
        def instructions_6():
            self.Text_main2.insert(tk.END, "\n to Pre-arm la Pelota. And thus we base the code on an algorithm that changes the") 
            self.window2.after(1000, instructions_7)

        def instructions_7():
            self.Text_main2.insert(tk.END, "\n digit that you entered. If you made a mistake keystroke? Do not worry, in order to")
            self.window2.after(1000, instructions_8)
         
        def instructions_8():
            self.Text_main2.insert(tk.END, "\n prevent acccidents a maximum allowance of failed attempts per digit is three. Understand") 
            self.window2.after(1000, instructions_9)

        def instructions_9():   
            self.Text_main2.insert(tk.END, "\nthat the actual launch codes of La pelota reside in the hands of the Commander-in-Chief")
            self.window2.after(1000, pre_arm_seq1)

        def pre_arm_seq1():
            self.Text_main2.insert(tk.END, "\nProceeding to pre-arm sequence of La Pelota")
            self.window2.after(1000, pre_arm_seq2)
        
        def pre_arm_seq2():
            self.Text_main2.insert(tk.END, "\n COMMENCING PRE-ARMING SEQUENCE")
            self.window2.after(1000, pre_arm_load)
        
        def pre_arm_load():
            self.Text_main2.insert(tk.END, "\n ========")
            self.window2.after(1000, pre_arm_load2)

        def pre_arm_load2():
            self.Text_main2.insert(tk.END, "\n ========")
            self.window2.after(1000, pre_arm_load3)
        
        def pre_arm_load3():
            self.Text_main2.insert(tk.END, "\n ========")
            self.window2.after(1000, command_Access_dial1)

        def command_Access_dial1():
            self.Text_main2.insert(tk.END, "\n ==COMMAND ACCESS NETWORK==")
            self.window2.after(1000, pre_arming)

        def pre_arming():
            self.Text_main2.insert(tk.END, "\n Preparing code sequence")
            self.window2.after(1000, pre_arming2)

        def pre_arming2():
            self.Text_main2.insert(tk.END, "\n Code sequence complete: ")
            self.Text_main2.insert(tk.END, "\n [x], [x], [x]")
            self.Text_main2.insert(tk.END, "\n Please input your code digit attempt in the box below: ")

        
        #What follows from this point on is the beginning of the Cypher algo, i want to bind the the three buttons 
        #with commands that will update the Entry box. And the entry box will be used to compare the value  theuser entrs
        # through the use of variable names and the entry.get method. 

        
        #OK I WILL ATTEMPT TO BRING THE SAME ALGO FROM NUKECLAS2 INTO THIS BECAUSE RECURSIVISM SEEMS TO KEEP ME IN AN INF LOOP
        #AND IT DOES NOT WANT TO LET ME GO

        def command_3bttn1():
            self.ENT_fordata2.insert(0, "1")
        
        def command_3bttn2():
            self.ENT_fordata2.insert(0, "2")

        def command_3bttn3():
            self.ENT_fordata2.insert(0, "3")
                
        self.Bttn_one2 = tk.Button(master=self.frame_d2, text="1", width=3, height=1,command=command_3bttn1,fg="red", bg="yellow")
        self.Bttn_two2 = tk.Button(master=self.frame_d2, text="2", width=3, height=1,command=command_3bttn2, fg="red", bg="yellow")
        self.Bttn_three2 = tk.Button(master=self.frame_d2, text="3",width=3, height=1,command=command_3bttn3, fg="red", bg="yellow")
        self.Bttn_one2.grid(row=1, column=1)
        self.Bttn_two2.grid(row=1, column=2)
        self.Bttn_three2.grid(row=1, column=3) 


        def arm_seq():
            self.Text_main2.insert(tk.END, "\n [x], [x], [x]")

            code_1 = random.randrange(1,3)

            code_1_try = int(self.ENT_fordata2.get())

            if code_1_try == code_1:
                self.Text_main2.insert(tk.END, "\n Your code attempt was a success. Proceeding to next digit")
                self.window2.after(1000, transfer_toNxt)

            else:
                self.Text_main2.insert(tk.END, "\n Your digit attempt was wrong, please try again. \n WARNING UNAUTHORIZED ACCESS SUSPESCTED PLEASE LEAVE THIS STATION\n or TERMINATOR PROTOCOLS WILL BE INIITIATED!!!")
                self.Text_main2.insert(tk.END, "\n CODE RE-SEQUENCING COMPLETE\n Please enter another number digit: ")
                self.ENT_fordata2.delete(0)
                self.window2.after(1000, pull_for_aseq2)

                
        def arm_seq2():
            self.Text_main2.insert(tk.END, "\n [x], [x], [x]")
            code_1a = random.randrange(1,3)

            code_1a_try = int(self.ENT_fordata2.get())
                        
            if code_1a_try == code_1a:
                self.Text_main2.insert(tk.END, "\a SUCCESS!!! Proceeding to next digit")
                self.window2.after(1000, transfer_toNxt)

            else:
                self.Text_main2.insert(tk.END, "\n Your digit attempt was wrong, if this is an unauthorized Entry attempt please leave this station NOW!!!\n OR YOU WILL BE EXTEEEEERMINATED!!!")
                self.Text_main2.insert(tk.END, "\n CODE RE-SEQUENCING COMPLETE! Please enter another number digit: ")
                self.ENT_fordata2.delete(0)
                self.window2.after(1000, pull_for_aseq3)

        def arm_seq3():
            self.Text_main2.insert(tk.END, "\n [x], [x], [x]")
            #self.ENT_fordata2.delete(0)
            code_1b = random.randrange(1,3)

            code_1b_try = int(self.ENT_fordata2.get())
                        
            if code_1b_try == code_1b:
                self.Text_main2.insert(tk.END, "\n Your code attempt was a success. Proceeding to next digit")
                self.window2.after(1000, transfer_toNxt)

            else:
                self.Text_main2.insert(tk.END, "\n Your FINAL digit attempt FAILED!, ACTIVATING SELF DESTRUCT OF LA PELOTA STATION")
                self.window2.after(1000, Terminator_rick)

        def transfer_toNxt():
            self.Text_main2.insert(tk.END, "\n Congrats! You have guessed the code for this sequence! Moving on to next stage of La Pelota Pre-arming sequence!")
            self.window2.after(2000, destroy_one_2)

        def Terminator_rick():
            self.Text_main3.insert(tk.END, "\n WARNING! WARNING!! TERMINATOR PROTOCOLS HAVE BEEN INITIATED! UNAUTHORIZED ACCESS TO THIS STATION WILL BE EXTERMINATED!!\n WHILE YOU WAIT FOR EXTERMINATOR SQUAD PLEASE ENJOY THIS PLEASANT SYMPHONY BY MR. RICKY ASTLEY!!")
            self.window2.after(2000, Terminator_roll)
                
        def Terminator_roll():
            self.Text_main3.insert(tk.END, "\n Never gonna give you up....")
            self.window2.after(1000, rick_finis)

        def rick_finis():
            self.Text_main3.insert(tk.END, "\n Never gonna let you down!!!")
            self.window3.after(5000, destroy_one_2)

        def destroy_one_2():
            self.window2.destroy()
    
        self.ENT_fordata2 = tk.Entry(master=self.frame_c2, state="normal", bg="Gainsboro")
        self.ENT_fordata2.pack(padx=50, pady=15)

        self.Ent_bttn2 = tk.Button(master=self.frame_c2,text="Enter", command=arm_seq, width=6)
        self.Ent_bttn2.pack(padx=10, pady=10)
                
        def pull_for_aseq2():
            self.Ent_bttn2 = tk.Button(master=self.frame_c2,text="Enter", command=arm_seq2, width=6)
            self.Ent_bttn2.place(x=150, y=79)


        def pull_for_aseq3():
            self.Ent_bttn2a = tk.Button(master=self.frame_c2,text="Enter", command=arm_seq3, width=6)
            self.Ent_bttn2a.place(x=150, y=79)


        self.Bttn_bypass2 = tk.Button(master=self.frame_e2, text="BYPASS N/A", fg="red", bg="yellow")
        self.Bttn_bypass2.pack()
        self.Bttn_input2 = tk.Button(master=self.frame_f2, text="Start", command=dialogue_start, fg="red", bg="yellow")
        self.Bttn_input2.pack()
        self.window2.mainloop()
