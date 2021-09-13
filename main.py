from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginFrom
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
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('regsister.html', title='Register', form=form)

@app.route("/Login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
