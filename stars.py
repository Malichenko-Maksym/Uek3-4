while True:
    try:
       x=int(input("Enter number of stars in the longest line: "))
    except:
        print("Not float, try again")
    else:
        break
for i in range(1,x+1):
    print("*"*i)
for i in reversed(range(1,x)):
    print("*"*i)
input()
