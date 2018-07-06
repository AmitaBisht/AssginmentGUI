from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
scrollbar = Scrollbar(frame)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(frame, yscrollcommand = scrollbar.set )
dict={"1":134453,"2":26543454,"3":342870,"4":27439810,"5":1349078,"6":36578709,"7":457987567,"8":56879843,"9":13675990,\
      "10":437876098,"11":1543143252,"12":2456789,"13":3546789, "14":144235346, "15":335253465,"16":36578709,"17":457987567,"18":56879843,"19":13675990,"20":3456789}
for item in dict:
    mylist.insert(END,"Key Is : " + str(item))
    mylist.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = mylist.yview )
mainloop()
