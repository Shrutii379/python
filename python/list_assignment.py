# %% [markdown]
# # List Assignment - Level Up
# 
# ## Instructions
# - Solve all questions using Python Lists.
# - Use loops and conditions wherever possible.
# - Read the input and produce the expected output.
# 

# %% [markdown]
#  Q1. Sort List in Ascending Order
# 
# Input
# nums = [45, 12, 78, 23, 5]
# # 
# Output
# [5, 12, 23, 45, 78]

# for i in range (len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]:
#             nums[i],nums[j]=nums[j],nums[i]
# print(nums)
        
        

# %% [markdown]
# ## Q2. Sort List in Descending Order
# 
# Input
# nums = [45, 12, 78, 23, 5]
# # 
# # Output
# # [78, 45, 23, 12, 5]
# for i in range (len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[j]>nums[i]:
#             nums[j],nums[i]=nums[i],nums[j]
# print(nums)


# %% [markdown]
# ## Q3. Find Largest Number
# 
# Input
# nums = [12, 45, 89, 23, 67]
# # 
# # Output
# # 89
# largest=nums[0]
# for i in range (len(nums)):
#     if nums[i]>largest:
#         largest=nums[i]
# print(largest)



# %% [markdown]
# ## Q4. Find Second Largest Number
# 
# Input
# nums = [12, 45, 89, 23, 67]
# # 
# # Output
# # 67

# largest=slargest=nums[0]
# for i in range(len(nums)):
#     if nums[i]>largest:
#         largest=nums[i]
#         slargest=largest
#     else:
#         nums[i]>slargest
#         slargest=nums[i]
# print(slargest)
# %% [markdown]
# ## Q5. Remove Duplicate Elements
# 
# Input
nums = [1, 2, 3, 2, 4, 1, 5]
unique=[] 
# Output
# [1, 2, 3, 4, 5]
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)




# %% [markd
# ## Q6. Count Frequency of Number 5
# 
# Input
# nums = [5, 2, 5, 7, 5, 1]
# count=0
# # Output
# # 3

# for i in nums:
#     if i==5:
#         count+=1
# print(count)

# %% [markdown]
# ## Q7. Print Only Even Numbers
# 
# Input
nums = [11, 20, 33, 40, 55, 60]
# 
# Output
# 20
# 40
# 60

even=[]
for i in nums:
    if i%2==0:
        even.append(i)
print(even)

# %% [markdown]
# ## Q8. Merge Two Lists
# 
# Input
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.extend(l2)
# print(l1)

# Output
# [1, 2, 3, 4, 5, 6]



# %% [markdown]
# ## Q9. Reverse a List
# 
# Input
# nums = [10, 20, 30, 40, 50]
# rev=[] 
# for i in range(len(nums)-1,-1,-1):
#     rev.append(nums[i])

# print(rev)



# %% [markdown]
# ## Q10. Find Sum of Elements at Even Index
# 
# Input
# nums = [10, 20, 30, 40, 50]
# sum=0
# # 
# # Output
# # 90
# for i in nums[0:5:2]:
#     sum+=i
# print(sum)



# %% [markdown]
# ## Q11. Find Second Smallest Number
# 
# Input
# nums = [45, 12, 78, 23, 5]
# # 
# # Output
# # 12


# smallest=s_smallest=nums[0]
# for i in nums:
#     if i < smallest:
#         s_smallest = smallest
#         smallest = i
#     elif i < s_smallest and i != smallest:
#         s_smallest = i
    
# print(s_smallest)

# %% [markdown]
# ## Q12. Check if List is Sorted
# 
# Input
# nums = [5, 10, 15, 20]
# sorted_list = True
# # 
# # Output
# # List is Sorted

# for i in range (len(nums)-1):
#     if nums[i]>nums[i+1]:
#      sorted_list = False
#     break
# if sorted_list:
#       print("List is sorted")
# else:
#     print("List is not sorted")

