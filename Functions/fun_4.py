#write a function to remove duplicate characters from a given string
#write a function to convert given string which only contains unique elements
#empty string
#char access(loop)
#check to verify presence of character in string
s = input()
clean_s = s.strip()
def f(s):
    temp =""
    for i in s:
       if i not in temp:
         temp+=i
    return(temp)
print(f(clean_s))