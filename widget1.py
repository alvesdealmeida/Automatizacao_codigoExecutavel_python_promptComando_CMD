from tkinter import * 
top = Frame(); top.pack(fill='both', expand=True) 
f = Frame(top); f.pack(fill='x')
a = Label(f,text='A'); a.pack(side='left',expand=True, fill='y')
b = Label(f,text='B'); b.pack(side='bottom',expand=True, fill='both')
c = Label(f,text='C'); c.pack(side='right')
d = Label(top,text='D'); d.pack(side='top')
for w in (a,b,c,d):
	w.configure(relief='groove', border=10, font='Time 24 bold')
	w.pack(side='left', expand=True, fill='both')
top.mainloop()
