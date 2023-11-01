#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?The two types of Boolean data types are True and False. True value represents the logic which is valid or "true' where as False value reprsents the value which is not valid or "false". In order to write the true value we will write True and we will use False. 2. What are the three different types of Boolean operators?Three different types of boolean operators are And , or and Not. Now let us understand each of them one by one
And operator:- This returns true only when both the operands are true else it will return false.
example:
true and true  = true
false and true = false
true and false = false
false and false = false

Or operator:- This returns true value when only one value is true within the operands.
example:
true or true = true
true or false = true
false or true = true
false or false = false

Not operator:- This is unary operator which changes the value of the operand.
example:
NOT true = false
Not false = true3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).And operator:
true and true  = true
false and true = false
true and false = false
false and false = false

OR operator:
true or true = true
true or false = true
false or true = true
false or false = false

Not operator:
NOT true = false
Not false = true4. What are the values of the following expressions?
(5 > 4) and (3 == 5) = False

not (5 > 4) = False

(5 > 4) or (3 == 5) = True

not ((5 > 4) or (3 == 5)) = False

(True and True) and (True == False) = False

(not False) or (not True) = True5. What are the six comparison operators?

1. Equal(==) = This checks if the values are equal.
2. Not Equal(!=) = This checks if the values are not equal.
3. Greater than(>) = This checks if the left operator is greater than the right operator.
4. Less than (<) = This checks if the left operator is less than the right operator.
5. Greater equal to (>=) = This checks if the left operator is greater than or equal to the right operator. 
6. Less than (<=) = This checks if the left operator is less than or equal the right operator.
6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.

The equal to (==) and the assignment operator (=) serves different purpose in python.
The equal to(==) operator checks whether the two values are equal or not and is also used for comparison whereas assignment operator (=) is used to assign value to a variable.7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print'bacon')
else:
print('ham')
print('spam&')
print('spam')


Block1 = spam = 0
Block2 = if spam ==10:
          print('eggs)
Block3 = if spam > 5:
         print'bacon')
         else:
         print('ham')
         print('spam&')
         print('spam')          8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.
# In[2]:


spam = 3
if spam ==1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

9.If your programme is stuck in an endless loop, what keys you’ll press?
ctrl +c10. How can you tell the difference between break and continue?

Break statement will terminate the loop before the completion of the full loop. It is done in order to stop the loop prematurely when a certain situation is satisfied where as continue statement continues the loop by skipping the current iteration and moving forward with the next iteration.11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# In[6]:


for i in range(10):
    print(i)


# In[7]:


for i in range(0,10):
    print(i)


# In[9]:


for i in range(0,10,1):
    print(i)

As we can see that there is no difference between the three given statement.12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.
# In[10]:


for i in range(1,11,1):
    print(i)


# In[11]:


a = 1
while a<11:
    print(a)
    if a==11:
        break
    a = a+1

13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

import spam
spam.bacon()
# In[ ]:




