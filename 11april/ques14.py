c,s=map(int,input("Enter cost and selling price").split())
if s>c:
    p=s-c
    per=p/c*100
    print("Profit= ",p,"Profit %= ",per,"%")
else :
    l=c-s
    per=l/c*100
    print("loss= ",l,"loss %= ",per,"%")
