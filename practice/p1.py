attempts=0
while attempts<3:
     password=input("enter the password")
     if password=="admin":
         print("granted")
         break
     attemts+=1   
     
else:
    print("too many failed,attempts")
