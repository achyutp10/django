n = int(input ("Enter the number you want to print: "))     
a = int(input('Enter 1st no: '))    
b = int(input('Enter 2nd no: '))

for i in range(0,n):  
    print(a, end = " ")   
    c = a+b   
    a = b  
    b = c 