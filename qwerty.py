from tkinter import *
from tkinter import ttk
import pymysql


class std:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1400x800+100+50')
        self.root.title('برنامج ادارة المدارس')
        self.root.configure(background='silver')
        self.root.resizable(False ,False)
        t = Label(self.root,text='برنامج تسجيل الطلاب' ,fg="white",bg="#282846",height=2 ,width=1400)
        t.pack(fill=X)
        # var 
        self.id_var =StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()
        self.cetri_var=StringVar()
        self.gender_var = StringVar()
        self.addrs_var=StringVar()
        self.del_var=StringVar()
        self.search_var=StringVar()
        
    ##      tools manger    
        manger = Frame(self.root, bg='white' )
        manger.place(x=1100,y=36,height=760,width=400)
        lbl_id = Label(manger,text='الرقم التسلسلي',bg='white')
        lbl_id.place(x=110,y=6)
        en_id = Entry(manger,textvariable=self.id_var,justify='center',bg= 'alice blue')
        en_id.place(x=90,y=30)
        
        lbl_name = Label(manger,text='اسم الطالب',bg='white')
        lbl_name.place(x=120,y=60)
        en_name = Entry(manger,textvariable=self.name_var,justify='center',bg= 'alice blue')
        en_name.place(x=90,y=80)  
        
        lbl_email = Label(manger,text='الايميل',bg='white')
        lbl_email.place(x=130,y=110)
        en_email = Entry(manger,textvariable=self.email_var,justify='center',bg= 'alice blue')
        en_email.place(x=90,y=130)   
        
        lbl_phone =Label(manger,text='الهاتف',bg='white')
        lbl_phone.place(x=130,y=160)
        en_phone = Entry(manger,textvariable=self.phone_var,justify='center',bg= 'alice blue')
        en_phone.place(x=90,y=180)  
             
        lbl_centri = Label(manger,text='مؤهلات',bg='white')
        lbl_centri.place(x=130,y=210)
        en_centri = Entry(manger,textvariable=self.cetri_var,justify='center',bg= 'alice blue')
        en_centri.place(x=90,y=230)
        
        lbl_gender = Label(manger,text='الجنس',bg='white')
        lbl_gender.place(x=130,y=260)
        cmb1 = ttk.Combobox(manger,textvariable=self.gender_var,state='readonly',value=('ذكر','انثى'))
        cmb1.place(x=80,y=280)
    
        lbl_addrs = Label(manger,text='عنوان',bg='white')
        lbl_addrs.place(x=130,y=310)
        en_addrs = Entry(manger,textvariable=self.addrs_var,justify='center',bg= 'alice blue')
        en_addrs.place(x=90,y=330)

        lbl_del = Label(manger,text='حذف',bg='white')
        lbl_del.place(x=130,y=360)
        en_del = Entry(manger,textvariable=self.del_var,justify='center',bg= '#FF6969')
        en_del.place(x=90,y=380)
    
        #    botton is
        t = Label(manger,text='لوحة التحكم' ,fg="white",bg="#282846",height=1 ,width=42)
        t.place(x=0,y=410) 
        
        add_btn= Button(manger, text="اضافة", bg= '#EC9B3B' ,width=35,command=self.add_std)
        add_btn.place(x=20,y=440)
        del_btn = Button(manger, text='حذف', bg= '#FDD2BF' ,width=35,command=self.del_std)
        del_btn.place(x=20,y=480)
        update_btn = Button(manger, text='تحديث', bg= '#B30C7B' ,width=35)
        update_btn.place(x=20,y=520)
        clear_btn = Button(manger, text='مسح الحقول', bg= '#7DACE4' ,width=35,command=self.clear)
        clear_btn.place(x=20,y=560)
        about_btn = Button(manger, text='معلومات عنا', bg= '#4ED99C' ,width=35,command=self.up_std)
        about_btn.place(x=20,y=600)
        exit_btn = Button(manger, text='خروج',command=exit,bg= '#5F6CAF',height=2 ,width=35)
        exit_btn.place(x=20,y=650)

        # fame for search 
        search =Frame(self.root,width=1100,height=75,bg='#E8F0F2')
        search.place(x=0,y=36)
        
        cmb2 = ttk.Combobox(search,state='readonly',value=('id','name','email','phone'))
        cmb2.place(x=900,y=28)
        en_search = Entry(search,textvariable=self.search_var,justify='center',bg= 'alice blue')
        en_search.place(x=700,y=30)
        search_btn = Button(search,text='بحث',bg='#AED9EF',width=14)
        search_btn.place(x=550,y=28)

        # frame for list view
        dis  = Frame(self.root,width=1100,height=684,bg='white')    
        dis.place(x=1,y=114)
        scroll_x = Scrollbar(self.root,orient=HORIZONTAL)  
        scroll_Y = Scrollbar(self.root,orient=VERTICAL)
        self.std_table=ttk.Treeview(dis,
        columns=('addrs','gender','certi','phone','email','name','id'),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_Y.set)
        self.std_table.place(x=18,y=1,width=1090,height=663)
        # scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.std_table.xview)
        scroll_Y.config(command=self.std_table.yview)
        
        self.std_table['show']='headings'
        self.std_table.heading('addrs',text='عنوان الطالب')
        self.std_table.heading('gender',text='جنس')
        self.std_table.heading('certi',text='مؤهل')
        self.std_table.heading('phone',text='الهاتف')
        self.std_table.heading('email',text='الايميل')
        self.std_table.heading('name',text='اسم')
        self.std_table.heading('id',text='الرقم التسلسلي')
        # SIZE for column
        
        self.std_table.column('addrs',width=130)
        self.std_table.column('gender',width=30)
        self.std_table.column('certi',width=80)
        self.std_table.column('phone',width=100)
        self.std_table.column('email',width=100)
        self.std_table.column('name',width=100)
        self.std_table.column('id',width=100)
        self.std_table.bind("<ButtonRelease-1>",self.get_cursor)
    
    # bottom add 
        self.list_all()
    def add_std(self):
            con = pymysql.connect(host='localhost',user='root',password='',database='stud')
            cur = con.cursor()
            cur.execute("insert into s1 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.addrs_var.get(),
                                                            self.gender_var.get(),
                                                            self.cetri_var.get(),
                                                            self.phone_var.get(),
                                                            self.email_var.get(),
                                                            self.name_var.get(),
                                                            self.id_var.get()
                                                            ))
            con.commit()
            self.list_all()
            self.clear()
            con.close()
    # print data in frame list
    def list_all(self):
            con = pymysql.connect(host='localhost',user='root',password='',database='stud')
            cur = con.cursor()
            cur.execute("select * from s1 ")
            rows = cur.fetchall()
            if len (rows) !=0:
                self.std_table.delete(*self.std_table.get_children())
                for row in rows:
                    self.std_table.insert("",END,value=row)
                con.commit()
            con.close()
    # delete students from the database
    def del_std(self):
            con = pymysql.connect(host='localhost',user='root',password='',database='stud')
            cur = con.cursor()
            cur.execute("delete from s1 where name=%s",self.del_var.get())
            con.commit()
            self.list_all()
            self.clear()
            con.close()
    # clearing clouns
    def clear(self):
            self.id_var.set('')
            self.name_var.set('')
            self.email_var.set('')
            self.phone_var.set('')
            self.cetri_var.set('')
            self.gender_var.set('')
            self.addrs_var.set('')
            self.del_var.set('')
            self.search_var.set('')
    def get_cursor(self,ev):
        cursor_row=self.std_table.focus()       
        conts = self.std_table.item(cursor_row)
        row = conts['values']
        self.id_var.set(row[6])
        self.name_var.set(row[5])
        self.email_var.set(row[4])
        self.phone_var.set(row[3])
        self.cetri_var.set(row[2])
        self.gender_var.set(row[1])
        self.addrs_var.set(row[0])
    # update the database for students
    def up_std(self):
            con = pymysql.connect(host='localhost',user='root',password='',database='stud')
            cur = con.cursor()
            cur.execute("update s1 set addrs=%s,gender=%s,cetri=%s,phone=%s,email=%s,name=%s,id=%s",(
                                                        self.addrs_var.get(),
                                                        self.gender_var.get(),
                                                        self.cetri_var.get(),
                                                        self.phone_var.get(),
                                                        self.email_var.get(),
                                                        self.name_var.get(),
                                                        self.id_var.get()
                                                        ))
            con.commit()
            self.list_all()
            self.clear()
            con.close()           
        
        
root = Tk()
ob = std(root)
root.mainloop()        
