# TakeoPython  By Shadab Khan (+91 7007 586 179)
6 June 2022

https://www.python.org/downloads/release/python-3105/
----------------------------------------------
Machine or Binary Language : Low lvel Programming Language
------------------------------------------------------------

00010101011 001110101010

-------------------------------
HLP:
------
C
C++
Java
Python
Go
Ruby
C#
R
JavaScript
----------------------------------------------------------
-> Python is a general purose High level programming language.
-> Python was developed by Guido Van Rossum was in 1989 while wotking at National Reasearch institute at Neitherlands.
-> But officially Python was available to puble in 1991.

-> Python is easy to learn:
--------------------------------

WAP to print "Hello World":
----------------------------
Using C:
===========

#include<stdio.h>

void main()
{
	printf("Hello World");
}

-------------------------------
Using C++:
===========

#include<stdio.h>

void main()
{
	cout<< "Hello World";
}
-------------------------------
Using Java:
===========

public class Demo
{

 public static void main(String[] args)
	{
		System.out.print("Hello World");
	}

}

Using Python:
=============
print("Hello World")

============================================
Where we can use Python:
-------------------------
1. For developing Desktop applicaton.
2. For developing Web applicaton.
3. For developing DATABASE applicaton.
4. For networking applicaton.
5. For Data Analysis applicaton.
6. Machine Learning
7. Artificial Inteligence
8. IOT(Internet Of Things)

We cannot develop mobile application using Python:
--------------------------------------------------

Features of Python:
------------------------------
1. Simple and Easy to learn
	-> Its has only 30+ keywords while in Java 53+
	
2. Opensource and freeware

3. High level language

4. Platform independent

---------------------------
5. Dynamically Typed Language


In Java:
---------
 int x = 10; // OK
   
     x = 15; // OK
	 
	 x = 2.3; // double value ERROR
	 x = false; // boolean ERROR
	 c = "Shadab"; // String ERROR


in Python:
---------------
  x = 10; // number
  
  x = 'Shadab' // string
  
  x = false // boolean

------------------------------------
-> Python is OOP lang, Function styple prog, proceedural style, modular programming.

-> Interpreted Language:
-------------------------
In Java:
------------
Source Code  ---Complier---> ByteCode ----JVM---->
                COMPILATION              EXECUTION
				
				
A.Java

> javac A.java     ---> A.class

> java A


In Python (Compilation and interpreatation) happens in one go.

-> Extensive Library:
-----------------------

=========================================================================
Flovors of Python:
------------------
1. CPython
------------
Standard version of python, Worked with C language.

2. Jython:
--------------
Python for Java Application

3. IronPython:
--------------
For C# DotNet framework

4. RubyPython:
-------------------
for Ruby application

5. Anaconda Python:
----------------------
It is for Big Data

6. PyPy:
----------

7. ShadabPython

------------------------------------------------------------
Indentifiers:
----------------
Name of variable, function, class etc called identifier.

1. Allowed characters 
		a) Alphabets(a-z, A-Z)
		b) Digits(0-9)
		c) Underscore('_')
		
Example:
-----------
### cash = 100  #OK

### my_salary = 101  #OK
	
### my-salary = 102  #ERROR
	
my$cash = 1100 #ERROR
--------------------------------------------------------
2. Identifier should not start with digit

sum123 = 99  #OK

123sum = 88  #ERROR

--------------------------------------------------------

 papa = 10
 papa = 20
 
 print(papa) # 10 or 20
 
 ---------------------------------
 
 3. Identifiers are case sensitive
 
mummy = 100
Mummy = 200
MUMMY = 300

print(Mummy) # 200

=======================================
Keywords or Reserve Words:
--------------------------------
There are 33 reserved words avaiable in Python
  
  -> True, False, None
  -> and, or, not, is
  -> if, elif, else
  -> while, for, break, continue, return , in , yield
  -> try, except, fially, raise, assert
  -> import, from, as, class, def, pass, global, nonlocal, lambda, del, with



  x = 10 # OK 
  
  if = 10 # ERROR
  
  IF = 10 # OK
  
  import keyword

print(keyword.kwlist)

--------------------------------

WAP to create 5 subject marks and print its average

------------------------------------------------------------------
Data Types:
-----------
1. int
2. float
3. complex
4. bool
5. str


6. bytes
7. bytearray
8. range
8. list
10. touple
11. set
12. frozenset
13. dict

-------------------------------------------
In-Built functions in Python:
==============================
1. type() -> to check type of variable

2. id() -> to get the address of object

3. print() -> to print the value

Base Conversion Functions

4. bin() -> we can use it to covert from any base to binary
--------------------------------------------------------------
*) Immutable/Non-Changeble object means no one can modifiy once they created.

int data type:
--------------
We can use int data type to represent whole numbers(integers)

a = 10
type(a)  # <class 'int'>

a) decimal form(base-10) :
---------------------------
-> Its default number system in python. 
-> Allowed digits are 0-9

e.g.     a = 10
         print(a) # 10
		
b) binary form(base-2) :
---------------------------
-> Allowed digits are 0-1

e.g.     a = 0B10
         print(a) # Yes


c) octal form(base-8) :
---------------------------
-> Allowed digits are 0-7

e.g.     a = 0o10
         print(a) # Yes
		 
d) hexa-decimal form(base-16) :
---------------------------
-> Allowed digits are 0-9, A-F

e.g.     a = 0X10
         print(a) # Yes

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

# It will alway print numbers into decimal-form (base-10)
a = 10  
print(a) # 10

a = 0b10  
print(a) # 2

a = 0o10  
print(a) # 8

a = 0x10  
print(a) # 16

a = 0xFACE  
print(a) # 64206

a = 0xBEEF  
print(a) # 48879

a = 0xBEER 
print(a) # ERROR

--------------------------------------------------------------------
float data type:
----------------
-> We can use float dat type to represent floating point values (decimal values)

E.g.

x = 1.25

type(x) # <class 'float'> 

-> We CANNOT represent float in binary, octal or hexa-decimal form

-> x = 1.2e3  OR x = 1.2E3
    print(x) #  1.2 * 1000 = 1200
	
	
-----------------------------------------------------------------------------
square root of 4 => 2
square root of 9 => 3
square root of 16 => 4

square root of 1 => 1

square root of -1 => imaginary i  but python j

3. complex data type:
---------------------
 a + bj   # a is a real part and b is an imaginary
 
 e.g
 
 z = 3 + 5j
 
 ---------------------------------------------------------------
 
4. bool data type:
------------------

-> True, False

-> In Python, C, C++, JavaScript, every non-zero number treated as True and zero should be treated as False.

-> Emplty string treated as False other strings treated True

E.G. X = "" 


in c programming:
----------------------
int a = 10;

if( a = 15)
{
	printf("Hi");
}
else
{
	printf("Bye");
}

OUTPUT -> 'Hi'
--------------------------------------------------
5. str data type:
-------------------
-> A string is a sequence of characters enclosed within single quotes or double quotes

---------------------------------------------------------------------------------------------
list data type:
-------------------
name1 = 'Java'
name2 = 'JavaScript'
name3 = 'Python'
name4 = 'HTML'
name5 = 'CSS' 

-> If we want to represent a group of values into a single entity where order required to preseve.
-> List can contains duplicate elements.
-> List are growable in nature


Example:
--------------
fruits = []

technologies =['Java', 'JavaScript', 'Python', 'HTML', 'CSS' ]
technologies =['Java', 'JavaScript', 'Python', 'HTML', 'CSS' ]
technologies
['Java', 'JavaScript', 'Python', 'HTML', 'CSS']
technologies[0]
'Java'
technologies[4]
'CSS'

technologies[5]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    technologies[5]
IndexError: list index out of range

technologies[-1]
'CSS'
technologies[-2]
'HTML'
technologies[-3]
'Python'


---------------------------------------------
How to access/print all the elements of a list


for tech in technologies:
	print(tech)

------------------------------------------------
Operators:
----------
1. Arithmetic Operators
2. Relational or Comparision Operators
3. Equality Operators
4. Logical operators
5. Assignment opeartors
6. Bitwise operators
7. Special operators

1. Arithmetic Operators;
=========================
+  ==> Addition operator
-  ==> Subtraction operator
*  ==> Multiplication operator
/  ==> Division operator
%  ==> Modulo operator

// ==> Floor Division operator
** ==> Exponent operator or power operator

operators.py:
-----------------
a = 10
b = 2

print('a + b = ', (a + b)) # 12
print('a - b = ', (a - b)) # 8
print('a * b = ', (a * b)) # 20
print('a / b = ', (a / b)) # 5.0
print('a % b = ', (a % b)) # 0
print('a // b = ', (a // b)) # 5
print('a ** b = ', (a ** b)) # 100


Some speciall cases:
---------------------
a)

name = 'shadab'
print(name * 5) # shadabshadabshadabshadabshadab

b) 

x = 10
y = 0
 
print(x/y) # ZeroDivisionError: division by zero

----------------------------------------------------------------------------------
2. Relational or Comparision Operators:
----------------------------------------
>, >=, <, <!

Example1:
----------
a = 10
b = 2

print('a > b = ', (a > b)) # True
print('a >= b = ', (a >= b)) # True
print('a < b = ', (a < b)) # False
print('a <= b = ', (a <= b)) # False

Example2:
----------
a = 'shadab'
b = 'shadab'

print('a > b = ', (a > b)) # False
print('a >= b = ', (a >= b)) # True
print('a < b = ', (a < b)) # False
print('a <= b = ', (a <= b)) # True

Example3:
----------
a = True  # 1
b = False # 0

print('a > b = ', (a > b)) # True
print('a >= b = ', (a >= b)) # True
print('a < b = ', (a < b)) # False
print('a <= b = ', (a <= b)) # False

Example4:
----------
a = 10
b = 'shadab'

print('a > b = ', (a > b)) # TypeError: '>' not supported between instances of 'int' and 'str'

3. Equality Operators:
-----------------------
 ==, !=
 
 -> We can apply these operators for any type even incompatible types also

a = 10
b = 2

print( a == b) # False
print( a != b) # True

print( 10 == True) # False

print( False == False) # True

print('shadab'  == 10) # False

4. Logical operators:
----------------------
-> and, or, not
-> We can apply for all types

-> For boolean types:
=========================
	True and False ==> False
	True or False ==> True
	not False ==> True


-> For non-boolean types:
=========================

a) 0 means False
b) non-zero means True
c) empty string always be treated as False

Example:
-----------
print(10 and 20) # True

-------------------------------------------
Ternary Operator:
===================

x = firstValue if condition else secondValue


a = ------
b = ------

a = 10
b = 17

if a > b :
	print('MAX = ', a)
else:
	print('MAX = ', b) 

 #### OR	

max = a if a > b else b
print('MAX = ', max)
======================================================
Lab-1 : WAP for minimum of 3 number

a = 56
b = 17
c = 19

if a > b :
    if a > c:
        print('MAX = ', a)
    else :
        print('MAX = ', c)
else:
    if b > c:
        print('MAX = ', b)
    else:
        print('MAX = ', c)

 #### OR	

max = (a if a > c else c) if a > b else (b if b > c else c)

-------------------------------------------------------------------------
Input and output statements :
-----------------------------
a =int( input("Enter first value: "))
print(type(a))

b =int( input("Enter second value: "))
print(type(b))

sum = a + b
print(sum)

==============================
// WAP to read employee data and display it

name = input('Enter Employee name: ')
age = int(input('Enter Employee age: '))
salary = float(input('Enter Employee salary: '))
married = bool(input('Employee married?[True | False]: '))

print(name, age, salary, married)

---------------------------------------------
eval():
----------
eval function take a string and evaluates the result.

expr = "10 + 20  + 30"

result = eval(expr)

print(result)

-----------------------------------------
Command Line arguments:
----------------------------------------
from sys import argv
print('Hello From Test')
print(type(argv)) # <class 'list'>
print(argv) # ['test.py', '10', '20', '30']

print( argv[1] +argv[2] +argv[3]) # '102030'

print( int(argv[1]) + int(argv[2]) + int(argv[3])) # '60'

------------------------------------------------------------------

C:\Users\user\Desktop\Takeo Python\TakeoPython>py test.py 10 20 30
Hello From Test
<class 'list'>
['test.py', '10', '20', '30']
102030
60

------------------------------------------------------
Output statements:
--------------------
Form-1: print() without arguments
==================================
Just it prints new line character

Form-2: print(string) 
==================================

print('Hello' + 'World')
print('Hello' * 10) 

Form-3: print(---------) with N number of arguments and with 'sep' attribute
=============================================================================
-> Default separator is SPACE
 
In Java:
------------
int a = 10, b = 15, c = 20; // OK

int a, b, c = 10, 15, 20; // ERROR

In Python:
------------
 a = 10, b = 15, c = 20; // OK

 a, b, c = 10, 15, 20; // OK
 
 print(a, b, c, "Hello", 'Hi', 'Bye')
 

 
print('Hello', name, 'your age is', age, 'and salary is $', salary, sep=':')
 # Hello:Shadab:your age is:35:and salary is $:101

Form-4: print(---------) with N number of arguments and with 'end' attribute
=============================================================================
 
print("Hello")
print("Java")
print("Consultant")

OUTPUT:
-------

Hello
Java
Consultant

--------------------------

print("Hello", end=' ')
print("Java", end=' ')
print("Consultant", end='\n')

OUTPUT:
-------
Hello Java Consultant

Form-5: print(formatted string) 
================================

print("formatted string" %(variable list))

%i  ===> int
%d  ===> int
%f  ===> float
%s  ===> str


Example:
--------
name = 'Prashad'
age = 21
salary = 999.25

print("Hello %s your age is %d and salary is %f"  %(age, name, salary))

-------------------------------------------------------------------------------------
Flow Control statemets:
-------------------------
1. Conditional Statements
		a) if
		b) if-else
		c) if-elif-else
		
2. Transfer Statements
		a) break
		b) continue
		c) pass
		
3. Iterative Statements
		a) for
		b) while


======================================================
x = int(input('Enter a number: '))

if ( x % 2 == 0):
    print('Even Number') 
else:
    print('Odd Number')
	
-----------------------------------------------------
x = int(input('Enter a number: '))

if ( x == 1):
    print('Monday')
elif ( x == 2):
    print('Tuesday') 
elif ( x == 3):
    print('Wednesday') 
elif ( x == 4):
    print('Thursday') 
elif ( x == 5):
    print('Friday') 
elif ( x == 6):
    print('Saturday') 
elif ( x == 7):
    print('Sunday') 
else:
    print('Pagal')

-----------------------------------------------------------------
3. Iterative Statements
	a) for loop
		
Syntax:
---------
for <var> in <sequence>:
	body

Example1:
---------
name = 'Shadab Ahmad Khan'

for x in name:
    print(x)
		
Example1:
---------
# Print number 0 to 9

for x in range(10):
    print(x)

# Print 10 to 1 in reverse direction
for x in range(10, 0, -1):
    print(x)
---------------------------------------------------------------	
 b) while loop
 --------------
 
 Syntax:
 -----------
	while <condition> :
		<body>

x =1

while x < 11:
    print(x)
    x = x+1
	
=====================================================
# WAP to print only ODD number between 1 to 100

for x in range(1,101):
    if x % 2 != 0:
        print(x)
---------------------------------------------------------
2. Transfer Statements
		a) break
		b) continue
		c) pass

Example:
==============
for x in range(10):
    if x == 6:
        break
    print(x)

Output:
----------
0
1
2
3
4
5

--------------------------------------
Example:
==============
for x in range(10):
    if x == 6:
        continue
    print(x)

Output:
----------
0
1
2
3
4
5
7
8
9

---------------------------------------------------------
Types of CSS:
--------------
1. Internal CSS:
================

<style>

  CSS goes HERE.....
  
</style>


2. External CSS:
=================
=> We will create a file wih any name but having extension '.css'
=> We can use this file in our HTML page by using link tag
	
	<link rel="stylesheet" href="path of css file" >


3. Inline CSS:
--------------------

Style as an attribute.

    <h1 style="color: red;">This is Table Demo</h1>


On a same Heading:

Default CSS -> Black
External css -> RED
Internal CSS -> Green
Inline CSS -> Blue

Output:
-----------
BLUE


















