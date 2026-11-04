#write common_elements(a,b,c) return the sorted list of element present in all three sets
# sample test
#a=21,2,3,44  b=22,3,54  c=23,2,9  common_elements(a,b,c) output(2,3)
a={21,2,3,44}
b={22,3,54}
c={23,2,9}
def common_elements(a,b,c):
    return sorted(list(a & b & c))