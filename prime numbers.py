while True:
    try:
        n=int(input("Enter N: "))
    except:
        print("Not float, try again")
    else:
        break
print("Prime numbers: ",end='')

for i in range(1,n+1):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2:
        print(i," ",end='')
