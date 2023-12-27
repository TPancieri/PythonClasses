# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
import tkinter, os

if __name__ == "__main__":
    mainWindow = tkinter.Tk()

    mainWindow.title("Calculator")
    mainWindow.geometry("640x480")
    mainWindow['padx'] = 8

    # Result display widget
    result = tkinter.Entry(mainWindow)
    result.grid(row=0, column=0, sticky="nw")

    # Buttons Frame
    buttonFrame = tkinter.Frame(mainWindow)
    buttonFrame.grid(row=1, column=0, sticky="new")
    # Buttons
    ClearButton = tkinter.Button(buttonFrame, text="C")
    CEButton = tkinter.Button(buttonFrame, text="CE")
    ClearButton.grid(row=1, column=3, sticky="new")
    CEButton.grid(row=1, column=4, sticky="new")
    button9 = tkinter.Button(buttonFrame, text="9")
    button9.grid(row=2, column=3, sticky="new")
    button8 = tkinter.Button(buttonFrame, text="8")
    button8.grid(row=2, column=4, sticky="new")
    button7 = tkinter.Button(buttonFrame, text="7")
    button7.grid(row=2, column=6, sticky="new")
    buttonPlus = tkinter.Button(buttonFrame, text=" + ")
    buttonPlus.grid(row=2, column=8, sticky="new")
    button6 = tkinter.Button(buttonFrame, text="6")
    button6.grid(row=3, column=3, sticky="new")
    button5 = tkinter.Button(buttonFrame, text="5")
    button5.grid(row=3, column=4, sticky="new")
    button4 = tkinter.Button(buttonFrame, text="4")
    button4.grid(row=3, column=6, sticky="new")
    buttonMinus = tkinter.Button(buttonFrame, text=" - ")
    buttonMinus.grid(row=3, column=8, sticky="new")
    button3 = tkinter.Button(buttonFrame, text="3")
    button3.grid(row=4, column=3, sticky="new")
    button2 = tkinter.Button(buttonFrame, text="2")
    button2.grid(row=4, column=4, sticky="new")
    button1 = tkinter.Button(buttonFrame, text="1")
    button1.grid(row=4, column=6, sticky="new")
    buttonMult = tkinter.Button(buttonFrame, text=" * ")
    buttonMult.grid(row=4, column=8, sticky="new")
    button0 = tkinter.Button(buttonFrame, text="0")
    button0.grid(row=5, column=3, sticky="new")
    buttonEq = tkinter.Button(buttonFrame, text=" = ")
    buttonEq.grid(row=5, column=4, sticky="new")
    buttonDiv = tkinter.Button(buttonFrame, text=" / ")
    buttonDiv.grid(row=5, column=6, sticky="new")

    mainWindow.mainloop()
