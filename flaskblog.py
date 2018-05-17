from flask import Flask, render_template
app = Flask(__name__)

posts = [
  {
    'author': 'Bence Orosz',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': '2018.05.17.'
  },
  {
    'author': 'Ervinbá',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': '2018.05.21.'
  }

]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html')


if __name__ == '__main__':
  #only true if we run .py directly
  app.run(debug=True)
