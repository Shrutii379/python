# BUBBLE SORT
# l=[34,56,12,6,89]
# for i in range(len(l)):
#     for j in range (i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)


#Second largest element in a list
# l=[23,56,67,12,32,89]
# largest=s_largest=l[0]
# index=sindex=0

# for i in range(len(l)):
#     if l[i]>largest:
#         s_largest=largest
#         largest=l[i]
#         sindex=index
#         index=i
#     elif l[i]>s_largest:
#         s_largest=l[i]
#         sindex=i
# print(largest,s_largest)
# print(index,sindex)


#Accept List elements and reprint it
# n=int(input("enter the size of the list"))
# l=[]
# for i in range (n):
#     element=int(input("enter the elements of the list"))
#     l.append(element)
# print(l)


#Pallindrome
# def pallindrome(name):
#       reverse=name[::-1]
#       if name==reverse:
#         print("pallindrome")
#       else:
#          print("not pallindrome")
# name="madam"
# pallindrome(name)



# d={'a':10,'b':20,'c':30,'d':40}
# sum=0
# for i in d:
#     sum+=d[i]
# print(sum)



# def greet():
#     print("good morning shruti!!")
# greet()



# def add(a,b):
#     print(a+b)
# add(10,20)


# def square(n):
#     print(n*n)
# square(5)


# def check(num):
#     if num%2==0:
#         print("num is even")
#     else:
#         print("num is odd")
# check(11)


# def largest():
#     a=10
#     b=89
#     if a>b:
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# largest()



# def vowels(name):
#     count=0
#     for ch in name:
#      if ch in "AEIOUaeiou": 
#       count+=1
#       print(count)
# vowels('shruti')



# def rev(s):
#     reverse=''
#     for i in range (len(s)-1,-1,-1):
#         reverse+=s[i]
#     print(reverse)
# rev('shruti')


# def factorial(n):
#    fact=1
#    for i in range(1,n+1):
#       fact*=i
#    return fact
# print(factorial(9))


# num=int(input("enter the number"))
# print(num)


# print("Name","Is","James",sep="**")


# num=12.4532
# print(f'{num:.2f}')


# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# print(num1+num2)

# a=56
# b=90
# c=a+b
# print(c)



# name=input("enter  your name")
# age=int(input("enter your age"))
# print(f'Hello {name}, You are {age} years old')



# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# print(factorial(5))



# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(9))




# def palindrome(name):
#     rev=name[::-1]
#     if name==rev:
#         print(f'{name} is palindrome')
#     else:
#         print(f'{name} is not a palindrome')
# palindrome('madam')      




# def palindrome(num):
#  copy=num
#  reverse=0
#  while num>0:
#      last=num%10
#      reverse=reverse*10+last
#      num=num//10
#  if copy==reverse:
#         print(f'{copy} is palindrome')
#  else:
#         print(f'{copy} is not palindrome')
# palindrome(123)




#Pattern Printing

# *
# **
# ***
# ****
# *****

# row=int(input("enter no.of rows"))
# for i in range(1,row+1): #if we want to accept no. of rows from user
# # #for i in range(1,6): # for 5 rows
#      print(i*"*")


# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")  #end=" " value ko same line pe rakhta h
#     print()  #ye line change kr rha h poora complete hone k baad


for i in range(5,0,-1):
    for j in range(i):
        print(i,end=" ")  #end=" " value ko same line pe rakhta h
    print()

    
  


    
    


