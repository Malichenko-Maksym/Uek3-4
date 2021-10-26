while True:
    try:
       a=float(input("Enter first number: "))
    except:
        print("Not float, try again")
    else:
        break
while True:
    try:
       b=float(input("Enter second number: "))
    except:
        print("Not float")
    else:
        break
if a>b:
    print(f"Numbers in ascending order: {b}  ,  {a}")
elif a==b:
    print(f"Numbers are equal: {a}")
else:
    print(f"Numbers in ascending order: {a}  ,  {b}")
input()

