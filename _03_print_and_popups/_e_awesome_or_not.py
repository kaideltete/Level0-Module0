from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window_3 = Tk()
    # Hide the window using the window's .withdraw() method
    window_3.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    v1=random.randint(0,3)
    # 2. Print your variable to the console
    print(v1)
    # 3. Get the user to enter something that they think is awesome
    q1 = simpledialog.askstring(title='', prompt="what do you think is awesome")


    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if (v1==0):
        messagebox.showinfo(message=q1 + " is awesome")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if (v1==1):
        messagebox.showinfo(message=q1 + " is ok")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if (v1==2):
        messagebox.showinfo(message=q1 + " is boring")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if (v1==3):
        messagebox.showinfo(message=q1 + " is sad")
    # Run the window's .mainloop() method
