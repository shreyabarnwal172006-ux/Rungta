#Pattern
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

#Even number sum
n=int(input("Enter a number="))
s=0
for i in range(0,n+1,2):
    if(i%2==0):
        s=s+i
print("Sum of n even number=",s)
+
#Odd number sum
n=int(input("Enter a number="))
s=0
for i in range(1,n+1):
    if(i%2!=0):
        s=s+i
print("Sum of n odd number=",s)

    
    
    
    
