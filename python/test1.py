# %% [markdown]
# # Python Test Assignment
# 
# Instructions: Solve all questions in the code cells below.

# %% [markdown]
# ## Question 1: Grade Calculator (if, elif, else)
# 
# Take percentage as input from the user and print the grade according to:
# 
# - Percentage >= 80 → Grade A+
# - Percentage >= 70 → Grade A
# - Percentage >= 60 → Grade B
# - Percentage >= 50 → Grade C
# - Otherwise → Fail
# 
# ### Sample Input
# 85
# 
# ### Sample Output
# Grade A+
# 
# percentage=int(input("enter the percentage"))
# if percentage>=80:
#     print("Grade A+")
# elif percentage>=70:
#     print("Grade A")
# elif percentage>=60:
#     print("Grade B")
# elif percentage>=50:
#     print("Grade C")
# else: 
#     print("Fail")


# %% [markdown]
# ## Question 2: Palindrome Number
# 
# Take a number as input and check whether it is a palindrome or not.
# 
# ### Sample Input
# 121
# 
# ### Sample Output
# Palindrome Number
# 

# n=int(input("enter the number"))
# copy=n
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# if copy==reverse:
#         print("palindrome")
# else:
#         print("not palindrome")

# %% [markdown]
# ## Question 3: Factorial of a Number
# 
# Take a number as input and find its factorial.
# 
# ### Sample Input
# 5
# 
# ### Sample Output
# 120


# def factorial(n):
#        fact=1
#        for i in range(1,n+1):
#               fact*=i
#        return fact
# print(factorial(5))


# %% [markdown]
#Question 4: Count Even and Odd Numbers in a Range
 
# Take starting number and ending number from the user.
# Count how many even and odd numbers are present in that range.
# 
# ### Sample Input
# Start = 1
# End = 10
# 
#  Sample Output
# Even Numbers = 5
# Odd Numbers = 5
# start=int(input("enter the starting point"))
# end=int(input("enter the end point"))
# even=0
# odd=0
# for i in range(1,end+1):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even,odd)

# %% [markdown]
# ## Question 5: Number Divisible by 3 and 5
# 
# Take a range from the user and print all numbers that are divisible by both 3 and 5.
# 
# ### Sample Input
# Start = 1
# End = 50
# 
# ### Sample Output
# 15 30 45
start=int(input("enter starting range"))
end=int(input("enter end range"))

for i in range(start,end+1):
    if i%3==0 and i%5==0:
        
     print(i)

#