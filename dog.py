while True:
    try:
       age=float(input("Enter the dog's age in human years: "))
    except:
        print("Not float, try again")
    else:
        break
if age<=2:
    age1=age*10.5
else:
    age1=10.5*2+(age-2)*4
print(f"The dog's age in dog’s years is {age1} years.")
input()