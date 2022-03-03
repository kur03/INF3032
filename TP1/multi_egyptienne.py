a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))

if (a < b) :
    temp = a
    a = b
    b = temp
    

counter = 1
res = 0
temp_a = a

    
while (b > 0) :
    temp_b = counter + counter
    if (b < temp_b) :
        b = b - counter
        res = temp_a + res
        temp_a = a   
        counter = 1
        
    else : 
        counter = temp_b
        temp_a += temp_a
        
print (res)
    
    

        
    