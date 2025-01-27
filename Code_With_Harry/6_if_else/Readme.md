<h2>If Else Conditional statements</h2>

Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to:  a >= b

Elif
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

Else
The else keyword catches anything which isn't caught by the preceding conditions.


<code>
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
</code>


Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

<code>if a > b: print("a is greater than b") </code>


Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

a = 2
b = 330
print("A") if a > b else print("B")


And
The and keyword is a logical operator, and is used to combine conditional statements:

if a > b and c > a:
  print("Both conditions are True")



  

Or
The or keyword is a logical operator, and is used to combine conditional statements:

if a > b or a > c:
  print("At least one of the conditions is True")


Not
The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
if not a > b:
  print("a is NOT greater than b")     #OP: a is NOT greater than b


<h2>Nested If</h2>
You can have if statements inside if statements, this is called nested if statements.

Example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


<h2>The pass Statement</h2>
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

Example
a = 33
b = 200

if b > a:
  pass    







