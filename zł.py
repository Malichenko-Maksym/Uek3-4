while True:
    try:
       zl=int(input("Enter the amount in PLN: "))
    except:
        print("Not int, try again")
    else:
        break
z1=zl%5
z5=zl//5
z2=z1//2
z1=z1%2
print(f"The amount of PLN {zl} in coins:")
if z5!=0:
    print(f"5 zł - {z5}")
if z2!=0:
    print(f"2 zł - {z2}")
if z1!=0:
    print(f"1 zł - {z1}")
input()
