from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    can_they = simpledialog.askstring(title='can you write code?', prompt="")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if (can_they=="yes" or can_they=="yes."):
        messagebox.showinfo(message="you will rule the world")
    if (can_they=="no" or can_they=="no."):
        messagebox.showinfo(message="you shuld learn")




















    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        messagebox.showinfo(message="https://youtu.be/dQw4w9WgXcQ")
    # Run the window's .mainloop() method
