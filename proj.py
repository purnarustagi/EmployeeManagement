from tkinter import*
root=Tk()

def Add_Record():
    f=open('employee.txt','a')
    emp_name=s2.get()
    emp_id=s1.get()
    depart=s3.get()
    PHONE_NUM=s4.get()
    email_id=s5.get()
    salary=s6.get()
    attendence=s7.get()
    doj=s8.get()
   
    f.writelines(emp_id.ljust(20)+emp_name.ljust(20)+depart.ljust(20)+PHONE_NUM.ljust(20)+email_id.ljust(20)+salary.ljust(20)+attendence.ljust(20)+doj.ljust(20)+"\n")
    s=emp_name+" added to the record!"
    s9.set(s)
    f.close()
    
def get_first():
    f=open("employee.txt",'r')
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1]) 
    s3.set(j[2]) 
    s4.set(j[3]) 
    s5.set(j[4]) 
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    f.close()

def get_last():
    f=open("employee.txt",'r')
    ctr= sum(1 for line in open("employee.txt"))-1
    print(ctr)
    try:
     k=f.readlines()[ctr]
     j=k.split()
     print(j)
    
     s1.set(j[0])
     s2.set(j[1]) 
     s3.set(j[2]) 
     s4.set(j[3]) 
     s5.set(j[4]) 
     s6.set(j[5])
     s7.set(j[6])
     s8.set(j[7])
    except Exception:
     s9.set("No record !!")
    f.close()
c=0

def get_next():
    global c
    f=open("employee.txt",'r')
    ctr= sum(1 for line in open("employee.txt"))-1
    print(ctr)
    try:
     k=f.readlines()[c]
     j=k.split()
     print(j)
    
     s1.set(j[0])
     s2.set(j[1]) 
     s3.set(j[2]) 
     s4.set(j[3]) 
     s5.set(j[4]) 
     s6.set(j[5])
     s7.set(j[6])
     s8.set(j[7])
    except Exception:
     s9.set("No record !!")
    c=c+1
    if(c==ctr+1):
        c=0
    f.close()


c1=0
def get_previous():
    global c1
    f=open("employee.txt",'r')
    ctr= sum(1 for line in open("employee.txt"))-1
    print(ctr)
    try:
     k=f.readlines()[c1]
     j=k.split()
    except Exception:
     s9.set("No record !!")
    
    print(j)
    s1.set(j[0])
    s2.set(j[1]) 
    s3.set(j[2]) 
    s4.set(j[3]) 
    s5.set(j[4]) 
    s6.set(j[5])
    s7.set(j[6])
    s8.set(j[7])
    c1=c1-1
    if(c1==-1):
        c1=ctr
    f.close()


    
def SEARCH():
    k=s1.get()
    f=open('employee.txt','r')
    h=f.readlines() 
    a=0
    for i in h: 
        j=i.split() 
        if(j[0]==k): 
            a=1
            s9.set("EMPLOYEE found")  
            print(j)
            s1.set(j[0])
            s2.set(j[1]) 
            s3.set(j[2]) 
            s4.set(j[3]) 
            s5.set(j[4]) 
            s6.set(j[5])
            s7.set(j[6])
            s8.set(j[7])

    if(a != 1):
        s9.set("EMPLOYEE NOT FOUND ")
    f.close()        


def update():

    x1=s1.get()
    x2=s2.get()
    x3=s3.get()
    x4=s4.get()
    x5=s5.get()
    x6=s6.get()
    x7=s7.get()
    x8=s8.get()
    f=open("employee.txt",'r')
    k=f.readlines()
    f.close()
    f=open("employee.txt",'w')
    z=0
    for i in k:
        j=i.split()
        if(j[0]!=x1):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(20)+j[5].ljust(20)+j[6].ljust(20)+j[7].ljust(20)+"\n")
            
            
        else:
            f.writelines(x1.ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(20)+x6.ljust(20)+x7.ljust(20)+x8.ljust(20)+"\n")
            z=1
            s9.set("Successfully updated")

    if(z==0):
        s9.set("Cannot be updated")
            
    
    
def clear():
     s1.set("")
     s2.set("") 
     s3.set("") 
     s4.set("") 
     s5.set("") 
     s6.set("")
     s7.set("")
     s8.set("")
     s9.set("")

        

def delrec(): 
    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get(),s6.get(),s7.get(),s8.get()] 
    f=open("employee.txt","r") 
    lines=f.readlines() 
    print(lines) 
    print(k) 
    f.close() 
    f=open("employee.txt","w") 
    for i in lines: 
        m=i.split() 
         
        if(m!=k): 
             f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(20)+m[5].ljust(20)+m[6].ljust(20)+m[7].ljust(20)+"\n") 
    f.close() 

    





l1=Label(root,text="*****EMPLOYEE MANAGEMENT SYSTEM***** ",bg="darkblue",font=('Ariel',22,'bold'),fg="white")
l1.grid(row=0,column=1)
l3=Label(root,text="EMPLOYEE NAME ",font=('Ariel',15,'bold'),fg="darkblue")
l2=Label(root,text="EMPLOYEE ID ",font=('Ariel',15,'bold'),fg="darkblue")
l4=Label(root,text="DEPARTMENT ",font=('Ariel',15,'bold'),fg="darkblue")
l5=Label(root,text="PHONE NUMBER",font=('Ariel',15,'bold'),fg="darkblue")
l6=Label(root,text="EMAIL ID",font=('Ariel',15,'bold'),fg="darkblue")
l7=Label(root,text="SALARY",font=('Ariel',15,'bold'),fg="darkblue")
l8=Label(root,text="ATTENDENCE",font=('Ariel',15,'bold'),fg="darkblue")
l9=Label(root,text="DATE OF JOINING ",font=('Ariel',15,'bold'),fg="darkblue")




l2.grid(row=2)
l3.grid(row=3)
l4.grid(row=4)
l5.grid(row=5)
l6.grid(row=2,column=2)
l7.grid(row=3,column=2)
l8.grid(row=4,column=2)
l9.grid(row=5,column=2)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()
s9=StringVar()






e2=Entry(root,textvariable=s1)
e3=Entry(root,textvariable=s2)
e4=Entry(root,textvariable=s3)
e5=Entry(root,textvariable=s4)
e6=Entry(root,textvariable=s5)
e7=Entry(root,textvariable=s6)
e8=Entry(root,textvariable=s7)
e9=Entry(root,textvariable=s8)
e10=Entry(root,textvariable=s9,width=50)



e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)
e5.grid(row=5,column=1)
e6.grid(row=2,column=3)
e7.grid(row=3,column=3)
e8.grid(row=4,column=3)
e9.grid(row=5,column=3)
e10.grid(row=6,column=2)


b11=Button(root,text="|<",width=15,bg="green",padx = 20,relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=get_first).grid(row=1, column=0)
b12=Button(root,text="<",width=15,bg="green",padx = 20,relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=get_previous).grid(row=1, column=1)
b13=Button(root,text=">",width=15,bg="green",padx = 20,relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=get_next).grid(row=1, column=2)
b14=Button(root,text=">|",width=15,bg="green",padx = 20,relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=get_last).grid(row=1, column=3)
b15=Button(root,text="CLEAR",width=15,bg="darkblue",relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=clear).grid(row=6, column=3)

b1=Button(root,text="ADD",width=15,bg="green", relief = GROOVE ,font=('Ariel',15,'bold'),fg="white",command=Add_Record).grid(row=10, column=0)
b2=Button(root,text="DELETE",width=15,bg="green", relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=delrec).grid(row=10, column=1)
b3=Button(root,text="SEARCH",width=15,bg="green",relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=SEARCH).grid(row=10, column=2)
b4=Button(root,text="UPDATE",width=15,bg="green",relief = GROOVE,font=('Ariel',15,'bold'),fg="white",command=update).grid(row=10, column=3)

root.mainloop()

