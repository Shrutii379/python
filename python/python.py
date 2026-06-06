

#functon ka naam=variable naam

 def greet():#function defining # calledparameters while makingfunctions
     name=input('enter your name:')
     print(f'hello{name}!')
 greet() #function call #calledarguments while calling



#que. print greatest between 2 variables 

def greatest():
    a=10
    b=5
    if a>b:
       print(f'{a} is greater than {b}')
    elif b>a:
       print(f'{b} is greater than {a}')
    else:
        print('both are equal')
greatest()

#que. palindrome

def palindrome(name):
    reverse=name[::-1]
    if name==reverse:
        print(f'{name} is a palindrome')
    else:
        print(f'{name} is not a palindrome')
name="madam"
palindrome(name)



#return sends the output to the function

def add():
    a=10
    b=20
    c=a+b
    return c   #use of return
print(add())

def greet():
    return "hello"
print(greet())

def add():
    print(greet())   #here without print it will not print hello ,only print 30
    a=10
    b=20
    return a+b
    print(add())

def add(a,b):   #function define krte waqt parameters
     print(a+b)
add(10,20)    #function call krte waqt arguments


# #type hinting means suggesting the datatype(variable:datatype)(syntax)


def add(a:int,b:int): #positional datatype
     print(a+b)
add(10,20)


 def add(a,b=0): #here b is default paramaeter having value 0
     print(a+b)
 add(10)
 add(10.20)


# #accept an parameter named as 'n' and print factorial of'n' using function

 def factorial(n:int):
     fact=1
     for i in range(1,n+1):
         fact*=i  #shorthand operator
     return fact 
 print(factorial(5))







