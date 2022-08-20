def ChooseFile():
    global file
    file = fd.askopenfilename()
    lb = Label(root, text=file, font=("simhei", 30))
    lb.pack()
    lb.place(x=0, y=100)