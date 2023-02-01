n=list(map(int,input("enter nos").split()))
print(n)
x=1
y=0
for i in n:
    x=x*i
    y=y+1
if(x<750):
    print("product",x)
else:
        print("sum",y)
    
    
    
