""" 
Gonzalo Guerra
Lab 11, introduction to Flask
March 10, 2026
"""

from flask import Flask, render_template


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
    my_images = ["images/image_1.jpg", "images/image_2.jpg", "images/image_3.jpg"]
    return render_template('about.html', images=my_images)

@app.route('/quotes')
def qoutes():
    return render_template('quotes.html')

# set the 'app' to run if you eecute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)