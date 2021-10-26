i=0
while i<3:
    while True:
        try:
            b=input("Enter the pin-code: ")
            while len(b)!=4:
                b=input("pin-code consists of 4 digits: ")
            a=int(b)
        except:
            print("Not int, try again")
        else:
            break
    if a==805:
        print("Success!")
        i=5       
    else:
        print("Incorect...")
        i+=1
if i<5:
    print("Sorry, your payment card has been blocked.")
input()
    
        
        