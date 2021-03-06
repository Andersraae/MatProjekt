from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '5d974a87bda95d334175f5724388be6a'

posts = [
    {
        'author': 'Navn',
        'title': 'Titel',
        'content': 'Indhold',
        'date_posted': 'Dato'
    },{
        'author': 'Navn2',
        'title': 'Titel2',
        'content': 'Indhold2',
        'date_posted': 'Dato2'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='Om Os')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Din konto er nu oprettet, { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Opret Konto', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login var successfuld!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login var ikke successfuld. Tjek din email og kodeord', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
