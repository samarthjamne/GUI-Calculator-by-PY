from tkinter import *
root=Tk()
root.title("calculator")


e1=Entry(root,borderwidth=5,width=35)
e1.grid(column=0,row=0,columnspan=3,padx=10,pady=10)

def click_button(number):
       current=e1.get()
       e1.delete(0,END)
       e1.insert(0,str(current)+str(number))

def add():
       first_num=e1.get()
       first_num=e1.get()
       global  f_num
       global math
       math="addition"
       f_num= int(first_num)
       e1.delete(0,END)

def multi():
       first_num=e1.get()
       first_num=e1.get()
       global  f_num
       global math
       math="multi"
       f_num= int(first_num)
       e1.delete(0,END)

def sub():
       first_num=e1.get()
       first_num=e1.get()
       global  f_num
       global math
       math="sub"
       f_num= int(first_num)
       e1.delete(0,END)

def div():
       first_num=e1.get()
       first_num=e1.get()
       global  f_num
       global math
       math="div"
       f_num= int(first_num)
       e1.delete(0,END)

def mod():
       first_num=e1.get()
       first_num=e1.get()
       global  f_num
       global math
       math="mod"
       f_num= int(first_num)
       e1.delete(0,END)

def equal():
     if(math=="addition"):
       second_num=e1.get() 
       e1.delete(0,END)           
       e1.insert(0,f_num+int(second_num))

     elif(math=="multi"):
       second_num=e1.get() 
       e1.delete(0,END)           
       e1.insert(0,f_num*int(second_num))
   
     elif(math=="div"):
       second_num=e1.get() 
       e1.delete(0,END)           
       e1.insert(0,f_num/int(second_num))

     elif(math=="sub"):
       second_num=e1.get() 
       e1.delete(0,END)           
       e1.insert(0,f_num-int(second_num))

     elif(math=="mod"):
       second_num=e1.get() 
       e1.delete(0,END)           
       e1.insert(0,f_num%int(second_num))

def clear() :
       
    e1.delete(0,END)
     

b1=Button(root,text="1",padx=30,pady=10, command=lambda: click_button(1))
b2=Button(root,text="2",padx=30,pady=10, command=lambda: click_button(2))
b3=Button(root,text="3",padx=30,pady=10, command=lambda: click_button(3))

b4=Button(root,text="4",padx=30,pady=10, command=lambda: click_button(4))
b5=Button(root,text="5",padx=30,pady=10, command=lambda: click_button(5))
b6=Button(root,text="6",padx=30,pady=10, command=lambda: click_button(6))

b7=Button(root,text="7",padx=30,pady=10, command=lambda: click_button(7))
b8=Button(root,text="8",padx=30,pady=10, command=lambda: click_button(8))
b9=Button(root,text="9",padx=30,pady=10, command=lambda: click_button(9))
b0=Button(root,text="0",padx=30,pady=10, command=lambda: click_button(0))

bclear=Button(root,text="clear",padx=62,pady=10, command=clear)
badd=Button(root,text="+",padx=30,pady=10, command=add)
bmulti=Button(root,text="*",padx=30,pady=10,command=multi)

bsub=Button(root,text="-",padx=30,pady=10,command=sub)
bdiv=Button(root,text="/",padx=30,pady=10,command=div)
bmod=Button(root,text="%",padx=30,pady=10,command=mod)
bequal=Button(root,text="=",padx=30,pady=10,command=equal)

b1.grid(column=0,row=3)
b2.grid(column=1,row=3)
b3.grid(column=2,row=3)

b4.grid(column=0,row=2)
b5.grid(column=1,row=2)
b6.grid(column=2,row=2)

b7.grid(column=0,row=1)
b8.grid(column=1,row=1)
b9.grid(column=2,row=1)

b0.grid(column=0,row=4)
bclear.grid(column=1,row=4,columnspan=2)
badd.grid(column=0,row=5)

bmulti.grid(column=1,row=5)
bsub.grid(column=2,row=5)
bdiv.grid(column=0,row=6)

bmod.grid(column=1,row=6)
bequal.grid(column=2,row=6)




root.mainloop()