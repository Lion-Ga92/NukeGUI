import tkinter as tk
from NukeClasses import GUI_pre_arm1
#from NukeClas2 import GUI_pre_arm2
#from NukeClas3 import GUI_pre_ARM3
import random
import sys

class RootIntro:

    def __init__(self, root):
        self.root = root


    def GUI_intro(self, root):
        self.root = tk.Tk()
        self.root.title("NukeTown Code cracker")
        self.frame_z = tk.Frame(master=self.root)
        self.frame_y = tk.Frame(master=self.root)
        self.frame_x= tk.Frame(master=self.root)
        self.frame_w = tk.Frame(master=self.root)
        self.frame_z.pack(fill=tk.BOTH, expand=True)
        self.frame_y.pack(fill=tk.BOTH, expand=True)
        self.frame_x.pack(fill=tk.BOTH, expand=True)
        self.frame_w.pack(fill=tk.BOTH, expand=True)
        self.lbl_name = tk.Label(master=self.frame_z, text="===============Welcome to the Nuketown Code cracking game===============")
        self.lbl_inst_1 = tk.Label(master=self.frame_y, text="please read the instructions below....")
        self.lbl_name.pack()
        self.lbl_inst_1.pack()
        self.Text_main_ins = tk.Text(master=self.frame_x, bg="Orange", fg="Black", wrap="word")
        self.Text_main_ins.pack(padx=1)

        def print_inst():
            self.Text_main_ins.insert("1.0", "Hello and welcome to the Game, in this game you will find a small code cracking")
            self.Text_main_ins.insert(tk.END, "\nsimulator.\n To start the game you need to press the 'Continue' button at the botton")
            self.root.after(1000, print_inst2)
        
        def print_inst2():
            self.Text_main_ins.insert(tk.END, "\n of thhe screen, which will then close this screen and you will be taken to the main game")
            self.Text_main_ins.insert(tk.END, "\n There you will find another window with two boxes and four buttons. To play the game press the")
            self.root.after(1000, print_inst3)

        def print_inst3():
            self.Text_main_ins.insert(tk.END, "\n'start' button from which point you will have the screen scroll the text of the")
            self.Text_main_ins.insert(tk.END, "\n game and just follow the on screen prompts")
            self.root.after(1000, print_inst4)

        def print_inst4():
            self.Text_main_ins.insert(tk.END, "\n please try to follow these instructions properly as i am not that experienced")
            self.Text_main_ins.insert(tk.END, "\n as a developer")
            self.Text_main_ins.insert(tk.END, "\n P.S. You will be asked to submit answers to the screen, word answers such as 'do you")
            self.root.after(1000, print_inst5)

        def print_inst5():
            self.Text_main_ins.insert(tk.END, "\n have rights to use this? need to be answered 'yes/no' exactly. for the Code cracking")
            self.Text_main_ins.insert(tk.END, "\n element we will have a different mechanic, which is you will click the allowed number")
            self.Text_main_ins.insert(tk.END, "\n and it will be printed in the entry box. after which you will click the enter button ") 
            self.root.after(100, print_inst6)

        def print_inst6():    
            self.Text_main_ins.insert(tk.END, "\nto see if your answer is correct and the program will then evaluate the answer and give \nyou the next printout")
            self.Text_main_ins.insert(tk.END, "\n CONTINUE TO MAIN GAME BY PRESSING CONTINUE")

        def Continue_game():
            main_game = GUI_app(self)
            main_game.GUI_outlay(win1=tk.Toplevel())
            self.root.destroy()
        
        def close_game():
            self.root.after
        
        self.Bttn_cont = tk.Button(master=self.frame_w, text="Continue", command=Continue_game)
        self.Bttn_close = tk.Button(master=self.frame_w, text="close game", command=close_game)
        self.Bttn_display = tk.Button(master=self.frame_w, text="Print instructions", command=print_inst)
        self.Bttn_cont.pack()
        self.Bttn_close.pack()
        self.Bttn_display.pack()


# THE CODE BELOW THIS COMMENT BELONGS TO  A SEPARATE CLASS THAT I HAD ADDED TO THIS SAME FILES

        class GUI_app:
            
            def __init__(self, win1):
                self.win1 = win1


            def GUI_outlay(self, win1):
                self.win1= tk.Tk()
                self.win1.title("NUCLEAR LAUNCH CODES SIMULATOR")
                self.frame_a = tk.Frame(master=self.win1)
                self.frame_a.pack(fill=tk.BOTH, expand=True)
                self.frame_b = tk.Frame(master=self.win1, bg="red")
                self.frame_b.pack(fill=tk.BOTH, expand=True)
                self.frame_c = tk.Frame(master=self.win1, bg="red")
                self.frame_c.pack(fill=tk.BOTH, expand=True)
                self.frame_d = tk.Frame(master=self.win1, bg="red")
                self.frame_d.place(x=920, y=878)
                self.frame_e = tk.Frame(master=self.win1, bg="red")
                self.frame_e.place(x=920, y=928)
                self.frame_f = tk.Frame(master=self.win1, bg="red")
                self.frame_f.place(x=1050, y=928)

                self.lbl_CAN = tk.Label(master=self.frame_a, text="#####COMMAND ACCESS NETWORK#####", fg="white", bg="Black")
                self.lbl_CAN.pack()
                self.lbl_Pelot = tk.Label(master=self.frame_a, text="*LA PELOTA PRE-ARMING SEQUENCE*", fg="white", bg="Dimgray")
                self.lbl_Pelot.pack()
                
                self.Text_main = tk.Text(master=self.frame_b, bg="Orange", fg="Black", wrap="word")
                self.Text_main.pack(padx=25, pady=15)

                self.Bttn_one = tk.Button(master=self.frame_d, text="1", width=3, height=1, fg="red", bg="yellow")
                self.Bttn_two = tk.Button(master=self.frame_d, text="2", width=3, height=1, fg="red", bg="yellow")
                self.Bttn_three = tk.Button(master=self.frame_d, text="3",width=3, height=1, fg="red", bg="yellow")
                self.Bttn_one.grid(row=1, column=1)
                self.Bttn_two.grid(row=1, column=2)
                self.Bttn_three.grid(row=1, column=3)  

        #due to my limits as a dev i had to place the meat of the function in the midts of the GUI tkinter code
                def dialogue_one():
                    self.Text_main.insert("1.0","+++++++++++++++++++++++++++\n")
                    self.Text_main.insert("2.0", "++++++++++++++++++++++++++++++++\n")
                    self.win1.after(3000, loading_2)
                
                def loading_2():
                    self.Text_main.insert("3.0", "+++++++++++++++++++++++++++++++++++++++\n")
                    self.Text_main.insert("4.0", "+++++++++++++++++++=====+++++++++++++++++++++\n")
                    self.win1.after(3000, CAN_Alert)
            
                def CAN_Alert():  
                    self.Text_main.insert("5.0", "==COMMAND ACCESS NETWORK SECURE SERVER==\n")
                    self.Text_main.insert("6.0", "==ALERT+ ACCESS TO THIS STATION HAS BEEN DETECTED, PERMISSION QUERY WILL FOLLOW +ALERT==")
                    self.win1.after(3000, Query_challenge)

                def Query_challenge():
                    self.Text_main.insert("7.0", "\nHostile intrusion to this system has been detected, delayanced protocols have initiated")
                    self.Text_main.insert("8.0", "\nThere are only three allowed users to this computer, their names are:\n")
                    self.win1.after(3000, Allowed_users)

                def Allowed_users():   
                    self.Text_main.insert("9.0", "[Luis], [Dania], [Zach], please type exactly as presented by the C-A-N\n")
                    self.Text_main.insert("10.0", "Click bypass button to load Bypass....\n")
                    
                def by_pass_lock_1():
                    self.Text_main.insert("11.0", "&%^*^(&(^$!@#$%^&*\n")
                    self.win1.after(3000, by_pass_lock2)

                def by_pass_lock2(): 
                    self.Text_main.insert("12.0", "*&*%^#$%&^*&(**&^%$@#%^&**^^$%\n")
                    self.win1.after(3000, by_pass_lock3)

                def by_pass_lock3():
                    self.Text_main.insert("13.0", "$%^&*()*&^%$#@%^&*(&^%$#@%^&*(^%$#@!$%^&*(\n")
                    self.win1.after(1000, check_creds_dial)  

                def check_creds_dial():
                    self.Text_main.insert(tk.END, "==COMMAND ACCESS NETWORK==\n CREDENTIAL CHECKER SYSTEM")
                    self.win1.after(1000, scroll_text1)

                def scroll_text1():
                    self.Text_main.insert(tk.END,"\n=================")
                    self.win1.after(1000, scroll_text2) 

                def scroll_text2():
                    self.Text_main.insert(tk.END,"\n=================")
                    self.win1.after(1000, scroll_text3) 

                def scroll_text3():
                    self.Text_main.insert(tk.END,"\n=================")
                    self.win1.after(1000, scroll_text4) 

                def scroll_text4():
                    self.Text_main.insert(tk.END,"\n=================\n Do you have permission to use this system? ") 

                
                def check_permission():
                    permit_check = self.ENT_fordata.get()

                    access_grant = random.randrange(0,30,2)

                    access_rights = (0, 2, 4, 5, 6, 7, 9, 11, 14, 16, 18, 20, 23, 25, 26)

                    if permit_check == "yes" and (access_grant in access_rights):
                        self.Text_main.insert(tk.END, "\nHello and welcome to La Pelota Nuclear Launch systems pre-arm sequence")
                        self.win1.after(4000, Launch_pre_arm)

                    else:
                        self.Text_main.insert(tk.END, "ACCESS DENIED!")
                    
                def Launch_pre_arm():
                    self.win1.destroy()



                self.ENT_fordata = tk.Entry(master=self.frame_c, state="normal", bg="Gainsboro")
                self.ENT_fordata.pack(padx=50, pady=15)

                self.Ent_bttn = tk.Button(master=self.frame_c,text="Enter", command=check_permission, width=6, )
                self.Ent_bttn.pack(padx=10, pady=10)

                self.Bttn_bypass = tk.Button(master=self.frame_e, text="bypass", command=by_pass_lock_1,fg="red", bg="yellow")
                self.Bttn_bypass.pack()
                self.Bttn_input = tk.Button(master=self.frame_f, text="Start", command=dialogue_one, fg="red", bg="yellow")
                self.Bttn_input.pack() 
 # ^^^THE CODE ABOVE THIS COMMENT BELONGS TO A SEPARATE CLASS THAT I I HAD PLACED WITHIN THIS SAME FILE ^^^^^^               
               
                def Continue_game():
                    main_game = GUI_app(self.win1)
                    main_game.GUI_outlay(win1=tk.Toplevel())
                    self.win1.after(2000, Continue_two)
                    self.root.destroy()

        sec_Wind = GUI_pre_arm1("win2")
        sec_Wind.GUI2_outlay(window2=tk.Toplevel())
        
        
        def Continue_two():
            sec_Wind = GUI_pre_arm1("win2")
            sec_Wind.GUI2_outlay(window2=tk.Toplevel())
            self.window2.after(2000, Continue_three)
            self.root.destroy()

        self.root.mainloop()

def launch():

    game = RootIntro("root")
    game.GUI_intro("root")

launch()




