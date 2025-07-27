from flask import render_template, redirect, url_for, flash
from app import create_app
from app.forms import LoginForm, SignupForm

app = create_app()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic
        flash('Login successful!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Handle signup logic
        flash('Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)