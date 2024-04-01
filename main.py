from tkinter import *
import ast  # Has methods for passing any kind of expression

root = Tk()
root.title("Calculator GUI")
root.config(padx=20, pady=20)

i = 0


def getNumber(number):  # Put number into display
    global i
    display.insert(i, number)
    i += 1


def getOperation(operator):  # Put math operation symbol into display
    global i
    symbolLength = len(operator)
    display.insert(i, operator)
    i += symbolLength


def clearAll():
    display.delete(0, END)  # Remove all text in display, index reset


def calculate():
    entireString = display.get()  # Get all the information in display
    try:
        node = ast.parse(entireString, mode="eval")
        result = eval(compile(node, '<string>', 'eval'))  # Process math string like an elaborate mathematical operation
        clearAll()  # Prepare display for the answer
        display.insert(0, result)  # Put in the result
    except Exception:
        clearAll()
        display.insert((0, "Error"))


def undo():
    entireString = display.get()
    if len(entireString):  # If there's text in the display
        newString = entireString[:-1]  # Display text minus the last character
        clearAll()
        display.insert(0, newString)
    else:
        clearAll()
        display.insert(0, "")


# Calculator Display
display = Entry(root, width=40)
display.grid(row=1, columnspan=6)

# Number Buttons
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        buttonText = numbers[counter]
        button = Button(root, text=buttonText, width=4, height=2, command=lambda text=buttonText: getNumber(text))  # Button takes number and puts it into the display area
        button.grid(row=x+2, column=y)
        counter += 1
button = Button(root, text="0", width=4, height=2, command=lambda: getNumber(0))
button.grid(row=5, column=1)

# Math Operation Buttons
count = 0
operations = ['+', '-', '*', '/', '*3.14', "%", "(", "**", ")", "**2"]
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=4, height=2, command=lambda text=operations[count]: getOperation(text))  # Button takes operation text and puts it into the display area
            count += 1
            button.grid(row=x+2, column=y+3)

# Clear display button
Button(root, text="AC", width=4, height=2, command=clearAll).grid(row=5, column=0)
# Equal sign button
Button(root, text="=", width=4, height=2, command=calculate).grid(row=5, column=2)
# Backspace button
Button(root, text="<-", width=4, height=2, command=lambda: undo()).grid(row=5, column=4)

root.mainloop()
