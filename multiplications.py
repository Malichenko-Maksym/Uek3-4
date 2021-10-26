while True:
    try:
       x=float(input("Enter number: "))
    except:
        print("Not float, try again")
    else:
        break
for i in range(1,11):
    print(f"{x} x {i} = {x*i}")
input()