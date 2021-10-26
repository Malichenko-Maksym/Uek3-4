while True:
    try:
       x=int(input("Enter number: "))
    except:
        print("Not float, try again")
    else:
        break
for i in range(1,x+1):
    print(f"{i}"*i)
input()