from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')

@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

@app.route('/pasta')
def pasta():
    return render_template('pasta.html')

@app.route('/bread')
def bread():
    return render_template('bread.html')

@app.route('/salad')
def salad():
    return render_template('salad.html')

@app.route('/sandwich')
def sandwich():
    return render_template('sandwich.html')

if __name__ == '__main__':
    app.run(debug=True)
