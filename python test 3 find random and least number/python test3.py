from random import randint
while(1):
    mystr = input()
    data = mystr.split()
    maximum = -1
    mValue = 0
    n = int(data[0])
    m = int(data[1])


    for a in range(1, m+1):
        ans = (randint(1,100))
        print(ans, end=" ")
        if (ans <=n):
            if ((n-ans)>maximum):
                maximum = n-ans
                mValue = ans
    if (maximum == -1):
        print()
        print("None")
    else:
        print()
        print(mValue)
    

        

