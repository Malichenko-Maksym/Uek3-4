while True:
    try:
       x=float(input("Enter x: "))
    except:
        print("Not float, try again")
    else:
        break
while True:
    try:
       y=float(input("Enter y: "))
    except:
        print("Not float")
    else:
        break
if x>0 and y>0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x>0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x<0 and y<0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x<0 and y>0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x!=0 and y==0:
    print(f"Point P({x},{y}) is on the OX axis of the coordinate system")
elif x==0 and y!=0:
    print(f"Point P({x},{y}) is on the OY axis of the coordinate system")
else:
    print(f"Point P located in the position ({x},{y}) of the coordinate system.")
input()