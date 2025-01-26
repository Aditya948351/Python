<h2>Example Code with Custom Separator and End</h2>
<p>Below is an example of using the <code>print</code> function in Python with custom <code>sep</code> and <code>end</code> parameters:</p>
<pre><code>print("Hey", 6, 7, sep="~", end="009\n")</code></pre>
<p>The output will be:</p>
<pre><code>Hey~6~7009</code></pre>

<h2>Example Code with Custom Separator and End</h2>


<h2>Built-in Data Types</h2>
<p>In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.</p>
<p>Python has the following data types built-in by default, in these categories:</p>
<ul>
    <li><strong>Text Type:</strong> <code>str</code></li>
    <li><strong>Numeric Types:</strong> <code>int</code>, <code>float</code>, <code>complex</code></li>
    <li><strong>Sequence Types:</strong> <code>list</code>, <code>tuple</code>, <code>range</code></li>
    <li><strong>Mapping Type:</strong> <code>dict</code></li>
    <li><strong>Set Types:</strong> <code>set</code>, <code>frozenset</code></li>
    <li><strong>Boolean Type:</strong> <code>bool</code></li>
    <li><strong>Binary Types:</strong> <code>bytes</code>, <code>bytearray</code>, <code>memoryview</code></li>
    <li><strong>None Type:</strong> <code>NoneType</code></li>
</ul>
<h3>Getting the Data Type</h3>
<p>You can get the data type of any object by using the <code>type()</code> function:</p>
<pre><code>
# Example
x = 5
print(type(x))
</code></pre>

<h3>Setting the Data Type</h3>
<p>In Python, the data type is set when you assign a value to a variable:</p>
<table>
    <tr>
        <th>Example</th>
        <th>Data Type</th>
    </tr>
    <tr>
        <td><code>x = "Hello World"</code></td>
        <td>str</td>
    </tr>
    <tr>
        <td><code>x = 20</code></td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>x = 20.5</code></td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>x = 1j</code></td>
        <td>complex</td>
    </tr>
    <tr>
        <td><code>x = ["apple", "banana", "cherry"]</code></td>
        <td>list</td>
    </tr>
    <tr>
        <td><code>x = ("apple", "banana", "cherry")</code></td>
        <td>tuple</td>
    </tr>
    <tr>
        <td><code>x = range(6)</code></td>
        <td>range</td>
    </tr>
    <tr>
        <td><code>x = {"name": "John", "age": 36}</code></td>
        <td>dict</td>
    </tr>
    <tr>
        <td><code>x = {"apple", "banana", "cherry"}</code></td>
        <td>set</td>
    </tr>
    <tr>
        <td><code>x = frozenset({"apple", "banana", "cherry"})</code></td>
        <td>frozenset</td>
    </tr>
    <tr>
        <td><code>x = True</code></td>
        <td>bool</td>
    </tr>
    <tr>
        <td><code>x = b"Hello"</code></td>
        <td>bytes</td>
    </tr>
    <tr>
        <td><code>x = bytearray(5)</code></td>
        <td>bytearray</td>
    </tr>
    <tr>
        <td><code>x = memoryview(bytes(5))</code></td>
        <td>memoryview</td>
    </tr>
    <tr>
        <td><code>x = None</code></td>
        <td>NoneType</td>
    </tr>
</table>

<h3>Setting the Specific Data Type</h3>
<p>If you want to specify the data type, you can use the following constructor functions:</p>
<table>
    <tr>
        <th>Example</th>
        <th>Data Type</th>
    </tr>
    <tr>
        <td><code>x = str("Hello World")</code></td>
        <td>str</td>
    </tr>
    <tr>
        <td><code>x = int(20)</code></td>
        <td>int</td>
    </tr>
    <tr>
        <td><code>x = float(20.5)</code></td>
        <td>float</td>
    </tr>
    <tr>
        <td><code>x = complex(1j)</code></td>
        <td>complex</td>
    </tr>
    <tr>
        <td><code>x = list(("apple", "banana", "cherry"))</code></td>
        <td>list</td>
    </tr>
    <tr>
        <td><code>x = tuple(("apple", "banana", "cherry"))</code></td>
        <td>tuple</td>
    </tr>
    <tr>
        <td><code>x = range(6)</code></td>
        <td>range</td>
    </tr>
    <tr>
        <td><code>x = dict(name="John", age=36)</code></td>
        <td>dict</td>
    </tr>
    <tr>
        <td><code>x = set(("apple", "banana", "cherry"))</code></td>
        <td>set</td>
    </tr>
    <tr>
        <td><code>x = frozenset(("apple", "banana", "cherry"))</code></td>
        <td>frozenset</td>
    </tr>
    <tr>
        <td><code>x = bool(5)</code></td>
        <td>bool</td>
    </tr>
    <tr>
        <td><code>x = bytes(5)</code></td>
        <td>bytes</td>
    </tr>
    <tr>
        <td><code>x = bytearray(5)</code></td>
        <td>bytearray</td>
    </tr>
    <tr>
        <td><code>x = memoryview(bytes(5))</code></td>
        <td>memoryview</td>
    </tr>
</table>


<h2>now,just see the single Python Numbers </h2>
