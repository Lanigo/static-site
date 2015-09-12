from flask import Flask, render_template

#initialization
app = Flask(__name__)

#configuration
app.config['FREEZER_DESTINATION'] = 'gh-pages'
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME', '.gitignore', 'readme.md']
app.config['FREEZER_RELATIVE_URLS'] = True

#controllers
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/html')
def html():
	return render_template('html.html')

@app.route('/CSS')
def css():
	return render_template('css.html')

@app.route('/JS')
def js():
	return render_template('js.html')

@app.route('/Py')
def py():
	return render_template('py.html')

@app.route('/datab')
def datab():
	return render_template('datab.html')

@app.route('/git')
def git():
	return render_template('git.html')

@app.route('/design')
def design():
	return render_template('design.html')

@app.route('/articles')
def articles():
	return render_template('articles.html')


#launch
if __name__ == "__main__":
    app.run(debug=True)