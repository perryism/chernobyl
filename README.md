# Installation

<pre>
pip install git+https://github.com/perryism/chernobyl.git
</pre>

# Create a project

<pre>
python -m chernobyl.new &lt;project_name&gt;
</pre>

Add CSS bootstrap

<pre>
python -m chernobyl.new &lt;project_name&gt; --bootstrap
</pre>

# Add controller

Inside the newly created project

<pre>
python -m chernobyl.generate &lt;module_name&gt; &lt;Camel case controller name&gt;
</pre>

# Run

<pre>
cd &lt;project_name&gt;
python -m &lt;project_name&gt;
curl http://localhost:5555/&lt;lower case controller name&gt;
</pre>
