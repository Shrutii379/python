#SETS

# empty set{} , set() -> empty set
#denoted by {}
#values in sets cannot be duplicate
#indexing is not allowed
#unordered or subscriptable because it has no index and keys
#heterogeneous data type except boolean
#mutable
#item assignment is done using a method


# s=set( ) -> empty set
# print(type(s))

# s={1,2,3,4,5}
# print(type(s))


# s={1,1,1,2,2,3,4,5,5}  #values in sets cannot be duplicate
# print(s)

# s={'hello',1,3.14,True}
# print(s)  #boolean values are not alllowed


#Methods in sets.
#1. Item Adding
# s={1,1,1,2,2,3,3,4,4,5,5}
# s.add(100)
# s.update([200,45,32,67])  #adding multiple values inside set
# print(s)

#2. Removing an element from the set 
# s={1,1,1,2,2,3,3,4,4,5,5}
# # .remove(element)
# #s.remove(1)#removes all occurence of 1
# #s.discard(6) # agar value exist nahi krti then it will return you exact set without any error
# s.clear()  #removes all values of set 
# print(s)



#Advanced methods in sets
# 1. Union ->  gives all the elements of ur sets
# 2. Intersection -> gives common elements between both sets

# s1={1,2,3,4,5}
# s2={1,6,7,8}
# #print(s1.union(s2))  #union of s1 and s2
# #print(s1.intersection(s2))  #intersection of s1 and s2
# #print(s1.difference(s2))  -> Difference -> s1 me present but not in s2ce
# #print(s2.difference(s1))   #-> Difference -> s2 me present but not in s1
# print(f'Symmetric difference b/w set1 and set2{s1.symmetric_difference(s2)}')


#3.  Symmetric Difference -> common elements ko chor k jo bach rhe vo sab la do


l=[1,2,1,2,1,3,3,3,4,5,6,7]
s=set()
for i in l:
 s.add(i)
print(s)



