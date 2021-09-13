from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
