s=0
a=1
i=0
while a!=0:
    while True:
        try:
            a=int(input("Enter number: "))
        except:
            print("Not float, try again")
        else:
            break
    s+=a
    i+=1
print(f"RESULT: Quantity={i-1}, Sum={s}, Mean={s/(i-1)}")
input()