#write a python function to move all the zeroes of the list to the end, keeping the other non-zero elements

l=[0,1,0,3,12]
nonzero =[]
zero = []
list =[]
def move_zeroes(l):
    for i in range(len(l)):
        if l[i] != 0:
            nonzero= l[i]
        zero = len[l]-len[nonzero]
        print([nonzero+zero])
move_zeroes(l)
