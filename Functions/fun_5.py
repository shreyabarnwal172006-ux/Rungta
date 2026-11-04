#write a function to count and print the longest word in a given string.
s = input()
clean_s = s.strip()
split_s = s.split()
def f(s):
    max = 0
    mylist = list(split_s)
    for i in mylist:
        if len(s[i])>max:
            max = len(s[i])
    return(max)
print(f(clean_s))