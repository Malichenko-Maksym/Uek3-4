while True:
    try:
       a, b=map(int, input("Enter the dimensions of the sides of the rectangle (first-heigth) *use SPACE between values *: ").split())
    except:
        print("Not float, try again")
    else:
        break
for i in range(1,a+1):
    if i==1 or i==a:
            print("*"*b)
    else:
        print("*"+" "*(b-2)+"*")
input()
    
        
        
        



