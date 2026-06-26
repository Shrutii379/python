# %% [markdown]
# # Dictionary Assignment (Basic Level)
# 
# Questions 1 to 14 with Input/Output examples.

# %% [markdown]
# ## Question 1: Create a Dictionary
# 
# Input:
# Name=Raj, Age=20, City=Bhopal
# 
# Output:
# {'Name':'Raj','Age':20,'City':'Bhopal'}
# d={'Name':'Raj','Age':20, 'City':'Bhopal'}
# print(d)

# %% [markdown]
# ## Question 2: Print Name
# 
# Input:
# d={'Name':'Raj','Age':20}
# # 
# # Output:
# # Raj
# print(d['Name'])


# %% [markdown]
# ## Question 3: Print Age
# 
# Input:
# d={'Name':'Raj','Age':20}
# # 
# # Output:
# # 20
# print(d['Age'])

# %% [markdown]
# ## Question 4: User Input Dictionary
# d={}
# n=int(input("enter the no of pairs"))
# for i in range(n):
#     key=input("enter key")
#     value=input("enter value")
#     d[key]=value
# print(d)

# Input:
# Rahul
# 22
# 
# Output:
# {'Name':'Rahul','Age':22}

# %% [markdown]
# ## Question 5: Add New Key
# 
# Input:
# d={'Name':'Raj','Age':20}
# # Add Course='Python'
# # 
# # Output:
# # {'Name':'Raj','Age':20,'Course':'Python'}
# d['Course']='Python'
# print(d)

# %% [markdown]
# ## Question 6: Update Value
# 
# Input:
# d={'Name':'Raj','Age':20}
# # d['Age']=25
# # print(d)


# d.update({'Age':25})
# print(d)
# Output:
# {'Name':'Raj','Age':25}

# %% [markdown]
# ## Question 7: Count Total Keys
# 
# Input:
# d={'Name':'Raj','Age':20,'City':'Bhopal'}

    
# print(len(d)) 
# Output:
# 3

# %% [markdown]
# ## Question 8: Print All Keys
# 
# Input:
# d={'Name':'Raj','Age':20,'City':'Bhopal'}
# print(d.keys()) 
# Output:
# dict_keys(['Name','Age','City'])

# %% [markdown]
# ## Question 9: Print All Values
# 
# Input:
# d={'Name':'Raj','Age':20,'City':'Bhopal'}
# print(d.values())
# Output:
# dict_values(['Raj',20,'Bhopal'])

# %% [markdown]
# ## Question 10: Print All Key-Value Pairs
# 
# Input:
# d={'Name':'Raj','Age':20,'City':'Bhopal'}
# print(d.items()) 
# Output:
# Name : Raj
# Age : 20
# City : Bhopal

# %% [markdown]
# ## Question 11: Check Key Exists
# 
# Input:
# Age
# d={'Name':'Raj','Age':20,'City':'Bhopal'}

# if 'Age' in d:
#     print("key found")
        
# else:
#     print("not found") 
# Output:
# Key Found

# %% [markdown]
# ## Question 12: Delete a Key
# 
# Input:
# d={'Name':'Raj','Age':20,'City':'Bhopal'}
# d.pop('City')
# print(d)
# Delete City
# 
# Output:
# {'Name':'Raj','Age':20}

# %% [markdown]
# ## Question 13: Find Dictionary Size
# 
# Input:
# d={'Name':'Raj','Age':20,'City':'Bhopal'}
# print(len(d))
# 
# Output:
# 3

# %% [markdown]
# ## Question 14: Merge Two Dictionaries
# 
# Input:
# d1={'a':1,'b':2}
# d2={'c':3,'d':4}
# for i in d2:
#     if i not in d1:
#         d1[i]=d2[i]

# print(d1)# Output:
# {'a':1,'b':2,'c':3,'d':4}


