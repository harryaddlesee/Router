from flask import Flask, render_template, url_for
from forms import SignUpForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '91beeaba2c6f4ad1f8eacc6451945e16'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/signup")
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
