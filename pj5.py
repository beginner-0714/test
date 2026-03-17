import tkinter

def func():
    print("Test Ok")

root = tkinter.Tk()
label = tkinter.Label(root, text = 'press button')
button = tkinter.Button(root, text = 'HERE', command=func)
button.pack()
