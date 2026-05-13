#1
sal,cs,nol=map(int,input("Enter salary,credit score and nuumber of existing loans").split())
if(sal>=30000):
    if(cs>=750):
        print("Loan is approved")
    else:
        if(nol<2):
            print("Loan is approved")
        else:
            print("Rejected")
else:
    print("Loan is rejected")

#2
cv=int(input("Enter card value"))
ut=input("Enter premium or regular")
if(cv>=5000):
    if(ut=='premium'):
        d=(cv*20)/100
        a=cv-d
        print("final amount ",a)
    else:
        d=cv/10
        a=cv-d
        print("final amount ",a)
else:
    if(cv>=2000):
        d=(cv*5)/100
        a=cv-d
        print("final amount ",a)
    else:
        print("no discount applied")

#3
nou=int(input("Enter number of units "))
if(nou>=100):
        if(nou>=300):
            print("high usage")
        else:
            if(nou>=200):
                print("moderate usage ")
            else:
                print("normal usage")
else:
    print("Low usage")


#4
age,w=map(int,input("Enter age and weight").split())
goal=input("Enter goal ")
if(age>=18):
    if(goal=='weight loss'):
        print("cardio plan")
    else:
        print("strength plan")
    if(w<80):
        print("general fitness plan")
else:
    print("not allowed")

#5
ab=int(input("Enter balance"))
wa=int(input("Enter withdrawl amount "))
pin=input("enter pin status correct or incorrect ")
if(ab>=wa):
    if(wa<=10000):
        if(pin=='correct'):
            print("transaction successful")
        else:
            print("invalid pin")
    else:
        print("limit exceeded")
else:
    print("insufficient balance")

#6
age=int(input("enter age"))
st,dt=map(str,input("Enter show time and day type").split())
if(age<18):
    if(st=='morning'):
        print("ticket price is 100 ")
    else:
        print("ticket price is 50")
elif(age>=18):
    if(st=='evening'):
        if(dt=='weekend'):
            print("ticket price is 300")
        else:
            print("250")
    else:
        print("ticket price is 200")
        
#7
ex=6
r=4
sal=40000
if(ex>=5):
    if r>=4:
        if sal<50000:
            b=(sal*20)/100
            print("bonus is ",b)
        else:
            b=(sal*10)/100
            print("bonus is ",b)
    else:
        b=(sal*5)/100
        print("bonus is ",b)
print("no bonus is given")

#8
u1,u2,u3,u4,u5,u6=map(int,input("enter 6 stocks value ").split())
if(u1>u2):
    if(u1>u3):
        if u1>u4:
            if u1>u5:
                if(u1>u6):
                    print("highest stock = ",u1)
                else:
                    print("highest stock = ",u6)
            elif u5>u6:
                print("highest stock = ",u5)
            else:
                print("highest stock = ",u6)
        elif u4>u5 and u4>u6:
            print("highest stock = ",u4)
        elif u5>u6:
            print("highest stock = ",u5)
        else:
            print("highest stock = ",u6)
    elif u3>u4 and u3>u5 and u3>u6:
        print("highest stock = ",u3)
    elif u4>u5 and u4>u6:
        print("highest stock = ",u4)
    elif u5>u6:
        print("highest stock = ",u5)
    else:
        print("highest stock = ",u6)
else:
    if u2>u3 and u2>u4 and u2>u5 and u2>u6:
        print("highest stock = ",u2)
    elif u3>u4 and u4>u5 and u5>u6:
        print("highest stock = ",u3)
    elif u4>u5 and u4>u6:
        print("highest stock = ",u4)
    elif u5>u6:
        print("highest stock = ",u5)
    else:
        print("highest stock = ",u6)