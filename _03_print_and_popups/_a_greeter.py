from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window_1 = Tk()
    # Hide the window using the window's .withdraw() method
    window_1.withdraw()
    # Ask the user for their name and save it to a variable
    window_1= simpledialog.askstring(title='hi', prompt="What is your name?")
    #window_1.askstring('Greeter', "What is your name?")
    # Show a message box with your message using the
    messagebox.showinfo(message='thanks')
    #window_1.showinfo()
    # Print your message to the console using the print() function
    print(window_1)
    # Show an error message using messagebox.showerror()
messagebox.showerror()
# Run the window's .mainloop() method

pass
