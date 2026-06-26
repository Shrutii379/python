# %% [markdown]
# # Python Assignment - Sets & Tuples (Basic)
# 
# **Instructions:** Solve all questions. Every question has a sample Input/Output.

# %% [markdown]
# ## Q1. Create a set containing 10, 20, 30, 40, 50 and print it.
# 
# Output:
# ```
# {10, 20, 30, 40, 50}
# ```

# s={10,20,30,40,50}
# print(s)

# %% [markdown]
# ## Q2. Create an empty set and add numbers 5, 10, 15, 20, 25 using a loop. Print the set.
# 
# Output:
# ```
# {5, 10, 15, 20, 25}
# ```
# s=set()
# for i in range(5,26,5):
#     s.add(i)
# print(s)

# %% [markdown]
# ## Q3. Take 5 integers from the user and store them in a set. Print the set.
# 
# Input:
# ```
# 10
# 20
# 30
# 20
# 40
# ```
# 
# Output:
# ```
# {40, 10, 20, 30}
# ```

# nums=int(input("how many rows you want"))
# s=set()
# s.add(nums)
# print(s)
# %% [markdown]
# ## Q4. Given:
# ```python
# s={10,20,30,40,50}
# ```
# Remove 30 and print the set.
# 
# Output:
# ```
# {40, 10, 20, 50}
# ```

# s={10,20,30,40,50}
# s.remove(30)
# print(s)

# %% [markdown]
# ## Q5. Given:
# ```python
# s={5,10,15,20}
# ```
# Take a number and check whether it is present.
# 
# Input:
# ```
# 15
# ```
# 
# Output:
# ```
# Found
# ```



#s={5,10,15,20}
# num=int(input("enter the number"))
# if num in s:
#     print("number is present")
# else:
#     print("number is not present ")

# %% [markdown]
# ## Q6. Given:
# ```python
# s={1,2,3,4,5,6}
# # ```
# # Print the number of elements.
# # 
# # Output:
# # ```
# # 6
# # ```

# count=0
# for i in range (len(s)):
#     count+=1
# print(count)


# %% [markdown]
# ## Q7. Find the union of:
# ```python
# a={1,2,3,4}
# b={3,4,5,6}
# # ```
# # 
# # Output:
# # ```
# # {1,2,3,4,5,6}
# # ```
# print(a.union(b))


# %% [markdown]
# ## Q8. Create a tuple containing 10,20,30,40,50 and print it.
# 
# Output:
# ```
# (10, 20, 30, 40, 50)
# ```

# t=(10,20,30,40,50)
# print(t)

# %% [markdown]
# ## Q9. Given:
# ```python
t=('Python','Java','C++','SQL','AI')
# ```
# Print first, last and third element.
# 
# Output:
# ```
# Python
# AI
# C++
# ```

for i in  range(len(t)):
    if i==0 or i==2 or i==len(t)-1:
    
     print(t[i])

# %% [markdown]
# ## Q10. Given:
# ```python
# t=(5,10,15,20,25,30)
# # ```
# # Print the length of the tuple.
# # 
# # Output:
# # ```
# # 6
# # ```

# print(len(t))


