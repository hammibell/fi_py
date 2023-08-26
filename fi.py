from tkinter import *

root = Tk()

root.title("Fibonacci Series")
root.geometry("500x500")



label_series = Label(root, text = "Fibonacci Series: ")
label_series.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label_sum = Label(root, text = "")
label_sum.place(relx = 0.5, rely = 0.4, anchor = CENTER)
entry = Entry(root)
entry.place(relx = 0.5, rely = 0.1, anchor = CENTER)


def Fibonacci():
    num = int(entry.get())
    first_num = int(entry.get())
    second_num = int(entry.get())
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] = str(sum) + " "
        counter = counter + 1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num

btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci)
btn.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    
root.mainloop()
    
    
    