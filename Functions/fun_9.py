#write a function check what elemnts gives the target sum in the given list :
#sample test case :
#target=9
# L = [1,2,3,4,5,8]
L=[1,2,3,4,5,8]
target = 9
def target_sum(L,target):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]+L[j]==target:
             print(L[i],L[j])        
    
target_sum(L, target)