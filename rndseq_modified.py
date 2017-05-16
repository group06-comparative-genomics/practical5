#! /usr/bin/env python
"prints first argument aa sequences of length second argument to screen"
import random
import sys
number=int(sys.argv[1])#5320
length=int(sys.argv[2])#20
aas="ARNDCEQGHILKMFPSTWYV"
aa_dictionary={}
def r20():
    return random.randrange(20)
id=0
for i in range(number):
    s=""
    for j in range(length):
        s+=aas[r20()]
    aa_dictionary[id]=s
    id+=1
print aa_dictionary
