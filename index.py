from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

@app.route('/test/credits/')
def credit_test():
    return "Credit Page"


# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/creditos', strict_slashes=False)
def creditos():
    return render_template("creditos.html")
    
# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
