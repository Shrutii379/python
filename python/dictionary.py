#DICTIONARY
#[] -> LIST (SQUARE BRACKETS)
#{} -> DICTIONARY (CURLY BRACKETS)


#Keys - Values pair
#keys - Index
#keys:values  (: - known as separator)
# keys cannot be duplicate but values can be duplicate
# values can be accesssed by using its keys
#Dictionary is heterogeneous and mutable
#ordered
#index can be created in dictionary
#in dictionary loops goes reverse for index we use i and for element we use range



# d = {'a':10 ,'b':20,'c':30,'d':40}
# print(d['b'])



#Creating a new key and assigning value to it
# d = {'a':10 ,'b':20,'c':30,'d':40}
# d['e']=100
# print(d)

# d={'a':10,'b':20,'c':30,'d':40,'e':100}
# d['e']=200  #old value at key 'e' will be overwrite
# print(d)



# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# info['age']=25   #item assignment
# print(info)


#Methods in dictionary
#1.  .values()  -> gives values of the dictionary
# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# print(info.values())


#2.  .keys()  ->  gives keys of the dictionary
# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# print(info.keys())


#3.  .items()  -> gives keys and values of the dictioanry
# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# print(info.items())


#4.  .pop()  -> removes key and value together by accepting the key
# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# info.pop('name')
# print(info)

# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# print(len(info))  # -> jitni keys utni length


# info={'name':'Rahul' ,'age':21 , 'marks':50 ,'present':'true'}
# for i in info:  #i -> keys
#     print(i,info[i])  #info[i] ->values


# for i in info.values():  #you will get only values of dictionary
#        print(i)


# for i in info.keys():   #you will get only keys of dictionary
#     print(i)



#5  .get()  #gives you the value of a key and if not present shows u none
# d={'a':10,'b':20,'c':30}
# print(d.get('d'))  #none is a datatype of python

#6  .update({key:value})
# d={'a':10,'b':20,'c':30}
# d.update({'c':300})
# print(d)


#7  .clear()  #REmoves all the elements of the dictionary
# d={'a':10,'b':20,'c':30}
# d.clear()
# print(d)

# del keyword removes permanently variable from the memory



#que. we have two lists and we have to make list1 as key of a dictionary and list2 as values
# l1=['a','b','c','d']
# l2=[10,20,30,40]
# d={}
# for i in range (len(l2)): #0,1,2,3
#  d[l1[i]]=l2[i]
# print(d) 


#you have a list make the indexes as the keys and elements present on those keys as values
# l=[10,20,30,40]
# d={}
# for i in range(len(l)):
#  d[i]=l[i]
# print(d)

#not in -> (membership operator)

#merge 2 dictionaries
# d1={'a':10,'b':20}
# d2={'c':30,'d':40}
# for i in d2:  #i ->c,d
#  if i not in d1: #c,d not in d1
#   d1[i]=d2[i]
# print(d1)


# d1={'a':10,'b':20}
# d2={'c':30,'d':40}
# d1.update()


#frequency count
l=[1,1,1,1,2,2,3,3,6,6,6,7,6,3,4,4,2]
d={}
for i in l:
 if i not in d:  #1 not in d
  d[i]=1
 else:
  d[i]+=1
print(d)

  
 








