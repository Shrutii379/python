

# #functon ka naam=variable naam

# def greet():#function defining # called parameters while making functions
#      name=input('enter your name:')
#      print(f'hello{name}!')
# greet() #function call #called arguments while calling



# que. print greatest between 2 variables 
# def greatest():
#     a=10
#     b=5
#     if a>b:
#        print(f'{a} is greater than {b}')
#     elif b>a:
#        print(f'{b} is greater than {a}')
#     else:
#         print('both are equal')
# greatest()

# que. palindrome
# def palindrome(name):
#     reverse=name[::-1]
#     if name==reverse:
#         print(f'{name} is a palindrome')
#     else:
#         print(f'{name} is not a palindrome')
# name="madam"
# palindrome(name)



# #return sends the output to the function

# def add():
#     a=10
#     b=20
#     c=a+b
#     return c   #use of return
# print(add())

# def greet():
#     return "hello"
# print(greet())

# def add():
#     print(greet())   #here without print it will not print hello ,only print 30
#     a=10
#     b=20
#     return a+b
#     print(add())

# def add(a,b):   #function define krte waqt parameters
#      print(a+b)
# add(10,20)    #function call krte waqt arguments


# # #type hinting means suggesting the datatype(variable:datatype)(syntax)


# def add(a:int,b:int): #positional datatype
#      print(a+b)
# add(10,20)


# def add(a,b=0): #here b is default paramaeter having value 0
#      print(a+b)
# add(10)
# add(10.20)


# accept an parameter named as 'n' and print factorial of'n' using function
# def factorial(n:int):
#      fact=1
#      for i in range(1,n+1):
#          fact*=i  #shorthand operator
#      return fact 
# print(factorial(5))



# #keyword parameters

# def info(name,age,gender,address):
#     print(name)
#     print(age)
#     print(gender)
#     print(address)
# info(gender='F',age=34,address='Bhopal',name= "Shruti")

# #check if a number is palindrome or not using keyword argument

# def palinderome(number):
#     copy=num
#     reverse=0
#     while number>0:
#         last=number%10
#         rev=rev*10+last
#         num=num//20
#         if  copy==rev:
#             print("f{copy} is a palindrome number")
#         else:
#              print("f{copy} is not  a palindrome number")
# palindrome(1221)


#Recursion
# def display(num):
#     if num>10:
#         return  #break is not directly used in conditional statements instead return is used
#     print(num)
#     display(num+1) #function calling itself
# display(1)

# def display(num):
#     if num<1:
#         return
#     print(num)
#     display(num-1) 
# display(10)
    

# #factorial using recursion

# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(6))


#lambda ,args,kwargs  (skipped in functions)




















