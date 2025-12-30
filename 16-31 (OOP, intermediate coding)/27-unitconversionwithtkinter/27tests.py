import tkinter

window = tkinter.Tk()
window.title("My first window")
window.minsize(500, 300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 25, "bold"))


my_label.grid(column=0, row=0)

my_label["text"] = "newer text"
my_label.config(text="new new text")
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
button2 = tkinter.Button(text="new button", command=button_clicked)
button2.grid(column=3, row=0)
input = tkinter.Entry(width=10)
input.grid(column=4,row=4)
print(input.get())





















window.mainloop()