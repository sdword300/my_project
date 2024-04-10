from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys

pro = Tk()
pro.geometry('800x550+300+125')
pro.title('Super Market')
pro.resizable(False ,False)
pro.iconbitmap('C:\\Users\\user\\Desktop\\spm\\market.ico')
tl = Label(pro , text='SUPER MARKET SYSTEM',fg='BLACK',bg='silver',height=2)
tl.pack(fill=X)
def open_facebook():
      webbrowser.open('https://www.facebook.com/')
def open_telegram():
      webbrowser.open('https://t.me/samire020')
def open_youtube():
      webbrowser.open('https://www.youtube.com/@iyad7126')      
def about_dev():
    messagebox.showinfo('المطور','samir')
def about_pro():
    messagebox.showinfo('البرنامج','برنامج سوبر ماركت')
      
      
def login():
    user = en1.get()
    passwd =en2.get()
    if user == 'samir' and passwd == '1234' :
        messagebox.showinfo('ترحيب','اهلا و سهلا بك')
    elif user == 'samir' and passwd == '123456' :
        messagebox.showinfo('ترحيب','اهلا و سهلا بك')
    else:
        messagebox.showerror('خطاء','البيانات غير صحيحة')
      
   
fr = Frame(pro,bg='#CA955C')
fr.place(x=490,y=36,height=515,width=340)
t1 = Label(fr , bg='#CA955C',text='ماركت السوبر مشروع',font=('Century Schoolbook',14))
t1.place(x=90,y=19)
t2 = Label(fr , bg='#CA955C',text='devlpor from NASA',font=('Century Schoolbook',14))
t2.place(x=75,y=59)
t3 = Label(fr , bg='#CA955C',text=' contact us ',font=('Georgia',14))
t3.place(x=105,y=99)

b1 = Button(fr , text='Facebook',width=26,height=2,bg='blue',fg='white',command= open_facebook)
b1.place(x=70,y=149)
b2 = Button(fr , text='Telgram',width=26,height=2,bg='#5FBDFF',command=open_telegram)
b2.place(x=70,y=199)
b3 = Button(fr , text='Youtube',width=26,height=2,bg='red',command=open_youtube)
b3.place(x=70,y=249)
b4 = Button(fr , text='about dev',width=26,height=2,bg='#FAA300',command=about_dev)
b4.place(x=70,y=299)
b5 = Button(fr , text='about project',width=26,height=2,bg='#FAA300',command=about_pro)
b5.place(x=70,y=349)
b6 = Button(fr , text='exit',width=26,height=2,bg='black',fg='white',command=exit,cursor="hand2")
b6.place(x=70,y=399)

ph = PhotoImage(file="C:\\Users\\user\\Desktop\\spm\\super_market.png")
imo = Label(pro, image=ph)
imo.place(x=50,y= 43, width=400,height=300)

fr2 =Frame(pro,width=490 , height=200,bg='#CAb55C')
fr2.place(x=0,y=350)

ph1 = PhotoImage(file="C:\\Users\\user\\Desktop\\spm\\user.png")
imo1 = Label(pro, image=ph1)
imo1.place(x=340,y=380,height=140,width=140)

t1 = Label(fr2 , bg='#CAb55C',text='المستخدم اسم',font=('Century Schoolbook',12))
t1.place(x=260,y=50)
t2 = Label(fr2 , bg='#CAb55C',text='المرور كلمة ',font=('Century Schoolbook',12))
t2.place(x=260,y=100)
en1 =Entry(fr2,justify=CENTER)
en1.place(x=125,y=55)
en2 =Entry(fr2, show="*")
en2.place(x=125,y=105)

b = Button(fr2,text='تسجيل الدخول',width=12,height=4,bg='#FAA300' ,cursor="hand2",command=login)
b.place(x=20,y=55)
  
      
pro.mainloop()