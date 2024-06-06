# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Akshith" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage


# define the route to mother webpage


# define the route to friends webpage


# add other routes, if you want

@app.route("/father")
def home1():

    name = "Rathnakar" # write your name
    age = "44" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route("/mother")
def home2():

    name = "Lavanya" # write your name
    age = "40" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route("/friend")
def home3():

    name = "Akshay" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
