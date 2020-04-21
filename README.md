# Create a project

<pre>
python -m chernobyl.new &lt;project_name&gt;
</pre>

# Add controller

<pre>
python -m chernobyl.new.controller &lt;project_name&gt; &lt;Camel case controller name&gt;
</pre>

# Run

<pre>
cd &lt;project_name&gt;
python -m &lt;project_name&gt;
curl http://localhost:5555/&lt;lower case controller name&gt;
</pre>
