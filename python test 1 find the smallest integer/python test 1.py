file = open("input.txt", "r")	#open file
minimum = 9999999
for counter in file:  #read data
    num = int(counter)
    if (num < minimum):
        minimum = num
file.close()

f1 = open("output.txt", "w")
print(minimum, file = f1)
f1.close()

