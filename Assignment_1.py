#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
* = Mathematical Operator
"hello" = String
-87.8 = Integer
- = Mathematical Operator
/ = Mathematical Operator
+ = Mathematical Operator
6 = Integer2.What is the difference between string and variable?
A string is a datatype that only stores the text value in python they are enclosed in generally "" or '' where as variables is a name that can store any data type including strings in python following is the example that that can further expand on the difference of string and variable
"My name is Abhisht"
#The above written text can be termed as a string as it is enclosed in a "" whereas in case of variable we can say that
name = "Abhisht"
Age = 24
# Here we can see that the variable is a name that is used to store any datatype
# We can simply print the variable by calling its name but in order to print a string we will have to use the whole string 
3. Describe three different data types.
The three different types of data types are
1.strings
2.integers
3.list
apart from there are some more types of datatypes which can be mentioned here as
1.float
2.Boolean4. What is an expression made up of? What do all expressions do? 
 An expression is a combination of values operators and variable along with fuctions to perform a specific set of   operation in python. For example an expression of 5+3 leads to the addition of 8 here we can see that two values uses an operator to attain a specific result. Another example of an expression can be suggested as if we have to see the length of a string of a type of a variable we can use len() function or type() function which can be said to as an expression so concluding my answer I would like to say that an expression is a combination of values operators and function to perform a specific set of operation to attain a particular result
 5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?

As mentioned in the above question an expression is a combination of values operators and variable along with fuctions to perform a specific set of operation in python to obtain a certain result but a statement is just a line of code that neccassarily does not provide any result hence spam = 10 is simply a statement that stores its data in the spam variable where as if we used type(spam) which will provide the result of type of the datatype then that is an expression.6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
The answer will still be 22 as the bacon will be used as an expression here not had it been bacon = bacon+1 then the value of the variable would have changed but not in this case.7. What should the values of the following two terms be?
'spam' + 'spamspam'
This happened because addition of two strings is can be done by using + operator where two strings can be concated to become one string hence the value that we will get in return will be 'spamspamspam'
"spam" *3
By using  * operator we can repeat the string three times as in this case hence here also we will get the result as spamspamspam
8. Why is eggs a valid variable name while 100 is invalid?
It is beacause the ruling of python is done is such a way that it does not accept a variable name starting from any number between(0-9) although it accepts the variable name ending with the number. Therefore eggs is a valid variable name whereas 100 is an invalid name for a variable.9. What three functions can be used to get the integer, floating-point number, or string
version of a value?
X = int(3.45)
This will give the integer version of a value
Y = float(42.5)
This will give the floating point value
Z = str(345)
This function will make a number in a string format
10. Why does this expression cause an error? How can you fix it?
"I have eaten" + 99 +  "burritos"
It is because we want to concate a string with an integer which is will in turn give an error therefore in order to fix it we should convert the integer into string first then we will get the desierd result and the correct expression will be:
"I have eaten" + "99" +  "burritos"