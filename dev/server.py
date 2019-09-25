from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os.path


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/technical-experience/')
def technicalExperience():
	if(os.path.exists('technicalExperience.html')):
		return render_template('technicalExperience.html')
	else:
		return 'Technical Experience'

@app.route('/interests/')
def intereinsts():
   return 'Interests'

@app.route('/get-in-touch/')
def contact():
	return 'Contact page'

if __name__ =='__main__':
	app.run(debug=True)
