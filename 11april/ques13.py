p,r,t=map(int,input("Enter principal, rate, time").split())
a=p*((1+(r/100))**t)
ci=a-p
print(a,ci)
