from tkinter import *
from tkinter import messagebox
import math , random , os

class Super:    
    def __init__(self,window):
        self.pro=window
        self.pro.title('super-market')
        self.pro.geometry('1300x700+150+100')
        self.pro.resizable(False,False)
        self.pro.iconbitmap('c:\\Users\\user\\Desktop\\spm\\sprm.ico')
        t1 = Label(self.pro, text='المخزن',fg='white',bg='#0B9F3A',font=('bold',14))
        t1.pack(fill=X)
        
        # varaibles total 
        self.bacolit=StringVar()
        self.adoat=StringVar()
        self.kahraba=StringVar()
        # varaibles customer
        self.name=StringVar()
        self.phone=StringVar()
        self.fatora=StringVar()
        x = random.randint(1000,9999)
        self.fatora.set(str(x))
        
        #varaibles  ba9oliyat   names 
        # varaibles adoat  md1 ==> md18
        # varaibles kahraba  br1 ==> br15
        
        # frame 1 CUSTOMER DATA  (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        f1 = Frame(pro,bg= '#8DB4C2',width=338,height=170)
        f1.place(x=962,y=28)
        
        # ===   label info customer
        tit = Label(f1,text='بيانات الزبون',bg='#8DB4C2',fg='#300532',font=('ariel',15,'bold'))
        tit.place(x=120,y=10)
        
        cust_name = Label(f1,text=': اسم المشتري ',bg='#8DB4C2',fg='#300532')
        cust_name.place(x=230,y=40)
        cust_phone = Label(f1,text=':   رقم المشتري ',bg='#8DB4C2',fg='#300532')
        cust_phone.place(x=230,y=70)
        cust_num = Label(f1,text=":    رقم الفاتورة ",bg='#8DB4C2',fg='#300532')
        cust_num.place(x=230,y=100)
        
        # === entry info customer
        en_name = Entry(f1,justify=CENTER,textvariable=self.name)
        en_name.place(x=90,y=42)
        en_phone = Entry(f1,justify=CENTER,textvariable=self.phone)
        en_phone.place(x=90,y=72)
        en_num = Entry(f1,justify=CENTER,textvariable=self.fatora)
        en_num.place(x=90,y=102)
        # === button customer
        btn = Button(f1,text='بحث',width=10,height=5,bg='#FAA300' ,cursor="hand2")
        btn.place(x=3,y=40)
        # title end
        tit1 = Label(f1,text='الفواتير ',fg='gold',font=("ariel",15,"bold"),bg='#8DB4C2')
        tit1.place(x=125,y=135)
        # frame 2        9(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        f2 = Frame(pro,bg= 'red',width=335,height=380)
        f2.place(x=962,y=200)
        scorl_y = Scrollbar(f2,orient=VERTICAL)
        self.textarea=Text(f2,yscrollcommand=scorl_y.set)
        scorl_y.pack(side=LEFT,fill=Y)
        scorl_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        # === price of the item ===
        #frame 3   (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        f3 = Frame(pro,bd=2,bg="#1C1678",width=657,height=112)
        f3.place(x=641,y=587)
        clc = Button(f3,text='الحساب',command=self.total,width=13,height=1,bg='#FAA300',cursor= "hand2")
        clc.place(x=536,y=10)
        fac = Button(f3,text='حفظ الفاتورة',command=self.save,width=13,height=1,bg='#FAA300',cursor="hand2")
        fac.place(x=536,y=55)
        clr = Button(f3,text='افراغ الحقول',command=self.clear,width=13,height=1,bg='#FAA300')
        clr.place(x=417,y=10)
        exite = Button(f3,text='اغلاق',width=13,height=1,bg='black',fg='white',command=exit)
        exite.place(x=417,y=55)
        # ========================
        lbl1 = Label(f3,text='المجموع للبقوليات',fg='gold',bg='#1C1678')
        lbl1.place(x=257,y=10)
        en1= Entry(f3,justify=CENTER,textvariable=self.bacolit)
        en1.place(x=45,y=12)
        lbl2 = Label(f3,text='المجموع اللوازم المنزلية',fg='gold',bg='#1C1678')
        lbl2.place(x=234,y=40)
        en2= Entry(f3,justify=CENTER,textvariable=self.adoat)
        en2.place(x=45,y=42)
        lbl3= Label(f3,text='المجموع الادوات الكهربائية',fg='gold',bg='#1C1678')
        lbl3.place(x=220,y=70)
        en3=Entry(f3,justify=CENTER,textvariable=self.kahraba)
        en3.place(x=45,y=72)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ frame 4  ==================================(((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))
        ff1 =Frame(pro,width=318,height=664,background= '#0B4C5F')
        ff1.place(x=1,y=30)
        t = Label(ff1,text='البقوليات',bg='#0B4C5F',fg='gold',font=('ariel',15,'bold'))
        t.place(x=122,y=0)
        bq1 = Label(ff1,text='الرز',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq1.place(x=250,y=50)
        self.rice_var =IntVar()
        bqen1 = Entry(ff1,width=12,textvariable=self.rice_var,justify=CENTER)
        bqen1.config(validate="key", validatecommand=(bqen1.register(lambda char: char.isdigit()), "%S"))
        bqen1.place(x=70,y=50)
        bq2 = Label(ff1,text='برغل',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq2.place(x=240,y=80)
        self.br_var =IntVar()
        bqen2 = Entry(ff1,width=12,textvariable=self.br_var,justify=CENTER)
        bqen2.config(validate="key", validatecommand=(bqen2.register(lambda char: char.isdigit()), "%S"))
        bqen2.place(x=70,y=80)
        bq3 = Label(ff1,text='الفاصوليا',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq3.place(x=220,y=110)
        self.fas_var =IntVar()
        bqen3 = Entry(ff1,width=12,textvariable=self.fas_var,justify=CENTER)
        bqen3.config(validate="key", validatecommand=(bqen3.register(lambda char: char.isdigit()), "%S"))
        bqen3.place(x=70,y=110)
        bq4 = Label(ff1,text='عدس',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq4.place(x=242,y=140)
        self.ads_var =IntVar()
        bqen4 = Entry(ff1,width=12,textvariable=self.ads_var,justify=CENTER)
        bqen4.config(validate="key", validatecommand=(bqen4.register(lambda char: char.isdigit()), "%S"))
        bqen4.place(x=70,y=140)
        bq5 = Label(ff1,text='معكرونة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq5.place(x=230,y=170)
        self.mk_var =IntVar()
        bqen5 = Entry(ff1,width=12,textvariable=self.mk_var,justify=CENTER)
        bqen5.config(validate="key", validatecommand=(bqen5.register(lambda char: char.isdigit()), "%S"))
        bqen5.place(x=70,y=170)
        bq6 = Label(ff1,text='فريكة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq6.place(x=244,y=200)
        self.fri_var =IntVar()
        bqen6 = Entry(ff1,width=12,textvariable=self.fri_var,justify=CENTER)
        bqen6.config(validate="key", validatecommand=(bqen6.register(lambda char: char.isdigit()), "%S"))
        bqen6.place(x=70,y=200)
        bq7 = Label(ff1,text='حمص',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq7.place(x=240,y=230)
        self.hms_var =IntVar()
        bqen7 = Entry(ff1,width=12,textvariable=self.hms_var,justify=CENTER)
        bqen7.config(validate="key", validatecommand=(bqen7.register(lambda char: char.isdigit()), "%S"))
        bqen7.place(x=70,y=230)
        bq8 = Label(ff1,text='فول',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq8.place(x=250,y=260)
        self.fol_var =IntVar()
        bqen8 = Entry(ff1,width=12,textvariable=self.fol_var,justify=CENTER)
        bqen8.config(validate="key", validatecommand=(bqen8.register(lambda char: char.isdigit()), "%S"))
        bqen8.place(x=70,y=260)
        bq9 = Label(ff1,text='ملح',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq9.place(x=250,y=290)
        self.salt_var =IntVar()
        bqen9 = Entry(ff1,width=12,textvariable=self.salt_var,justify=CENTER)
        bqen9.config(validate="key", validatecommand=(bqen9.register(lambda char: char.isdigit()), "%S"))
        bqen9.place(x=70,y=290)
        bq10 = Label(ff1,text='سكر',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq10.place(x=250,y=320)
        self.suger_var =IntVar()
        bqen10 = Entry(ff1,width=12,textvariable=self.suger_var,justify=CENTER)
        bqen10.config(validate="key", validatecommand=(bqen10.register(lambda char: char.isdigit()), "%S"))
        bqen10.place(x=70,y=320)
        bq11 = Label(ff1,text='فلفل اسود',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq11.place(x=220,y=350)
        self.noir_var =IntVar()
        bqen11 = Entry(ff1,width=12,textvariable=self.noir_var,justify=CENTER)
        bqen11.config(validate="key", validatecommand=(bqen11.register(lambda char: char.isdigit()), "%S"))
        bqen11.place(x=70,y=350)
        bq12 = Label(ff1,text='فلفل احمر',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq12.place(x=220,y=380)
        self.rouge_var =IntVar()
        bqen12 = Entry(ff1,width=12,textvariable=self.rouge_var,justify=CENTER)
        bqen12.config(validate="key", validatecommand=(bqen12.register(lambda char: char.isdigit()), "%S"))
        bqen12.place(x=70,y=380)
        bq13 = Label(ff1,text='اللوبيا',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq13.place(x=242,y=410)
        self.lob_var =IntVar()
        bqen13 = Entry(ff1,width=12,textvariable=self.lob_var,justify=CENTER)
        bqen13.config(validate="key", validatecommand=(bqen13.register(lambda char: char.isdigit()), "%S"))
        bqen13.place(x=70,y=410)
        bq14 = Label(ff1,text='الاندمي',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq14.place(x=237,y=440)
        self.indo_var =IntVar()
        bqen14 = Entry(ff1,width=12,textvariable=self.indo_var,justify=CENTER)
        bqen14.config(validate="key", validatecommand=(bqen14.register(lambda char: char.isdigit()), "%S"))
        bqen14.place(x=70,y=440)
        bq15 = Label(ff1,text='القمح',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq15.place(x=245,y=470)
        self.amh_var =IntVar()
        bqen15 = Entry(ff1,width=12,textvariable=self.amh_var,justify=CENTER)
        bqen15.config(validate="key", validatecommand=(bqen15.register(lambda char: char.isdigit()), "%S"))
        bqen15.place(x=70,y=470)
        bq16 = Label(ff1,text='الشعير',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq16.place(x=242,y=500)
        self.chir_var =IntVar()
        bqen16 = Entry(ff1,width=12,textvariable=self.chir_var,justify=CENTER)
        bqen16.config(validate="key", validatecommand=(bqen16.register(lambda char: char.isdigit()), "%S"))
        bqen16.place(x=70,y=500)
        bq17 = Label(ff1,text='الشوفان',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq17.place(x=235,y=530)
        self.chof_var =IntVar()
        bqen17 = Entry(ff1,width=12,textvariable=self.chof_var,justify=CENTER)
        bqen17.config(validate="key", validatecommand=(bqen17.register(lambda char: char.isdigit()), "%S"))
        bqen17.place(x=70,y=530)
        bq18= Label(ff1,text='الذرة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        bq18.place(x=250,y=560)
        self.dor_var =IntVar()
        bqen18 = Entry(ff1,width=12,textvariable=self.dor_var,justify=CENTER)
        bqen18.config(validate="key", validatecommand=(bqen18.register(lambda char: char.isdigit()), "%S"))
        bqen18.place(x=70,y=560)
        ################################ frame 5 (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))
        ff2 =Frame(pro,width=318,height=664,background= '#0B4C5F')
        ff2.place(x=321,y=30)    
        t = Label(ff2,text='اللوازم المنزلية',bg='#0B4C5F',fg='gold',font=('ariel',15,'bold'))
        t.place(x=105,y=0)
        md1 = Label(ff2,text='مصفاة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md1.place(x=240,y=50)
        self.md1_var =IntVar()
        mden1 = Entry(ff2,width=12,textvariable=self.md1_var,justify=CENTER)
        mden1.config(validate="key", validatecommand=(mden1.register(lambda char: char.isdigit()), "%S"))
        mden1.place(x=70,y=50)    
        md2= Label(ff2,text='صحن',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md2.place(x=245,y=80)
        self.md2_var =IntVar()
        mden2 = Entry(ff2,width=12,textvariable=self.md2_var,justify=CENTER)
        mden2.config(validate="key", validatecommand=(mden2.register(lambda char: char.isdigit()), "%S"))
        mden2.place(x=70,y=80)
        md3= Label(ff2,text="كاس",bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md3.place(x=250,y=110)
        self.md3_var =IntVar()
        mden3 = Entry(ff2,width=12,textvariable=self.md3_var,justify=CENTER)
        mden3.config(validate="key", validatecommand=(mden3.register(lambda char: char.isdigit()), "%S"))
        mden3.place(x=70,y=110)
        md4= Label(ff2,text='ابريق',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md4.place(x=243,y=140)
        self.md4_var =IntVar()
        mden4 = Entry(ff2,width=12,textvariable=self.md4_var,justify=CENTER)
        mden4.config(validate="key", validatecommand=(mden4.register(lambda char: char.isdigit()), "%S"))
        mden4.place(x=70,y=140)
        md5= Label(ff2,text='سكين',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md5.place(x=243,y=170)
        self.md5_var =IntVar()
        mden5 = Entry(ff2,width=12,textvariable=self.md5_var,justify=CENTER)
        mden5.config(validate="key", validatecommand=(mden5.register(lambda char: char.isdigit()), "%S"))
        mden5.place(x=70,y=170)
        md6= Label(ff2,text='شوك',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md6.place(x=245,y=200)
        self.md6_var =IntVar()
        mden6 = Entry(ff2,width=12,textvariable=self.md6_var,justify=CENTER)
        mden6.config(validate="key", validatecommand=(mden6.register(lambda char: char.isdigit()), "%S"))
        mden6.place(x=70,y=200)
        md7= Label(ff2,text='طنجرة ',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md7.place(x=235,y=230)
        self.md7_var =IntVar()
        mden7 = Entry(ff2,width=12,textvariable=self.md7_var,justify=CENTER)
        mden7.config(validate="key", validatecommand=(mden7.register(lambda char: char.isdigit()), "%S"))
        mden7.place(x=70,y=230)
        md8= Label(ff2,text='سلة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md8.place(x=250,y=260)
        self.md8_var =IntVar()
        mden8 = Entry(ff2,width=12,textvariable=self.md8_var,justify=CENTER)
        mden8.config(validate="key", validatecommand=(mden8.register(lambda char: char.isdigit()), "%S"))
        mden8.place(x=70,y=260)
        md9 = Label(ff2,text='ملاعق',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md9.place(x=235,y=290)
        self.md9_var =IntVar()
        mden9 = Entry(ff2,width=12,textvariable=self.md9_var,justify=CENTER)
        mden9.config(validate="key", validatecommand=(mden9.register(lambda char: char.isdigit()), "%S"))
        mden9.place(x=70,y=290)
        md10 = Label(ff2,text='صينية',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md10.place(x=235,y=320)
        self.md10_var =IntVar()
        mden10 = Entry(ff2,width=12,textvariable=self.md10_var,justify=CENTER)
        mden10.config(validate="key", validatecommand=(mden10.register(lambda char: char.isdigit()), "%S"))
        mden10.place(x=70,y=320)
        md11= Label(ff2,text='وعاء الخلط',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md11.place(x=205,y=350)
        self.md11_var =IntVar()
        mden11 = Entry(ff2,width=12,textvariable=self.md11_var,justify=CENTER)
        mden11.config(validate="key", validatecommand=(mden11.register(lambda char: char.isdigit()), "%S"))
        mden11.place(x=70,y=350)
        md12 = Label(ff2,text='فتاحة علب',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md12.place(x=210,y=380)
        self.md12_var =IntVar()
        mden12 = Entry(ff2,width=12,textvariable=self.md12_var,justify=CENTER)
        mden12.config(validate="key", validatecommand=(mden12.register(lambda char: char.isdigit()), "%S"))
        mden12.place(x=70,y=380)
        md13 = Label(ff2,text='مقشرة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md13.place(x=232,y=410)
        self.md13_var =IntVar()
        mden13 = Entry(ff2,width=12,textvariable=self.md13_var,justify=CENTER)
        mden13.config(validate="key", validatecommand=(mden13.register(lambda char: char.isdigit()), "%S"))
        mden13.place(x=70,y=410)
        md14 = Label(ff2,text='لوح التقطيع',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md14.place(x=200,y=440)
        self.md14_var =IntVar()
        mden14 = Entry(ff2,width=12,textvariable=self.md14_var,justify=CENTER)
        mden14.config(validate="key", validatecommand=(mden14.register(lambda char: char.isdigit()), "%S"))
        mden14.place(x=70,y=440)
        md15 = Label(ff2,text='حفارة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md15.place(x=235,y=470)
        self.md15_var =IntVar()
        mden15 = Entry(ff2,width=12,textvariable=self.md15_var,justify=CENTER)
        mden15.config(validate="key", validatecommand=(mden15.register(lambda char: char.isdigit()), "%S"))
        mden15.place(x=70,y=470)
        md16 = Label(ff2,text='سلة قمامة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md16.place(x=210,y=500)
        self.md16_var =IntVar()
        mden16 = Entry(ff2,width=12,textvariable=self.md16_var,justify=CENTER)
        mden16.config(validate="key", validatecommand=(mden16.register(lambda char: char.isdigit()), "%S"))
        mden16.place(x=70,y=500)
        md17 = Label(ff2,text='منفخة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md17.place(x=230,y=530)
        self.md17_var =IntVar()
        mden17 = Entry(ff2,width=12,textvariable=self.md17_var,justify=CENTER)
        mden17.config(validate="key", validatecommand=(mden17.register(lambda char: char.isdigit()), "%S"))
        mden17.place(x=70,y=530)
        md18 = Label(ff2,text='اكياس',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        md18.place(x=232,y=560)
        self.md18_var =IntVar()
        mden18 = Entry(ff2,width=12,textvariable=self.md18_var,justify=CENTER)
        mden18.config(validate="key", validatecommand=(mden18.register(lambda char: char.isdigit()), "%S"))
        mden18.place(x=70,y=560)
        # frame 6 ((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        ff3 =Frame(pro,width=318,height=550,background= '#0B4C5F')
        ff3.place(x=641,y=30)    
        t = Label(ff3,text=' الادوات الكهربائية',bg='#0B4C5F',fg='gold',font=('ariel',15,'bold'))
        t.place(x=105,y=0)
        br1 = Label(ff3,text='مكنسة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br1.place(x=232,y=50)
        self.br1_var=IntVar()
        bren1=Entry(ff3,width=12,justify=CENTER,textvariable=self.br1_var)
        bren1.place(x=70,y=50)
        br2 = Label(ff3,text='تلفزيون',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br2.place(x=232,y=80)
        self.br2_var=IntVar()
        bren2=Entry(ff3,width=12,justify=CENTER,textvariable=self.br2_var)
        bren2.place(x=70,y=80)
        br3 = Label(ff3,text='غسالة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br3.place(x=232,y=110)
        self.br3_var=IntVar()
        bren3=Entry(ff3,width=12,justify=CENTER,textvariable=self.br3_var)
        bren3.place(x=70,y=110)
        br4 = Label(ff3,text='ميكرويف',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br4.place(x=232,y=140)
        self.br4_var=IntVar()
        bren4=Entry(ff3,width=12,justify=CENTER,textvariable=self.br4_var)
        bren4.place(x=70,y=140)
        br5 = Label(ff3,text='خلاط',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br5.place(x=232,y=170)
        self.br5_var=IntVar()
        bren5=Entry(ff3,width=12,justify=CENTER,textvariable=self.br5_var)
        bren5.place(x=70,y=170)
        br6 = Label(ff3,text='فرن غاز',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br6.place(x=232,y=200)
        self.br6_var=IntVar()
        bren6=Entry(ff3,width=12,justify=CENTER,textvariable=self.br6_var)
        bren6.place(x=70,y=200)
        br7 = Label(ff3,text='مقلاة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br7.place(x=232,y=230)
        self.br7_var=IntVar()
        bren7=Entry(ff3,width=12,justify=CENTER,textvariable=self.br7_var)
        bren7.place(x=70,y=230)
        br8 = Label(ff3,text='مروحة 1',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br8.place(x=232,y=260)
        self.br8_var=IntVar()
        bren8=Entry(ff3,width=12,justify=CENTER,textvariable=self.br8_var)
        bren8.place(x=70,y=260)
        br9 = Label(ff3,text='مروحة 2',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br9.place(x=232,y=290)
        self.br9_var=IntVar()
        bren9=Entry(ff3,width=12,justify=CENTER,textvariable=self.br9_var)
        bren9.place(x=70,y=290)
        br10 = Label(ff3,text='تلفزيون 32',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br10.place(x=232,y=320)
        self.br10_var=IntVar()
        bren10=Entry(ff3,width=12,justify=CENTER,textvariable=self.br10_var)
        bren10.place(x=70,y=320)
        br11 = Label(ff3,text='تلفزيون 43',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br11.place(x=232,y=350)
        self.br11_var=IntVar()
        bren11=Entry(ff3,width=12,justify=CENTER,textvariable=self.br11_var)
        bren11.place(x=70,y=350)
        br12 = Label(ff3,text='فلتر ماء',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br12.place(x=232,y=380)
        self.br12_var=IntVar()
        bren12=Entry(ff3,width=12,justify=CENTER,textvariable=self.br12_var)
        bren12.place(x=70,y=380)
        br13 = Label(ff3,text='غسالة اوتو',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br13.place(x=232,y=410)
        self.br13_var=IntVar()
        bren13=Entry(ff3,width=12,justify=CENTER,textvariable=self.br13_var)
        bren13.place(x=70,y=410)
        br14 = Label(ff3,text='مكواة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br14.place(x=232,y=440)
        self.br14_var=IntVar()
        bren14=Entry(ff3,width=12,justify=CENTER,textvariable=self.br14_var)
        bren14.place(x=70,y=440)
        br15 = Label(ff3,text='مبردة',bg='#0B4C5F',fg='white',font=('ariel',13,'bold'))
        br15.place(x=232,y=470)
        self.br15_var=IntVar()
        bren15=Entry(ff3,width=12,justify=CENTER,textvariable=self.br15_var)
        bren15.place(x=70,y=470)
        
        self.welcome()
    
    def total(self):
        self.rez=self.rice_var.get()*1.5
        self.bor=self.br_var.get()*0.5
        self.adss=self.ads_var.get()*1
        self.makron=self.mk_var.get()*1.5
        self.frika=self.fri_var.get()*2
        self.hams=self.hms_var.get()*1
        self.fol=self.fol_var.get()*1
        self.salt=self.salt_var.get()*1.5
        self.suger=self.suger_var.get()*1
        self.noir=self.noir_var.get()*1
        self.rouge=self.rouge_var.get()*1.5
        self.lob=self.lob_var.get()*1.5
        self.indo=self.indo_var.get()*1
        self.amh=self.amh_var.get()*2
        self.chir=self.chir_var.get()*1
        self.chof=self.chof_var.get()*2
        self.dor=self.dor_var.get()*1.5
        self.totabako=float(
            self.rez+
            self.bor+
            self.adss+
            self.makron+
            self.frika+
            self.hams+
            self.fol+
            self.salt+
            self.suger+
            self.noir+
            self.rouge+
            self.lob+
            self.indo+
            self.amh+
            self.chir+
            self.chof+
            self.dor
        )
        self.bacolit.set(f"{str(self.totabako)}$")
        
        self.x1=self.md1_var.get()*1.5
        self.x2=self.md2_var.get()*2
        self.x3=self.md3_var.get()*1
        self.x4=self.md4_var.get()*1.5
        self.x5=self.md5_var.get()*1.5
        self.x6=self.md6_var.get()* 1.5
        self.x7=self.md7_var.get()*2
        self.x8=self.md8_var.get()*3
        self.x9=self.md9_var.get()*0.5
        self.x0=self.md10_var.get()*2
        self.x11=self.md11_var.get()*4
        self.x12=self.md12_var.get()*5
        self.x13=self.md13_var.get()*1.5
        self.x14=self.md14_var.get()*4
        self.x15=self.md15_var.get()*3
        self.x16=self.md16_var.get()*1
        self.x17=self.md17_var.get()*2
        self.x18=self.md18_var.get()*3
        self.totaladoit=float(
            self.x1+
            self.x2+
            self.x3+
            self.x4+
            self.x5+
            self.x6+
            self.x7+
            self.x8+
            self.x9+
            self.x0+
            self.x11+
            self.x12+
            self.x13+
            self.x14+
            self.x15+
            self.x16+
            self.x17+
            self.x18            
        )
        self.adoat.set(f"{str(self.totaladoit)}$")
        
        self.y1=self.br1_var.get()*33
        self.y2=self.br2_var.get()*35
        self.y3=self.br3_var.get()*43
        self.y4=self.br4_var.get()*35
        self.y5=self.br5_var.get()*20
        self.y6=self.br6_var.get()*67
        self.y7=self.br7_var.get()*50
        self.y8=self.br8_var.get()*40
        self.y9=self.br9_var.get()*30
        self.y0=self.br10_var.get()*70
        self.y11=self.br11_var.get()*60
        self.y12=self.br12_var.get()*30
        self.y13=self.br13_var.get()*77
        self.y14=self.br14_var.get()*70
        self.y15=self.br15_var.get()*70
        self.totalkahraba=float(
            self.y1+
            self.y2+
            self.y3+
            self.y4+
            self.y5+
            self.y6+
            self.y7+
            self.y8+
            self.y9+
            self.y0+
            self.y11+
            self.y12+
            self.y13+
            self.y14+
            self.y15         
        )
        self.kahraba.set(f"{str(self.totalkahraba)}$") 
        self.all=float(self.totabako+
                       self.totaladoit+
                       self.totalkahraba
        )
        
    def welcome(self):
        self.textarea.delete("1.0", END)
        self.textarea.insert(END, "\t  سوبر ماركيت يرحب بكم")
        self.textarea.insert(END, "\n========================================")
        self.textarea.insert(END, f"\n\t b.NUM  :{self.fatora.get()}")
        self.textarea.insert(END, f"\n\t NAME   :{self.name.get()}")
        self.textarea.insert(END, f"\n\t PHONE  :{self.phone.get()}")
        self.textarea.insert(END, "\n========================================")
        self.textarea.insert(END, f"\n   السعر   \t    العدد \t        المشتريات")
        self.textarea.insert(END, "\n========================================")

    def clear(self):
        self.rice_var.set('0')
        self.br_var.set('0')
        self.fas_var.set('0')
        self.ads_var.set('0')
        self.mk_var.set('0')
        self.fri_var.set('0')
        self.hms_var.set('0')
        self.fol_var.set('0')
        self.salt_var.set('0')
        self.suger_var.set('0')
        self.noir_var.set('0')
        self.rouge_var.set('0')
        self.lob_var.set('0')
        self.indo_var.set('0')
        self.amh_var.set('0')
        self.chir_var.set('0')
        self.chof_var.set('0')
        self.dor_var.set('0')
        
        self.br1_var.set('0')
        self.br2_var.set('0')
        self.br3_var.set('0')
        self.br4_var.set('0')
        self.br5_var.set('0')
        self.br6_var.set('0')
        self.br7_var.set('0')
        self.br8_var.set('0')
        self.br9_var.set('0')
        self.br10_var.set('0')
        self.br11_var.set('0')
        self.br12_var.set('0')
        self.br13_var.set('0')
        self.br14_var.set('0')
        self.br15_var.set('0')
        
        self.md1_var.set('0')
        self.md2_var.set('0')
        self.md3_var.set('0')
        self.md4_var.set('0')
        self.md5_var.set('0')
        self.md6_var.set('0')
        self.md7_var.set('0')
        self.md8_var.set('0')
        self.md9_var.set('0')
        self.md10_var.set('0')
        self.md11_var.set('0')
        self.md12_var.set('0')
        self.md13_var.set('0')
        self.md14_var.set('0')
        self.md15_var.set('0')
        self.md16_var.set('0')
        self.md17_var.set('0')
        self.md18_var.set('0')
        
        self.bacolit.set('')
        self.adoat.set('')
        self.kahraba.set('')
        self.name.set('')
        self.phone.set('')
        
        x = random.randint(1000,9999)
        self.fatora.set(str(x))
        self.welcome()

    def save(self):
        op = messagebox.askyesno('حفظ','هل تريد حفظ الفاتورة ؟')
        if op > 0 :
            self.bb = self.textarea.get('1.0',END)
            f1 = open('D:\\buy\\'+str(self.fatora.get())+".txt","w",encoding='utf-8')
            f1.write(self.bb)
            f1.close()
            self.welcome()
        else:
            return

pro= Tk()
ob = Super(pro)
pro.mainloop() 