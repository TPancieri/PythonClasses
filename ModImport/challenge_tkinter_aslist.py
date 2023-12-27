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

    mainWindow.minsize(180, 240)
    mainWindow.maxsize(180, 240)

    mainWindow.title("Calculator")
    mainWindow.geometry("180x240")
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
    ClearButton.grid(row=1, column=0, sticky="new")
    CEButton.grid(row=1, column=2, sticky="new")
    buttonList = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "0", "=", "/"]
    r = 2
    counter = 0
    c = 0
    for item in buttonList:
        button = tkinter.Button(buttonFrame, text=item)
        if counter < 3:
            counter += 1
            c += 2
            button.grid(row=r, column=c)
        else:
            r += 2
            c = 0
            button.grid(row=r, column=c)
            c = 0
            counter = 0

    mainWindow.mainloop()
