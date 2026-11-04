# write a function to calcuate the character frequency to return a dictionary which shows the count of each char in given string
#sample test case
#word ==("banana")
#output - {'b':1,'a':3,'n':2}
word = "banana"
def freq_cal(t):
    empt_dict = {}
    for i in word:
        if i in empt_dict:
            empt_dict[i]+=1
        else:
            empt_dict[i]=1
    return empt_dict
print(freq_cal(word))

       