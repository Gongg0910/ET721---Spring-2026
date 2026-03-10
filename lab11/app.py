""" 
Gonzalo Guerra
Lab 11, introduction to Flask
March 10, 2026
"""

from flask import Flask, render_template

""" from water import static, mountain.jpg """

"""
create an object 'app' from the Flask module 
"""

app = Flask(__name__)

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "Prof. Wu"
    fruits = ['apple', 'orange', 'grapes']
    fruit = 'orange'
    return render_template('index.html', username = name, listfruits = fruits, f = fruit)

# endpoints refer to the name of the view in an app
@app.route('/about')
def about():
    return '<h1>About us</h1>'

@app.route('/quotes')
def qoutes():
    return '<h1>Quotes</h1>'

# set the 'app' to run if you eecute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)