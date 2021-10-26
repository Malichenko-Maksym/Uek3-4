a=[0]*53
a[1]=1
for i in range(2,53):
    print(a[i-2]," ",end='')
    a[i]=a[i-1]+a[i-2]
   