<h2>Python - Slicing Strings</h2>

<h3>Slicing</h3>
<p>Return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string:</p>
<pre><code>
b = "Hello, World!"
print(b[2:5])  <!-- Output: llo -->
</code></pre>
<p><em>Note: The first character has index 0.</em></p>

<h3>Slice From the Start</h3>
<p>Leaving out the start index, the range will start at the first character:</p>
<pre><code>
b = "Hello, World!"
print(b[:5])  <!-- Output: Hello -->
</code></pre>

<h3>Slice To the End</h3>
<p>Leaving out the end index, the range will go to the end:</p>
<pre><code>
b = "Hello, World!"
print(b[2:])  <!-- Output: llo, World! -->
</code></pre>

<h3>Negative Indexing</h3>
<p>Use negative indexes to start the slice from the end of the string:</p>
<p>Get the characters from "o" in "World!" (position -5) to, but not included, "d" in "World!" (position -2):</p>
<pre><code>
b = "Hello, World!"
print(b[-5:-2])  <!-- Output: orl -->
</code></pre>
