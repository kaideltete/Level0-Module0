from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    u_score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    q1 = simpledialog.askstring(title='1?', prompt="what is 1+1")
    #      // 3.  Use an if statement to check if their answer is correct
    q2 = simpledialog.askstring(title='2?', prompt="what is 3+1")
    #      // 4.  if the user's answer was correct, add one to their score 
    q3 = simpledialog.askstring(title='3?', prompt="what is 9+1")
    q4 = simpledialog.askstring(title='4?', prompt="what is (9+1)*2*3+4")
    q5 = simpledialog.askstring(title='5?', prompt="what is (9+1)*2/4")
    q6 = simpledialog.askstring(title='5?', prompt="does Hot water turn into ice faster than cold water?")
    q7 = simpledialog.askstring(title='5?', prompt="what is iron in the periodic table?")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    if (q1=="2"):
        u_score+=1
    if (q2=="4"):
        u_score+=1
    if (q3=="10"):
        u_score+=1
    if (q4=="64"):
        u_score+=5
    if (q5=="5"):
        u_score+=2
    if (q6=="hot water"):
        u_score+=3
    if (q7=="FE"):
        u_score+=2
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(message=str(u_score))
    # Run the window's .mainloop() method
    window.mainloop()
