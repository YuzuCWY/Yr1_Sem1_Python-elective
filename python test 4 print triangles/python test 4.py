num = int(input())
while(num>0):
    for a in range(1, num+1): #print (" ")
        for b in range(1, num-a+1):
            print(" ", end = "")
        ##triange part

        if (a==1): #first row
            print("#", end="")
        elif (a==num): # last row
            for b in range(1, 2*a):
                if (b%2 == 0):
                    print(" ", end = "")
                else:
                    print("#", end = "")
            
        else:
            for b in range(1, 2*a):
                if (b == 1 or b == 2*a -1):
                    print("#", end="")
                else:
                    print("*", end = "")
            
        print()
    num = int(input())
        
