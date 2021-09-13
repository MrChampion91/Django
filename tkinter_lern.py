import tkinter
import webbrowser

app = tkinter.Tk()  # create windows
app.title("google finder")  # get name

search_label = tkinter.Label(app, text="search")    # add search text
search_label.grid(row=0, column=0)  # set search position on grid

text_field = tkinter.Entry(app, width=25)   # add enter text
text_field.grid(row=0, column=1)

# search fnk by button
def search():
    if text_field.get().strip() !="":
        webbrowser.open("https://www.google.com/search?q=" + text_field.get())

# search fnk by enter
def enterBtn(event):
    if text_field.get().strip() != "":
        webbrowser.open("https://www.google.com/search?q=" + text_field.get())


button_1 = tkinter.Button(app, text="find", width=15, command=search)   # add button
button_1.grid(row=0, column=2)

text_field.bind("<Return>", enterBtn)   # event enter
app.wm_attributes("-topmost", True)

app.mainloop()  # loop while close app

