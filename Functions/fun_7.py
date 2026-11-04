#write a function to print largest and second largest elememt of a list
l = [20,39,48,50,18]
def largest(l):
    lar = l[0]
    for i in range(0,len(l)):
        if l[i]>lar:
            sec = lar
            lar = l[i]
    print(lar)
    print(sec)
print(largest(l))
        