from tkinter import *

window = Tk()
window.title("Kilometers to miles")
#window.geometry("500x500")
miles_input = Entry()

label_miles = Label(text="miles")

miles_input.grid(column=1, row=0)
label_miles.grid(column=2, row=0)
label_equal = Label(text="is equal to ")
label_Result = Label(text="0" )
label_kilometers = Label(text="Km")
label_equal.grid(column=0, row=1)
label_Result.grid(column=1, row=1)
label_kilometers.grid(column=2, row=1)
def button_clicked():
    miles = miles_input.get()
    label_Result.configure(text=str(int(miles) * 1.609))
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)












window.mainloop()