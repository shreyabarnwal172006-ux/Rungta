str = "Recursion is very useful"

reversed =""
str3=""

print("R")
print("l")

str1 = str[2:6]
print(str1)

str2 = str[6:1:-1]
print(str2)


for j in str:
    reversed=j+reversed
print(reversed)


for i in str:
    if i=="e":
        str3 = str3+i.upper()
    str3+=i
print(str3)
