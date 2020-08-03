from tkinter import *
import time
from tkinter import ttk
import datetime

msg1='Welcome to Python Programming...'
msg2='Welcome to our Hotel...'
msg3='Powered by Python Programming...'
msg4='Thank you for your patronage...'
msg5='Welcome to Python Programming...'
msg6='Welcome to Python Programming...'
text1=''
n=0



#=================================== CALCULATOR FUNCTIONS ============================

def btn(numbers):
    global operator
    operator=operator+str(numbers)
    txt_input.set(operator)

    
def clear():
    global operator
    operator=''
    txt_input.set('')
    Display.insert(0,'start calculation....')
    
def equal():
    global operator
    sumup=float(eval(operator))
    txt_input.set(sumup)
    operator =''
    
#==================================== TOTAL FUNCTION=================================
def total_result():
    #============= COST OF MEAL ===========================
    varme1=Mealdicator.get()
    varme2=Meal1.get()
    if varme1 == 'Fried Rice':
        varme3 = (varme2*1.8)
        Cost.set(varme3)
        
    elif varme1 == 'Fried Rice & Chicken':
        varme3 = (varme2*3.7)
        Cost.set(varme3)
        
    elif varme1 == 'Manchurian':
        varme3 = (varme2*1.6)
        Cost.set(varme3)
        
    elif varme1 == 'Cheese':
        varme3 = (varme2*0.9)
        Cost.set(varme3)
        
    elif varme1 == 'Burger':
        varme3 = (varme2*1.01)
        Cost.set(varme3)
        
    else:
        varme3 = (varme2*0.00)
        Cost.set(varme3)
       
    
    #===================== COST OF DRINK ===========================
    vardi1=Drinkdicator.get()
    vardi2=Drink1.get()
    if vardi1 == 'Coka Cola':
        vardi3 = (vardi2*1.8)
        Drinks.set(vardi3)
        
    elif vardi1 == 'Appy Fizz':
        vardi3 = (vardi2*3.7)
        Drinks.set(vardi3)
        
    elif vardi1 == 'Pepsi':
        vardi3 = (vardi2*1.6)
        Drinks.set(vardi3)
        
    elif vardi1 == 'Red Wine':
        vardi3 = (vardi2*0.9)
        Drinks.set(vardi3)
        
    elif vardi1 == 'Bottled Water':
        vardi3 = (vardi2*1.01)
        Drinks.set(vardi3)
        
    else:
        vardi3 = (vardi2*0.00)
        Drinks.set(vardi3)    
        
    #=================== DELIVERY COST====================
    num1=float(Cost.get())
    num2=float(Drinks.get())
    Delivery=(num1+num2)* 0.2
    
    #=================== COST OF ROOM ====================
    room=v.get()
    null=0.0
    
    rvip=10.0   # cost of vip room
    rvip1=Delivery/(10*0.5) # vip room with delivery cost
      
    rnormal=5.0  # cost of normal room
    rnormal1=Delivery/(5*2.5)  # normal room delivery cost
    
    if room ==1:
        if chkb1.get() ==1:
            ServiceCharge.set(rvip1)
            RoomCost.set(10.0)
            DevCost.set(Delivery)  
        else:
            ServiceCharge.set(null)
            DevCost.set(null)
            RoomCost.set(10.0)
            
    elif room==2:
        if chkb1.get() ==1:
            ServiceCharge.set(rnormal)
            RoomCost.set(5.0)
            DevCost.set(Delivery)  
        else:
            ServiceCharge.set(null)
            DevCost.set(null)
            RoomCost.set(5.0)
        
    elif room==3:
        if chkb1.get() ==1:
            ServiceCharge.set(null)
            RoomCost.set(null)
            DevCost.set(null)  
        else:
            ServiceCharge.set(null)
            DevCost.set(null)
            RoomCost.set(null)
            
    
    #======================= TOTAL RESULT ==========================
    num3=float(DevCost.get())
    num4=float(RoomCost.get())
    num5=float(ServiceCharge.get())
    
    MyTotal=num1+num2+num3+num4+num5
    Total.set(MyTotal)
    FinalTotal="Total = $",MyTotal
    
    num6=Total.get()
    Display.delete(0,END)
    Display.insert(0,FinalTotal)    
        
    if num6 == '0.0':
        Display.delete(0,END)
        Display.insert(0,'Please, make an Order')
        
#================================= CONVERTER ==============================================
def Convert():
    var2=indicator.get()
    var3=var1.get()
    if var2 == 'India':
        Display.delete(0,END)
        var4=('Rupee ₹ ',(var3*74.93))
        Display.insert(0,var4)
    elif var2== 'France':
        Display.delete(0,END)
        var4=('Euro € ',(var3*0.85))
        Display.insert(0,var4)
    elif var2== 'Ghana':
        Display.delete(0,END)
        var4=('Cedi ₵ ',(var3*4.88))
        Display.insert(0,var4)
    elif var2== 'Mexico':
        Display.delete(0,END)
        var4=('MXN $ ',(var3*18.90))
        Display.insert(0,var4)
    elif var2== 'Nigeria':
        Display.delete(0,END)
        var4=('Naira ₦ ',(var3*361.01))
        Display.insert(0,var4)
    elif var2== 'USA':
        Display.delete(0,END)
        var4=('USD $ ',(var3*1.00))
        Display.insert(0,var4)
    else:
        Display.delete(0,END)
        Display.insert(0,'Error:Select a Country!!')
    
#==================================== RESET BUTTON ==========================================

'''def scroll():
    for line in Line:
        for c in line:
            print(c, end='')
            sys.stdout.flush()
            sleep(0.1)
        print('')'''


def Hotel():
    Display.delete(0,END)
    Display.insert(0,'Hotel Management Sys.')
    
def Powered():
    Display.delete(0,END)
    Display.insert(0,'Powered by Python....')
    
def Reset():
    Display.delete(0,END)
    Display.insert(0,'System Resetting.....')
    Display.after(2000,Hotel)
    Display.after(4000,Powered)
    Display.after(6000,Rest)
    
def Rest():
    clear()
    Display.delete(0,END)
    Display.insert(0,'Hello Welcome !!!')
    Mealdicator.set(value='Delicious Meal')
    Drinkdicator.set(value='Fresh Drink')
    indicator.set(value='Choose a Country')
    txtQtyofMeal.delete(0,END)
    txtQtyofMeal.insert(0,0)
    txtQtyofDrink.delete(0,END)
    txtQtyofDrink.insert(0,0)
    txtAmount.delete(0,END)
    txtAmount.insert(0,0)
    RoomCost.set(0.0)
    Total.set(0.0)
    ServiceCharge.set(0.0)
    Drinks.set(0.0)
    Cost.set(0.0)
    chkb1.set(0.0)
    v.set(3)
    DevCost.set(0.0)
    
#============================= CLEAR BUTTON =============================
def ClearScreen():
    Display.delete(0,END)
    RoomCost.set('')
    Total.set('')
    ServiceCharge.set('')
    Drinks.set('')
    Cost.set('')
    DevCost.set('')
    
#============================= EXIT BUTTON ===================================
def Stop():
    root.destroy()

def Exit():
    Display.delete(0,END)
    Display.insert(0,'Thanks for Patronage.... ')
    Display.after(3000,Stop)

#============================= TIME ========================================
def tick():
    d = datetime.datetime.now()
    Today = '{:%B %d, %Y}'.format(d)

    mytime = time.strftime('%I:%M:%S%p')
    lblinfo.config(text=(mytime+' '+Today))
    lblinfo.after(200,tick)

#========================== SCROLL FUNCTION ==============================
def display():
    global text1,n,msg1
    for t in range(len(msg1)):
        for k in range(t):
            text1 +=' '
        for g in range(len(msg1) - t):
            text1 += msg1[g]
        text1 = text1.strip()
        f2.update()
        f2.after(200)
        text1 = text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1 = ''
    scroll_text.set('')
    txtscroll.after(200,display)
    
    

root=Tk()
root.geometry("1366x768")
root.title("HOTEL MANAGEMENT SYSTEM")


#=============================== WINDOW'S PARTITION ==========================================
Tops=Frame(root,width=1600,height=100,bg="blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=800,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3=Frame(root,width=35,height=700,relief=SUNKEN)
f3.pack(side=LEFT)

f4=Frame(root,width=100,height=700,relief=SUNKEN)
f4.pack(side=RIGHT)

#==================================== MAIN SCREEN ===========================================
txt_input=StringVar(value='Work in Progress....')
Display=Entry(Tops,font=("arial",70,"bold"),fg="black",bd=25,bg="light blue",justify="right",textvariable=txt_input)
Display.grid(columnspan=4)

#================================ DATE & TIME ===============================================

lblinfo=Label(f2,font=('arial',20,'bold'),text=localtime,fg='black',bd=5,anchor=W)
lblinfo.grid(row=1,column=0,columnspan=4)
tick()

#================================== ROW 1 ======================================================
operator=''

btn7=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='7',command=lambda:btn(7)).grid(row=2,column=0)
btn8=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='8',command=lambda:btn(8)).grid(row=2,column=1)
btn9=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='9',command=lambda:btn(9)).grid(row=2,column=2)
btnC=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='C',bg='light yellow',command=clear).grid(row=2,column=3)


#================================== ROW 2 ======================================================

btn4=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='4',command=lambda:btn(4)).grid(row=3,column=0)
btn5=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='5',command=lambda:btn(5)).grid(row=3,column=1)
btn6=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='6',command=lambda:btn(6)).grid(row=3,column=2)
btnplus=Button(f2,padx=18,pady=5,bd=8,font=('arial',20,'bold'),text='+',bg='light blue',command=lambda:btn('+')).grid(row=3,column=3)

#================================== ROW 3 ======================================================

btn1=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='1',command=lambda:btn(1)).grid(row=4,column=0)
btn2=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='2',command=lambda:btn(2)).grid(row=4,column=1)
btn3=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='3',command=lambda:btn(3)).grid(row=4,column=2)
btnminus=Button(f2,padx=23,pady=5,bd=8,font=('arial',20,'bold'),text='-',bg='light blue',command=lambda:btn('-')).grid(row=4,column=3)

#================================== ROW 4 ======================================================

btn0=Button(f2,padx=15,pady=5,bd=8,font=('arial',20,'bold'),text='0',command=lambda:btn(0)).grid(row=5,column=0)
btndot=Button(f2,padx=21,pady=5,bd=8,font=('arial',20,'bold'),text='.',bg='light blue',command=lambda:btn('.')).grid(row=5,column=1)
btndivision=Button(f2,padx=20,pady=5,bd=8,font=('arial',20,'bold'),text='/',bg='light blue',command=lambda:btn('/')).grid(row=5,column=2)
btnmultiply=Button(f2,padx=19,pady=5,bd=8,font=('arial',20,'bold'),text='x',bg='light blue',command=lambda:btn('*')).grid(row=5,column=3)

#================================== ROW 5 ======================================================

btnequals=Button(f2,padx=64,pady=2,bd=8,font=('arial',20,'bold'),text='=',bg='light yellow',command=equal).grid(row=6,column=0,columnspan=2)
btnopenbracket=Button(f2,padx=19,pady=2,bd=8,font=('arial',20,'bold'),text='(',bg='light blue',command=lambda:btn('(')).grid(row=6,column=2)
btnclosebracket=Button(f2,padx=23,pady=2,bd=8,font=('arial',20,'bold'),text=')',bg='light blue',command=lambda:btn(')')).grid(row=6,column=3)

#=================================== CHOOSE MEAL =============================================
Meal1=IntVar()
Mealdicator=StringVar(value="Delicious Meals")

lblMeal=Label(f1,font=('arial',16,'bold'),text='Choose Meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Mealdicator)
txtMeal['values']=('Fried Rice','Fried Rice & Chicken','Manchurian','Cheese','Burger')
txtMeal.grid(row=0,column=1)


lblQtofMeal=Label(f1,font=('arial',16,'bold'),text='Qty. of Meal',bd=10,anchor=W)
lblQtofMeal.grid(row=1,column=0)
txtQtyofMeal=Entry(f1,font=('arial',16,'bold'),textvariable=Meal1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtyofMeal.grid(row=1,column=1)

#========================================= CHOOSE DRINK =========================================
Drink1=IntVar()
Drinkdicator=StringVar(value="Fresh Drinks")

lblDrink=Label(f1,font=('arial',16,'bold'),text='Choose Drink',bd=10,anchor=W)
lblDrink.grid(row=2,column=0)
txtDrink=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=Drinkdicator)
txtDrink['values']=('Coka Cola','Appy Fizz','Pepsi','Red Wine','Bottled Water')
txtDrink.grid(row=2,column=1)


lblQtofDrink=Label(f1,font=('arial',16,'bold'),text='Qty. of Drink',bd=10,anchor=W)
lblQtofDrink.grid(row=3,column=0)
txtQtyofDrink=Entry(f1,font=('arial',16,'bold'),textvariable=Drink1,bd=10,insertwidth=4,bg='white',justify='right')
txtQtyofDrink.grid(row=3,column=1)

#================================== ORDER DELIVERY ===============================================
chkb1 =IntVar()

lblHomeDev=Label(f1,font=('arial',16,'bold'),text='Order Delivery',bd=10,anchor=W)
lblHomeDev.grid(row=4,column=0)
check1=Checkbutton(f1,text='YES',variable=chkb1,font=('arial',16,'bold'))
check1.grid(row=4,column=1)

#==================================== BOOK A ROOM ===================================================
v=IntVar()
v.set(3)

lblRoom=Label(f1,font=('arial',16,'bold'),text='Book a Room',bd=10,anchor=W)
lblRoom.grid(row=5,column=0)
MyRadios=Radiobutton(f1,text='VIP',font=('arial',16,'bold'),variable=v,value=1)
MyRadios.grid(row=5,column=1,sticky=W)
MyRadios=Radiobutton(f1,text='Normal',font=('arial',16,'bold'),variable=v,value=2)
MyRadios.grid(row=5,column=1)
MyRadios=Radiobutton(f1,text='No',font=('arial',16,'bold'),variable=v,value=3)
MyRadios.grid(row=5,column=1,sticky=E)

#====================================== COST DISPLAY SCREEN ==========================================
Cost=StringVar()
lblMeal1=Label(f1,font=('arial',16,'bold'),text='Cost of Meal($)',bd=16,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,fg='black',bd=10,insertwidth=4,bg='light blue',justify='right')
txtMeal1.grid(row=0,column=3)

Drinks=StringVar()
lblDrink1=Label(f1,font=('arial',16,'bold'),text='Cost of Drink($)',bd=16,anchor=W)
lblDrink1.grid(row=1,column=2)
txtDrink1=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,fg='black',bd=10,insertwidth=4,bg='light blue',justify='right')
txtDrink1.grid(row=1,column=3)

DevCost=StringVar()
lblDev=Label(f1,font=('arial',16,'bold'),text='Delivery Cost($)',bd=16,anchor=W)
lblDev.grid(row=2,column=2)
txtDev=Entry(f1,font=('arial',16,'bold'),textvariable=DevCost,fg='black',bd=10,insertwidth=4,bg='light blue',justify='right')
txtDev.grid(row=2,column=3)

RoomCost=StringVar()
lblRoom=Label(f1,font=('arial',16,'bold'),text='Cost of Room($)',bd=16,anchor=W)
lblRoom.grid(row=3,column=2)
txtRoom=Entry(f1,font=('arial',16,'bold'),textvariable=RoomCost,fg='black',bd=10,insertwidth=4,bg='light blue',justify='right')
txtRoom.grid(row=3,column=3)

ServiceCharge=StringVar()
lblService=Label(f1,font=('arial',16,'bold'),text='Service Fee($)',bd=16,anchor=W)
lblService.grid(row=4,column=2)
txtService=Entry(f1,font=('arial',16,'bold'),textvariable=ServiceCharge,fg='black',bd=10,insertwidth=4,bg='light blue',justify='right')
txtService.grid(row=4,column=3)

Total=StringVar()
lblTotal=Label(f1,font=('arial',16,'bold'),text='Total Cost($)',bd=16,anchor=W)
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,fg='black',bd=10,insertwidth=4,bg='light blue',justify='right')
txtTotal.grid(row=5,column=3)

#=============================== CURRENCY CONVERTER ============================================
var1=IntVar()
indicator=StringVar(value='Choose a Country')

lblCuncon=Label(f1,font=('arial',16,'bold italic'),text='------------------ currency converter ----------------------',bd=20,anchor=W)
lblCuncon.grid(row=6,column=0,columnspan=4)

lblCountry=Label(f1,font=('arial',16,'bold'),text='Nationality',bd=20,anchor=W)
lblCountry.grid(row=7,column=0)
txtCountry=ttk.Combobox(f1,font=('arial',16,'bold'),textvariable=indicator)
txtCountry['value']=('India','France','Ghana','Mexico','Nigeria','USA')
txtCountry.grid(row=7,column=1)

lblAmount=Label(f1,font=('arial',16,'bold'),text='Amount($)',bd=20,anchor=W)
lblAmount.grid(row=7,column=2)
txtAmount=Entry(f1,font=('arial',16,'bold'),textvariable=var1,bd=10,insertwidth=4,bg='light blue',justify='right')
txtAmount.grid(row=7,column=3)

#=================================== CONTROL BUTTONS =============================================
btnConvert=Button(f1,padx=2,pady=2,bd=10,fg='white',font=('arial',16,'bold'),width=10,text='Convert',bg='black',
                  command=Convert)
btnConvert.grid(row=8,column=2)

btnTotal=Button(f4,padx=10,pady=1,bd=10,fg='white',font=('arial',16,'bold'),width=2,text='Total',bg='black',
                command=total_result)
btnTotal.grid(row=0,column=0)

btnScreen=Button(f4,padx=10,pady=2,bd=10,fg='white',font=('arial',16,'bold'),width=2,text='Clear',bg='black',command=ClearScreen)
btnScreen.grid(row=1,column=0)

btnReset=Button(f4,padx=10,pady=2,bd=10,fg='white',font=('arial',16,'bold'),width=2,text='Reset',bg='black',
               command=Reset)
btnReset.grid(row=2,column=0)

btnExit=Button(f4,padx=10,pady=2,bd=10,fg='white',font=('arial',16,'bold'),width=2,text='Exit',bg='red',
              command=Exit)
btnExit.grid(row=3,column=0)

#====================================== LOGO ===================================================
#photo=PhotoImage(file=r'D:\logo.jpg')
#myphoto=Label(f1,image=photo)
#myphoto.grid(row=8,column=0)

#===================================== SCROLLABLE TEXT============================================
scroll_text=StringVar()
txtscroll=Entry(f2,textvariable=scroll_text,font=('arial',16,'bold italic'),fg='white',bd=10,bg='black',width=27)
txtscroll.grid(row=0,column=0,columnspan=4)
display()

root.mainloop()
