from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-us')
def about():
    return render_template('about.html')

@app.route('/contact-us')
def contact():
    return 'CONTACT US PAGE'



if __name__ == "__main__":
    app.run(debug=True)  