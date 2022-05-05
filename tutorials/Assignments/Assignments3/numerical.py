#!/usr/bin/env python3

import random

ap=['+','-','*','/']
num_lst=input().split()
result=input()

i=1 
for i in range(10000):
    lst=[]
    for j in range(len(num_lst)):                
        lst.append(str(num_lst[j]))
        if(j != len(num_lst)-1 ):
            sym=random.choice(ap)
            lst.append(sym)
    res=eval("".join(lst)) 
    if(int(res)==int(result)):
        print(lst, result, res) 
        break

print("Program completed") 
