s1 = " hello world "
s2 = s1.strip()#string is immutable so store it in another var first to change
print(s2)

s3 = s1.lstrip()#to remove spaces from right handside
print(f"lstrip :{s3}")

s4 = s1.rstrip()#to remove spaces from left handside
print(f"rstrip :{s4}")

s5 = "This is my laptop  "
s7 = "Apple,Mango,Banana"
s8 = s7.split(",",2)
print(s8)
s6 = s5.split()
print(s6)