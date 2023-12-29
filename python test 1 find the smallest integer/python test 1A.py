file = open("input.txt", "r")	#open file
minimum = 9999999
hasdata = 0
for counter in file:  #read data
    num = int(counter)
    hasdata = hasdata + 1
    if (hasdata == 1):
        minimum = num
    else: 
        if (num < minimum):
            minimum = num
print(minimum, end=" ")
file.close()
