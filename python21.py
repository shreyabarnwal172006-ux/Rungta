str=input("Enter a string=")
s=0
for i in str:
    if(i.count("1")!="1"):
        s+=1
        print(s)