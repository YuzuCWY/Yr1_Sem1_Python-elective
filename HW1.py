M1 = 1
M2 = 1
for M1 in range (1,10):
    if(M1%2 == 1):
        for M2 in range (1, 10):
            print(M1, "X", M2, "=", M1*M2)

for M1 in range (1, 10):
    if(M1%2 == 0):
        for M2 in range (1, 10):
            if (M2%2==1):
                print(M1, "X", M2, "=", M1*M2)
for M1 in range (1, 10):
    if (M1%2 == 0):
        for M2 in range (1,10):
            if (M2%2 == 0):
                print(M1, "X", M2, "=", M1*M2)
