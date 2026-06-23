# %% [markdown]
# # Python Practice Assignment
# 
# ## While Loop, For Loop, Functions and Return Statement

# %% [markdown]
# ### While TakeLoop Questions
# 1. Print numbers from 1 to 10 using a while loop.
# i=1
# while i<=10:
#     print(i)
#     i+=1
# %% [markdown]
# 2. Print all even numbers between 1 and 20 using a while loop.

# i=1
# while i<20:
#     if i%2==0:
#      print(i)
#     i+=1


# %% [markdown]
# 3. Take a number n from the user and find the sum of numbers from 1 to n using a while loop.

# n=int(input("enter the number"))
# i=1
# sum=0
# while i<=n:
#  sum+=i
#  i+=1
# print(sum)


# %% [markdown]
# 4.Take a number from the user and count how many digits it contains using a while loop.

# n=int(input("enter the number"))
# i=1
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)


# %% [markdown]
# 5. Take a number from the user and print its reverse using a while loop.

# n=int(input("enter the number"))
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse * 10 + digit
#     n=n//10
# print(reverse) 

# %% [markdown]
# ### For Loop Questions
# 6. Print numbers from 1 to 20 using a for loop.

# for i in range (1,21):
#     print(i)

# %% [markdown]
# 7. Take a number from the user and print its multiplication table up to 10 using a for loop.

# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n, "x", i, "=", n * i)

# %% [markdown]
# 8. Find the sum of all even numbers between 1 and 50 using a for loop.

# sum=0
# for i in range(1,51):
#     if i%2==0:
#      sum+=i
# print(sum)
# %% [markdown]
# 9. Take a string from the user and count the number of vowels using a for loop.
# s=input("enter the string")
# count=0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)

# %% [markdown]
# 10. Given nums = [12, 45, 7, 89, 23], find the largest number using a for loop.
# nums = [12, 45, 7, 89, 23]
# largest=nums[0]
# for i in range(len(nums)):
#     if nums[i]>largest:
#         largest=nums[i]
        
# print(largest)



# %% [markdown]
# ### Function Questions
# 11. Create a function greet() that prints 'Welcome to Python'.

# def greet():
#     print("Welcome to Python")
# greet()
# %% [markdown]
# 12. Create a function square(num) that prints the square of a number.

# def square(num):
#     print(num*num)
# square(5)

# %% [markdown]
# 13. Create a function check_even_odd(num) that prints whether a number is even or odd.

# def check_even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# check_even_odd(98) 

# %% [markdown]
# ### Return Statement Questions
# 14. Create a function add(a, b) that returns the sum of two numbers.
def add(a,b):
    return a+b
print(add(45,89))


# 15. Create a function largest(a, b) that returns the larger number.

# def largest(a,b):
#     if a>b:
#      return a
#     else:
#      return b
# print(largest(76,54))        


