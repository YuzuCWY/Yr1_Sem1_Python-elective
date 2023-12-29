file = open("input.txt", "r")	#open file

for counter in file:  #read data
    num = int(counter)
    if (num % 7 == 0):
        print(num)
        

file.close()
