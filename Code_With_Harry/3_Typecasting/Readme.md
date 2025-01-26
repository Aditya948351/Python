<h2>Type Casting in Python (Implicit and Explicit) with Examples</h2>
<p>Type Casting is the process of converting the Python variable datatype into a certain data type for performing required operations. There are two types of Type Casting:</p>
<ul>
    <li>Implicit Type Conversion</li>
    <li>Explicit Type Conversion</li>
</ul>

<h3>Implicit Type Conversion in Python</h3>
<p>In this method, Python converts the datatype into another datatype automatically. Users don’t have to be involved in this process.</p>
<pre><code>
# Python program to demonstrate 
# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Python automatically converts 
# c to float as it is a float addition 
c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))
</code></pre>

<h3>Explicit Type Conversion in Python</h3>
<p>In this method, Python needs user involvement to convert the variable data type into the required data type. Some examples of type casting:</p>
<pre><code>
# Convert int to float
a = 5
n = float(a)
print(n)
print(type(n))
</code></pre>

<h3>Int to Float</h3>
<pre><code>
a = 5
n = float(a)
print(n)
print(type(n))
</code></pre>

<h3>Float to Int</h3>
<pre><code>
a = 5.9
n = int(a)
print(n)
print(type(n))
</code></pre>

<h3>Int to String</h3>
<pre><code>
a = 5
n = str(a)
print(n)
print(type(n))
</code></pre>

<h3>String to Float</h3>
<pre><code>
a = "5.9"
n = float(a)
print(n)
print(type(n))
</code></pre>

<h3>String to Int</h3>
<p>If the given string is not a number, it will throw an error.</p>
<pre><code>
a = "5"
b = 't'
n = int(a)
print(n)
print(type(n))

try:
    print(int(b))
except ValueError as e:
    print(f"Error: {e}")
</code></pre>

<h3>Addition of String and Integer Using Explicit Conversion</h3>
<p>Trying to add a string and an integer directly will cause a TypeError:</p>
<pre><code>
a = 5
b = 't'

try:
    n = a + int(b)
    print(n)
    print(type(n))
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"TypeError: {e}")
</code></pre>
