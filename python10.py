#Even number to n

n=int(input("Enter a number="))
for i in range(1,n+1):
    if(i%2==0):
        print(i)

# n from user and divisible by 3
n=int(input("Enter a number="))
for i in range(1,n+1):
    if(i%3==0):
        print(i)

#count even and odd amoung 10 inputs
c=0
for i in range(1,11):
    n=int(input("Enter number="))
    if(n%2==0):
        c+=1     
print("Even numbers=",c)
print("Odd numbers=",(10-c))


        
        
          
      
        
        
        
