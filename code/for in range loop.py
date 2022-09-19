#For in range loop


for i in range(10): #One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
    print(i) # prints all from 0..9 (10 numbers)
    
print("\n")

#Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
for i in range(12,20): 
    print(i)  #Prints all from 12..19 (8 numbers)


print("\n")

#Three parameters will create a sequence starting with the first parameter
#and stopping before the second parameter, but this time increasing each step by the third parameter
for i in range(4,23,2):
    print(i)  #Prints all from 4,6,....22 as 23 is last limit , 24 won't print
