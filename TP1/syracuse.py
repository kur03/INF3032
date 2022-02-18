nbr = int(input("Enter a number : "))

count = 0

while (nbr != 1) :
    if (nbr % 2 == 0) :
        nbr = int(nbr/2)
        count += 1

    else :
        nbr = int(nbr*3+1)
        count += 1
        
    print(nbr, " ")
print("There were ", count, " iteration until we reached 1.")
