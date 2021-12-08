from flask import Flask, render_template, url_for, flash, redirect
from forms import SignUpForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '91beeaba2c6f4ad1f8eacc6451945e16'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@climb.com' and form.password.data == 'password':
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
