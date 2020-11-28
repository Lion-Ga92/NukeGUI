# NukeGUI

##### Here is the read out from me running the program 
I am trying to  turn a CLI code breaker game into a GUI application through tkinter
At first i wanted to avoid an OOP approach as im still rather noobie, and still need study a bit more about it. 
Anyway i have gone through that approach, just to as the saying goes "sink or swim" it seem that i have most of the set up correctly. At least to the best of my ability but after finally getting rid of one issue in my code that kept throwing up a bug. I ran into this problem which is that i am tying to use a function that will update a text box in the app. But when i try to use the tkinter insert method it seems to think that i had made a string object and refuses to accept the method. 

#### Here is the CLI traceback readout 
 line 11, in dialogue_one
    self.Text_main.insert("1.0","+++++++++++++++++++++++++++\n")
AttributeError: 'str' object has no attribute 'insert'