# username and passward login page
from tkinter import*
from tkinter import messagebox
def ok():
    username = e1.get()
    passward = e2.get()
    if (username == ' 'and passward == ' '):
        messagebox.showinfo('','blank were not allowed')
    elif (username == 'gowtham' and passward == '143'):
        messagebox.showinfo('','login success')
        root.destory()
    elif (username!='ABCDEF'and username!='@&%$#'):
        messagebox.showinfo('','kindly use some letters as username and use numbers as passward')    
    else:
        messagebox.showinfo('','incorrect password')
root = Tk()
# global username
# global passward
root.title('login page')
root.geometry('300x200')
Label(root,text='username').place(x = 20,y=5)
Label(root,text='passward').place(x = 30,y=30)    
e1 = Entry(root)
e1.place(x=140,y=10)
e2 = Entry(root)
e2.place(x = 140,y=40)
e2.config(show='*')
Button(root,text='login',command=ok,height=3,width=13).place(x=10,y=100)
root.mainloop()



                
