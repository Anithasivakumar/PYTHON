n=int(input())
s=0
t=n
while(t>0):
    r=t%10
    s=s+(r*r*r)
    t=t//10
if(n==s):
        print("yes")
else:
        print("no")
    
