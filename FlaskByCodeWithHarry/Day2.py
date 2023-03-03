'''
Today we will learn about static and templates folder.
It's like how i explained server side scripting and client side
scripting in the Day1.py. Templates is server side and static is
client side.
'''

'''
Static Folder:
This folder is public, client can access it. The static folder on 
the other hand contains the public content like the images, css,
javascript and other files. These files can also be viewed using
the www.website-url/static address.
'''

'''
Templates:
This folder is private, client can't access it. All the sensitive
data is put in it. Flask uses its template folder for storing the
raw templates which can be filled through the python program.
By default flask makes static folder public and templates folder 
private. You can make these two folders where your python file is
kept.
'''

'''
render_template():
Now we will do learn how to return a template(HTML page) through our
python file instead just returning 'Hello World!'
First we need to make an HTML file to return so we will make that
in templates folder(code in the video is given below). After making our
webpage we have to return it through our python file. So for that 
we will go in our python file and import a function named render_template.

    <from flask import Flask, render_template>
'''

'''
Now we will use this function to render our templateand return it.
So for that we will write:

    <render_template('html_file_name.html') #as shown in the code below
Then we start our app and open our HTML page.
Note: If we are making changes in HTML file then we don't have to 
reload our python app again and again as changes are made in HTML
file. We just have to reload our page. Like this we can make many
end points(like home, about, contact) and return templates.
'''

'''
Variables:
This is something very important and interesting. We can make a
variable in our python file and send it to our HTML file. It is 
interesting because it opens a lot of new possibilities We can do
a lot of things through this. We can import a python module, scrap
something, store that data in a variable and send it to our HTML file.
Suddenly the things which we were doing in command line, now we are
doing in form of a website which means better UI.
'''

"""
How to send variable to HTML file?
We will first make a variable and then in our render_template function pass as an
argument like this:

@app.rout("/about")
def harry():
    name = "rohan das"
    return render_template('about.html',name2 = name)
    
You can also write:
@app.route("/about")
def harry():
    return render_template('about.html', name = "rohan das")

Then to display this variable in our webpage we have to use jinja.
It's pretty simple.
Syntax:
{{variable_name}}
That's it! if you want to display variable in h1 tag then it would
be:
<h1>Hi I am {{ variable_name }}!</h1>

The complete code is given below
"""

from flask import Flask, render_template
app = Flask(__name__)
    
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def harry():
    name = "harry"
    return render_template('about.html', name2 = name)
app.run(debug = True)
