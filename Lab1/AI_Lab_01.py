#!/usr/bin/env python
# coding: utf-8

# # <center>Artificial Intelligence</center>  <center>Fall 2023</center>
# ## Lab 01
# #### Name: Abdul Mateen
# #### Roll number: 2021-cs-190
# 

# Take weight in kgs and convert it into pounds. 1 pound = 1 kg 2.2046 **(2 marks)**

# In[1]:


## add code here

weight_in_kgs = float(input("Enter weight in kilograms: "))
weight_pounds = weight_in_kgs * 2.2046
print(f"{weight_in_kgs} kilograms is equal to {weight_pounds} pounds")

# Calculate the cost of all the items in a shopping cart. **(2 marks)**

# In[2]:


prices =[20,50,80,10,56,89]

## add code here

prices = [20, 50, 80, 10, 56, 89]
total_cost = sum(prices)
print(f"Total cost of items in the shopping cart: ${total_cost}")

# Write a function that returns the maximum of two numbers. **(2 marks)**

# In[3]:


## add code here

def max_of_two_numbers(a, b):
    return max(a, b)

# Write a function called **deepmind** that takes a number  **(4 marks)**
# * If the number is divisible by 3, it should return deep.
# * If it is divisible by 5, it should return mind.
# * If it is divisible by both 3 and 5, it should return deepmind.
# * Otherwise, it should return the same number.
# 
# 
# 

# In[4]:


## add code here

def deepmind(number):
    if number % 3 == 0 and number % 5 == 0:
        return "deepmind"
    elif number % 3 == 0:
        return "deep"
    elif number % 5 == 0:
        return "mind"
    else:
        return number

# **listA** =  [1,2,3,4,5,6,7,8,9,10]  
# 
# If an element of **listA** is smaller than 5, replace it with 0. And if an element of x is bigger than 5, replace it with 1. (**2 marks**)

# In[5]:


## add code here

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listA = [0 if x < 5 else 1 for x in listA]
print(listA)
# Compute the square of **listA** elements in one line. (**2 marks**)
# 

# In[6]:


listA = [1,2,3,4,5,6,7,8,9,10]
## add code here
squared_listA = [x ** 2 for x in listA]
print(squared_listA)
# Concatenate b1 and b2. (**2 marks**)

# In[7]:


b1 = ['Hello', 'in','first']
b2 = ['Students','the','recitation']
## add code here

concatenated_list = b1 + b2
print(concatenated_list)

# Create a dictionary of student **Ali** where the keys are courses and values are total and obtaining marks in each course. Print the dictionary items subjects wise **(2 marks)**

# In[8]:


## add code here

ali_marks = {
    'Math': {'Total': 100, 'Obtained': 85},
    'Science': {'Total': 100, 'Obtained': 90},
    'English': {'Total': 100, 'Obtained': 78}
}

for subject, marks in ali_marks.items():
    print(f"Subject: {subject}, Total Marks: {marks['Total']}, Obtained Marks: {marks['Obtained']}")

# Create a class 'calculator' with the following functions to compute i) addition, ii) subtraction, iii)multiplication, iv)division and v)square
# between two numbers. **(2 marks)**

# In[9]:


## add code here

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Devide by zero not possible"

    def square(self, a):
        return a ** 2
