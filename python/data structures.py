"" "" " "
# Data structures(advanced data types)

# 1. list
# 2.dictionary
# 3.tuples
# 4.set


#1. List
#"denoted by-> [] Square brackets"



# l=[10,20,30,40,50]
# #l=[] #empty list
# print(l)
# print(type(l))


#1. it can store  data of multiple data types-heterogeneous data structure
#2. duplicacy of data is allowed
#3. list is ordered
#4. Mutable-> we can change the value of the item of the list.
""""""

# l=[10,20,30,40,50]
# print(l[3])
# l[3]=400  #item assignment

#l[5]=100
#print (l) #index out of range
# l=[10,20,30,40,50]

#item wise loop.
# for i in l:
#     print(l)


#index wise loop.
# for i in range(len(l)):
#                print(i,l[i])
#i -> index of list
#l[i] -> item at index


# l=[1,67,10,25,14,77]
# for i in l:
#          if i>15:
#           print(i)





# sum all the elements of the list

# l=[10,20,30,40,50]
# sum=0
# for i in l:
#         sum+=i
# print(sum)



# Slicing
# [start=0:stop-1:step=1]
# l=[10,20,30,40,50]
# print[1:4:1]



#Methods in List
# print()
# input()
# .append()  #method

#1.  .append() -> adds single element at the last of the list
# l=[10,20,30,40,50]
# l.append(100)
# print(l)



#2.  .extend() -> adds multiple elements at the last of the list 
# l1=[10,20,30,40,50]
# l2=[60,70,80]
# l1.extend(l2)
#print(l1)



#3. .insert(index,value) -> insert element at particular index value
# l1=[10,20,30,40,50]


# l1.insert(1,100)
# print(l1)




#4.  .pop(index) ->removes specific element from the list
# l1=[10,20,30,40,50]
# l1.pop(1)
# print(l1)


#5.   .remove(element)
# l1=[1,2,3,4,5,5,5,8]
# l1.remove(5)  #agar duplicate value hai toh first occurence remove hoga
# print(l1) 



#6.  len() -> calculates the length of the list
# l1=[1,2,3,4,5,5,5,8]
# print(len(l1))



#que.  Accept List elements and reprint it
#part1 Accept elements
# n=int(input("enter the size of the list:"))
# l=[]
# for i in range(n):  #0,1,2,3,4
#       element=int(input("enter the elements:"))
#       l.append(element)
# print(l)



# n=int(input("enter the size of the list:"))
# l=[]
# for i in range(n):  #0,1,2,3,4
#       element=input(f'enter the elements{i} for your list')
#       l.append(element)
# print(l)


#que.   reverse a list without using slicing
# l=[1,2,3,4,5]
# l.reverse()
# print(l)


# l=[1,2,3,4,5]
# rev=[]
# for i in range (len(l)-1,-1,-1):
#     rev.append(l[i])
# print(rev)



#que.  Reverse a list using slicing
# l1=[1,2,3,4,5]   
# l2=l1[::-1]
# print(l2)



#que.  find second largest number in a given list
# l=[45,65,78,34,56]
# largest = second = l[0]
# for i in l:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second=i
# print("Second largest number is:",second)


#que. print positive and negative elements of a list
# l=[10,-9,30,20,-12,-8]
# neg=[]
# pos=[]
# for i in l:
#     if i<0:
#         neg.append(i)
#     else:
#         pos.append(i)
# print(neg)
# print(pos)



#BUBBLE SORT
# l=[1,5,3,7,4,10]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#       if l[i]>l[j]:
#          l[i],l[j]=l[j],l[i]
# print(l)





# def hello():
#    print("HEllo World")
# hello()
# hello()
# hello()
# hello()
# hello()


  
# for i in range(6):
#      print("HEllo World"*5)

#que. Largest element from a list
# l=[2,96,69,77,145,20]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)


# l=[2,96,69,77,145,20]
# l.sort()
# print(max(l))



# l=[2,96,69,77,145,20]
# max=l[0]
# index=0
# for i in range (len(l)):
#     if l[i]>max:
#         max=l[i]
#         index=i
# print(f'max element from the list is {max} and at index{index}')


#que. mean of the list
# l=[20,30,40,50,60]
# sum=0
# for i in l:
#     sum+=i
# mean=sum / len(l)
# print(mean)




# l=[2,96,69,77,145,20]
# min=l[0]
# index=0
# for i in range (len(l)):
#     if l[i]<min:
#         min=l[i]
#         index=i
# print(f'smallest element from the list is {min} and at index{index}')




#que. check a list is sorted or not
# l=[23,45,67,89,12]
# l.sort()
# if l==l.sort():
#  print("List is sorted")
# else:
#  print("List is not sorted")


#USING FOR LOOP
# l=[23,45,67,89,12]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)




#que. second largest element at index
# l=[10,5,20,15]
# largest=l[0] #20
# s_largest=l[0]#15
# index=0
# sindex=0
# for i in range(len(l)) : #i->2
#     if l[i]>largest:  #15>20
#         s_largest=largest
#         largest=l[i]
#         largest=l[i]

#         sindex=index
#         index=i
#     elif l[i]>s_largest:  #15>10
#         s_largest=l[i]
#         sindex=i
# print(largest,s_largest)
# print(index,sindex)





#que.Check if List is sorted or not.
# l = [78,554,8,14,43,22]
# sorted_list = True
# for i in range(len(l) - 1):
#     if l[i] > l[i + 1]:
#         sorted_list = False
#         break
# if sorted_list:
#     print("List is sorted")
# else:
#     print("List is not sorted")



#enumerate() -> index k sath unki values bhi deta h
# l=[10,20,30,40,50]
# for index,value in enumerate(l): # enumerate k liye 2 variables ki need hogi
#     print(index,value)


# l=[10,20,30,40,50]
# for index,value in enumerate(l): 
#     print(index+1,value)  #for printing position of element along wiwth thte element



#common elements from lists
# l=[1,2,3,4,5]
# l2=[1,3,4,5,6]
# new=[]
# for i in l:
#     for j in l2:
#      if i==j:
#         new.append(i)
# print(new)


# l1=[1,2,3,4,5]
# l2=[1,3,4,5,6]
# common=[]
# for i in l1:
#    if i in l2:
#       common.append(i)
# print(common)


#Pallindrome or not
#Method -1
# l=[1,2,2,9]
# for i in range(len(l)):
#     if l[i]!=l[len(l)-1-i]:
#         print('Not pallindrome')
#         break
#     else:
#         print('list is pallindrome')



#Method -2 
# l=[1,2,2,1]
# rev=[]
# for i in range(len(l)-1,-1,-1):
#     rev.append(l[i])
# if l==rev:
#        print('list is pallindrome')
# else:
#        print('list is not pallindrome')



#que. you have a list [1,2,3,4,5] and you have a variable k=2 and you just have to rotate the list by k elements
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     last=l[-1] #storing last value of the list
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=last
# print(l)


#you have a list[1,1,1,2,2,2,3,3,4,4,5,5,6] frquency count
l=[1,1,1,2,2,2,3,3,4,4,5,5,6]
d={}
for i in d:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    print(d)

















  












