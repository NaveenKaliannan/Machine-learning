
a=[1,2,3]
a=["hello",2,"zzzz"]
a=["zhzzzzzello","aads","zazzzzzzzzzz"]
print(a)
print("List * scalar", a*2)
print("List + List concatenate"  , a+[1])
print(" -, /, vector * scalar, vector + scalar operations are not possible for list")
print("max and min works only for same data type ")
print("max", max(a), "min",min(a), "len", len(a))
a.append("halloe")
print(a.sort(), a)


print("  ")
print("  ")

b=(1,2,3)
b=("hello",2,"zzzz")
b=("hello","aads","zzzz")
print(b)
print("tuple * scalar", b*2)
print("tuple + tuple concatentate"  , b + (1,2) )
print(" -, /, tuple * scalar operations are not possible for list")
print("max and min works only for same data type ")
print("max", max(b), "min",min(b), "len", len(b))
print("sorting is not possible, immutable")
print("tuple has no  append")
print(sorted(b), "b.sort() not possible")

print("  ")
print("  ")
c=set(["1",2,"zzzz"])
c=set([1,2,3])
c=set(["hello","aads","zzzz"])
print(c)
print(" no opertations is possible for set -, /, set * scalar multiplications, set * scalar, set + set concatentate replicate operations are not possible for list")
print( "len", len(c))
print( "max", max(c))
print("min", min(c))
print("max and min works only for same data type ")
print("sorting is not possible")
print("set has no  append")
print(sorted(c), "c.sort() not possible")

print(list("12345"),tuple("12345"),set('123344'))
print(" a number cannot be passed list the following list(1), tuple(1), set(1), instead list([1])....")


print("  ")
print("  ")
d={"zhello":[1,2,3],"nave":2}
print(d)
print(" no opertations is possible for set -, /, set * scalar multiplications, set * scalar, set + set concatentate replicate operations are not possible for list")
print(len(d), max(d), min(d), "max and min of key are given")
print("dict has no  append")
dnew=sorted(d)
print(sorted(d), dnew[0][2], "d.sort() not possible, sorted only sorts the key. it has no work for values")

print("you can add new key by simply d['newkey'] = new value, also d['newkey'].append() , .update({'before': 23}), .update(after=10)")
print("get() method takes maximum of two parameters: get(k,v=[])")

print("  ")
print("  ")
di={"hjd":1,"sds":2}
print(di)
di["new"]= di.get("new",[])
di["new"].append(1)
di["new"]= di.get("new",[])
di["new"].append(1)
print(di)
