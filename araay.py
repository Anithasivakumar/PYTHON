a,b=map(int,input().split())
n=list(map(int,input().split()))[0:a]
for i in n:
    if(b==i):
        print("yes")
        break
    else:
        continue
