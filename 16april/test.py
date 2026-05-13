#1
dis=int(input("Enter distance in km"))
t=int(input("Enter time in hours"))
s=dis//t
print(f"distance={dis}\ntime={t}\nSpeed={s}")

#2
dw,days=map(int,input("Enter daily wage and number of days").split())
sal=dw*days
print(f"Daily wage={dw}\ndays={days}\nSalary={sal}")

#3
un=int(input("Enter units"))
billl=6*un
print(billl)

#4
l,b=map(int,input("Enter length and breadth").split())
ar=l*b
print(f"length={l}\nbreadth={b}\nArea={ar}")

#5
a1,b2,c3=map(int,input("Enter marks of 3 subjects").split())
fi=(a1+b2+c3)/3
print(f"Marks1 is={a1}\nMarks2 is ={b2}\nMarks3={c3}\nAverage={fi}")

#6
am=int(input("Enter total amount"))
disc=am/10
fin=am-disc
print(f"discount={disc}\nfinal={fin}")

#7
rad=int(input("Enter radius"))
c=3.14*rad*rad
print("Area of circle is ")
      
#1
b=int(input("Enter total bill amount"))
nof=4
gst=(b*5)/100
serc=b/10
tb=b+gst+serc
pp=tb/nof
print(f"final bill = {tb}\nEach person pays= {pp}")

#2
mp=int(input("Enter mobile price"))
dp=5000
ra=mp-dp
i=ra/10
twi=ra+i
emi=twi/10

print(f"Remaining amount= {ra}\nTotal with interest= {twi}\nMonthly Emi= {emi}")

#3
m1,m2,m3,m4,m5=map(int,input("Enter marks of five subject").split())
to=m1+m2+m3+m4+m5
av=to/5
per=(to/500)*100
print(f"Total= {to}\nAverage= {av}\nPercentage= {per}")

#4
hrs,mins=map(int,input("Enter Speed then Enter Time in hours then Enter time in minutes").split())
fmins=mins/60
ftime=hrs+fmins
dis=sp*ftime
print(f"Total time= {ftime} hrs\nDistance= {dis}")

#5
msalary,wdays,whrs=map(int,input("Enter salary, working days and working hours").split())#1
b=int(input("Enter total bill amount"))
nof=4
gst=(b*5)/100
serc=b/10
tb=b+gst+serc
pp=tb/nof
print(f"final bill = {tb}\nEach person pays= {pp}")

#2
mp=int(input("Enter mobile price"))
dp=5000
ra=mp-dp
i=ra/10
twi=ra+i
emi=twi/10

print(f"Remaining amount= {ra}\nTotal with interest= {twi}\nMonthly Emi= {emi}")

#3
m1,m2,m3,m4,m5=map(int,input("Enter marks of five subject").split())
to=m1+m2+m3+m4+m5
av=to/5
per=(to/500)*100
print(f"Total= {to}\nAverage= {av}\nPercentage= {per}")

#4
hrs,mins=map(int,input("Enter Speed then Enter Time in hours then Enter time in minutes").split())
fmins=mins/60
ftime=hrs+fmins
dis=sp*ftime
print(f"Total time= {ftime} hrs\nDistance= {dis}")

#5
msalary,wdays,whrs=map(int,input("Enter salary, working days and working hours"…
[10:52 pm, 16/04/2026] saransh patil infobean: Aaj ka homework
[9:24 am, 17/04/2026] Vishal Patil: Ok
[9:37 am, 17/04/2026] Vishal Patil: Kaha bheja home work
[12:01 pm, 17/04/2026] Vishal Patil: #1
b=int(input("Enter total bill amount"))
nof=4
gst=(b*5)/100
serc=b/10
tb=b+gst+serc
pp=tb/nof
print(f"final bill = {tb}\nEach person pays= {pp}")

#2
mp=int(input("Enter mobile price"))
dp=5000
ra=mp-dp
i=ra/10
twi=ra+i
emi=twi/10

print(f"Remaining amount= {ra}\nTotal with interest= {twi}\nMonthly Emi= {emi}")

#3
m1,m2,m3,m4,m5=map(int,input("Enter marks of five subject").split())
to=m1+m2+m3+m4+m5
av=to/5
per=(to/500)*100
print(f"Total= {to}\nAverage= {av}\nPercentage= {per}")

#4
hrs,mins=map(int,input("Enter Speed then Enter Time in hours then Enter time in minutes").split())
fmins=mins/60
ftime=hrs+fmins
dis=sp*ftime
print(f"Total time= {ftime} hrs\nDistance= {dis}")

#5
msalary,wdays,whrs=map(int,input("Enter salary, working days and working hours"
Ye shayad pehle ka hai
[6:39 pm, 17/04/2026] Vishal Patil: Saransh Kal wala home work send karna
[6:40 pm, 17/04/2026] saransh patil infobean: Baad me bhejunga abhi dawai Li he
[6:44 pm, 17/04/2026] Vishal Patil: Ok bro
[10:34 pm, 17/04/2026] saransh patil infobean: #1
age=int(input("Enter age"))
idproof=str(input("Enter id proof is available or not "))
if age>=18 and idproof=="available":
          print("Elligible for vote")
else:
    print("not elligible")


#2
marks=int(input("Enter marks"))
if marks>=40:
    if marks>=75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("fail")

#3
cartValue=float(input("Enter cart value"))
if (cartValue>=500):
    if(cartValue>=1000):
        cartValue/=10
        print("Free delivery applied\nDiscount Coupon unlocked\n")
    else:
        print("Free Delivery applied")

#4
age,bmi=map(int,input("Enter age and BMI ").split())
if (age>=18):
    print("Allowed for gym")
if(bmi>25):
    print("Enroll in weight loss program")

#5
username="admin"
pwd="123456789" #length only work on string not number
if(username=="admin"):
    print("valid user")
if(len(pwd)>=8):
    print("strong password")

#6
temp=34
humidity=73
if(temp>=30):
    print("hot day")
if(humidity>=70):
    print("high humidity alert")

#7
sal=64000
if(sal>=30000):
    if(sal>=50000):
        print("Elligble for pf")
    print("bonus applicable")

#8
num=20
if(num%2==0):
    print("Even")
if(num%5==0):
    print("divisible by 5")

#9
mem="yes"
bissue=2
if(mem=="yes"):
    if(bissue<3):
        print("Entery allowed\nCan issue more books")
    else:
        print("Entry allowed")

#10
marks,attendance=60,80
if(marks>=40):
    if(attendance>=75):
        print("Pass and elligible for certificate")
    else:
        print("pass")