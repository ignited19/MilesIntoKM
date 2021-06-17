from tkinter import *


print("Let's Rock!")

KM_PER_MILE = 1.60934

GUI = Tk()
GUI.title("Miles to Kilometers")
GUI.minsize(width=500, height=300)

#Label to display results
Title_label = label = Label(text="Kilometers:",font=("Arial",24,"bold"))
Title_label.pack()

results_label = label = Label(text="0.0",font=("Arial",24,"bold"))
results_label.pack()



#Calculate the new converted value
def Calculate():
    user_miles = int(user_input.get())*KM_PER_MILE
    results_label.config(text=user_miles)





#Entry
user_input = Entry(width = 10)
user_input.pack()


#Button
button = Button(text="Convert Miles into KM", command=Calculate)
button.pack()

GUI.mainloop()
