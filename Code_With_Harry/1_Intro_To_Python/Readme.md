<h2>Comments</h2>

Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

Creating a Comment
Comments starts with a #, and Python will ignore them:

ExampleGet your own Python Server
#This is a comment
print("Hello, World!")
Comments can be placed at the end of a line, and Python will ignore the rest of the line:

Example
print("Hello, World!") #This is a comment
A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:

Example
#print("Hello, World!")
print("Cheers, Mate!")
ADVERTISEMENT

Multiline Comments
Python does not really have a syntax for multiline comments.

To add a multiline comment you could insert a # for each line:

Example
#This is a comment
#written in
#more than just one line
print("Hello, World!")
Or, not quite as intended, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

Example
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.




<h2>Escape Characters</h2>
<p>To insert characters that are illegal in a string, use an escape character. An escape character is a backslash <code>\</code> followed by the character you want to insert.</p>
<p>An example of an illegal character is a double quote inside a string that is surrounded by double quotes:</p>
<pre><code>txt = "We are the so-called "Vikings" from the north."</code></pre>
<p>You will get an error if you use double quotes inside a string that is surrounded by double quotes. To fix this problem, use the escape character <code>\"</code>:</p>
<pre><code>txt = "We are the so-called \"Vikings\" from the north."</code></pre>
<p>Other escape characters used in Python:</p>
<table>
    <tr>
        <th>Code</th>
        <th>Result</th>
        <th>Use</th>
    </tr>
    <tr>
        <td><code>\'</code></td>
        <td>Single Quote</td>
        <td>Allows insertion of a single quote within a string surrounded by single quotes: <code>txt = 'It\'s a sunny day.'</code></td>
    </tr>
    <tr>
        <td><code>\\</code></td>
        <td>Backslash</td>
        <td>Inserts a backslash character: <code>txt = "This is a backslash: \\."</code></td>
    </tr>
    <tr>
        <td><code>\n</code></td>
        <td>New Line</td>
        <td>Inserts a new line: <code>txt = "Hello\nWorld!"</code></td>
    </tr>
    <tr>
        <td><code>\r</code></td>
        <td>Carriage Return</td>
        <td>Inserts a carriage return (rarely used in modern text): <code>txt = "Hello\rWorld!"</code></td>
    </tr>
    <tr>
        <td><code>\t</code></td>
        <td>Tab</td>
        <td>Inserts a tab character: <code>txt = "Hello\tWorld!"</code></td>
    </tr>
    <tr>
        <td><code>\b</code></td>
        <td>Backspace</td>
        <td>Inserts a backspace character: <code>txt = "Hello\bWorld!"</code></td>
    </tr>
    <tr>
        <td><code>\f</code></td>
        <td>Form Feed</td>
        <td>Inserts a form feed character: <code>txt = "Hello\fWorld!"</code></td>
    </tr>
    <tr>
        <td><code>\ooo</code></td>
        <td>Octal Value</td>
        <td>Inserts a character based on its octal value: <code>txt = "\141\142\143"</code> (results in "abc")</td>
    </tr>
    <tr>
        <td><code>\xhh</code></td>
        <td>Hex Value</td>
        <td>Inserts a character based on its hex value: <code>txt = "\x61\x62\x63"</code> (results in "abc")</td>
    </tr>
</table>






<h2>Variable Names</h2>
<p>A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Here are the rules for Python variables:</p>
<ul>
    <li>A variable name must start with a letter or the underscore character</li>
    <li>A variable name cannot start with a number</li>
    <li>A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )</li>
    <li>Variable names are case-sensitive (age, Age, and AGE are three different variables)</li>
    <li>A variable name cannot be any of the Python keywords.</li>
</ul>
<h3>Example</h3>
<p><strong>Legal variable names:</strong></p>
<pre>
<code>
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
</code>
</pre>
<p><strong>Illegal variable names:</strong></p>
<pre>
<code>
2myvar = "John"
my-var = "John"
my var = "John"
</code>
</pre>
<p>Remember that variable names are case-sensitive.</p>
<h2>Multi Words Variable Names</h2>
<p>Variable names with more than one word can be difficult to read. There are several techniques you can use to make them more readable:</p>
<h3>Camel Case</h3>
<p>Each word, except the first, starts with a capital letter:</p>
<pre>
<code>myVariableName = "John"</code>
</pre>
<h3>Pascal Case</h3>
<p>Each word starts with a capital letter:</p>
<pre>
<code>MyVariableName = "John"</code>
</pre>
<h3>Snake Case</h3>
<p>Each word is separated by an underscore character:</p>
<pre>
<code>my_variable_name = "John"</code>
</pre>
