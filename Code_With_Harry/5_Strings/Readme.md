<h2>Strings in Python</h2>

<p>Strings in Python are surrounded by either single quotation marks or double quotation marks:</p>
<pre><code>print("Hello")</code></pre>
<pre><code>print('Hello')</code></pre>

<h3>Quotes Inside Quotes</h3>
<pre><code>print("It's alright")</code></pre>
<pre><code>print("He is called 'Johnny'")</code></pre>
<pre><code>print('He is called "Johnny"')</code></pre>

<h3>Assign String to a Variable</h3>
<pre><code>
a = "Hello"
print(a)
</code></pre>

<h3>Multiline Strings</h3>
<p>Using three double quotes or three single quotes:</p>
<pre><code>
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit"""
print(a)
</code></pre>

<pre><code>
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit'''
print(a)
</code></pre>

<h3>Strings are Arrays</h3>
<p>Access elements using square brackets:</p>
<pre><code>
a = "Hello, World!"
print(a[1])
</code></pre>

<h3>Looping Through a String</h3>
<p>Loop through the characters with <code>for</code> loop:</p>
<pre><code>
for x in "banana":
  print(x)
</code></pre>

<h3>String Length</h3>
<p>Using the <code>len()</code> function:</p>
<pre><code>
a = "Hello, World!"
print(len(a))
</code></pre>

<h3>Check String</h3>
<p>Using the keyword <code>in</code>:</p>
<pre><code>
txt = "The best things in life are free!"
print("free" in txt)
</code></pre>

<h3>Check if NOT</h3>
<p>Using the keyword <code>not in</code>:</p>
<pre><code>
txt = "The best things in life are free!"
print("expensive" not in txt)
</code></pre>
