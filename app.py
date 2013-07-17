from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return render_template('layout.html', name='scott')

@app.route('/go')
def go():
    return render_template('gone.html', name='have gone')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404error.html')

if __name__ == '__main__':
    app.run()
