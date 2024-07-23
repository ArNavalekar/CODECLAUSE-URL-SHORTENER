import pyshorteners
from tkinter import *

root=Tk()
root.geometry("400x270")
root.configure(bg='pink')

#Function
def short():
	url=e1.get()
	s=pyshorteners.Shortener().tinyurl.short(url)
	
	e2.insert(END,s)

#label for entering user url
Label(root,text="Enter url",font="impack 17 bold",bg="black",fg="white").pack(fill="x")

#Entry box font=10 use
e1=Entry(root,font="impack 6 bold",bd=10,width=200)
e1.pack(pady=30)

#button
Button(root,text="click here",font="impack 12 bold",bg="blue",fg="white",width="14",command=short).pack()


#Entry 2
e2=Entry(root,font="impack 16 bold",bg='pink',width=24,bd=0)
e2.pack(pady=30)
root.mainloop()