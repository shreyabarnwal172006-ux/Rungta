
n=int(input("Enter a number="))
for i in range(1,n+1):
    print(i)


#sum of n natural numbers
s=0
for i in range(1,n+1):
    s=s+i
print(f"Sum of Natural numbers={s}")


#fibonacci series
n=int(input("Enter the Range="))
a=0
b=1
print(a)
print(b)
for i in range(0,n+1):
    s=a+b
    print(s)
    a=b
    b=s

#factorial
n=int(input("Enter the Number="))   
f=1
for i in range(1,n+1 ):
    f=f*i
print(f"Factorial={f}")


#reverse
n=int(input("Enter the range="))
for i in range(n,0,-1):
    print(i)

