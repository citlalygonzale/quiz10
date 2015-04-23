def dotproduct(p,q):
 a = 0
 n = 0
 for item in p:
  a = a+(p[n]*q[n])
  n += 1
 return a

l1 = [2,4,5,6]
l2 = [1,2,3,4]

print(l1)
print(l2)
r = dotproduct(l1,l2)
print ("The dot product is:",r)
